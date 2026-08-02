# NWN.Toolbox public API index

Generated from NWN.Toolbox `v8193.37.6`.

One `##` heading per **public** type in `Jorteck.Toolbox`, with its public and
protected members bulleted beneath and enum values inlined. Internal types, types
nested inside internal types, and generated EF migration code are excluded on
purpose — if a type isn't listed here, a consuming plugin either cannot reference
it or has no reason to, and the answer is "that's not part of the API" rather than
"read the source".

Grep this rather than reading it:

```
rg -A 40 '^## Jorteck\.Toolbox\.Core\.WindowController' reference/api-index.md
rg 'ApplyPermissionBindings' reference/api-index.md      # which type exposes a member
rg '^## Jorteck\.Toolbox\.Features\.Chat' reference/api-index.md
```

Signatures are extracted textually, so a member declared across multiple lines may
be truncated, and interface default-implementations appear without their bodies.
The `[file]` note on each heading points at the defining source file if you do need
to confirm behaviour.

Regenerate with `python3 scripts/generate_api_index.py /path/to/NWN.Toolbox`.

## Jorteck.Toolbox.Core.LanguageConfig  [class]  (Core/Config/Features/LanguageConfig.cs)
- bool Enabled
- bool EnableBuiltIn

## Jorteck.Toolbox.Core.Persistence.IPersistenceStore  [interface]  (Core/Persistence/IPersistenceStore.cs)
- T GetState<T>(NwPlayer player, string key)
- void UpdateState<T>(NwPlayer player, string key, T value)

## Jorteck.Toolbox.Core.Persistence.PersistenceStorageService  [class]  (Core/Persistence/PersistenceStorageService.cs)
- PersistenceStorageService(SchedulerService schedulerService)
- void SetActiveStore(IPersistenceStore store)
- T GetState<T>(NwPlayer player, string key)
- void UpdateState<T>(NwPlayer player, string key, T value)
- void Dispose()

## Jorteck.Toolbox.Core.Persistence.PersistentVariablePersistenceStore  [class]  (Core/Persistence/PersistentVariablePersistenceStore.cs)
- T GetState<T>(NwPlayer player, string key)
- void UpdateState<T>(NwPlayer player, string key, T value)

## Jorteck.Toolbox.Core.IWindowController  [interface]  (Core/Windows/IWindowController.cs)
- NuiWindowToken Token
- bool AutoClose
- void Init()
- void ProcessEvent(ModuleEvents.OnNuiEvent eventData)
- void Close(bool destroyWindow = true)

## Jorteck.Toolbox.Core.IWindowView  [interface]  (Core/Windows/IWindowView.cs)
- string Id
- string Title
- bool ListInToolbox
- IWindowController CreateDefaultController(NwPlayer player)

## Jorteck.Toolbox.Core.DialogPopupController<T>  [class]  (Core/Windows/Popups/DialogPopupController.cs)
- DialogResult DialogResult
- async Task<DialogResult> WaitForDialogResult()
- override void ProcessEvent(ModuleEvents.OnNuiEvent eventData)
- protected override void OnClose()

## Jorteck.Toolbox.Core.DialogResult  [enum]  (Core/Windows/Popups/DialogResult.cs)
- values: Unknown, Ok, Cancel, Close

## Jorteck.Toolbox.Core.IDialogView  [interface]  (Core/Windows/Popups/IDialogView.cs)
- NuiButton OkButton
- NuiButton CancelButton

## Jorteck.Toolbox.Core.ObjectSelectionListController  [class]  (Core/Windows/Shared/ObjectSelectionListController.cs)
- NwObject SelectedObject
- event Action OnObjectSelectChange
- bool RestrictTypeSelection
- bool RestrictAreaSelection
- ObjectSelectionListController(ObjectSelectionListView view, NuiWindowToken windowToken)
- void Init(NwArea area, ObjectSelectionTypes initialSelectionTypes = ObjectSelectionTypes.Creature)
- bool ProcessEvent(ModuleEvents.OnNuiEvent eventData)
- void Refresh()
- async void JumpToObject(NwGameObject gameObject)

## Jorteck.Toolbox.Core.ObjectSelectionListView  [class]  (Core/Windows/Shared/ObjectSelectionListView.cs)
- readonly string ObjectRowId = "obj_rows"
- readonly NuiBind<string> Search = new NuiBind<string>("search_val")
- readonly NuiBind<int> SearchObjectType = new NuiBind<int>("search_type_val")
- readonly NuiBind<string> SearchDistance = new NuiBind<string>("search_dist_val")
- readonly NuiBind<string> CurrentArea = new NuiBind<string>("area")
- readonly NuiBind<Color> RowColors = new NuiBind<Color>("obj_row_colors")
- readonly NuiBind<string> ObjectTypes = new NuiBind<string>("obj_types_val")
- readonly NuiBind<string> ObjectNames = new NuiBind<string>("obj_names_val")
- readonly NuiBind<string> ObjectResRefs = new NuiBind<string>("obj_resrefs_val")
- readonly NuiBind<string> ObjectTags = new NuiBind<string>("obj_tags_val")
- readonly NuiBind<string> ObjectHPs = new NuiBind<string>("obj_hps_val")
- readonly NuiBind<string> ObjectCRs = new NuiBind<string>("obj_crs_val")
- readonly NuiBind<int> ObjectCount = new NuiBind<int>("obj_count")
- readonly NuiLabel ObjectTypeTexts
- readonly NuiLabel ObjectNameTexts
- readonly NuiLabel ObjectHPTexts
- readonly NuiLabel ObjectCRTexts
- readonly NuiLabel ObjectResRefTexts
- readonly NuiLabel ObjectTagTexts
- readonly NuiButtonImage ObjectPickerButton
- readonly NuiButtonImage SearchButton
- readonly NuiButton ChangeAreaButton
- readonly NuiCombo ObjectTypeFilter
- readonly NuiBind<bool> UnrestrictedArea = new NuiBind<bool>("vis_area")
- readonly NuiBind<bool> UnrestrictedType = new NuiBind<bool>("vis_type")
- IReadOnlyList<NuiElement> SubView
- ObjectSelectionListView()

## Jorteck.Toolbox.Core.ObjectSelectionTypes  [enum]  (Core/Windows/Shared/ObjectSelectionTypes.cs)
- values: Creature, Item, Trigger, Door, AreaOfEffect, Waypoint, Placeable, Store, Encounter, Sound, Player, All

## Jorteck.Toolbox.Core.WindowAutoCloseService  [class]  (Core/Windows/WindowAutoCloseService.cs)
- WindowAutoCloseService(SchedulerService schedulerService)
- void RegisterWindowForAutoClose(IWindowController windowController)

## Jorteck.Toolbox.Core.WindowController<TView>  [class]  (Core/Windows/WindowController.cs)
- PermissionsService PermissionsService
- TView View
- NuiWindowToken Token
- virtual bool AutoClose
- abstract void Init()
- abstract void ProcessEvent(ModuleEvents.OnNuiEvent eventData)
- void Close(bool destroyWindow = true)
- protected abstract void OnClose()
- protected void ApplyPermissionBindings(params NuiBind<bool>[] binds)

## Jorteck.Toolbox.Core.WindowManager  [class]  (Core/Windows/WindowManager.cs)
- WindowManager(InjectionService injectionService, WindowAutoCloseService windowAutoCloseService, IEnumerable<IWindowView> windowViews)
- TController OpenWindow<TView, TController>(NwPlayer player, Action<TController> configure = null)
- void OpenWindow<T>(NwPlayer player) where T : WindowView<T>, new()
- void OpenWindow(NwPlayer player, IWindowView view)

## Jorteck.Toolbox.Core.WindowView<TView>  [class]  (Core/Windows/WindowView.cs)
- abstract string Id
- abstract string Title
- abstract NuiWindow WindowTemplate
- virtual bool ListInToolbox
- abstract IWindowController CreateDefaultController(NwPlayer player)
- protected T CreateController<T>(NwPlayer player) where T : WindowController<TView>, new()

## Jorteck.Toolbox.Core.IWizardRootView  [interface]  (Core/Windows/Wizards/IWizardRootView.cs)
- NuiBind<string> WindowTitleText
- NuiGroup ViewContainer
- WizardTexts WizardTexts
- NuiButton NextButton
- NuiBind<bool> NextButtonEnabled
- NuiBind<string> NextButtonText
- NuiButton PreviousButton
- NuiBind<bool> PreviousButtonEnabled

## Jorteck.Toolbox.Core.IWizardStepController  [interface]  (Core/Windows/Wizards/IWizardStepController.cs)
- IWizardStepView View
- NuiWindowToken Token
- bool CanCompleteStep
- string StepTitle
- void Init()
- void ProcessEvent(ModuleEvents.OnNuiEvent eventData)
- void OnClose()

## Jorteck.Toolbox.Core.IWizardStepController<TView>  [interface]  (Core/Windows/Wizards/IWizardStepController.cs)
- new TView View

## Jorteck.Toolbox.Core.IWizardStepView  [interface]  (Core/Windows/Wizards/IWizardStepView.cs)
- NuiLayout ViewTemplate

## Jorteck.Toolbox.Core.WizardRootController<T>  [class]  (Core/Windows/Wizards/WizardRootController.cs)
- protected InjectionService InjectionService
- protected readonly List<IWizardStepController> Steps = new List<IWizardStepController>()
- protected IWizardStepController CurrentStep
- sealed override void Init()
- abstract void InitWizard()
- abstract void OnWizardComplete()
- override void ProcessEvent(ModuleEvents.OnNuiEvent eventData)
- protected virtual bool IsFinalStep(IWizardStepController step)
- protected virtual IWizardStepController GetNextStep()
- protected virtual IWizardStepController GetPreviousStep()
- protected virtual TStep GetStep<TStep>() where TStep : IWizardStepController
- protected TController RegisterStep<TView, TController>()
- protected void RegisterStep(IWizardStepController controller)
- protected virtual void RefreshWizardButtons()
- protected override void OnClose()

## Jorteck.Toolbox.Core.WizardTexts  [class]  (Core/Windows/Wizards/WizardTexts.cs)
- string NextButton
- string PreviousButton
- string FinishButton
- static readonly WizardTexts Default = new WizardTexts

## Jorteck.Toolbox.ChatExtensions  [class]  (Extensions/ChatUtils.cs)
- static ChatVolume ToChatVolume(this TalkVolume talkVolume)
- static TalkVolume ToTalkVolume(this ChatVolume talkVolume)
- static string GetAreaShoutMessage(string message)

## Jorteck.Toolbox.CreatureSizeExtensions  [class]  (Extensions/CreatureSizeExtensions.cs)
- static int ACModifier(this CreatureSize size)

## Jorteck.Toolbox.NuiUtils  [class]  (Extensions/NuiUtils.cs)
- static NuiCombo CreateComboForEnum<T>(NuiBind<int> selected) where T : struct, Enum
- static T Assign<T>(this T value, out T assign)
- static T Configure<T>(this T value, Action<T> configure) where T : NuiElement

## Jorteck.Toolbox.ObjectExtensions  [class]  (Extensions/ObjectExtensions.cs)
- static string GetTypeName(this NwObject gameObject)
- static ObjectSelectionTypes GetSelectionType(this NwObject gameObject)

## Jorteck.Toolbox.Features.Blueprints.BlueprintManager  [class]  (Features/Blueprints/BlueprintManager.cs)
- BlueprintManager(IEnumerable<IBlueprintSource> blueprintSources)
- List<IBlueprint> GetMatchingBlueprints(BlueprintObjectType objectType, string search, int max)

## Jorteck.Toolbox.Features.Blueprints.BlueprintObjectType  [enum]  (Features/Blueprints/BlueprintObjectType.cs)
- values: Creature, Door, Encounter, Item, Placeable, Sound, Store, Trigger, Waypoint

## Jorteck.Toolbox.Features.Blueprints.IBlueprint  [interface]  (Features/Blueprints/IBlueprint.cs)
- string FullName
- string Name
- string Category
- float? CR
- string Faction
- BlueprintObjectType ObjectType
- NwObject Create(Location location)
- NwItem Create(NwGameObject owner)

## Jorteck.Toolbox.Features.Blueprints.IBlueprintSource  [interface]  (Features/Blueprints/IBlueprintSource.cs)
- IEnumerable<IBlueprint> GetBlueprints(BlueprintObjectType blueprintType, int start, string search, int count)

## Jorteck.Toolbox.Features.Chat.AreaShoutService  [class]  (Features/Chat/AreaShoutService.cs)
- void SendMessage(NwCreature sender, string message)
- string GetFormattedAreaMessage(string message)

## Jorteck.Toolbox.Features.Chat.ChatVolume  [enum]  (Features/Chat/ChatVolume.cs)
- values: Talk, Whisper, Party, Area

## Jorteck.Toolbox.Features.Chat.CommandUsage  [class]  (Features/Chat/CommandUsage.cs)
- string SubCommand
- string Description
- CommandUsage(string subCommand, string description)
- CommandUsage(string description)

## Jorteck.Toolbox.Features.Chat.AppearanceCommand  [class]  (Features/Chat/Commands/AppearanceCommand.cs)
- string Command
- bool DMOnly
- Range ArgCount
- string Description
- string[] Aliases
- CommandUsage[] Usages
- void ProcessCommand(NwPlayer caller, IReadOnlyList<string> args)

## Jorteck.Toolbox.Features.Chat.AreaShoutCommand  [class]  (Features/Chat/Commands/AreaShoutCommand.cs)
- string Command
- bool DMOnly
- Range ArgCount
- string Description
- string[] Aliases
- CommandUsage[] Usages
- void ProcessCommand(NwPlayer caller, IReadOnlyList<string> args)

## Jorteck.Toolbox.Features.Chat.EncounterCommand  [class]  (Features/Chat/Commands/EncounterCommand.cs)
- string Command
- string[] Aliases
- bool DMOnly
- Range ArgCount
- string Description
- CommandUsage[] Usages
- void ProcessCommand(NwPlayer caller, IReadOnlyList<string> args)

## Jorteck.Toolbox.Features.Chat.HelpCommand  [class]  (Features/Chat/Commands/HelpCommand.cs)
- string Command
- Range ArgCount
- bool DMOnly
- string Description
- CommandUsage[] Usages
- void ProcessCommand(NwPlayer caller, IReadOnlyList<string> args)
- void ShowAvailableCommandsToPlayer(NwPlayer player)
- void ShowCommandHelpToPlayer(NwPlayer player, IChatCommand command)
- string GetCommandHelp(IChatCommand command)
- string GetCommandHelp(IEnumerable<IChatCommand> commands)

## Jorteck.Toolbox.Features.Chat.IChatCommand  [interface]  (Features/Chat/Commands/IChatCommand.cs)
- string Command
- string[] Aliases
- bool DMOnly
- string PermissionKey
- Range ArgCount
- string Description
- CommandUsage[] Usages
- bool IsAvailable
- void ProcessCommand(NwPlayer caller, IReadOnlyList<string> args)

## Jorteck.Toolbox.Features.Chat.LanguageCommand  [class]  (Features/Chat/Commands/LanguageCommand.cs)
- string Command
- string[] Aliases
- Range ArgCount
- bool DMOnly
- bool IsAvailable
- string Description
- CommandUsage[] Usages
- void ProcessCommand(NwPlayer caller, IReadOnlyList<string> args)

## Jorteck.Toolbox.Features.Chat.LanguageDMCommand  [class]  (Features/Chat/Commands/LanguageDMCommand.cs)
- string Command
- string[] Aliases
- Range ArgCount
- bool DMOnly
- bool IsAvailable
- string Description
- CommandUsage[] Usages
- void ProcessCommand(NwPlayer caller, IReadOnlyList<string> args)

## Jorteck.Toolbox.Features.Chat.ReloadServerCommand  [class]  (Features/Chat/Commands/ReloadServerCommand.cs)
- string Command
- Range ArgCount
- bool DMOnly
- string Description
- bool IsAvailable
- CommandUsage[] Usages
- void ProcessCommand(NwPlayer caller, IReadOnlyList<string> args)

## Jorteck.Toolbox.Features.Chat.ShortcutCommand  [class]  (Features/Chat/Commands/ShortcutCommand.cs)
- string Command
- Range ArgCount
- bool DMOnly
- string Description
- CommandUsage[] Usages
- void ProcessCommand(NwPlayer caller, IReadOnlyList<string> args)

## Jorteck.Toolbox.Features.ChatWatchCommand  [class]  (Features/ChatWatch/ChatWatchCommand.cs)
- string Command
- Range ArgCount
- bool DMOnly
- string Description
- CommandUsage[] Usages
- void ProcessCommand(NwPlayer caller, IReadOnlyList<string> args)

## Jorteck.Toolbox.Features.AbilityCheckCommand  [class]  (Features/DiceRolls/Commands/AbilityCheckCommand.cs)
- string Command
- bool DMOnly
- Range ArgCount
- string Description
- CommandUsage[] Usages
- AbilityCheckCommand()
- void ProcessCommand(NwPlayer caller, IReadOnlyList<string> args)

## Jorteck.Toolbox.Features.RollDiceCommand  [class]  (Features/DiceRolls/Commands/RollDiceCommand.cs)
- string Command
- bool DMOnly
- Range ArgCount
- string Description
- CommandUsage[] Usages
- void ProcessCommand(NwPlayer caller, IReadOnlyList<string> args)

## Jorteck.Toolbox.Features.RollModeCommand  [class]  (Features/DiceRolls/Commands/RollModeCommand.cs)
- string Command
- bool DMOnly
- Range ArgCount
- string Description
- CommandUsage[] Usages
- void ProcessCommand(NwPlayer caller, IReadOnlyList<string> args)

## Jorteck.Toolbox.Features.SaveThrowCommand  [class]  (Features/DiceRolls/Commands/SaveThrowCommand.cs)
- string Command
- bool DMOnly
- Range ArgCount
- string Description
- CommandUsage[] Usages
- void ProcessCommand(NwPlayer caller, IReadOnlyList<string> args)

## Jorteck.Toolbox.Features.SkillCheckCommand  [class]  (Features/DiceRolls/Commands/SkillCheckCommand.cs)
- string Command
- bool DMOnly
- Range ArgCount
- string Description
- CommandUsage[] Usages
- SkillCheckCommand()
- void ProcessCommand(NwPlayer caller, IReadOnlyList<string> args)

## Jorteck.Toolbox.Features.CreatureRollSettings  [class]  (Features/DiceRolls/CreatureRollSettings.cs)
- bool AutoSuccess
- bool AutoFail
- RollBroadcastTargets RollBroadcastTargets

## Jorteck.Toolbox.Features.DiceRollService  [class]  (Features/DiceRolls/DiceRollService.cs)
- static readonly Color NameColor = new Color(153, 255, 255)
- static readonly Color CheckMessageColor = new Color(1, 102, 255)
- static readonly Color SaveMessageColor = new Color(138, 240, 240)
- RollBroadcastTargets GetBroadcastMode(NwPlayer player)
- void SetBroadcastMode(NwPlayer player, RollBroadcastTargets newValue)
- int RollDice(NwCreature creature, int numSides, int numDice, RollBroadcastTargets broadcastTargets = RollBroadcastTargets.LocalTalk | RollBroadcastTargets.DM)
- bool AbilityCheckVsDc(NwCreature creature, Ability ability, int dc, out int abilityCheckDifference, CreatureRollSettings settings = null)
- int AbilityRoll(NwCreature creature, Ability ability, RollBroadcastTargets broadcastTargets = RollBroadcastTargets.LocalTalk | RollBroadcastTargets.DM)
- int SkillRoll(NwCreature creature, NwSkill skill, RollBroadcastTargets broadcastTargets = RollBroadcastTargets.LocalTalk | RollBroadcastTargets.DM)
- bool SkillCheckVsDc(NwCreature creature, NwSkill skill, int dc, out int skillCheckDifference, CreatureRollSettings settings = null)
- int SavingThrowRoll(NwCreature creature, SavingThrow savingThrow, RollBroadcastTargets broadcastTargets = RollBroadcastTargets.LocalTalk | RollBroadcastTargets.DM)
- bool SavingThrowRollVsDc(NwCreature creature, SavingThrow savingThrow, int dc, out int savingThrowDifference, CreatureRollSettings settings = null)

## Jorteck.Toolbox.Features.RollBroadcastTargets  [enum]  (Features/DiceRolls/RollBroadcastTargets.cs)
- values: None, PrivateLog, PrivateChat, LocalTalk, DM

## Jorteck.Toolbox.Features.Languages.LanguageChatService  [class]  (Features/Languages/LanguageChatService.cs)
- void SendTranslatedMessage(NwCreature sender, ChatVolume volume, bool isDm, bool matchChatPattern, string message, ILanguage language, int proficiency)

## Jorteck.Toolbox.Features.Languages.LanguageDisplayType  [enum]  (Features/Languages/LanguageDisplayType.cs)
- values: Both, Translated, Native

## Jorteck.Toolbox.Features.Languages.LanguageOutput  [struct]  (Features/Languages/LanguageOutput.cs)
- readonly ILanguage Language
- readonly string Output
- readonly string Interpretation
- LanguageOutput(ILanguage language, string interpretation, string output)

## Jorteck.Toolbox.Features.Languages.LanguageProficiency  [class]  (Features/Languages/LanguageProficiency.cs)
- const int Untrained = 0
- const int Beginner = 25
- const int Intermediate = 50
- const int Advanced = 75
- const int Fluent = 100

## Jorteck.Toolbox.Features.Languages.LanguageService  [class]  (Features/Languages/LanguageService.cs)
- IReadOnlyCollection<ILanguage> Languages
- LanguageService(IList<ILanguage> languages, PersistenceStorageService persistenceStorageService)
- bool PlayerKnowsLanguage(NwPlayer player, ILanguage language, LanguageState languageState)
- int? GetLanguageProficiency(NwPlayer player, ILanguage language, LanguageState languageState)
- LanguageState GetStateForPlayer(NwPlayer player)
- void UpdateLanguageState(NwPlayer player, Action<LanguageState> transaction)
- LanguageDisplayType GetDisplayType(NwPlayer player)
- void SetDisplayType(NwPlayer player, LanguageDisplayType displayType)
- bool TryGetLanguage(string key, out ILanguage language)
- void RegisterLanguage(ILanguage language)
- void ListPlayerLanguages(NwPlayer showTo, NwPlayer target)

## Jorteck.Toolbox.Features.Languages.LanguageState  [class]  (Features/Languages/LanguageState.cs)
- Dictionary<string, int> LanguageProficiencies
- string CurrentLanguageId
- LanguageDisplayType DisplayType

## Jorteck.Toolbox.Features.Languages.LanguageUtils  [class]  (Features/Languages/LanguageUtils.cs)
- static LanguageOutput TranslateUsingDictionary(ILanguage language, Dictionary<char, string> dictionary, string phrase, int proficiency)
- static LanguageOutput TranslateWithSeed(ILanguage language, int seed, string phrase, int proficiency)

## Jorteck.Toolbox.Features.Languages.ILanguage  [interface]  (Features/Languages/Translations/ILanguage.cs)
- string Id
- string[] Aliases
- string Name
- Color ChatColor
- bool Enabled
- LanguageOutput Translate(string phrase, int proficiency)

## Jorteck.Toolbox.Features.Languages.LanguageAbyssal  [class]  (Features/Languages/Translations/LanguageAbyssal.cs)
- string Id
- string Name
- Color ChatColor
- bool Enabled
- LanguageOutput Translate(string phrase, int proficiency)

## Jorteck.Toolbox.Features.Languages.LanguageCelestial  [class]  (Features/Languages/Translations/LanguageCelestial.cs)
- string Id
- string Name
- Color ChatColor
- bool Enabled
- LanguageOutput Translate(string phrase, int proficiency)

## Jorteck.Toolbox.Features.Languages.LanguageDraconic  [class]  (Features/Languages/Translations/LanguageDraconic.cs)
- string Id
- string Name
- Color ChatColor
- bool Enabled
- LanguageOutput Translate(string phrase, int proficiency)

## Jorteck.Toolbox.Features.Languages.LanguageDruidic  [class]  (Features/Languages/Translations/LanguageDruidic.cs)
- string Id
- string Name
- Color ChatColor
- bool Enabled
- LanguageOutput Translate(string phrase, int proficiency)

## Jorteck.Toolbox.Features.Languages.LanguageDwarven  [class]  (Features/Languages/Translations/LanguageDwarven.cs)
- string Id
- string Name
- string[] Aliases
- Color ChatColor
- bool Enabled
- LanguageOutput Translate(string phrase, int proficiency)

## Jorteck.Toolbox.Features.Languages.LanguageElven  [class]  (Features/Languages/Translations/LanguageElven.cs)
- string Id
- string Name
- string[] Aliases
- Color ChatColor
- bool Enabled
- LanguageOutput Translate(string phrase, int proficiency)

## Jorteck.Toolbox.Features.Languages.LanguageGnome  [class]  (Features/Languages/Translations/LanguageGnome.cs)
- string Id
- string Name
- string[] Aliases
- Color ChatColor
- bool Enabled
- LanguageOutput Translate(string phrase, int proficiency)

## Jorteck.Toolbox.Features.Languages.LanguageGoblin  [class]  (Features/Languages/Translations/LanguageGoblin.cs)
- string Id
- string Name
- Color ChatColor
- bool Enabled
- LanguageOutput Translate(string phrase, int proficiency)

## Jorteck.Toolbox.Features.Languages.LanguageHalfling  [class]  (Features/Languages/Translations/LanguageHalfling.cs)
- string Id
- string Name
- Color ChatColor
- bool Enabled
- LanguageOutput Translate(string phrase, int proficiency)

## Jorteck.Toolbox.Features.Languages.LanguageInfernal  [class]  (Features/Languages/Translations/LanguageInfernal.cs)
- string Id
- string Name
- Color ChatColor
- bool Enabled
- LanguageOutput Translate(string phrase, int proficiency)

## Jorteck.Toolbox.Features.Languages.LanguageMulhorandi  [class]  (Features/Languages/Translations/LanguageMulhorandi.cs)
- string Id
- string Name
- Color ChatColor
- bool Enabled
- LanguageOutput Translate(string phrase, int proficiency)

## Jorteck.Toolbox.Features.Languages.LanguageOrc  [class]  (Features/Languages/Translations/LanguageOrc.cs)
- string Id
- string Name
- Color ChatColor
- bool Enabled
- LanguageOutput Translate(string phrase, int proficiency)

## Jorteck.Toolbox.Features.Languages.LanguageRashemi  [class]  (Features/Languages/Translations/LanguageRashemi.cs)
- string Id
- string Name
- Color ChatColor
- bool Enabled
- LanguageOutput Translate(string phrase, int proficiency)

## Jorteck.Toolbox.Features.Languages.LanguageSylvan  [class]  (Features/Languages/Translations/LanguageSylvan.cs)
- string Id
- string Name
- Color ChatColor
- bool Enabled
- LanguageOutput Translate(string phrase, int proficiency)

## Jorteck.Toolbox.Features.Languages.LanguageThievesCant  [class]  (Features/Languages/Translations/LanguageThievesCant.cs)
- string Id
- string Name
- string[] Aliases
- Color ChatColor
- bool Enabled
- LanguageOutput Translate(string phrase, int proficiency)

## Jorteck.Toolbox.Features.Languages.LanguageUndercommon  [class]  (Features/Languages/Translations/LanguageUndercommon.cs)
- string Id
- string[] Aliases
- string Name
- Color ChatColor
- bool Enabled
- LanguageOutput Translate(string phrase, int proficiency)

## Jorteck.Toolbox.Features.Permissions.PermissionSet  [class]  (Features/Permissions/Config/PermissionSet.cs)
- HashSet<string> Permissions
- HashSet<string> WildcardPermissions

## Jorteck.Toolbox.Features.Permissions.DMPermissionConstants  [class]  (Features/Permissions/DMPermissionConstants.cs)
- const string ChatShout = "chat.shout"
- const string TargetSelf = ".self"
- const string TargetCreature = ".creature"
- const string TargetPlayer = ".player"
- const string TargetItem = ".item"
- const string TargetEncounter = ".encounter"
- const string TargetWaypoint = ".waypoint"
- const string TargetTrigger = ".trigger"
- const string TargetDoor = ".door"
- const string TargetPlaceable = ".placeable"
- const string TargetStore = ".store"
- const string PlayerDMLogin = "playerdm.login"
- const string PlayerDMForceLogin = "playerdm.forcelogin"
- const string PlayerDMLogout = "playerdm.logout"
- const string DMGiveGold = "dm.give.gold"
- const string DMGiveXp = "dm.give.xp"
- const string DMGiveLevel = "dm.give.level"
- const string DMGiveAlignment = "dm.give.alignment"
- const string DMGiveItem = "dm.give.item"
- const string DMSpawn = "dm.spawn"
- const string DMHeal = "dm.heal"
- const string DMKill = "dm.kill"
- const string DMInvulnerable = "dm.invulnerable"
- const string DMForceRest = "dm.forcerest"
- const string DMImmortal = "dm.immortal"
- const string DMLimbo = "dm.limbo"
- const string DMToggleAI = "dm.toggleai"
- const string DMGoTo = "dm.goto"
- const string DMPossess = "dm.possess"
- const string DMPossessFullPower = "dm.possess.full"
- const string DMToggleLock = "dm.lock.toggle"
- const string DMDisableTrap = "dm.trap.disable"
- const string DMJump = "dm.jump"
- const string DMJumpAllPlayers = "dm.jump.allplayers"
- const string DMChangeDifficulty = "dm.changedifficulty"
- const string DMViewInventory = "dm.viewinventory"
- const string DMSpawnTrap = "dm.spawntrap"
- const string DMGetLocal = "dm.local.get"
- const string DMSetLocal = "dm.local.set"
- const string DMDumpLocals = "dm.local.dump"
- const string DMAppear = "dm.appear"
- const string DMDisappear = "dm.disappear"
- const string DMSetFaction = "dm.faction.set"
- const string DMGetFactionReputation = "dm.faction.getreputation"
- const string DMSetFactionReputation = "dm.faction.setreputation"
- const string DMTakeItem = "dm.takeitem"
- const string DMSetStat = "dm.setstat"
- const string DMSetTime = "dm.time.settime"
- const string DMSetDate = "dm.time.setdate"

## Jorteck.Toolbox.Features.Permissions.PermissionsService  [class]  (Features/Permissions/PermissionsService.cs)
- bool IsEnabled
- bool HasPermission(NwPlayer player, string permission, bool defaultIfDisabled = false)
- IEnumerable<string> GetGroups(NwPlayer player, bool includeDefault = true)

## Jorteck.Toolbox.Features.ServerRestart.DelayResetCommand  [class]  (Features/ServerRestart/ChatCommands/DelayResetCommand.cs)
- string Command
- Range ArgCount
- bool DMOnly
- bool IsAvailable
- string Description
- CommandUsage[] Usages
- void ProcessCommand(NwPlayer caller, IReadOnlyList<string> args)

## Jorteck.Toolbox.Features.ServerRestart.GetResetTimeCommand  [class]  (Features/ServerRestart/ChatCommands/GetResetTimeCommand.cs)
- string Command
- Range ArgCount
- bool DMOnly
- bool IsAvailable
- string Description
- CommandUsage[] Usages
- void ProcessCommand(NwPlayer caller, IReadOnlyList<string> args)

## Jorteck.Toolbox.Features.ServerRestart.SetResetTime  [class]  (Features/ServerRestart/ChatCommands/SetResetTime.cs)
- string Command
- Range ArgCount
- bool DMOnly
- bool IsAvailable
- string Description
- CommandUsage[] Usages
- void ProcessCommand(NwPlayer caller, IReadOnlyList<string> args)

## Jorteck.Toolbox.Features.ServerRestart.ServerRestartService  [class]  (Features/ServerRestart/ServerRestartService.cs)
- TimeSpan TimeUntilRestart
- bool IsEnabled
- void SendRestartTimeMessageToAllPlayers()
- void SendRestartTimeMessageToPlayer(NwPlayer player)

## Jorteck.Toolbox.Features.ToolWindows.CreaturePropertiesBasicWindowController  [class]  (Features/ToolWindows/CreatureTools/CreaturePropertiesBasicWindowController.cs)
- override void Init()
- override void ProcessEvent(ModuleEvents.OnNuiEvent eventData)
- protected override void OnClose()

## Jorteck.Toolbox.Features.ToolWindows.CreaturePropertiesBasicWindowView  [class]  (Features/ToolWindows/CreatureTools/CreaturePropertiesBasicWindowView.cs)
- override string Id
- override string Title
- override NuiWindow WindowTemplate
- override IWindowController CreateDefaultController(NwPlayer player)
- readonly NuiBind<bool> NameEnabled = new NuiBind<bool>("name")
- readonly NuiBind<bool> TagEnabled = new NuiBind<bool>("tag")
- readonly NuiBind<bool> RaceEnabled = new NuiBind<bool>("race")
- readonly NuiBind<bool> AppearanceEnabled = new NuiBind<bool>("appearance")
- readonly NuiBind<bool> PhenotypeEnabled = new NuiBind<bool>("phenotype")
- readonly NuiBind<bool> GenderEnabled = new NuiBind<bool>("gender")
- readonly NuiBind<bool> DescriptionEnabled = new NuiBind<bool>("description")
- readonly NuiBind<bool> PortraitEnabled = new NuiBind<bool>("portrait")
- readonly NuiBind<bool> DialogEnabled = new NuiBind<bool>("dialog")
- readonly NuiBind<bool> CREnabled = new NuiBind<bool>("cr")
- readonly NuiBind<bool> SaveEnabled = new NuiBind<bool>("save")
- readonly NuiBind<string> Name = new NuiBind<string>("name_val")
- readonly NuiBind<string> Tag = new NuiBind<string>("tag_val")
- readonly NuiBind<string> Race = new NuiBind<string>("race_val")
- readonly NuiBind<string> Appearance = new NuiBind<string>("appearance_val")
- readonly NuiBind<string> Phenotype = new NuiBind<string>("phenotype_val")
- readonly NuiBind<int> Gender = new NuiBind<int>("gender_val")
- readonly NuiBind<string> Description = new NuiBind<string>("description_val")
- readonly NuiBind<string> Portrait = new NuiBind<string>("portrait_val")
- readonly NuiBind<string> PortraitPreview = new NuiBind<string>("portrait_prev")
- readonly NuiBind<string> Dialog = new NuiBind<string>("dialog_val")
- readonly NuiBind<string> CR = new NuiBind<string>("cr_val")
- readonly NuiButton SelectCreatureButton
- readonly NuiButton SaveChangesButton
- readonly NuiButton DiscardChangesButton
- CreaturePropertiesBasicWindowView()

## Jorteck.Toolbox.Features.ToolWindows.CreaturePropertiesStatsWindowController  [class]  (Features/ToolWindows/CreatureTools/CreaturePropertiesStatsWindowController.cs)
- override void Init()
- override void ProcessEvent(ModuleEvents.OnNuiEvent eventData)
- protected override void OnClose()

## Jorteck.Toolbox.Features.ToolWindows.CreaturePropertiesStatsWindowView  [class]  (Features/ToolWindows/CreatureTools/CreaturePropertiesStatsWindowView.cs)
- override string Id
- override string Title
- override NuiWindow WindowTemplate
- override IWindowController CreateDefaultController(NwPlayer player)
- readonly NuiGroup AbilityScoreListContainer
- readonly NuiGroup SavesListContainer
- readonly NuiGroup ACListContainer
- readonly NuiGroup HitPointsListContainer
- readonly NuiGroup SpeedContainer
- readonly NuiBind<bool> StrengthScoreRawEnabled = new NuiBind<bool>("strength_score_raw")
- readonly NuiBind<bool> DexterityScoreRawEnabled = new NuiBind<bool>("dexterity_score_raw")
- readonly NuiBind<bool> ConstitutionScoreRawEnabled = new NuiBind<bool>("constitution_score_raw")
- readonly NuiBind<bool> IntelligenceScoreRawEnabled = new NuiBind<bool>("intelligence_score_raw")
- readonly NuiBind<bool> WisdomScoreRawEnabled = new NuiBind<bool>("wisdom_score_raw")
- readonly NuiBind<bool> CharismaScoreRawEnabled = new NuiBind<bool>("charisma_score_raw")
- readonly NuiBind<bool> FortitudeBaseEnabled = new NuiBind<bool>("fortitude_base")
- readonly NuiBind<bool> ReflexBaseEnabled = new NuiBind<bool>("reflex_base")
- readonly NuiBind<bool> WillBaseEnabled = new NuiBind<bool>("will_base")
- readonly NuiBind<bool> NaturalACEnabled = new NuiBind<bool>("natural_ac")
- readonly NuiBind<bool> BaseHitPointsEnabled = new NuiBind<bool>("base_hit_points")
- readonly NuiBind<bool> MovementRateEnabled = new NuiBind<bool>("movement_rate")
- readonly NuiBind<bool> SaveEnabled = new NuiBind<bool>("save")
- readonly NuiBind<string> StrengthScoreRaw = new NuiBind<string>("strength_score_raw_val")
- readonly NuiBind<string> StrengthScoreRacial = new NuiBind<string>("strength_score_racial_val")
- readonly NuiBind<string> StrengthScoreTotal = new NuiBind<string>("strength_score_total_val")
- readonly NuiBind<string> StrengthScoreMod = new NuiBind<string>("strength_score_mod_val")
- readonly NuiBind<string> DexterityScoreRaw = new NuiBind<string>("dexterity_score_raw_val")
- readonly NuiBind<string> DexterityScoreRacial = new NuiBind<string>("dexterity_score_racial_val")
- readonly NuiBind<string> DexterityScoreTotal = new NuiBind<string>("dexterity_score_total_val")
- readonly NuiBind<string> DexterityScoreMod = new NuiBind<string>("dexterity_score_mod_val")
- readonly NuiBind<string> ConstitutionScoreRaw = new NuiBind<string>("constitution_score_raw_val")
- readonly NuiBind<string> ConstitutionScoreRacial = new NuiBind<string>("constitution_score_racial_val")
- readonly NuiBind<string> ConstitutionScoreTotal = new NuiBind<string>("constitution_score_total_val")
- readonly NuiBind<string> ConstitutionScoreMod = new NuiBind<string>("constitution_score_mod_val")
- readonly NuiBind<string> IntelligenceScoreRaw = new NuiBind<string>("intelligence_score_raw_val")
- readonly NuiBind<string> IntelligenceScoreRacial = new NuiBind<string>("intelligence_score_racial_val")
- readonly NuiBind<string> IntelligenceScoreTotal = new NuiBind<string>("intelligence_score_total_val")
- readonly NuiBind<string> IntelligenceScoreMod = new NuiBind<string>("intelligence_score_mod_val")
- readonly NuiBind<string> WisdomScoreRaw = new NuiBind<string>("wisdom_score_raw_val")
- readonly NuiBind<string> WisdomScoreRacial = new NuiBind<string>("wisdom_score_racial_val")
- readonly NuiBind<string> WisdomScoreTotal = new NuiBind<string>("wisdom_score_total_val")
- readonly NuiBind<string> WisdomScoreMod = new NuiBind<string>("wisdom_score_mod_val")
- readonly NuiBind<string> CharismaScoreRaw = new NuiBind<string>("charisma_score_raw_val")
- readonly NuiBind<string> CharismaScoreRacial = new NuiBind<string>("charisma_score_racial_val")
- readonly NuiBind<string> CharismaScoreTotal = new NuiBind<string>("charisma_score_total_val")
- readonly NuiBind<string> CharismaScoreMod = new NuiBind<string>("charisma_score_mod_val")
- readonly NuiBind<string> FortitudeBase = new NuiBind<string>("fortitude_base_val")
- readonly NuiBind<string> FortitudeBonus = new NuiBind<string>("fortitude_bonus_val")
- readonly NuiBind<string> FortitudeTotal = new NuiBind<string>("fortitude_total_val")
- readonly NuiBind<string> ReflexBase = new NuiBind<string>("reflex_base_val")
- readonly NuiBind<string> ReflexBonus = new NuiBind<string>("reflex_bonus_val")
- readonly NuiBind<string> ReflexTotal = new NuiBind<string>("reflex_total_val")
- readonly NuiBind<string> WillBase = new NuiBind<string>("will_base_val")
- readonly NuiBind<string> WillBonus = new NuiBind<string>("will_bonus_val")
- readonly NuiBind<string> WillTotal = new NuiBind<string>("will_total_val")
- readonly NuiBind<string> NaturalAC = new NuiBind<string>("natural_ac_val")
- readonly NuiBind<string> DexterityAC = new NuiBind<string>("dexterity_ac_val")
- readonly NuiBind<string> SizeModifierAC = new NuiBind<string>("size_modifier_ac")
- readonly NuiBind<string> TotalAC = new NuiBind<string>("total_ac_val")
- readonly NuiBind<string> BaseHitPoints = new NuiBind<string>("base_hit_points_val")
- readonly NuiBind<string> BonusHitPoints = new NuiBind<string>("bonus_hit_points_val")
- readonly NuiBind<string> TotalHitPoints = new NuiBind<string>("total_hit_points_val")
- readonly NuiBind<int> MovementRate = new NuiBind<int>("movement_rate_val")
- readonly NuiButton SelectCreatureButton
- readonly NuiButton SaveChangesButton
- readonly NuiButton DiscardChangesButton
- CreaturePropertiesStatsWindowView()

## Jorteck.Toolbox.Features.ToolWindows.ChatImpersonatorWindowController  [class]  (Features/ToolWindows/ObjectTools/ChatImpersonatorWindowController.cs)
- override void Init()
- override void ProcessEvent(ModuleEvents.OnNuiEvent eventData)
- protected override void OnClose()

## Jorteck.Toolbox.Features.ToolWindows.ChatImpersonatorWindowView  [class]  (Features/ToolWindows/ObjectTools/ChatImpersonatorWindowView.cs)
- override string Id
- override string Title
- override NuiWindow WindowTemplate
- readonly NuiBind<string> ChatHistory = new NuiBind<string>("chat_history")
- readonly NuiBind<string> Message = new NuiBind<string>("message")
- readonly NuiBind<List<NuiComboEntry>> Languages = new NuiBind<List<NuiComboEntry>>("languages")
- readonly NuiBind<string> WindowTitle = new NuiBind<string>("title")
- readonly NuiBind<int> SelectedChatVolume = new NuiBind<int>("selected_chat_volume")
- readonly NuiBind<int> SelectedLanguage = new NuiBind<int>("selected_language")
- readonly NuiBind<bool> LanguagesEnabled = new NuiBind<bool>("language_enable")
- readonly NuiButton SendButton
- readonly NuiButtonImage SelectObjectButton
- override IWindowController CreateDefaultController(NwPlayer player)
- ChatImpersonatorWindowView()

## Jorteck.Toolbox.Features.ToolWindows.ChooserWindowController  [class]  (Features/ToolWindows/ObjectTools/ChooserWindowController.cs)
- override void Init()
- void Init(NwArea area)
- override void ProcessEvent(ModuleEvents.OnNuiEvent eventData)
- protected override void OnClose()

## Jorteck.Toolbox.Features.ToolWindows.ChooserWindowView  [class]  (Features/ToolWindows/ObjectTools/ChooserWindowView.cs)
- override string Id
- override string Title
- override NuiWindow WindowTemplate
- override IWindowController CreateDefaultController(NwPlayer player)
- readonly ObjectSelectionListView SelectionListView
- readonly NuiButtonImage GoToButton
- readonly NuiButtonImage DestroyButton
- readonly NuiButtonImage JumpButton
- readonly NuiButtonImage ToggleAIButton
- readonly NuiButtonImage HealButton
- readonly NuiButtonImage ControlButton
- readonly NuiButtonImage RestButton
- readonly NuiButtonImage LimboButton
- readonly NuiButtonImage ExamineButton
- readonly NuiButtonImage PossessButton
- readonly NuiButtonImage ToggleImmortalButton
- readonly NuiButtonImage TogglePlotModeButton
- readonly NuiButtonImage CloneButton
- readonly NuiBind<bool> GoToButtonEnabled = new NuiBind<bool>("goto")
- readonly NuiBind<bool> DestroyButtonEnabled = new NuiBind<bool>("kill")
- readonly NuiBind<bool> JumpButtonEnabled = new NuiBind<bool>("jump")
- readonly NuiBind<bool> ToggleAIButtonEnabled = new NuiBind<bool>("ai")
- readonly NuiBind<bool> HealButtonEnabled = new NuiBind<bool>("heal")
- readonly NuiBind<bool> ControlButtonEnabled = new NuiBind<bool>("control")
- readonly NuiBind<bool> RestButtonEnabled = new NuiBind<bool>("rest")
- readonly NuiBind<bool> LimboButtonEnabled = new NuiBind<bool>("limbo")
- readonly NuiBind<bool> ExamineButtonEnabled = new NuiBind<bool>("examine")
- readonly NuiBind<bool> PossessButtonEnabled = new NuiBind<bool>("possess")
- readonly NuiBind<bool> ToggleImmortalButtonEnabled = new NuiBind<bool>("immortal")
- readonly NuiBind<bool> TogglePlotButtonEnabled = new NuiBind<bool>("god")
- readonly NuiBind<bool> CloneButtonEnabled = new NuiBind<bool>("clone")
- readonly NuiBind<bool>[] AllButtonStates
- ChooserWindowView()

## Jorteck.Toolbox.Features.ToolWindows.CreatorWindowController  [class]  (Features/ToolWindows/ObjectTools/CreatorWindowController.cs)
- BlueprintManager BlueprintManager
- override void Init()
- override void ProcessEvent(ModuleEvents.OnNuiEvent eventData)
- protected override void OnClose()

## Jorteck.Toolbox.Features.ToolWindows.CreatorWindowView  [class]  (Features/ToolWindows/ObjectTools/CreatorWindowView.cs)
- readonly string BlueprintRowId = "rows"
- override string Id
- override string Title
- override NuiWindow WindowTemplate
- override IWindowController CreateDefaultController(NwPlayer player)
- readonly NuiBind<string> Search = new NuiBind<string>("search_val")
- readonly NuiBind<int> BlueprintType = new NuiBind<int>("type_val")
- readonly NuiBind<Color> RowColors = new NuiBind<Color>("row_colors")
- readonly NuiBind<string> BlueprintNamesAndCategories = new NuiBind<string>("names_val")
- readonly NuiBind<string> BlueprintCRs = new NuiBind<string>("crs_val")
- readonly NuiBind<string> BlueprintFactions = new NuiBind<string>("factions_val")
- readonly NuiBind<int> BlueprintCount = new NuiBind<int>("count")
- readonly NuiButtonImage SearchButton
- readonly NuiButton CreateButton
- readonly NuiBind<bool> CreateButtonEnabled = new NuiBind<bool>("create")
- CreatorWindowView()

## Jorteck.Toolbox.Features.ToolWindows.VisualTransformWindowController  [class]  (Features/ToolWindows/ObjectTools/VisualTransformWindowController.cs)
- override void Init()
- override void ProcessEvent(ModuleEvents.OnNuiEvent eventData)
- protected override void OnClose()

## Jorteck.Toolbox.Features.ToolWindows.VisualTransformWindowView  [class]  (Features/ToolWindows/ObjectTools/VisualTransformWindowView.cs)
- override string Id
- override string Title
- override NuiWindow WindowTemplate
- override IWindowController CreateDefaultController(NwPlayer player)
- readonly NuiBind<bool> ValidObjectSelected = new NuiBind<bool>("obj_valid")
- readonly NuiBind<float> TranslationX = new NuiBind<float>("vt_trans_x")
- readonly NuiBind<float> TranslationY = new NuiBind<float>("vt_trans_y")
- readonly NuiBind<float> TranslationZ = new NuiBind<float>("vt_trans_z")
- readonly NuiBind<float> RotationX = new NuiBind<float>("vt_rot_x")
- readonly NuiBind<float> RotationY = new NuiBind<float>("vt_rot_y")
- readonly NuiBind<float> RotationZ = new NuiBind<float>("vt_rot_z")
- readonly NuiBind<float> Scale = new NuiBind<float>("vt_scale")
- readonly NuiBind<float> AnimSpeed = new NuiBind<float>("vt_animspeed")
- readonly NuiBind<string> TranslationXStr = new NuiBind<string>("vt_trans_x_str")
- readonly NuiBind<string> TranslationYStr = new NuiBind<string>("vt_trans_y_str")
- readonly NuiBind<string> TranslationZStr = new NuiBind<string>("vt_trans_z_str")
- readonly NuiBind<string> RotationXStr = new NuiBind<string>("vt_rot_x_str")
- readonly NuiBind<string> RotationYStr = new NuiBind<string>("vt_rot_y_str")
- readonly NuiBind<string> RotationZStr = new NuiBind<string>("vt_rot_z_str")
- readonly NuiBind<string> ScaleStr = new NuiBind<string>("vt_scale_str")
- readonly NuiBind<string> AnimSpeedStr = new NuiBind<string>("vt_animspeed_str")
- readonly NuiButton SelectObjectButton
- VisualTransformWindowView()

## Jorteck.Toolbox.Features.ToolWindows.PlayerAppearanceWindowController  [class]  (Features/ToolWindows/PlayerTools/PlayerAppearanceWindowController.cs)
- override void Init()
- override void ProcessEvent(ModuleEvents.OnNuiEvent eventData)
- protected override void OnClose()

## Jorteck.Toolbox.Features.ToolWindows.PlayerAppearanceWindowView  [class]  (Features/ToolWindows/PlayerTools/PlayerAppearanceWindowView.cs)
- override string Id
- override string Title
- override NuiWindow WindowTemplate
- override IWindowController CreateDefaultController(NwPlayer player)
- readonly NuiBind<bool> PortraitEnabled = new NuiBind<bool>("portrait")
- readonly NuiBind<bool> SoundSetEnabled = new NuiBind<bool>("voice_set")
- readonly NuiBind<bool> AppearanceEnabled = new NuiBind<bool>("appearance")
- readonly NuiBind<bool> SaveEnabled = new NuiBind<bool>("save")
- readonly NuiBind<string> PlayerName = new NuiBind<string>("player_name_val")
- readonly NuiBind<string> CreatureName = new NuiBind<string>("creature_name_val")
- readonly NuiBind<string> Portrait = new NuiBind<string>("portrait_val")
- readonly NuiBind<string> PortraitPreview = new NuiBind<string>("portrait_prev")
- readonly NuiBind<string> SoundSet = new NuiBind<string>("sound_set")
- readonly NuiBind<string> Appearance = new NuiBind<string>("appearance_val")
- readonly NuiButton SelectPlayerButton
- readonly NuiButton SaveChangesButton
- readonly NuiButton DiscardChangesButton
- PlayerAppearanceWindowView()

## Jorteck.Toolbox.Features.ToolWindows.PlayerVitalsWindowController  [class]  (Features/ToolWindows/PlayerTools/PlayerVitalsWindowController.cs)
- override void Init()
- override void ProcessEvent(ModuleEvents.OnNuiEvent eventData)
- protected override void OnClose()

## Jorteck.Toolbox.Features.ToolWindows.PlayerVitalsWindowView  [class]  (Features/ToolWindows/PlayerTools/PlayerVitalsWindowView.cs)
- override string Id
- override string Title
- override NuiWindow WindowTemplate
- override IWindowController CreateDefaultController(NwPlayer player)
- readonly NuiBind<bool> FirstNameEnabled = new NuiBind<bool>("first_name")
- readonly NuiBind<bool> LastNameEnabled = new NuiBind<bool>("last_name")
- readonly NuiBind<bool> GenderEnabled = new NuiBind<bool>("gender")
- readonly NuiBind<bool> RaceEnabled = new NuiBind<bool>("race")
- readonly NuiBind<bool> SubRaceEnabled = new NuiBind<bool>("subrace")
- readonly NuiBind<bool> AgeEnabled = new NuiBind<bool>("age")
- readonly NuiBind<bool> DeityEnabled = new NuiBind<bool>("deity")
- readonly NuiBind<bool> DescriptionEnabled = new NuiBind<bool>("description")
- readonly NuiBind<bool> SaveEnabled = new NuiBind<bool>("save")
- readonly NuiBind<string> PlayerName = new NuiBind<string>("player_name_val")
- readonly NuiBind<string> FirstName = new NuiBind<string>("first_name_val")
- readonly NuiBind<string> LastName = new NuiBind<string>("last_name_val")
- readonly NuiBind<int> Gender = new NuiBind<int>("gender_val")
- readonly NuiBind<string> Race = new NuiBind<string>("race_val")
- readonly NuiBind<string> SubRace = new NuiBind<string>("subrace_val")
- readonly NuiBind<string> Age = new NuiBind<string>("age_val")
- readonly NuiBind<string> Deity = new NuiBind<string>("deity_val")
- readonly NuiBind<string> Description = new NuiBind<string>("description_val")
- readonly NuiButton SelectPlayerButton
- readonly NuiButton SaveChangesButton
- readonly NuiButton DiscardChangesButton
- PlayerVitalsWindowView()

## Jorteck.Toolbox.Features.ToolWindows.ToolboxWindowButtonController  [class]  (Features/ToolWindows/Toolbox/ToolboxWindowButtonController.cs)
- Lazy<WindowManager> WindowManager
- override void Init()
- override void ProcessEvent(ModuleEvents.OnNuiEvent eventData)
- protected override void OnClose()

## Jorteck.Toolbox.Features.ToolWindows.ToolboxWindowButtonInitializer  [class]  (Features/ToolWindows/Toolbox/ToolboxWindowButtonInitializer.cs)
- void Init()

## Jorteck.Toolbox.Features.ToolWindows.ToolboxWindowButtonView  [class]  (Features/ToolWindows/Toolbox/ToolboxWindowButtonView.cs)
- override string Id
- override string Title
- override NuiWindow WindowTemplate
- override bool ListInToolbox
- override IWindowController CreateDefaultController(NwPlayer player)
- readonly NuiButton Button
- readonly NuiBind<NuiRect> ButtonGeometry = new NuiBind<NuiRect>("btn_geo")
- ToolboxWindowButtonView()

## Jorteck.Toolbox.Features.ToolWindows.ToolboxWindowController  [class]  (Features/ToolWindows/Toolbox/ToolboxWindowController.cs)
- override void Init()
- override void ProcessEvent(ModuleEvents.OnNuiEvent eventData)
- protected override void OnClose()

## Jorteck.Toolbox.Features.ToolWindows.ToolboxWindowView  [class]  (Features/ToolWindows/Toolbox/ToolboxWindowView.cs)
- override string Id
- override string Title
- override NuiWindow WindowTemplate
- override bool ListInToolbox
- override IWindowController CreateDefaultController(NwPlayer player)
- readonly NuiBind<string> Search = new NuiBind<string>("search_val")
- readonly NuiBind<string> WindowNames = new NuiBind<string>("win_names")
- readonly NuiBind<int> WindowCount = new NuiBind<int>("window_count")
- readonly NuiButtonImage SearchButton
- readonly NuiButtonImage OpenWindowButton
- ToolboxWindowView()
