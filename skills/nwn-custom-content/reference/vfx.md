# Custom Visual Effects (VFX)

Last reviewed: 2026-08. **nwn.wiki is canonical; this file is a navigation aid and will drift.** Where this file and the wiki disagree, the wiki wins.

Sources: https://nwn.wiki/spaces/NWN1/pages/38175069/visualeffects.2da · https://nwn.wiki/spaces/NWN1/pages/38175071/progfx.2da · https://nwn.wiki/spaces/NWN1/pages/38176565/Player+and+Creature+Accessories+Using+ProgFX+Type+12 · https://nwn.wiki/display/NWN1/Visual+Effect+Editing · https://nwn.wiki/display/NWN1/Models · https://nwn.wiki/spaces/NWN1/pages/12027273/MDL+ASCII · https://nwnlexicon.com/EffectVisualEffect · https://gist.github.com/mtijanic/97f309b8d9262f0cf4f7dfba6618ea6a (Beamdog's own progfx.2da doc, more compact than the wiki's)

Provenance markers used below: **[wiki]** = documented on nwn.wiki or Beamdog's docs. **[tested]** = confirmed by hands-on project work. **[unverified]** = plausible but unconfirmed; verify before relying on it.

A VFX is a `visualeffects.2da` row that ties together a model, sounds, and (since patch 1.80.8193.14) "progfx" parameters that used to be hardcoded. Two layers matter: `visualeffects.2da` (which node/impact/duration/cessation slots fire, and legacy fixed attachment points) and `progfx.2da` (typed parameter blocks — this is where node-attachment and most tunable behavior lives). Model-level `.mdl` editing is needed for genuinely new particle art **and** for recoloring an existing particle VFX — see the colour note below, which is the most commonly-got-wrong part of this system.

## Not covered here — resolve live before acting

Named gaps, because "when this isn't enough" is not something you can judge from a document that looks complete:

- **Binary `.mdl` decompiling.** The neverwinter.nim CLI has no model compiler or decompiler. Do not name a decompiler from memory — tool recommendations in this space go stale and the obvious old answer has incomplete EE support. Fetch https://nwn.wiki/display/NWN1/Models and its decompiling page and use whatever it currently recommends.
- **Anything requiring a running game client** (in-game hot-reload, console commands, visual confirmation). Not available to an agent — see "What you cannot verify" at the end.
- Tileset, creature-part, and armour-part model work; shader/material authoring. Different pages, different constraints.

## Quick answers

- **Color** **[tested]**: depends on *what* you want colored, and it's easy to get this backwards. `progfx.2da` Types 3, 5, 6 take raw RGB floats (0.0–1.0) and Type 4 uses named preset color models — but all of them tint **the model of the object receiving the effect** (creature selfillum/alpha, the tab-highlight look). They do *not* recolor the particle emitters of the model named in the `Imp_Root_*`/`Imp_*_Node` columns. To recolor an existing particle VFX (an aura ring, a glow burst), there is no 2DA route: clone the `.mdl` and edit the emitters' `colorStart`/`colorEnd`. See "Recoloring an existing particle VFX" below.
- **Size** **[wiki]**: yes, but it's a script-time parameter, not a 2DA column — `EffectVisualEffect()`'s `fScale` argument (EE-only, default 1.0) scales any visualeffects.2da line per-application. `vTranslate`/`vRotate` on the same function offset position/rotation. Caveat **[tested]**: these are arguments to *your* `EffectVisualEffect` call, so they're unavailable whenever the engine applies the visual for you — most notably a `vfx_persistent.2da` row's `DurationVFX` (see the AoE note under visualeffects.2da below). To regain them for an AoE, clear `DurationVFX` and apply the visual yourself onto the AoE's creator instead.
- **Attachment point** **[wiki]**: yes — `progfx.2da` Type 12 lets you name *any* dummy or trimesh node in the target model as the attachment point (Param1 = node name, Param2 = VFX model to play there). This superseded the old fixed set of attachment points (`Imp_HeadCon_Node`, `Imp_Impact_Node`, `Imp_Root_[S/M/L/H]_Node`) still present directly on `visualeffects.2da`.

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
| 3 | Static Glow (SelfIllum) | Solid-color glow/highlight on the *receiving object's own model*, same visual as tab-highlight | Param1–3: R/G/B floats 0.0–1.0 |
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

## Recoloring an existing particle VFX

The common ask ("same aura, different color"). **[tested]** end to end on an EE install.

**The whole workflow is text editing on ASCII `.mdl` source.** You never need to produce a compiled model: the engine loads ASCII `.mdl` directly and compiles it at load time **[wiki]**. Pre-compiling is a release-time performance optimisation, not a build step (see "Compiling" below).

**Step 0 — get ASCII source, and treat this as a precondition rather than a step you drive.** Extract the model with `nwn_resman_extract` (see `reference/neverwinter-nim-cli.md`), but note that stock VFX models ship *compiled binary*, and the neverwinter.nim CLI cannot decompile them. So:

- Resolve the current decompiler from https://nwn.wiki/display/NWN1/Models rather than from memory. **Do not assume the long-established, widely-mentioned tool is the right one** — as of this review the wiki flags it as only partially EE-updated, missing some EE model parameters, while recommending a newer CLI-capable alternative. This is exactly the trap described in the skill's tool-resolution rule.
- Fidelity warning: because decompilers differ in EE parameter coverage, **a round-trip that produces a same-size file does not prove fidelity** — parameters can be silently dropped. Confirm EE support from the wiki page instead of inventing a proxy check.
- If no usable decompiler is available in your environment, **stop and ask the user for the ASCII source.** Do not attempt to edit or guess at the binary, and do not improvise an install procedure.

Then:

1. **Rename every identifier**, not just the file **[tested]**: `newmodel`, `setsupermodel`, `beginmodelgeom`/`endmodelgeom`, `animroot`, and each `doneanim <name> <model>` all repeat the model name, and every one must match the resref. A blanket find/replace of the old name across the ASCII source is the safe move. Keep the resref ≤16 chars.
2. **Edit `colorStart`/`colorEnd` on every emitter node** **[tested]**. Watch for emitters whose `colorEnd` is `1 1 1` — that's a fade-to-white and will flash white unless you change it too.
3. **Ship the ASCII `.mdl` plus any new texture to *clients*** — hakpack or NWSync. A server-side override does nothing for rendering **[tested]**.
4. **Point the `visualeffects.2da` row's `Imp_Root_*`/`Imp_*_Node` column at the new resref.**

### Going dark: the `blend Normal` / alpha-channel trap

**[tested]**, and the single most expensive surprise in this workflow.

`blend Lighten` is additive, so dark colors render as nothing — a black or muted version of an existing VFX *requires* `blend Normal`. But most stock particle textures are **24-bit RGB with no alpha channel** (typically a soft white shape on black, authored for additive blending), and under `blend Normal` a texture without alpha draws each particle as an opaque square. So switching blend modes usually forces you to author a texture too.

The fix: produce a texture with **pure white RGB, and the original's luminance moved into the alpha channel**. The shape survives, and because RGB is white the emitter `colorStart`/`colorEnd` become the sole control over tint — every later recolor is then a model-only edit with no texture work.

That's a two-operation image edit (colorize to white; copy a greyscale/luminance copy of the original into alpha) achievable with any scriptable image library or CLI — pick whatever is present in the environment rather than assuming a specific tool. Requirements for the output:

- 32-bit RGBA TGA, uncompressed, alpha channel present and non-empty. Verify by extracting the alpha and inspecting it — a blank alpha silently renders as nothing.
- Carry over the original's `.txi` directives (e.g. `downsamplemax 0` / `downsamplemin 0`) but **drop any `blending additive` line**.
- Re-check `alphaStart`/`alphaEnd` on the emitters: values tuned for additive blending (0.7 is typical) read much denser under `Normal`, often as a solid band rather than smoke.

## Building genuinely new VFX (model-level)

Covered by "Visual Effect Editing" on nwn.wiki. Two construction styles: actual animated geometry (rare, e.g. gate effects) or emitter-based particles (the vast majority). Emitters are plain text in ASCII `.mdl` — a text editor is all that's needed, and a 3D editor buys little since emitter parameters aren't previewable there anyway.

- **Color**: set on the emitter node via `colorStart`/`colorEnd` (RGB triples). Use `blend Normal` instead of the default `blend Lighten` if you want true blacks/greys — `Lighten` mode is additive and can only brighten toward white. `Normal` additionally requires the texture to have an alpha channel; see the `blend Normal` trap above before switching.
- **Authoring format**: write and ship ASCII. Everything an agent needs to do here is text manipulation on ASCII `.mdl` source; no compile step is required for the content to work.
- Prefer DDS textures over TGA for finished content (built-in mipmaps, smaller for equivalent quality, faster load); `cachedmodels.2da` (1.89.8193.37+) can preload VFX models/textures client-side.
- To dissect an existing Bioware VFX, extract with `nwn_resman_extract` (see `reference/neverwinter-nim-cli.md`); stock models are compiled, so getting to ASCII needs a decompiler — see Step 0 of the recoloring section, and resolve the tool from the wiki rather than from recall.

### Compiling (optional, and not an agent task)

ASCII models work as shipped. Pre-compiling only reduces load-time cost, since the engine otherwise parses and compiles the text on every load — worth doing for released content with complex models, irrelevant during development **[wiki]**.

There are two routes, neither of which an agent should plan around. The in-game console (`compilemodel <name>`, plus compile-loaded-models variants) needs a running client, which an agent doesn't have. A standalone compiler would have to be identified per the tool-resolution rule — and isn't worth the trouble, since the gain is purely load-time.

So: ship ASCII, note that pre-compiling is available as a release optimisation, and never block delivery on it.

### Iterating (human-side)

The game hot-reloads a changed `.mdl` a second or so after it stops playing, and a reload can be forced from the in-game debug panel's ResMan section. This needs a running client, so it belongs to the user, not the agent — produce the edit, then hand off.

## Testing in-game (hand these to the user)

An agent cannot run these. Produce them as a test script for the user alongside the content, rather than describing the work as verified. Replace `100` with your visualeffects.2da line:

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

## What you cannot verify

VFX work is visual, and nothing here can be checked without rendering it. There is no compile error for "wrong colour", "invisible", or "opaque squares instead of smoke" — the failure modes are silent, and several of them (blank alpha channel, missing node name, dropped EE model parameters) produce *nothing on screen* rather than an error.

So: do not invent a proxy for visual verification, and do not report a VFX change as working. State what was changed, list the specific things most likely to be wrong (from the traps above), and hand over a test script. If a step needed a tool that wasn't available, say so plainly instead of routing around it.
