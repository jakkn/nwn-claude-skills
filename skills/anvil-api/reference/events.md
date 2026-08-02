# Anvil event catalogue

Every engine event Anvil exposes, grouped by the type that publishes it. Generated from
Anvil source — see the version note in `api-index.md`.

## Contents

- [How subscription works](#how-subscription-works)
- [Skipping and modifying](#skipping-and-modifying)
- [Two families of event](#two-families-of-event)
- Catalogue: [NwModule](#nwmodule--142-events) · [NwPlayer](#nwplayer--68-events) ·
  [NwCreature](#nwcreature--60-events) · [NwGameObject](#nwgameobject--11-events) ·
  [NwArea](#nwarea--4-events) · [NwAreaOfEffect](#nwareaofeffect--4-events) ·
  [NwItem](#nwitem--4-events) · [NwPlaceable](#nwplaceable--18-events) ·
  [NwDoor](#nwdoor--16-events) · [NwTrigger](#nwtrigger--9-events) ·
  [NwEncounter](#nwencounter--5-events) · [NwStore](#nwstore--2-events)

## How subscription works

Events are plain C# events. Subscribe on `NwModule.Instance` to hear about every
occurrence server-wide, or on a specific object to hear only about that object:

```csharp
NwModule.Instance.OnCreatureDamage += OnAnyDamage;   // every creature
someCreature.OnCreatureDamage      += OnThisDamage;  // just this one
```

Where the same event name appears on several types, it is the same event data class —
`NwModule` publishes the unfiltered stream and the specific type publishes the filtered
one. `NwPlayer` events filter to that player's controlled creature.

Handlers are `Action<TEvent>` and therefore synchronous. Anvil will not await you. For
asynchronous work, start a task and discard it:

```csharp
NwModule.Instance.OnClientEnter += eventData => _ = OnClientEnterAsync(eventData);
```

Unsubscribe with `-=` using the same delegate instance (so don't subscribe with a lambda
you'll later need to remove). `EventService.ClearObjectSubscriptions(obj)` removes every
subscription registered against one object — useful when tearing down a system.

Subscribing to an event installs the underlying engine hook lazily, so unused events cost
nothing. There's no reason to avoid subscribing to a chatty event like `OnHeartbeat`
beyond your own handler's cost — but prefer `SchedulerService` over heartbeats for
timed work, since it isn't tied to the 6-second engine tick.

## Skipping and modifying

Events marked **Skip** in the tables below expose a `Skip` property; setting it to `true`
suppresses the engine's default behaviour. This is how you replace built-in mechanics
rather than just observing them.

Many events instead expose mutable data that changes the outcome without skipping —
`PreventLevelUp`, `BlockConnection`, `Bypass`, `DamageData`, `KickMessage` and friends.
Check the event data column before assuming you need a function hook.

The typed `+=` accessors subscribe `EventCallbackType.Before`, which is also the default on
every `EventService.Subscribe` overload.

`EventCallbackType.After` is only meaningful for the native (hook-backed) events, which
raise `Before`, call the original engine function, then raise `After`. Toolset events go
through `GameEventFactory`, which only ever raises `Before` — subscribing `After` to one of
those compiles and silently never fires.

Note also that for toolset events "Before" is relative to Anvil's dispatch, not the
module's scripts: `GameEventFactory` runs the module's original NWScript first and then
invokes your handler.

## Two families of event

**Toolset events** correspond to the script slots you'd set in the toolset
(`ModuleEvents.*`, `AreaEvents.*`, `CreatureEvents.*`, `DoorEvents.*`, `PlaceableEvents.*`,
`TriggerEvents.*`, `StoreEvents.*`, `EncounterEvents.*`, `AreaOfEffectEvents.*`). They are
namespaced under a container class and fire where the corresponding NWScript would have run.
Assigning a handler replaces nothing — the module's own scripts still run.

**Native events** are unqualified class names (`OnCreatureDamage`, `OnItemEquip`,
`OnSpellCast`, `OnServerCharacterSave`…). These come from function hooks Anvil installs into
the engine and expose behaviour NWScript never had. They're generally the more powerful
family, and are where `Skip` shows up most.


## NwModule — 142 events

| Event | Data type | Skip | Event data |
| --- | --- | --- | --- |
| `OnAcquireItem` | `ModuleEvents.OnAcquireItem` |  | `AcquiredBy`, `AcquiredFrom`, `AmountAcquired`, `Item` |
| `OnActivateItem` | `ModuleEvents.OnActivateItem` |  | `ActivatedItem`, `ItemActivator`, `TargetLocation`, `TargetObject` |
| `OnAssociateAdd` | `OnAssociateAdd` |  | `Associate`, `AssociateType`, `Owner` |
| `OnAssociateRemove` | `OnAssociateRemove` |  | `Associate`, `Owner` |
| `OnBarterEnd` | `OnBarterEnd` |  | `Complete`, `Initiator`, `InitiatorItems`, `Target`, `TargetItems` |
| `OnBarterStart` | `OnBarterStart` |  | `Initiator`, `Target` |
| `OnCalendarTimeChange` | `OnCalendarTimeChange` |  | `NewValue`, `OldValue`, `TimeChangeType` |
| `OnChatMessageSend` | `OnChatMessageSend` | yes | `ChatChannel`, `Message`, `Sender`, `Target` |
| `OnCheckEffectImmunity` | `OnCheckEffectImmunity` |  | `Bypass`, `Creature`, `ImmunityType` |
| `OnClientConnect` | `OnClientConnect` |  | `BlockConnection`, `CDKey`, `ClientPlatform`, `ClientVersion`, `DM`, `IP`, `KickMessage`, `PlayerName` |
| `OnClientDisconnect` | `OnClientDisconnect` |  | `Player` |
| `OnClientEnter` | `ModuleEvents.OnClientEnter` |  | `Player` |
| `OnClientLeave` | `ModuleEvents.OnClientLeave` |  | `Player` |
| `OnClientLevelUpBegin` | `OnClientLevelUpBegin` |  | `Player`, `PreventLevelUp`, `Result` |
| `OnCombatDRBroken` | `OnCombatDRBroken` |  | `Creature`, `Type` |
| `OnCombatModeToggle` | `OnCombatModeToggle` |  | `Creature`, `ForceNewMode`, `ForceNewModeOverride`, `NewMode`, `PreventToggle` |
| `OnCombatRoundStart` | `OnCombatRoundStart` |  | `Creature`, `Target` |
| `OnCombatStatusChange` | `OnCombatStatusChange` |  | `CombatStatus`, `Player` |
| `OnCreatureAcquireItem` | `OnCreatureAcquireItem` | yes | `Item`, `AcquiredBy`, `AcquiredFrom`, `Result` |
| `OnCreatureAttack` | `OnCreatureAttack` |  | `Attacker`, `AttackModifier`, `AttackNumber`, `AttackResult`, `AttackRoll`, `AttackType`, `DamageData`, `IsAttackDeflected`, `IsCoupDeGrace`, `IsCriticalThreat` |
| `OnCreatureCheckProficiencies` | `OnCreatureCheckProficiencies` |  | `Creature`, `Item`, `ResultOverride`, `TargetSlot` |
| `OnCreatureDamage` | `OnCreatureDamage` |  | `DamageData`, `DamagedBy`, `Target`, `Spell` |
| `OnCutsceneAbort` | `ModuleEvents.OnCutsceneAbort` |  | `Player` |
| `OnDMAppear` | `OnDMAppear` |  | — |
| `OnDMChangeDifficulty` | `OnDMChangeDifficulty` |  | `NewDifficulty` |
| `OnDMDisableTrap` | `OnDMDisableTrap` |  | — |
| `OnDMDisappear` | `OnDMDisappear` |  | — |
| `OnDMDumpLocals` | `OnDMDumpLocals` |  | `Target`, `Type` |
| `OnDMForceRest` | `OnDMForceRest` |  | — |
| `OnDMGetFactionReputation` | `OnDMGetFactionReputation` |  | — |
| `OnDMGetVariable` | `OnDMGetVariable` |  | — |
| `OnDMGiveAlignment` | `OnDMGiveAlignment` |  | `Alignment`, `Amount`, `Target` |
| `OnDMGiveGold` | `OnDMGiveGold` |  | — |
| `OnDMGiveItem` | `OnDMGiveItem` |  | `Target`, `Item` |
| `OnDMGiveLevel` | `OnDMGiveLevel` |  | — |
| `OnDMGiveXP` | `OnDMGiveXP` |  | — |
| `OnDMGoTo` | `OnDMGoTo` |  | — |
| `OnDMHeal` | `OnDMHeal` |  | — |
| `OnDMJumpAllPlayersToPoint` | `OnDMJumpAllPlayersToPoint` |  | — |
| `OnDMJumpTargetToPoint` | `OnDMJumpTargetToPoint` |  | `NewArea`, `NewPosition`, `Targets` |
| `OnDMJumpToPoint` | `OnDMJumpToPoint` |  | — |
| `OnDMKill` | `OnDMKill` |  | — |
| `OnDMLimbo` | `OnDMLimbo` |  | — |
| `OnDMPlayerDMLogin` | `OnDMPlayerDMLogin` |  | `Password` |
| `OnDMPlayerDMLogout` | `OnDMPlayerDMLogout` |  | — |
| `OnDMPossess` | `OnDMPossess` |  | — |
| `OnDMPossessFullPower` | `OnDMPossessFullPower` |  | — |
| `OnDMSetDate` | `OnDMSetDate` |  | — |
| `OnDMSetFaction` | `OnDMSetFaction` |  | — |
| `OnDMSetFactionReputation` | `OnDMSetFactionReputation` |  | — |
| `OnDMSetStat` | `OnDMSetStat` |  | — |
| `OnDMSetTime` | `OnDMSetTime` |  | — |
| `OnDMSetVariable` | `OnDMSetVariable` |  | — |
| `OnDMSpawnObject` | `OnDMSpawnObject` |  | `Area`, `ObjectType`, `Position`, `ResRef`, `SpawnedObject` |
| `OnDMSpawnTrapOnObject` | `OnDMSpawnTrapOnObject` |  | `Target` |
| `OnDMTakeItem` | `OnDMTakeItem` |  | — |
| `OnDMToggleAI` | `OnDMToggleAI` |  | — |
| `OnDMToggleImmortal` | `OnDMToggleImmortal` |  | — |
| `OnDMToggleInvulnerable` | `OnDMToggleInvulnerable` |  | — |
| `OnDMToggleLock` | `OnDMToggleLock` |  | — |
| `OnDMViewInventory` | `OnDMViewInventory` |  | `IsOpening`, `Target` |
| `OnDebugPlayVisualEffect` | `OnDebugPlayVisualEffect` | yes | `Effect`, `Player`, `TargetObject`, `TargetPosition`, `Duration` |
| `OnDebugRunScript` | `OnDebugRunScript` | yes | `Player`, `ScriptName`, `Target` |
| `OnDebugRunScriptChunk` | `OnDebugRunScriptChunk` | yes | `Player`, `ScriptChunk`, `Target`, `WrapIntoMain` |
| `OnDetectModeUpdate` | `OnDetectModeUpdate` |  | `Creature`, `EventType`, `Prevent` |
| `OnDisarmWeapon` | `OnDisarmWeapon` |  | `DisarmedBy`, `DisarmedObject`, `Feat`, `PreventDisarm`, `Result` |
| `OnDispelMagicApply` | `OnDispelMagicApply` | yes | `Object`, `Type`, `Effect`, `NumEffectsDispelled` |
| `OnDoListenDetection` | `OnDoListenDetection` |  | `Creature`, `Target`, `VisibilityOverride` |
| `OnDoSpotDetection` | `OnDoSpotDetection` |  | `Creature`, `Target`, `VisibilityOverride` |
| `OnDoorSetOpenState` | `OnDoorSetOpenState` |  | `Door`, `OpenState`, `PreventStateChange` |
| `OnEffectApply` | `OnEffectApply` |  | `Effect`, `Object`, `PreventApply` |
| `OnEffectRemove` | `OnEffectRemove` |  | `Effect`, `Object`, `PreventRemove` |
| `OnExamineObject` | `OnExamineObject` |  | `ExaminedBy`, `ExaminedObject` |
| `OnExamineTrap` | `OnExamineTrap` |  | `ExaminedBy`, `ExaminedObject`, `Success` |
| `OnFamiliarPossess` | `OnFamiliarPossess` |  | `Familiar`, `Owner` |
| `OnFamiliarUnpossess` | `OnFamiliarUnpossess` |  | `Familiar`, `Owner` |
| `OnHeal` | `OnHeal` |  | `HealAmount`, `Healer`, `Target` |
| `OnHealKitUse` | `OnHealKitUse` |  | `ItemPropertyIndex`, `ItemUsed`, `MoveToTarget`, `PreventUse`, `Result`, `Target`, `UsedBy` |
| `OnHeartbeat` | `ModuleEvents.OnHeartbeat` |  | `Trigger` |
| `OnInventoryGoldAdd` | `OnInventoryGoldAdd` |  | `Creature`, `Gold`, `PreventGoldAdd` |
| `OnInventoryGoldRemove` | `OnInventoryGoldRemove` |  | `Creature`, `Gold`, `PreventGoldRemove` |
| `OnInventoryItemAdd` | `OnInventoryItemAdd` |  | `AcquiredBy`, `Item`, `PreventItemAdd`, `Result` |
| `OnInventoryItemRemove` | `OnInventoryItemRemove` |  | `Item`, `RemovedFrom` |
| `OnItemDecrementStackSize` | `OnItemDecrementStackSize` |  | — |
| `OnItemDestroy` | `OnItemDestroy` |  | — |
| `OnItemEquip` | `OnItemEquip` |  | `EquippedBy`, `Item`, `PreventEquip`, `Result`, `Slot` |
| `OnItemInventoryClose` | `OnItemInventoryClose` |  | `ClosedBy`, `Container`, `PreventClose` |
| `OnItemInventoryOpen` | `OnItemInventoryOpen` |  | `Container`, `OpenedBy`, `PreventOpen` |
| `OnItemPayToIdentify` | `OnItemPayToIdentify` |  | `Creature`, `Item`, `PreventPayToIdentify`, `Store` |
| `OnItemScrollLearn` | `OnItemScrollLearn` |  | `Creature`, `PreventLearnScroll`, `Scroll` |
| `OnItemUnequip` | `OnItemUnequip` |  | `Creature`, `Item`, `PreventUnequip` |
| `OnItemUse` | `OnItemUse` |  | `Item`, `ItemPropertyIndex`, `ItemSubPropertyIndex`, `PreventUseItem`, `SuppressCannotUseFeedback`, `TargetArea`, `TargetObject`, `TargetPosition`, `UseCharges` |
| `OnItemValidateEquip` | `OnItemValidateEquip` |  | `Item`, `Result`, `Slot`, `UsedBy` |
| `OnItemValidateUse` | `OnItemValidateUse` |  | `CanUse`, `Item`, `UsedBy` |
| `OnLevelDown` | `OnLevelDown` |  | `Creature` |
| `OnLevelUp` | `OnLevelUp` |  | `Creature` |
| `OnLevelUpAutomatic` | `OnLevelUpAutomatic` |  | `Creature` |
| `OnLoadCharacterFinish` | `OnLoadCharacterFinish` |  | `Player` |
| `OnMapPinAddPin` | `OnMapPinAddPin` |  | `Note`, `Player`, `Position`, `PreventPinAdd` |
| `OnMapPinChangePin` | `OnMapPinChangePin` |  | `Id`, `Note`, `Player`, `Position`, `PreventPinChange` |
| `OnMapPinDestroyPin` | `OnMapPinDestroyPin` |  | `Id`, `Player`, `PreventPinDestroy` |
| `OnModuleLoad` | `ModuleEvents.OnModuleLoad` |  | — |
| `OnModuleStart` | `ModuleEvents.OnModuleStart` |  | — |
| `OnNuiEvent` | `ModuleEvents.OnNuiEvent` |  | `ArrayIndex`, `ElementId`, `EventType`, `Player`, `Token` |
| `OnObjectUse` | `OnObjectUse` |  | `Object`, `UsedBy`, `PreventObjectUse` |
| `OnPartyEvent` | `OnPartyEvent` |  | `EventType`, `Player`, `PreventEvent`, `Result`, `Target` |
| `OnPlayerChat` | `ModuleEvents.OnPlayerChat` |  | `Message`, `Sender`, `Volume` |
| `OnPlayerDeath` | `ModuleEvents.OnPlayerDeath` |  | `DeadPlayer`, `Killer` |
| `OnPlayerDying` | `ModuleEvents.OnPlayerDying` |  | `Player` |
| `OnPlayerEquipItem` | `ModuleEvents.OnPlayerEquipItem` |  | `Item`, `Player`, `Slot` |
| `OnPlayerGuiEvent` | `ModuleEvents.OnPlayerGuiEvent` |  | `EventObject`, `EventType`, `Player` |
| `OnPlayerLevelUp` | `ModuleEvents.OnPlayerLevelUp` |  | `Player` |
| `OnPlayerQuickChat` | `OnPlayerQuickChat` |  | `Player`, `VoiceChat`, `PreventQuickChat` |
| `OnPlayerRespawn` | `ModuleEvents.OnPlayerRespawn` |  | `Player` |
| `OnPlayerRest` | `ModuleEvents.OnPlayerRest` |  | `Player`, `RestEventType` |
| `OnPlayerTarget` | `ModuleEvents.OnPlayerTarget` |  | `Player`, `TargetObject`, `TargetPosition` |
| `OnPlayerTileAction` | `ModuleEvents.OnPlayerTileAction` |  | `ActionId`, `Player`, `TargetPosition` |
| `OnPlayerUnequipItem` | `ModuleEvents.OnPlayerUnequipItem` |  | `Item`, `UnequippedBy`, `Slot` |
| `OnPolymorphApply` | `OnPolymorphApply` |  | `Creature`, `PolymorphType`, `PreventPolymorph` |
| `OnPolymorphRemove` | `OnPolymorphRemove` |  | `Creature`, `PolymorphType`, `PreventRemove` |
| `OnServerCharacterSave` | `OnServerCharacterSave` |  | `Player`, `PreventSave` |
| `OnServerSendArea` | `OnServerSendArea` |  | `Area`, `IsPlayerNewToModule`, `Player` |
| `OnSpellAction` | `OnSpellAction` |  | `Caster`, `CasterLevel`, `ClassIndex`, `Domain`, `Feat`, `IsAreaTarget`, `IsFake`, `IsInstant`, `IsSpontaneous`, `MetaMagic`, `PreventSpellCast`, `ProjectilePat |
| `OnSpellBroadcast` | `OnSpellBroadcast` |  | `Caster`, `ClassIndex`, `Feat`, `PreventSpellCast`, `Spell`, `TargetObject`, `TargetPosition` |
| `OnSpellCast` | `OnSpellCast` |  | `Caster`, `Harmful`, `Item`, `MetaMagicFeat`, `SaveDC`, `Spell`, `SpellCastClass`, `SpellLevel`, `IsSpontaneousCast`, `TargetLocation`, `TargetObject` |
| `OnSpellInterrupt` | `OnSpellInterrupt` |  | `ClassIndex`, `Domain`, `Feat`, `InterruptedCaster`, `MetaMagic`, `Spell`, `Spontaneous` |
| `OnSpellSlotClear` | `OnSpellSlotClear` |  | `ClassIndex`, `Creature`, `PreventClear`, `SlotIndex`, `SpellLevel` |
| `OnSpellSlotMemorize` | `OnSpellSlotMemorize` |  | `ClassIndex`, `Creature`, `Domain`, `FromClient`, `MetaMagic`, `PreventMemorize`, `SlotIndex`, `Spell` |
| `OnStealthModeUpdate` | `OnStealthModeUpdate` |  | `Creature`, `EnterOverride`, `EventType`, `PreventExit` |
| `OnStoreRequestBuy` | `OnStoreRequestBuy` |  | `Creature`, `Item`, `PreventBuy`, `Price`, `Result`, `Store` |
| `OnStoreRequestSell` | `OnStoreRequestSell` |  | `Creature`, `Item`, `PreventSell`, `Price`, `Result`, `Store` |
| `OnTrapDisarm` | `OnTrapDisarm` |  | — |
| `OnTrapEnter` | `OnTrapEnter` | yes | `EnteredObject`, `Trigger`, `ForceSet` |
| `OnTrapExamine` | `OnTrapExamine` |  | — |
| `OnTrapFlag` | `OnTrapFlag` |  | — |
| `OnTrapRecover` | `OnTrapRecover` |  | — |
| `OnTrapSet` | `OnTrapSet` |  | `InRange`, `Creature`, `TargetObject`, `TargetLocation`, `ResultOverride`, `Result` |
| `OnTriggerEnter` | `OnTriggerEnter` | yes | `EnteredObject`, `IsTrap`, `IsTrapForceSet`, `Trigger` |
| `OnUnacquireItem` | `ModuleEvents.OnUnacquireItem` |  | `Item`, `LostBy` |
| `OnUseFeat` | `OnUseFeat` |  | `Creature`, `Feat`, `PreventFeatUse`, `SubFeatId`, `TargetArea`, `TargetObject`, `TargetPosition` |
| `OnUseSkill` | `OnUseSkill` |  | `Area`, `Creature`, `PreventSkillUse`, `Skill`, `SubSkill`, `Target`, `TargetPosition`, `UsedItem` |
| `OnUserDefined` | `ModuleEvents.OnUserDefined` |  | `EventNumber`, `Trigger` |

## NwPlayer — 67 events

| Event | Data type | Skip | Event data |
| --- | --- | --- | --- |
| `OnBarterEnd` | `OnBarterEnd` |  | `Complete`, `Initiator`, `InitiatorItems`, `Target`, `TargetItems` |
| `OnBarterStart` | `OnBarterStart` |  | `Initiator`, `Target` |
| `OnClientDisconnect` | `OnClientDisconnect` |  | `Player` |
| `OnClientEnter` | `ModuleEvents.OnClientEnter` |  | `Player` |
| `OnClientLeave` | `ModuleEvents.OnClientLeave` |  | `Player` |
| `OnClientLevelUpBegin` | `OnClientLevelUpBegin` |  | `Player`, `PreventLevelUp`, `Result` |
| `OnCombatStatusChange` | `OnCombatStatusChange` |  | `CombatStatus`, `Player` |
| `OnCutsceneAbort` | `ModuleEvents.OnCutsceneAbort` |  | `Player` |
| `OnDMAppear` | `OnDMAppear` |  | — |
| `OnDMChangeDifficulty` | `OnDMChangeDifficulty` |  | `NewDifficulty` |
| `OnDMDisableTrap` | `OnDMDisableTrap` |  | — |
| `OnDMDisappear` | `OnDMDisappear` |  | — |
| `OnDMDumpLocals` | `OnDMDumpLocals` |  | `Target`, `Type` |
| `OnDMForceRest` | `OnDMForceRest` |  | — |
| `OnDMGetFactionReputation` | `OnDMGetFactionReputation` |  | — |
| `OnDMGetVariable` | `OnDMGetVariable` |  | — |
| `OnDMGiveAlignment` | `OnDMGiveAlignment` |  | `Alignment`, `Amount`, `Target` |
| `OnDMGiveGold` | `OnDMGiveGold` |  | — |
| `OnDMGiveItem` | `OnDMGiveItem` |  | `Target`, `Item` |
| `OnDMGiveLevel` | `OnDMGiveLevel` |  | — |
| `OnDMGiveXP` | `OnDMGiveXP` |  | — |
| `OnDMGoTo` | `OnDMGoTo` |  | — |
| `OnDMHeal` | `OnDMHeal` |  | — |
| `OnDMJumpAllPlayersToPoint` | `OnDMJumpAllPlayersToPoint` |  | — |
| `OnDMJumpTargetToPoint` | `OnDMJumpTargetToPoint` |  | `NewArea`, `NewPosition`, `Targets` |
| `OnDMJumpToPoint` | `OnDMJumpToPoint` |  | — |
| `OnDMKill` | `OnDMKill` |  | — |
| `OnDMLimbo` | `OnDMLimbo` |  | — |
| `OnDMPlayerDMLogin` | `OnDMPlayerDMLogin` |  | `Password` |
| `OnDMPlayerDMLogout` | `OnDMPlayerDMLogout` |  | — |
| `OnDMPossess` | `OnDMPossess` |  | — |
| `OnDMPossessFullPower` | `OnDMPossessFullPower` |  | — |
| `OnDMSetDate` | `OnDMSetDate` |  | — |
| `OnDMSetFaction` | `OnDMSetFaction` |  | — |
| `OnDMSetFactionReputation` | `OnDMSetFactionReputation` |  | — |
| `OnDMSetStat` | `OnDMSetStat` |  | — |
| `OnDMSetTime` | `OnDMSetTime` |  | — |
| `OnDMSetVariable` | `OnDMSetVariable` |  | — |
| `OnDMSpawnObject` | `OnDMSpawnObject` |  | `Area`, `ObjectType`, `Position`, `ResRef`, `SpawnedObject` |
| `OnDMSpawnTrapOnObject` | `OnDMSpawnTrapOnObject` |  | `Target` |
| `OnDMTakeItem` | `OnDMTakeItem` |  | — |
| `OnDMToggleAI` | `OnDMToggleAI` |  | — |
| `OnDMToggleImmortal` | `OnDMToggleImmortal` |  | — |
| `OnDMToggleInvulnerable` | `OnDMToggleInvulnerable` |  | — |
| `OnDMToggleLock` | `OnDMToggleLock` |  | — |
| `OnDMViewInventory` | `OnDMViewInventory` |  | `IsOpening`, `Target` |
| `OnExamineObject` | `OnExamineObject` |  | `ExaminedBy`, `ExaminedObject` |
| `OnExamineTrap` | `OnExamineTrap` |  | `ExaminedBy`, `ExaminedObject`, `Success` |
| `OnMapPinAddPin` | `OnMapPinAddPin` |  | `Note`, `Player`, `Position`, `PreventPinAdd` |
| `OnMapPinChangePin` | `OnMapPinChangePin` |  | `Id`, `Note`, `Player`, `Position`, `PreventPinChange` |
| `OnMapPinDestroyPin` | `OnMapPinDestroyPin` |  | `Id`, `Player`, `PreventPinDestroy` |
| `OnNuiEvent` | `ModuleEvents.OnNuiEvent` |  | `ArrayIndex`, `ElementId`, `EventType`, `Player`, `Token` |
| `OnPartyEvent` | `OnPartyEvent` |  | `EventType`, `Player`, `PreventEvent`, `Result`, `Target` |
| `OnPlayerChat` | `ModuleEvents.OnPlayerChat` |  | `Message`, `Sender`, `Volume` |
| `OnPlayerDeath` | `ModuleEvents.OnPlayerDeath` |  | `DeadPlayer`, `Killer` |
| `OnPlayerDying` | `ModuleEvents.OnPlayerDying` |  | `Player` |
| `OnPlayerEquipItem` | `ModuleEvents.OnPlayerEquipItem` |  | `Item`, `Player`, `Slot` |
| `OnPlayerGuiEvent` | `ModuleEvents.OnPlayerGuiEvent` |  | `EventObject`, `EventType`, `Player` |
| `OnPlayerLevelUp` | `ModuleEvents.OnPlayerLevelUp` |  | `Player` |
| `OnPlayerQuickChat` | `OnPlayerQuickChat` |  | `Player`, `VoiceChat`, `PreventQuickChat` |
| `OnPlayerRespawn` | `ModuleEvents.OnPlayerRespawn` |  | `Player` |
| `OnPlayerRest` | `ModuleEvents.OnPlayerRest` |  | `Player`, `RestEventType` |
| `OnPlayerTarget` | `ModuleEvents.OnPlayerTarget` |  | `Player`, `TargetObject`, `TargetPosition` |
| `OnPlayerTileAction` | `ModuleEvents.OnPlayerTileAction` |  | `ActionId`, `Player`, `TargetPosition` |
| `OnPlayerUnequipItem` | `ModuleEvents.OnPlayerUnequipItem` |  | `Item`, `UnequippedBy`, `Slot` |
| `OnServerCharacterSave` | `OnServerCharacterSave` |  | `Player`, `PreventSave` |
| `OnServerSendArea` | `OnServerSendArea` |  | `Area`, `IsPlayerNewToModule`, `Player` |

## NwCreature — 60 events

| Event | Data type | Skip | Event data |
| --- | --- | --- | --- |
| `OnActivateItem` | `ModuleEvents.OnActivateItem` |  | `ActivatedItem`, `ItemActivator`, `TargetLocation`, `TargetObject` |
| `OnAssociateAdd` | `OnAssociateAdd` |  | `Associate`, `AssociateType`, `Owner` |
| `OnAssociateRemove` | `OnAssociateRemove` |  | `Associate`, `Owner` |
| `OnBlocked` | `CreatureEvents.OnBlocked` |  | `BlockingDoor`, `Creature` |
| `OnCheckEffectImmunity` | `OnCheckEffectImmunity` |  | `Bypass`, `Creature`, `ImmunityType` |
| `OnCombatDRBroken` | `OnCombatDRBroken` |  | `Creature`, `Type` |
| `OnCombatModeToggle` | `OnCombatModeToggle` |  | `Creature`, `ForceNewMode`, `ForceNewModeOverride`, `NewMode`, `PreventToggle` |
| `OnCombatRoundEnd` | `CreatureEvents.OnCombatRoundEnd` |  | `Creature` |
| `OnCombatRoundStart` | `OnCombatRoundStart` |  | `Creature`, `Target` |
| `OnConversation` | `CreatureEvents.OnConversation` |  | `Placeable`, `LastSpeaker`, `PlayerSpeaker`, `ListenPattern` |
| `OnCreatureAcquireItem` | `OnCreatureAcquireItem` | yes | `Item`, `AcquiredBy`, `AcquiredFrom`, `Result` |
| `OnCreatureAttack` | `OnCreatureAttack` |  | `Attacker`, `AttackModifier`, `AttackNumber`, `AttackResult`, `AttackRoll`, `AttackType`, `DamageData`, `IsAttackDeflected`, `IsCoupDeGrace`, `IsCriticalThreat` |
| `OnCreatureCheckProficiencies` | `OnCreatureCheckProficiencies` |  | `Creature`, `Item`, `ResultOverride`, `TargetSlot` |
| `OnCreatureDamage` | `OnCreatureDamage` |  | `DamageData`, `DamagedBy`, `Target`, `Spell` |
| `OnDamaged` | `CreatureEvents.OnDamaged` |  | `DamagedObject`, `Damager`, `TotalDamageDealt` |
| `OnDeath` | `CreatureEvents.OnDeath` |  | `KilledObject`, `Killer` |
| `OnDetectModeUpdate` | `OnDetectModeUpdate` |  | `Creature`, `EventType`, `Prevent` |
| `OnDisturbed` | `CreatureEvents.OnDisturbed` |  | `DisturbedItem`, `Disturber`, `DisturbType`, `Placeable` |
| `OnDoListenDetection` | `OnDoListenDetection` |  | `Creature`, `Target`, `VisibilityOverride` |
| `OnDoSpotDetection` | `OnDoSpotDetection` |  | `Creature`, `Target`, `VisibilityOverride` |
| `OnFamiliarPossess` | `OnFamiliarPossess` |  | `Familiar`, `Owner` |
| `OnFamiliarUnpossess` | `OnFamiliarUnpossess` |  | `Familiar`, `Owner` |
| `OnHealKitUse` | `OnHealKitUse` |  | `ItemPropertyIndex`, `ItemUsed`, `MoveToTarget`, `PreventUse`, `Result`, `Target`, `UsedBy` |
| `OnHeartbeat` | `CreatureEvents.OnHeartbeat` |  | `Trigger` |
| `OnInventoryGoldAdd` | `OnInventoryGoldAdd` |  | `Creature`, `Gold`, `PreventGoldAdd` |
| `OnInventoryGoldRemove` | `OnInventoryGoldRemove` |  | `Creature`, `Gold`, `PreventGoldRemove` |
| `OnItemEquip` | `OnItemEquip` |  | `EquippedBy`, `Item`, `PreventEquip`, `Result`, `Slot` |
| `OnItemInventoryClose` | `OnItemInventoryClose` |  | `ClosedBy`, `Container`, `PreventClose` |
| `OnItemInventoryOpen` | `OnItemInventoryOpen` |  | `Container`, `OpenedBy`, `PreventOpen` |
| `OnItemPayToIdentify` | `OnItemPayToIdentify` |  | `Creature`, `Item`, `PreventPayToIdentify`, `Store` |
| `OnItemScrollLearn` | `OnItemScrollLearn` |  | `Creature`, `PreventLearnScroll`, `Scroll` |
| `OnItemUnequip` | `OnItemUnequip` |  | `Creature`, `Item`, `PreventUnequip` |
| `OnItemUse` | `OnItemUse` |  | `Item`, `ItemPropertyIndex`, `ItemSubPropertyIndex`, `PreventUseItem`, `SuppressCannotUseFeedback`, `TargetArea`, `TargetObject`, `TargetPosition`, `UseCharges` |
| `OnItemValidateEquip` | `OnItemValidateEquip` |  | `Item`, `Result`, `Slot`, `UsedBy` |
| `OnItemValidateUse` | `OnItemValidateUse` |  | `CanUse`, `Item`, `UsedBy` |
| `OnLevelDown` | `OnLevelDown` |  | `Creature` |
| `OnLevelUp` | `OnLevelUp` |  | `Creature` |
| `OnLevelUpAutomatic` | `OnLevelUpAutomatic` |  | `Creature` |
| `OnObjectUse` | `OnObjectUse` |  | `Object`, `UsedBy`, `PreventObjectUse` |
| `OnPerception` | `CreatureEvents.OnPerception` |  | `Creature`, `PerceivedCreature`, `PerceptionEventType` |
| `OnPhysicalAttacked` | `CreatureEvents.OnPhysicalAttacked` |  | `Attacker`, `AttackType`, `Placeable` |
| `OnPolymorphApply` | `OnPolymorphApply` |  | `Creature`, `PolymorphType`, `PreventPolymorph` |
| `OnPolymorphRemove` | `OnPolymorphRemove` |  | `Creature`, `PolymorphType`, `PreventRemove` |
| `OnRested` | `CreatureEvents.OnRested` |  | `Creature` |
| `OnSpawn` | `CreatureEvents.OnSpawn` |  | `Creature` |
| `OnSpellAction` | `OnSpellAction` |  | `Caster`, `CasterLevel`, `ClassIndex`, `Domain`, `Feat`, `IsAreaTarget`, `IsFake`, `IsInstant`, `IsSpontaneous`, `MetaMagic`, `PreventSpellCast`, `ProjectilePat |
| `OnSpellCastAt` | `CreatureEvents.OnSpellCastAt` |  | `Caster`, `Harmful`, `Placeable`, `Spell` |
| `OnSpellSlotClear` | `OnSpellSlotClear` |  | `ClassIndex`, `Creature`, `PreventClear`, `SlotIndex`, `SpellLevel` |
| `OnSpellSlotMemorize` | `OnSpellSlotMemorize` |  | `ClassIndex`, `Creature`, `Domain`, `FromClient`, `MetaMagic`, `PreventMemorize`, `SlotIndex`, `Spell` |
| `OnStealthModeUpdate` | `OnStealthModeUpdate` |  | `Creature`, `EnterOverride`, `EventType`, `PreventExit` |
| `OnStoreRequestBuy` | `OnStoreRequestBuy` |  | `Creature`, `Item`, `PreventBuy`, `Price`, `Result`, `Store` |
| `OnStoreRequestSell` | `OnStoreRequestSell` |  | `Creature`, `Item`, `PreventSell`, `Price`, `Result`, `Store` |
| `OnTrapDisarm` | `OnTrapDisarm` |  | — |
| `OnTrapExamine` | `OnTrapExamine` |  | — |
| `OnTrapFlag` | `OnTrapFlag` |  | — |
| `OnTrapRecover` | `OnTrapRecover` |  | — |
| `OnTrapSet` | `OnTrapSet` |  | `InRange`, `Creature`, `TargetObject`, `TargetLocation`, `ResultOverride`, `Result` |
| `OnUseFeat` | `OnUseFeat` |  | `Creature`, `Feat`, `PreventFeatUse`, `SubFeatId`, `TargetArea`, `TargetObject`, `TargetPosition` |
| `OnUseSkill` | `OnUseSkill` |  | `Area`, `Creature`, `PreventSkillUse`, `Skill`, `SubSkill`, `Target`, `TargetPosition`, `UsedItem` |
| `OnUserDefined` | `CreatureEvents.OnUserDefined` |  | `EventNumber`, `Trigger` |

## NwGameObject — 11 events

| Event | Data type | Skip | Event data |
| --- | --- | --- | --- |
| `OnAcquireItem` | `ModuleEvents.OnAcquireItem` |  | `AcquiredBy`, `AcquiredFrom`, `AmountAcquired`, `Item` |
| `OnChatMessageSend` | `OnChatMessageSend` | yes | `ChatChannel`, `Message`, `Sender`, `Target` |
| `OnDisarmWeapon` | `OnDisarmWeapon` |  | `DisarmedBy`, `DisarmedObject`, `Feat`, `PreventDisarm`, `Result` |
| `OnDispelMagicApply` | `OnDispelMagicApply` | yes | `Object`, `Type`, `Effect`, `NumEffectsDispelled` |
| `OnEffectApply` | `OnEffectApply` |  | `Effect`, `Object`, `PreventApply` |
| `OnEffectRemove` | `OnEffectRemove` |  | `Effect`, `Object`, `PreventRemove` |
| `OnHeal` | `OnHeal` |  | `HealAmount`, `Healer`, `Target` |
| `OnSpellBroadcast` | `OnSpellBroadcast` |  | `Caster`, `ClassIndex`, `Feat`, `PreventSpellCast`, `Spell`, `TargetObject`, `TargetPosition` |
| `OnSpellCast` | `OnSpellCast` |  | `Caster`, `Harmful`, `Item`, `MetaMagicFeat`, `SaveDC`, `Spell`, `SpellCastClass`, `SpellLevel`, `IsSpontaneousCast`, `TargetLocation`, `TargetObject` |
| `OnSpellInterrupt` | `OnSpellInterrupt` |  | `ClassIndex`, `Domain`, `Feat`, `InterruptedCaster`, `MetaMagic`, `Spell`, `Spontaneous` |
| `OnUnacquireItem` | `ModuleEvents.OnUnacquireItem` |  | `Item`, `LostBy` |

## NwArea — 4 events

| Event | Data type | Skip | Event data |
| --- | --- | --- | --- |
| `OnEnter` | `AreaEvents.OnEnter` |  | `EnteringObject`, `Trigger` |
| `OnExit` | `AreaEvents.OnExit` |  | `ExitingObject`, `Trigger` |
| `OnHeartbeat` | `AreaEvents.OnHeartbeat` |  | `Trigger` |
| `OnUserDefined` | `AreaEvents.OnUserDefined` |  | `EventNumber`, `Trigger` |

## NwAreaOfEffect — 4 events

| Event | Data type | Skip | Event data |
| --- | --- | --- | --- |
| `OnEnter` | `AreaOfEffectEvents.OnEnter` |  | `EnteringObject`, `Trigger` |
| `OnExit` | `AreaOfEffectEvents.OnExit` |  | `ExitingObject`, `Trigger` |
| `OnHeartbeat` | `AreaOfEffectEvents.OnHeartbeat` |  | `Trigger` |
| `OnUserDefined` | `AreaOfEffectEvents.OnUserDefined` |  | `EventNumber`, `Trigger` |

## NwItem — 4 events

| Event | Data type | Skip | Event data |
| --- | --- | --- | --- |
| `OnInventoryItemAdd` | `OnInventoryItemAdd` |  | `AcquiredBy`, `Item`, `PreventItemAdd`, `Result` |
| `OnInventoryItemRemove` | `OnInventoryItemRemove` |  | `Item`, `RemovedFrom` |
| `OnItemDecrementStackSize` | `OnItemDecrementStackSize` |  | — |
| `OnItemDestroy` | `OnItemDestroy` |  | — |

## NwPlaceable — 18 events

| Event | Data type | Skip | Event data |
| --- | --- | --- | --- |
| `OnClose` | `PlaceableEvents.OnClose` |  | `Creature`, `Store` |
| `OnConversation` | `PlaceableEvents.OnConversation` |  | `Placeable`, `LastSpeaker`, `PlayerSpeaker`, `ListenPattern` |
| `OnDamaged` | `PlaceableEvents.OnDamaged` |  | `DamagedObject`, `Damager`, `TotalDamageDealt` |
| `OnDeath` | `PlaceableEvents.OnDeath` |  | `KilledObject`, `Killer` |
| `OnDisarm` | `PlaceableEvents.OnDisarm` |  | `Placeable` |
| `OnDisturbed` | `PlaceableEvents.OnDisturbed` |  | `DisturbedItem`, `Disturber`, `DisturbType`, `Placeable` |
| `OnHeartbeat` | `PlaceableEvents.OnHeartbeat` |  | `Trigger` |
| `OnInventoryItemAdd` | `OnInventoryItemAdd` |  | `AcquiredBy`, `Item`, `PreventItemAdd`, `Result` |
| `OnInventoryItemRemove` | `OnInventoryItemRemove` |  | `Item`, `RemovedFrom` |
| `OnLeftClick` | `PlaceableEvents.OnLeftClick` |  | `ClickedBy`, `Placeable` |
| `OnLock` | `PlaceableEvents.OnLock` |  | `LockedBy`, `LockedPlaceable` |
| `OnOpen` | `PlaceableEvents.OnOpen` |  | `Player`, `Store` |
| `OnPhysicalAttacked` | `PlaceableEvents.OnPhysicalAttacked` |  | `Attacker`, `AttackType`, `Placeable` |
| `OnSpellCastAt` | `PlaceableEvents.OnSpellCastAt` |  | `Caster`, `Harmful`, `Placeable`, `Spell` |
| `OnTrapTriggered` | `PlaceableEvents.OnTrapTriggered` |  | `Trigger`, `TriggeredBy` |
| `OnUnlock` | `PlaceableEvents.OnUnlock` |  | `Placeable`, `UnlockedBy` |
| `OnUsed` | `PlaceableEvents.OnUsed` |  | `Placeable`, `UsedBy` |
| `OnUserDefined` | `PlaceableEvents.OnUserDefined` |  | `EventNumber`, `Trigger` |

## NwDoor — 16 events

| Event | Data type | Skip | Event data |
| --- | --- | --- | --- |
| `OnAreaTransitionClick` | `DoorEvents.OnAreaTransitionClick` |  | `ClickedBy`, `Door`, `TransitionTarget` |
| `OnClose` | `DoorEvents.OnClose` |  | `Creature`, `Store` |
| `OnConversation` | `DoorEvents.OnConversation` |  | `Placeable`, `LastSpeaker`, `PlayerSpeaker`, `ListenPattern` |
| `OnDamaged` | `DoorEvents.OnDamaged` |  | `DamagedObject`, `Damager`, `TotalDamageDealt` |
| `OnDeath` | `DoorEvents.OnDeath` |  | `KilledObject`, `Killer` |
| `OnDisarm` | `DoorEvents.OnDisarm` |  | `Placeable` |
| `OnDoorSetOpenState` | `OnDoorSetOpenState` |  | `Door`, `OpenState`, `PreventStateChange` |
| `OnFailToOpen` | `DoorEvents.OnFailToOpen` |  | `Door`, `WhoFailed` |
| `OnHeartbeat` | `DoorEvents.OnHeartbeat` |  | `Trigger` |
| `OnLock` | `DoorEvents.OnLock` |  | `LockedBy`, `LockedPlaceable` |
| `OnOpen` | `DoorEvents.OnOpen` |  | `Player`, `Store` |
| `OnPhysicalAttacked` | `DoorEvents.OnPhysicalAttacked` |  | `Attacker`, `AttackType`, `Placeable` |
| `OnSpellCastAt` | `DoorEvents.OnSpellCastAt` |  | `Caster`, `Harmful`, `Placeable`, `Spell` |
| `OnTrapTriggered` | `DoorEvents.OnTrapTriggered` |  | `Trigger`, `TriggeredBy` |
| `OnUnlock` | `DoorEvents.OnUnlock` |  | `Placeable`, `UnlockedBy` |
| `OnUserDefined` | `DoorEvents.OnUserDefined` |  | `EventNumber`, `Trigger` |

## NwTrigger — 9 events

| Event | Data type | Skip | Event data |
| --- | --- | --- | --- |
| `OnClicked` | `TriggerEvents.OnClicked` |  | `ClickedBy`, `Trigger` |
| `OnDetectModeUpdate` | `OnTriggerEnter` | yes | `EnteredObject`, `IsTrap`, `IsTrapForceSet`, `Trigger` |
| `OnDisarmed` | `TriggerEvents.OnDisarmed` |  | `DisarmedBy`, `Trigger` |
| `OnEnter` | `TriggerEvents.OnEnter` |  | `EnteringObject`, `Trigger` |
| `OnExit` | `TriggerEvents.OnExit` |  | `ExitingObject`, `Trigger` |
| `OnHeartbeat` | `TriggerEvents.OnHeartbeat` |  | `Trigger` |
| `OnTrapEnter` | `OnTrapEnter` | yes | `EnteredObject`, `Trigger`, `ForceSet` |
| `OnTrapTriggered` | `TriggerEvents.OnTrapTriggered` |  | `Trigger`, `TriggeredBy` |
| `OnUserDefined` | `TriggerEvents.OnUserDefined` |  | `EventNumber`, `Trigger` |

## NwEncounter — 5 events

| Event | Data type | Skip | Event data |
| --- | --- | --- | --- |
| `OnEnter` | `EncounterEvents.OnEnter` |  | `EnteringObject`, `Trigger` |
| `OnExhausted` | `EncounterEvents.OnExhausted` |  | `Encounter` |
| `OnExit` | `EncounterEvents.OnExit` |  | `ExitingObject`, `Trigger` |
| `OnHeartbeat` | `EncounterEvents.OnHeartbeat` |  | `Trigger` |
| `OnUserDefined` | `EncounterEvents.OnUserDefined` |  | `EventNumber`, `Trigger` |

## NwStore — 2 events

| Event | Data type | Skip | Event data |
| --- | --- | --- | --- |
| `OnClose` | `StoreEvents.OnClose` |  | `Creature`, `Store` |
| `OnOpen` | `StoreEvents.OnOpen` |  | `Player`, `Store` |
