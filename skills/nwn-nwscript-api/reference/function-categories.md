# NWN Lexicon Function Categories

Source: https://nwnlexicon.com/Category:Functions (1,941 functions total across these categories; some functions appear in more than one).

Each category page (`https://nwnlexicon.com/Category:<Name>_Functions`) lists the individual function pages in it — browse there when you know the task but not the function name. Individual function pages are at `https://nwnlexicon.com/<FunctionName>`.

| Category | Page count | Category URL |
|---|---|---|
| Action on Object | 129 | https://nwnlexicon.com/Category:Action_on_Object_Functions |
| Alignment | 12 | https://nwnlexicon.com/Category:Alignment_Functions |
| Animation | 32 | https://nwnlexicon.com/Category:Animation_Functions |
| Area | 72 | https://nwnlexicon.com/Category:Area_Functions |
| Camera | 10 | https://nwnlexicon.com/Category:Camera_Functions |
| Combat Actions | 28 | https://nwnlexicon.com/Category:Combat_Actions_Functions |
| Combat | 35 | https://nwnlexicon.com/Category:Combat_Functions |
| Combat Information | 34 | https://nwnlexicon.com/Category:Combat_Information_Functions |
| Consoles | 1 | https://nwnlexicon.com/Category:Console_Functions |
| Conversation | 27 | https://nwnlexicon.com/Category:Conversation_Functions |
| Core AI | 67 | https://nwnlexicon.com/Category:Core_AI_Functions |
| Core AI Talent | 23 | https://nwnlexicon.com/Category:Core_AI_Talent_Functions |
| Cut-Scene | 17 | https://nwnlexicon.com/Category:Cut-Scene_Functions |
| Database | 38 | https://nwnlexicon.com/Category:Database_Functions |
| Debug | 24 | https://nwnlexicon.com/Category:Debug_Functions |
| Effects | 140 | https://nwnlexicon.com/Category:Effects_Functions |
| Encounter | 12 | https://nwnlexicon.com/Category:Encounter_Functions |
| Get Data | 63 | https://nwnlexicon.com/Category:Get_Data_Functions |
| Get Data from Creature | 144 | https://nwnlexicon.com/Category:Get_Data_from_Creature_Functions |
| Get Data from Object | 101 | https://nwnlexicon.com/Category:Get_Data_from_Object_Functions |
| GFF | — | https://nwnlexicon.com/Category:GFF_Functions |
| Henchmen/Familiars/Summoned | 73 | https://nwnlexicon.com/Category:Henchmen_Familiars_Summoned_Functions |
| Horse | 33 | https://nwnlexicon.com/Category:Horse_Functions |
| Inventory | 69 | https://nwnlexicon.com/Category:Inventory_Functions |
| Item Creation | 213 | https://nwnlexicon.com/Category:Item_Creation_Functions |
| Item Properties | 47 | https://nwnlexicon.com/Category:Item_Properties_Functions |
| Journal | 5 | https://nwnlexicon.com/Category:Journal_Functions |
| JSON | — | https://nwnlexicon.com/Category:JSON_Functions |
| Lighting Effects | 11 | https://nwnlexicon.com/Category:Lighting_Effects_Functions |
| Local Variables | 45 | https://nwnlexicon.com/Category:Local_Variables_Functions |
| Math | 32 | https://nwnlexicon.com/Category:Math_Functions |
| Miscellaneous | 86 | https://nwnlexicon.com/Category:Miscellaneous_Functions |
| Module | 25 | https://nwnlexicon.com/Category:Module_Functions |
| Module Specific | 96 | https://nwnlexicon.com/Category:Module_Specific_Functions |
| Money | 17 | https://nwnlexicon.com/Category:Money_Functions |
| Movement | 60 | https://nwnlexicon.com/Category:Movement_Functions |
| Music Effects | 18 | https://nwnlexicon.com/Category:Music_Effects_Functions |
| NWNX | 1 | https://nwnlexicon.com/Category:NWNX_Functions |
| NUI (Nuklear User Interface) | — | https://nwnlexicon.com/Category:NUI_Functions |
| Party | 45 | https://nwnlexicon.com/Category:Party_Functions |
| PC Only | 50 | https://nwnlexicon.com/Category:PC_Only_Functions |
| Perception | 14 | https://nwnlexicon.com/Category:Perception_Functions |
| Private Functions | 13 | https://nwnlexicon.com/Category:Private_Functions |
| Prototyped but Unused | 18 | https://nwnlexicon.com/Category:Prototyped_but_Unused_Functions |
| Reputation/Faction | 44 | https://nwnlexicon.com/Category:Reputation_Faction_Functions |
| Saving Throw | 14 | https://nwnlexicon.com/Category:Saving_Throw_Functions |
| Server | 7 | https://nwnlexicon.com/Category:Server_Functions |
| Sound Effects | 24 | https://nwnlexicon.com/Category:Sound_Effects_Functions |
| Spell Casting Effects | 28 | https://nwnlexicon.com/Category:Spell_Casting_Effects_Functions |
| Spells | 121 | https://nwnlexicon.com/Category:Spells_Functions |
| SQL (SQLite) | 20 | https://nwnlexicon.com/Category:SQL_Functions |
| Stores | 10 | https://nwnlexicon.com/Category:Stores_Functions |
| String | 27 | https://nwnlexicon.com/Category:String_Functions |
| Talents/Skills/Feats | 45 | https://nwnlexicon.com/Category:Talents_Skills_Feats_Functions |
| Targeting | 22 | https://nwnlexicon.com/Category:Targeting_Functions |
| Time | 20 | https://nwnlexicon.com/Category:Time_Functions |
| Traps | 34 | https://nwnlexicon.com/Category:Traps_Functions |
| Type Casting/Conversion | 15 | https://nwnlexicon.com/Category:Type_Casting_Conversion_Functions |
| Visual Effects | 20 | https://nwnlexicon.com/Category:Visual_Effects_Functions |

## Notable categories for common multiplayer-module tasks

- **Item Creation Functions** (213 pages) — note: `itemproperty` constructor functions live here. They construct an item-property "object" that must then be applied with `AddItemProperty()`, the same two-step pattern effects use (construct, then apply). The `x2_inc_itemprop` include file has `IPSafeAddItemProperty` to remove conflicting properties before adding — worth using instead of raw `AddItemProperty` to avoid stacking duplicate properties.
- **Effects Functions** (140 pages) — `Effect*()` constructors + `ApplyEffectToObject`/`ApplyEffectAtLocation`.
- **Database Functions** (38) and **SQL Functions** (20) — for persistent-world data storage (campaign database / SQLite), relevant for any multiplayer module doing player data persistence.
- **NWNX Functions** — only usable if the server actually runs the NWNX extension framework alongside the server binary; don't assume these are available unless the module's server setup confirms it.
- **Local Variables Functions** (45) — `GetLocalInt/Object/String/Float` + `SetLocal*`, the main per-object state mechanism.
- **Module Specific Functions** (96) — functions defined in a particular module's own `#include` files, not general-purpose engine functions. If a function isn't found on the Lexicon at all, it may be a project-specific helper defined in this module's own includes rather than an engine function — check the repo's include scripts before assuming it doesn't exist.

## Other reference categories (not functions)

- Constants: https://nwnlexicon.com/Category:Constants
- Events: https://nwnlexicon.com/Category:Events
- Data Types: https://nwnlexicon.com/Category:Data_Types
- Game Include (standard `#include` files shipped with the game, e.g. `x2_inc_itemprop`): https://nwnlexicon.com/Category:Game_Include
- NWN:EE-specific additions: https://nwnlexicon.com/Category:Neverwinter_Nights_Enhanced_Edition
- Tutorials: https://nwnlexicon.com/Category:Tutorials
- Primers: https://nwnlexicon.com/Category:Primers
