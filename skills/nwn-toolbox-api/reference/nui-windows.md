# NUI windows

Toolbox wraps Anvil's raw NUI API in a view/controller pair. You get: automatic
registration and listing in the DM toolbox, event dispatch to the right controller,
per-player controller lifetimes, cleanup on client leave and server shutdown, optional
auto-close on player movement, and permission-driven widget enabling.

All the window types live in `Jorteck.Toolbox.Core`.

## The view/controller split

**View** — built exactly once, at service construction, and shared by every player. It
owns the `NuiWindow` template and the `NuiBind<T>` / `NuiButton` field declarations. It
must have a parameterless constructor and must hold no per-player state.

**Controller** — one instance per open window per player. It owns the mutable state and
handles events. It must also have a parameterless constructor; dependencies come in via
`[Inject]` properties, not the constructor, because Toolbox constructs it with `new T()`
and then runs Anvil's `InjectionService` over it.

```csharp
using System.Collections.Generic;
using Anvil.API;
using Anvil.API.Events;
using Anvil.Services;
using Jorteck.Toolbox.Core;

public sealed class MyToolWindowView : WindowView<MyToolWindowView>
{
  public override string Id => "myplugin.mytool";     // globally unique, prefix it
  public override string Title => "My Tool";          // never null — nulls are filtered out
  public override NuiWindow WindowTemplate { get; }

  public override IWindowController CreateDefaultController(NwPlayer player)
  {
    return CreateController<MyToolWindowController>(player);
  }

  // Binds: declare as readonly fields so the controller can reference them via View.
  public readonly NuiBind<string> StatusText = new NuiBind<string>("status_val");
  public readonly NuiBind<bool> ApplyEnabled = new NuiBind<bool>("apply");

  // Buttons: captured out of the tree with .Assign() so you can compare Ids later.
  public readonly NuiButton ApplyButton;

  public MyToolWindowView()
  {
    NuiColumn root = new NuiColumn
    {
      Children = new List<NuiElement>
      {
        new NuiRow
        {
          Height = 40f,
          Children = new List<NuiElement>
          {
            new NuiLabel(StatusText),
            new NuiSpacer(),
            new NuiButton("Apply")
            {
              Id = "btn_apply",
              Enabled = ApplyEnabled,
            }.Assign(out ApplyButton),
          },
        },
      },
    };

    WindowTemplate = new NuiWindow(root, Title)
    {
      Geometry = new NuiRect(500f, 100f, 400f, 300f),
    };
  }
}

public sealed class MyToolWindowController : WindowController<MyToolWindowView>
{
  [Inject]
  private SomeService SomeService { get; init; }

  public override bool AutoClose { get; set; } = false;

  public override void Init()          // after construction + injection, before display
  {
    Refresh();
  }

  public override void ProcessEvent(ModuleEvents.OnNuiEvent eventData)
  {
    switch (eventData.EventType)
    {
      case NuiEventType.Click:
        if (eventData.ElementId == View.ApplyButton.Id)
        {
          Apply();
        }

        break;
      case NuiEventType.Open:
        Refresh();
        break;
    }
  }

  protected override void OnClose() { }   // called on every close path; release refs here

  private void Refresh()
  {
    ApplyPermissionBindings(View.ApplyEnabled);
    Token.SetBindValue(View.StatusText, "Ready");
  }

  private void Apply() { }
}
```

**Don't annotate the view with `[ServiceBinding(typeof(IWindowView))]`.** The attribute on
`WindowView<TView>` is inherited, so your subclass is registered as an `IWindowView`
automatically and appears in the DM toolbox list. Repeating it is redundant rather than
harmful — registrations are keyed by implementation type, so the duplicate overwrites
rather than double-listing — but it misleads the next reader into thinking the
registration is explicit.

Set `ListInToolbox => false` to keep it out of that list — correct for windows you open
programmatically, sub-windows, and popups.

## Reading and writing binds

`Token` is the `NuiWindowToken` for this player's instance of the window.

```csharp
Token.SetBindValue(View.StatusText, "Ready");
Token.SetBindValues(View.RowLabels, listOfStrings);   // list-bound (NuiList) values
string current = Token.GetBindValue(View.StatusText)!;
Token.SetGroupLayout(View.SomeGroup, someLayout);     // swap a NuiGroup's contents
NwPlayer player = Token.Player;
```

`GetBindValue` returns a nullable — the `!` is normal here, Anvil's annotations are
conservative. `Token.Dispose()` destroys the window; you don't normally call it, `Close()`
does.

## Opening a window

Inject `WindowManager`:

```csharp
windowManager.OpenWindow<MyToolWindowView>(player);                          // default controller
windowManager.OpenWindow<MyToolWindowView, MyToolWindowController>(player,   // configure first
  controller => controller.TargetCreature = someCreature);
```

The two-type overload is how you pass arguments into a window — the `configure` callback
runs after injection and before `Init()`, so `Init()` can rely on what you set. It's also
where you set `AutoClose` (see below).

Only the two-type overload returns anything: the controller, or `null` if the player's
client can't render NUI or the view type isn't registered. The single-type overload and
`OpenWindow(NwPlayer, IWindowView)` both return `void`, so you get no failure signal in
code — use the two-type overload when you care. An unregistered view type is at least
logged; a client that can't render NUI fails silently on every overload.

None of them check permissions.

`OpenWindow(NwPlayer, IWindowView)` is for when you have a view instance rather than a type
— that's what the toolbox list itself uses.

## Lifecycle

- Constructed via `new TController()`, then `InjectionService.Inject(...)` fills `[Inject]`
  properties, then your `configure` callback, then `Init()`.
- `ProcessEvent` is dispatched by `WindowManager` off `NwModule.Instance.OnNuiEvent`,
  matched by token.
- `NuiEventType.Close` triggers `Close(destroyWindow: false)` — the client already tore the
  window down — and the controller is dropped from the player's list.
- Client leave and `WindowManager` disposal both call `Close()` on everything still open.

**Make `OnClose()` idempotent.** Controllers are only removed from the manager's list on a
`NuiEventType.Close` event. A programmatic `Close()` — auto-close, or a
`DialogPopupController` Ok/Cancel — leaves the controller registered, so client leave or
manager disposal calls `Close()` again, running `OnClose()` and `Token.Dispose()` a second
time.

Because controllers are per-open, anything that must outlive the window belongs in a
service or in `PersistenceStorageService`.

### AutoClose

`AutoClose = true` registers with `WindowAutoCloseService`, which closes the window when
the player leaves the area, or moves more than 3 units from where it was opened. It polls
once a second.

Two traps:

- `WindowManager` reads `controller.AutoClose` **before** calling `Init()`, so setting it
  inside `Init()` silently does nothing. Override the property, or set it in the
  `configure` callback of the two-type `OpenWindow`.
- The open position is captured from `LoginCreature.Location`, but the distance check uses
  `ControlledCreature.Location`. A DM possessing a creature elsewhere gets an immediate
  close.

## Permission-gated widgets

`ApplyPermissionBindings(params NuiBind<bool>[])` sets each bind to whether the player
holds `toolbox.window.use.{viewId}.{bindKey}`, both lowercased. So a view with
`Id => "myplugin.mytool"` and a bind keyed `"apply"` checks
`toolbox.window.use.myplugin.mytool.apply`.

It defaults to `true` when the permissions feature is disabled server-side, so an
ungated server behaves as though everyone has everything. See `permissions.md` — in
particular, this gates *widgets*, not *opening the window*.

## Dialog popups

`DialogPopupController<T>` implements the OK/Cancel handling and exposes the result as a
task. The view must implement `IDialogView` (which just requires `OkButton` and
`CancelButton`) alongside `WindowView<T>`:

```csharp
public sealed class ConfirmView : WindowView<ConfirmView>, IDialogView
{
  public NuiButton OkButton { get; }
  public NuiButton CancelButton { get; }
  // ... Id, Title, WindowTemplate, CreateDefaultController as usual
}

public sealed class ConfirmController : DialogPopupController<ConfirmView>
{
  public override void Init() { }
}

// caller
ConfirmController dialog = windowManager.OpenWindow<ConfirmView, ConfirmController>(player);
DialogResult result = await dialog.WaitForDialogResult();
if (result == DialogResult.Ok) { /* ... */ }
```

`DialogResult` is `Unknown | Ok | Cancel | Close`. `Close` means the player dismissed the
window via its titlebar rather than either button. `DialogPopupController` already
overrides `ProcessEvent` and `OnClose`; override `Init` only, and if you do need
`ProcessEvent` for extra widgets, call `base.ProcessEvent(eventData)`.

Give popups `ListInToolbox => false`.

## Wizards

`WizardRootController<T>` drives a multi-step flow inside one window: a `NuiGroup` whose
layout is swapped per step, plus Next/Previous buttons. The root view implements
`IWizardRootView`; each step is an `IWizardStepView` (just a `NuiLayout ViewTemplate`) and
an `IWizardStepController<TView>`.

```csharp
public sealed class MyWizardController : WizardRootController<MyWizardView>
{
  public override void InitWizard()
  {
    RegisterStep<Step1View, Step1Controller>();
    RegisterStep<Step2View, Step2Controller>();
  }

  public override void OnWizardComplete()
  {
    Step1Controller step1 = GetStep<Step1Controller>();
    // read collected state off the step controllers, then act
  }
}
```

- `Init()` is sealed on the base — put your setup in `InitWizard()`, which must register at
  least one step (`Steps[0]` is selected immediately).
- `CanCompleteStep` drives whether Next is enabled and is re-read after every event, so a
  computed value works. `StepTitle` drives the window title bind but is read **only when
  the step changes** — to retitle mid-step, call
  `Token.SetBindValue(View.WindowTitleText, …)` yourself.
- `IWizardStepController.OnClose()` fires when leaving a step in either direction, not just
  at the end.
- Steps share the root window's `Token`. Bind keys must be unique across all steps.
- Override `GetNextStep()` / `GetPreviousStep()` / `IsFinalStep()` for branching flows; the
  defaults walk the `Steps` list linearly.
- On the final step, Next closes the window and then calls `OnWizardComplete()` — in that
  order, so don't read binds in `OnWizardComplete`, read state the step controllers saved.
- `WizardTexts` overrides the Next/Previous/Finish button labels via
  `IWizardRootView.WizardTexts`; it defaults to `WizardTexts.Default`.

## Object selection list

`ObjectSelectionListView` / `ObjectSelectionListController` are a reusable "pick an object
in an area" sub-panel — search box, type filter, distance filter, area switcher, and a
click-to-select list. Unlike windows, you compose them by hand rather than deriving:

```csharp
// in your view
public readonly ObjectSelectionListView ObjectList = new ObjectSelectionListView();
// ... splice ObjectList.SubView (IReadOnlyList<NuiElement>) into your layout's Children

// in your controller
private ObjectSelectionListController objectList;

public override void Init()
{
  objectList = new ObjectSelectionListController(View.ObjectList, Token);
  objectList.OnObjectSelectChange += HandleSelectionChanged;

  // Init() dereferences the area unguarded — null it and you get an NRE.
  NwArea area = Token.Player.ControlledCreature?.Area;
  if (area != null)
  {
    objectList.Init(area);
  }
}

public override void ProcessEvent(ModuleEvents.OnNuiEvent eventData)
{
  if (objectList.ProcessEvent(eventData))
  {
    return;   // the list consumed it
  }
  // your own handling
}
```

The panel assumes a controlled creature throughout, not just at `Init` — its refresh path
uses `Token.Player.ControlledCreature!`.

`ProcessEvent` returns `true` for search-button clicks and row selections. It is **not** a
reliable "handled" signal: the object-picker button is handled (it enters target mode) but
still returns `false`, so your own handler has to ignore that element id explicitly.

`SelectedObject`, `RestrictTypeSelection`, `RestrictAreaSelection`, `Refresh()`, and
`JumpToObject(NwGameObject)` are the rest of the surface. `ObjectSelectionTypes` is a
`[Flags]` enum of the filterable categories.

One dead control: `ChangeAreaButton` renders by default (`RestrictAreaSelection` is
`false`) but has no handler anywhere in v8193.37.6. Clicking it does nothing. Set
`RestrictAreaSelection = true` to hide it, or implement area switching yourself.

## Helpers

`NuiUtils` (in `Jorteck.Toolbox`, not `Jorteck.Toolbox.Core`):

- `NuiUtils.CreateComboForEnum<T>(NuiBind<int> selected)` — a `NuiCombo` with one entry per
  enum value, labelled by `ToString()`, valued by the underlying int.
- `element.Assign(out field)` — returns the element so you can capture it mid-tree.
- `element.Configure(e => { ... })` — returns the element after running a setup lambda;
  useful for setting properties on something a factory built, e.g.
  `NuiUtils.CreateComboForEnum<Gender>(GenderBind).Configure(c => c.Enabled = GenderEnabled)`.

Both extension methods are what make the nested-initializer style above readable — the
alternative is declaring every button before the tree and referencing them inside it.
