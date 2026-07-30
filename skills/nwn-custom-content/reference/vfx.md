# Custom Visual Effects (VFX)

Sources: https://nwn.wiki/spaces/NWN1/pages/38175069/visualeffects.2da · https://nwn.wiki/spaces/NWN1/pages/38175071/progfx.2da · https://nwn.wiki/spaces/NWN1/pages/38176565/Player+and+Creature+Accessories+Using+ProgFX+Type+12 · https://nwn.wiki/display/NWN1/Visual+Effect+Editing · https://nwnlexicon.com/EffectVisualEffect · https://gist.github.com/mtijanic/97f309b8d9262f0cf4f7dfba6618ea6a (Beamdog's own progfx.2da doc, more compact than the wiki's)

A VFX is a `visualeffects.2da` row that ties together a model, sounds, and (since patch 1.80.8193.14) "progfx" parameters that used to be hardcoded. Two layers matter: `visualeffects.2da` (which node/impact/duration/cessation slots fire, and legacy fixed attachment points) and `progfx.2da` (typed parameter blocks — this is where color, node-attachment, and most other tunable behavior actually lives). Model-level `.mdl` editing is only needed for genuinely new geometry/particle art, not for color or attachment tweaks to existing VFX.

## Quick answers

- **Color**: yes, without touching any model — `progfx.2da` Types 3, 5, and 6 take raw RGB float parameters (0.0–1.0) directly. Type 4 (colored light) uses named preset color models instead of raw RGB. For genuinely custom particle VFX, color also lives in the `.mdl` emitter's `colorStart`/`colorEnd` properties.
- **Size**: yes, but it's a script-time parameter, not a 2DA column — `EffectVisualEffect()`'s `fScale` argument (EE-only, default 1.0) scales any visualeffects.2da line per-application. `vTranslate`/`vRotate` on the same function offset position/rotation.
- **Attachment point**: yes — `progfx.2da` Type 12 lets you name *any* dummy or trimesh node in the target model as the attachment point (Param1 = node name, Param2 = VFX model to play there). This superseded the old fixed set of attachment points (`Imp_HeadCon_Node`, `Imp_Impact_Node`, `Imp_Root_[S/M/L/H]_Node`) still present directly on `visualeffects.2da`.

## visualeffects.2da — the outer wrapper

Every VFX is one row here. Key columns:

| Column | Purpose |
|---|---|
| `Label` | Human-readable name, often the nwscript.nss constant |
| `Type_FD` | F (fire-and-forget/instant), D (duration), P (projectile/MIRV, always instant), B (beam) — affects how the engine treats duration and whether it's beam/projectile in nature |
| `Imp_HeadCon_Node` / `Imp_Impact_Node` / `Imp_Root_[S/M/L/H]_Node` | Legacy fixed attachment points: head, body-center, and size-appropriate root-dummy. Pre-EE mechanism, still works, but superseded by progfx Type 12 for arbitrary nodes |
| `ProgFX_Impact` / `ProgFX_Duration` / `ProgFX_Cessation` | Line references into `progfx.2da`, fired once-on-apply / continuously-while-active / once-on-removal respectively. This is where the real behavior configuration happens |
| `ShakeType` / `ShakeDelay` / `ShakeDuration` | Optional camera shake (1 = one-off bump, 2 = a duration of larger bumps) |
| `LowViolence` / `LowQuality` | Override models for low-violence or low-graphics settings |
| `OrientWithGround` | Rarely used; orients VFX to sloped ground |
| `OrientWithObject` | Makes the VFX inherit the attached object's orientation (used for eyes, flags) — relevant when attaching to a node via Type 12 |
| `SoundImpact` / `SoundDuration` / `SoundCessastion` | Sound resrefs (note: the cessation column is misspelled in the actual 2DA — "Cessastion" not "Cessation" — you must match that misspelling or rename the column entirely for it to work) |

Note there's a separate exception: `vfx_persistent.2da` (used for area-of-effect/persistent VFX objects) generally **cannot** use progfx — only one hardcoded line (blade barrier) does.

## progfx.2da — where color, attachment, and behavior really live

Not "custom programming" — it's a parameter table for 13 fixed engine-understood "Types." Any progfx.2da line can be any type; the `Type` column is what matters, not the row's position (though by convention the base game groups them by hundreds, e.g. Type 3 starts around row 200, Type 5 around 400). You're free to add new rows anywhere — pad the file out to row 2000+ and use that range for all your custom lines to avoid clashing with future Beamdog/Ossian additions.

| Type | Name | What it does | Key params |
|---|---|---|---|
| 1 | Skin Overlay | Swaps the creature's texture to an overlay model (stoneskin, barkskin, etc.), optionally overriding hit-chunk VFX | Param1: overlay model name (`vdu_*`); Param2: weapon-sound armor type; Param3/4: chunk VFX override for medium/small creatures |
| 2 | Environment Map | Sets an env-map file on the model | Param1: envmap model name |
| 3 | Static Glow (SelfIllum) | Solid-color glow/highlight, same visual as tab-highlight | Param1–3: R/G/B floats 0.0–1.0 |
| 4 | Light Source | Colored dynamic light, via named preset models | Param1: animation name (e.g. `Blue_5m`); Param2: speed (negative = fade); Param3: casts shadows; Param4: priority (lower wins, used for vision-type conflicts); Param5: suppress near other lights; Param6: clear all scene lights while active; Param7: base light model (`fx_light_clr`) |
| 5 | Alpha Transparency | Transparency + optional glow color, optional pulse | Param1: lower-bound alpha; Param2–4: optional glow R/G/B (skipped if Param2 ≤ 0); Param5: pulse time in ms (0 = static); Param6: upper-bound alpha if pulsing |
| 6 | Pulsing Aura (SelfIllumPulse) | Pulses between two full RGB colors | Param1–3: color 1 R/G/B; Param4–6: color 2 R/G/B; Param7: ms to go color1→color2 (same time back) |
| 7 | Beam | Point-to-point emitter (Bezier/Gravity/Lightning) between a source and target, unhardcoding what were previously lightning-only beams | Param1: beam model resref; Param2: animation name to trigger on start |
| 8 | Delete Model | Hides the model | No real params; effectiveness/use cases are murky per community testing |
| 9 | Chunk Model | Ties to the engine's hardcoded gib/chunk system | No params — can't force a specific chunk |
| 10 | MIRV | Multiple simultaneous projectiles (Magic Missile, Acid Arrow style) | Param1: model; Param2: a **spells.2da line ID** (yes, really); Param3: orientation type; Param4: projectile path type (see constants below); Param5: timing calc (`log`/`linear`/`linear2`) |
| 11 | Cheat | Rarely relevant for custom content | Param1: model; Param2: impact sound; Param3: projectile type; Param4: initial sound |
| 12 | SpellVisual (node attachment) | **Attach a VFX to any named node on the target model** — the answer to "what part of an object" | Param1: target node name (any dummy/trimesh in the base phenotype, not in attached armor/weapons); Param2: VFX model to play there |
| 13 | Freeze Anim | Freezes the model's current animation frame | No documented params |

Projectile path types (Type 10, also usable as the `nProjectilePathType` param on `ActionCastSpellAtObject`/`AtLocation`): `DEFAULT`(0), `HOMING`(1), `BALLISTIC`(2), `HIGH_BALLISTIC`(3), `BURST_UP`(4), `ACCELERATING`(5), `SPIRAL`(6), `LINKED`(7), `BOUNCE`(8), `BURST`(9), `LINKED_BURST_UP`(10), `TRIPLE_BALLISTIC_HIT`(11), `TRIPLE_BALLISTIC_MISS`(12), `DOUBLE_BALLISTIC`(13).

## Building a node-attached VFX (Type 12) end to end

1. Get a model to attach (ring, accessory, small flame, etc.) — see the model-editing section below if building new, or reuse/adapt existing content.
2. Add a `progfx.2da` row with `Type` = 12, `Param1` = the target node name (e.g. `rhand`, or a custom node you've added to the phenotype file), `Param2` = your VFX model resref.
3. Add a `visualeffects.2da` row: `Type_FD` = D for a persistent accessory (F for an instant one-off), and point `ProgFX_Duration` (or `ProgFX_Impact`) at your new progfx.2da row ID.
4. Apply it in script the same as any VFX: `effect e = EffectVisualEffect(<visualeffects.2da line>); ApplyEffectToObject(DURATION_TYPE_PERMANENT, e, oTarget);`
5. If the base phenotype doesn't expose a node where you want one, add it directly to the four phenotype files (e.g. `pmh0.mdl`) and parent it to whatever existing node makes sense — this also lets you author the accessory model at position [0,0,0] so one model fits every race/gender instead of needing per-race offsets.

Known limits (from community testing): only nodes in the base phenotype are reachable — nodes inside attached armor, weapons, or other equipped parts are not. Danglymesh/skinmesh-animated nodes won't carry an attached VFX along with their vertex animation (it'll clip). If the target model doesn't have the named node, the VFX silently does nothing.

## Sizing (fScale) and positioning (vTranslate/vRotate)

`EffectVisualEffect()`'s full EE signature:

```
effect EffectVisualEffect(
    int nVisualEffectId,
    int nMissEffect = FALSE,
    float fScale = 1.0f,        // EE only — scales the VFX
    vector vTranslate = [0,0,0], // EE only — position offset
    vector vRotate = [0,0,0]     // EE only — rotation offset
);
```

This is the general mechanism for resizing/repositioning any VFX without a new 2DA line — call the same visualeffects.2da line with a different `fScale` for a bigger/smaller version. Untested/unconfirmed by the community as of the Type 12 writeup: whether `fScale` behaves the same for progfx Type-12 node-attached VFX as it does for normal ones — worth verifying directly if scale matters for an attachment use case.

Practical note on reapplying with a different transform: if you apply the *same* visualeffects.2da line ID again with a different transform while a duration version is already active, the client won't visibly update — `RemoveEffect()` first, then `DelayCommand(0.01, ...)` the new application.

## Building genuinely new VFX (model-level)

Covered by "Visual Effect Editing" on nwn.wiki. Two construction styles: actual animated geometry (rare, e.g. gate effects) or emitter-based particles (the vast majority). Emitters are hand-edited as ASCII `.mdl` text (Notepad++ or similar) — there's little benefit to a 3D editor since emitter parameters aren't previewable there.

- **Color**: set on the emitter node via `colorStart`/`colorEnd` (RGB triples). Use `blend Normal` instead of the default `blend Lighten` if you want true blacks/greys — `Lighten` mode can only brighten toward white and can't produce genuinely dark colors.
- **Iteration loop**: put the test `.mdl` in your development folder, edit, wait a second after it's not actively playing, and the game hot-reloads it. Force a reload via the Debug Panel (Ctrl+Shift+F12) → ResMan → Reload Models if it doesn't pick up automatically.
- **Compile when done**: run `compilemodel MODELNAME` in the console — compiled VFX load faster since they aren't kept in memory long after use.
- Prefer DDS textures over TGA (built-in mipmaps, smaller for equivalent quality, faster load); `cachedmodels.2da` (1.89.8193.37+) can preload VFX models/textures client-side.
- To dissect an existing Bioware VFX, extract it with NWN Explorer (or `nwn_resman_extract` — see `reference/neverwinter-nim-cli.md`) and decompile with `nwnmdlcomp` if it's in compiled form.

## Testing in-game

Quick script-window snippets (replace `100` with your visualeffects.2da line):

```
object oCaster = GetFirstPC();
object oTarget = GetNearestCreature(4, 1, oCaster);

// Instant, on a target
ApplyEffectToObject(DURATION_TYPE_INSTANT, EffectVisualEffect(100), oTarget);

// Duration, on a target
ApplyEffectToObject(DURATION_TYPE_PERMANENT, EffectVisualEffect(100), oTarget);

// Beam
ApplyEffectToObject(DURATION_TYPE_TEMPORARY, EffectBeam(100, oCaster, BODY_NODE_HAND), oTarget, 6.0);

// Instant, at a location
ApplyEffectAtLocation(DURATION_TYPE_INSTANT, EffectVisualEffect(100), GetLocation(oTarget));
```

For a spells.2da-driven VFX (e.g. testing MIRV/Type 10 setups): `ActionCastSpellAtObject(100, oTarget, 0, TRUE)` with `100` as the spells.2da line.

Duration-based VFX applied for testing wear off on rest (they're treated as magical).

## Known gotchas (from Beamdog issue tracker / community testing)

- VFX applied to placeables can become impossible to remove if the last player leaves the area or enters cutscene mode while it's active — reapply/remove around those transitions, or use `SetObjectVisualTransform()` to hide the placeable instead.
- A player moving in and out of range of a placeable with an active VFX can cause it to visually duplicate.
- `EffectLinkEffects()` containing *only* visual effects doesn't reliably work — combine with at least one non-visual effect.
- `nMissEffect = TRUE` (random near-miss location) is widely considered to look bad and is mostly superseded by using `vTranslate` for a controlled offset instead.
