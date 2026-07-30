# Custom Spells

Sources: https://nwn.wiki/spaces/NWN1/pages/38175046/spells.2da · https://nwn.wiki/spaces/NWN1/pages/38174848/Spells+and+Abilities · https://nwn.wiki/display/NWN1/Custom+Spellbooks+using+classes.2da+and+spells.2da

A "spell" in NWN is a script that fires with some metadata around it (icon, animations, targeting, saves) — all defined in one row of `spells.2da`. This file covers the process end to end and the axes you can vary.

## Core process

1. **Add a row to `spells.2da`** on an ID past the base game's reserved range (see the hardcoded-lines table below for IDs to never reuse). Required columns: `Label` (internal name, not shown in game), `Name` (TLK entry — the display name), `IconResRef`, `School`, `Range`, `VS`, and **`Innate`** (the fallback spell level — always fill this in even for non-spellbook abilities; blanking it causes save DC / spell resistance / dispel bugs). `SpellDesc` (TLK entry) is the in-game description text.
2. **Add the TLK entries** for `Name` and `SpellDesc` in a custom TLK (only one TLK per module — merge if combining with other custom content sources).
3. **Set casting presentation** (all optional, default to plausible-looking spell-like behavior if left blank): `ConjTime`/`ConjAnim` + `Conj*Visual`/`ConjSound*` for the "conjuring" phase, `CastAnim`/`CastTime`/`Cast*Visual`/`CastSound` for the release phase, `Proj`/`ProjModel`/`ProjType`/`ProjSpwnPoint`/`ProjSound`/`ProjOrientation` if it should travel as a projectile rather than resolve instantly.
4. **Write `ImpactScript`** (an .nss script, referenced without the extension) — fires once the spell successfully lands (after any projectile travel time; not at all if interrupted by a concentration failure). Typical structure:
   - Read the target: `GetSpellTargetObject()` / `GetSpellTargetLocation()`
   - Check metamagic: `GetMetaMagicFeat()` (Empower/Extend/Maximize — Still/Silent/Quicken are handled by the engine automatically)
   - Build effect(s) with the relevant `Effect*()` constructors
   - Apply with `ApplyEffectToObject()` / `ApplyEffectAtLocation()` — same construct-then-apply pattern as any other effect
   - Handle saving throws and spell resistance as needed for the spell's design (see nwn-nwscript-api skill for the general effect-application pattern; verify exact helper function signatures against NWN Lexicon before use)
5. **Wire it to a caster**, by one of:
   - Add it to an existing class's spell-level column in `spells.2da` (e.g. `Wiz_Sorc`, `Cleric`) at the desired level
   - Give it directly on a creature blueprint's special-abilities/innate spell list (works even for spells no class can normally cast)
   - Link it from a `feat.2da` line via the spell's `FeatID` column (for feat-triggered abilities)
   - Grant it through an item property (`iprp_spells.2da` for scrolls/wands, or the item on-hit "Cast Spell" property)
6. **Test**: memorize/cast in-game (or trigger the ability), check icon/VFX timing, and if it's meant to interact with saves/SR/counterspelling, confirm those actually apply (see UserType table below — this is the #1 thing that silently doesn't work as expected).

### Hardcoded spells.2da lines — never reuse these IDs

| Spell | ID | Why |
|---|---|---|
| HealingKit | 506 | Fires `OnSpellCastAt` for the Heal skill |
| SPELL_LESSER_DISPEL / DISPEL / GREATER_DISPEL / MORDENKAINENS_DISJUNCTION | 94 / 41 / 67 / 122 | Counterspell + On Hit: Dispel variants |
| SPELL_KNOCK | 93 | On Hit: Knock; also used by `DoDoorCommand`/`DoPlaceableCommand` |
| Wild Shape / Elemental Shape | 401–405 / 397–400 | Hardcoded into the feat's sub-feat system |
| SPELL_CONTROL_UNDEAD | 28 | Special exception for `EffectDominate()` vs. undead mind immunity |
| SPELL_DARKNESS / SHADOW_CON_DARKNESS | 36 / 345 | Special-cased for sight-state detection |
| Cure Wounds / Inflict Wounds | 31–35 / 431–435 | `GetHasSpell` special-cases this ID range for spontaneous casting |

## Where the variation comes from

### UserType — the biggest fork in the road

This changes which game mechanics apply at all, independent of anything else on the row:

| UserType | What it is | Saves / SR / concentration / counterspell / AoO | Notes |
|---|---|---|---|
| 1 — Spell | Full spell mechanics | All apply | Normal spellbook spells, also usable for monster-only "spells" (creature blueprint spell list, not in any class's book) |
| 2 — Special/Creature Ability | No concentration, no AoO, can't be counterspelled, no caster level (uses HD instead in the toolset, 1–15 range) | `ResistSpell()` fails and returns -1 (spell absorption/immunity are still checked) | Monster gazes, auras, cone/breath abilities |
| 3 — Feat | Hidden from the toolset entirely, tied to a `feat.2da` line via `FeatID` | Mostly doesn't work as a spell (by design) — no metamagic, no concentration, `ResistSpell()` broken | Turn Undead—style feat abilities; caster level = class level of the class the feat came from |
| 4 — Item/Other | No spell resistance; caster level comes from the item property | No AoO/concentration/spell-failure interaction | Rod of Wonder—style items, cutscene-only effects, cheat-cast-only spells kept out of the toolset |

### Targeting and area

- `TargetType` — bitwise: self(1)/creature(2)/area(4)/items(8)/door(16)/placeable(32)/trigger(64). **Always include items (8)** or the spell can't be put on a scroll via crafting.
- `TargetShape` + `TargetSizeX`/`TargetSizeY` — client-side AoE preview shape: `sphere`, `cone`, `rectangle`, `hsphere` (donut), or a custom integer if you supply your own shader. Purely cosmetic/predictive — doesn't affect actual game logic, so keep it in sync with what the script actually does.
- `TargetFlags` — bitwise, controls AoE marker color and self/ally/enemy semantics: Harms Enemies (1), Harms Allies (2), Helps Allies (4), Ignores Self (8), Origin on Self (16 — for cones/breaths), Suppress with Target (32 — hide AoE marker when a single target is hovered, e.g. Dispel Magic).

### Casting economy

- `ConjTime`/`CastTime` (milliseconds) — tunes how long the spell takes and how it interacts with Haste (halves conjure time) and Quicken (caps at 500ms or less).
- `MetaMagic` — bitwise, which of Empower(1)/Extend(2)/Maximize(4)/Quicken(8)/Silent(16)/Still(32) are legal on this spell. Only Empower/Maximize/Extend need handling in your script; the others are engine-handled.
- `UseConcentration` — whether interruption/concentration checks apply (doesn't affect attacks of opportunity, which are separate).
- `HostileSetting` — whether the spell is flagged hostile for AI/reaction purposes.
- `AltMessage` (TLK entry) — replaces the default "X casts Y" feedback and **skips the Spellcraft identification check** — useful for abilities you don't want identifiable as a specific known spell.

### Projectiles

`Proj` (has a traveling projectile at all) and `HasProjectile` (script waits for it to land) are separate flags — a breath weapon can have visual-only projectile VFX (`HasProjectile=1`) while firing its script immediately (`Proj=0`). `ProjType` gives eight distinct motion profiles: `homing`, `ballistic`, `accelerating`, `bounce`, `burst`, `highballistic`, `linked`, `spiral` — each with a different speed multiplier and arc.

### Bundling and counters

- `SubRadSpell1`–`8` (NWN:EE added 6–8) — bundle multiple spell variants under one radial-menu cast, the way Polymorph offers different forms from one spell slot. `Master` marks a spell as a sub-option of another.
- `Counter1`/`Counter2` — mark specific spells.2da lines as automatic, always-successful counters when counterspelling (bypassing a Dispel check).
- `SpontaneouslyCast` — lets a class substitute this spell the way Clerics swap a prepared spell for Cure/Inflict Wounds (domain spells memorized this way are exempt).

### Building custom caster classes (classes.2da)

NWN:EE unhardcoded spellbook columns, so you can design real caster archetypes, not just new spells:

| Column | Controls |
|---|---|
| `SpellGainTable` | Which `.2da` defines spell slots per level (can skip levels, cap max spell level, etc.) |
| `SpellKnownTable` | Spells known per level-up, for Sorcerer/Bard-style "known" casters |
| `MemorizesSpells` | 1 = prepare specific spells into slots (Wizard/Cleric); 0 = cast any known spell freely up to per-level uses (Sorcerer/Bard) |
| `SpellbookRestricted` | 0 = knows its entire spell list automatically (pure divine-style); 1 = must learn a subset (via `SpellKnownTable` and/or `LearnScroll`) |
| `PickDomains` / `PickSchool` | Cleric-domain-style or Wizard-school-style bonus picks |
| `LearnScroll` | Can learn from scrolls; also grants a fixed number of free spell picks per level-up (6 at level 1, 2 per level after) |
| `SpellcastingAbil` | Which ability score drives bonus slots and save DCs |
| `SpellTableColumn` | Which `spells.2da` column is this class's own spell list — **add a new column** (anywhere, usually at the end) for a genuinely custom spell list separate from existing classes |
| `CLMultiplier` | Caster level multiplier for level-capped classes (untested/possibly non-functional per community notes — verify in practice) |
| `MinCastingLevel` | Class level spellcasting starts at (e.g. Ranger/Paladin start at 4) |
| `MinAssociateLevel` | Animal Companion (divine) or Familiar (arcane) gate/level |
| `CanCastSpontaneously` | Enables the `Spontaneous` column substitution behavior |

Example archetypes this enables: a Sorcerer-style caster who knows their *entire* spellbook (`SpellbookRestricted=1`, `MemorizesSpells=0`, `SpellKnownTable` with every spell at every level), a scroll-only learner with no innate known spells, a low-level-cap class with a caster-level multiplier to stay relevant, or a divine caster who also learns from scrolls (`MemorizesSpells=1`, `SpellbookRestricted=1`, `LearnScroll=1`).

## Granting spells outside the class system

- **Feats**: link a `feat.2da` line to a `spells.2da` line via `FeatID`. For feats with sub-options (Wild Shape-style), see the Subfeat Spells approach on nwn.wiki.
- **Items**: `iprp_spells.2da` for scroll/wand/staff cast-spell properties; the on-hit "Cast Spell" item property for weapons. Note the innate level column in `iprp_spells.2da` is ignored by the game — caster level defaults to `10 + 3` regardless.
- **Creatures only**: put it directly on a blueprint's spell-like ability / innate list — works for spells not in any class's book, capped at caster level 15 (hardcoded, tied to network packet bit allocation).
- **Cheat-cast / DM-only**: `ActionCastSpell*` with the `bCheat` parameter — bypasses spellbook entirely, useful for boss mechanics or cutscene-only effects. Caster level defaults to `max(10, 2×Innate−1)` when cheat-cast.

## Verifying

Most of the subtle bugs here are about which mechanics silently don't apply (see the UserType table) rather than compile errors — there's no way to unit-test "does this actually get counterspelled correctly" except by testing in-game. When in doubt about an exact function signature for the impact script (`GetMetaMagicFeat`, `ResistSpell`, saving throw helpers, etc.), fetch the NWN Lexicon page per the nwn-nwscript-api skill's lookup rule rather than guessing — spellcasting functions are exactly the kind of similarly-named-but-different-signature case that skill warns about.
