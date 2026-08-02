# Anvil public API index

Generated from Anvil `v8193.36.2-dev-83-g06b3969b0`.

One `##` heading per public type in `Anvil.API` / `Anvil.Services`, with its public
members bulleted beneath and enum values inlined. Grep this rather than reading it:

```
rg -A 60 '^## Anvil\.API\.NwCreature ' reference/api-index.md   # one type's members
rg 'ApplyEffect' reference/api-index.md                          # which types expose a member
rg '^## Anvil\.API\.\w*Effect' reference/api-index.md            # types matching a pattern
```

Signatures are extracted textually, so a member declared across multiple lines may be
truncated. Overload sets are complete. If something looks off, confirm against
https://nwn-dotnet.github.io/Anvil/ before assuming the API is missing.

Regenerate with `python3 scripts/generate_api_index.py /path/to/Anvil`.

## Anvil.API.IAwaitable  [interface]

## Anvil.API.IAwaitable<out TResult>  [interface]

## Anvil.API.IAwaiter  [interface]

## Anvil.API.IAwaiter<out TResult>  [interface]

## Anvil.API.NwTask  [class]
- static Task Delay(TimeSpan delay, CancellationToken? cancellationToken = null)
- static Task DelayFrame(int frames, CancellationToken? cancellationToken = null)
- static Task NextFrame()
- static async Task Run(Func<Task> function)
- static async Task<T> Run<T>(Func<Task<T>> function)
- static IAwaitable SwitchToMainThread()
- static Task WaitUntil(Func<bool> test, CancellationToken? cancellationToken = null)
- static Task WaitUntilValueChanged<T>(Func<T> valueSource, CancellationToken? cancellationToken = null)
- static async Task WhenAll(params Task[] tasks)
- static async Task WhenAll(IEnumerable<Task> tasks)
- static async Task<TResult[]> WhenAll<TResult>(params Task<TResult>[] tasks)
- static async Task<TResult[]> WhenAll<TResult>(IEnumerable<Task<TResult>> tasks)
- static async Task WhenAny(params Task[] tasks)
- static async Task WhenAny(IEnumerable<Task> tasks)
- static async Task<Task<TResult>> WhenAny<TResult>(params Task<TResult>[] tasks)
- static async Task<Task<TResult>> WhenAny<TResult>(IEnumerable<Task<TResult>> tasks)

## Anvil.API.Color  [struct]
- readonly byte Alpha
- readonly byte Blue
- readonly byte Green
- readonly byte Red
- Color(byte red, byte green, byte blue, byte alpha = 255)
- Color(float red, float green, float blue, float alpha = 1.0f)
- float AlphaF
- float BlueF
- float GreenF
- float RedF
- static unsafe Color FromRGBA(int rgba)
- static unsafe Color FromRGBA(uint rgba)
- static Color FromRGBA(string rgbaHexString)
- static bool operator ==(Color left, Color right)
- static bool operator !=(Color left, Color right)
- bool Equals(Color other)
- override bool Equals(object? obj)
- override int GetHashCode()
- string ToColorToken()
- int ToRGBA()
- override string ToString()
- uint ToUnsignedRGBA()

## Anvil.API.ColorConstants  [class]
- static readonly Color Black = new Color(0, 0, 0)
- static readonly Color Blue = new Color(0, 0, 255)
- static readonly Color Brown = new Color(165, 42, 42)
- static readonly Color Cyan = new Color(0, 255, 255)
- static readonly Color Gray = new Color(128, 128, 128)
- static readonly Color Green = new Color(0, 128, 0)
- static readonly Color Lime = new Color(0, 255, 0)
- static readonly Color Magenta = new Color(255, 0, 255)
- static readonly Color Maroon = new Color(128, 0, 0)
- static readonly Color Navy = new Color(0, 0, 128)
- static readonly Color Olive = new Color(128, 128, 0)
- static readonly Color Orange = new Color(255, 165, 0)
- static readonly Color Pink = new Color(255, 170, 170)
- static readonly Color Purple = new Color(128, 0, 128)
- static readonly Color Red = new Color(255, 0, 0)
- static readonly Color Rose = new Color(255, 150, 150)
- static readonly Color Silver = new Color(192, 192, 192)
- static readonly Color Teal = new Color(0, 128, 128)
- static readonly Color White = new Color(255, 255, 255)
- static readonly Color Yellow = new Color(255, 255, 0)

## Anvil.API.ACBonus  [enum]
- values: Dodge, Natural, ArmourEnchantment, ShieldEnchantment, Deflection, VsDamageTypeAll

## Anvil.API.AiLevel  [enum]
- values: Invalid, Default, VeryLow, Low, Normal, High, VeryHigh

## Anvil.API.Ability  [enum]
- values: Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma

## Anvil.API.Action  [enum]
- values: MoveToPoint, PickupItem, DropItem, AttackObject, CastSpell, OpenDoor, CloseDoor, DialogObject, DisableTrap, RecoverTrap, FlagTrap, ExamineTrap, SetTrap, OpenLock, Lock, UseObject, AnimalEmpathy, Rest, Taunt, ItemCastSpell, CounterSpell, Heal, Pickpocket, Follow, Wait, Sit, SmiteGood, KiDamage, RandomWalk, Invalid

## Anvil.API.ActionMode  [enum]
- values: Detect, Stealth, Parry, PowerAttack, ImprovedPowerAttack, CounterSpell, FlurryOfBlows, RapidShot, Expertise, ImprovedExpertise, DefensiveCast, DirtyFighting

## Anvil.API.ActionState  [enum]
- values: Unknown, InProgress, Complete, Failed

## Anvil.API.AddPropPolicy  [enum]
- values: IgnoreExisting, ReplaceExisting, KeepExisting

## Anvil.API.Alignment  [enum]
- values: All, Neutral, Lawful, Chaotic, Good, Evil

## Anvil.API.AmbientSound  [enum]
- values: None, MenWhisperInside, WomenWhisperInside, PeopleWhisperInside, SmallGroupTalksInside, MediumGroupTalksInside, LargeGroupTalksInside, CommonerTavernTalk, NobleTavernTalk, CitySlumsDayCrowded, CitySlumsDaySparse, CitySlumsNight, CityDayCrowded, CityDaySparse, CityNight, CityMarket, CityTempleDistrict, TownDayCrowded, TownDaySparse, TownNight, BordelloWomen, BordelloMenAndWomen, RiotOutside, RiotMuffled, CombatOutside1, CombatOutside2, CombatMuffled1, CombatMuffled2, DungeonLakeLava, SewerSludgeLake, WindSoft, WindMedium, WindStrong, WindForest, GustChasm, GustCavern, GustGrass, GustDraft, RainLight, RainHard, RainStormSmall, RainStormBig, CaveInsects1, CaveInsects2, InteriorInsects1, InteriorInsects2, LizardFolkCaveCrystals, Sewers1, Sewers2, ForestDay1, ForestDay2, ForestDay3, ForestDayScary, ForestNight1, ForestNight2, ForestNightScary, ForestMagical, EvilDungeonSmall, EvilDungeonMedium, EvilDungeonLarge, CaveSmall, CaveMedium, CaveLarge, MineSmall, MineMedium, MineLarge, CastleInteriorSmall, CastleInteriorMedium, CastleInteriorLarge, CryptSmall, CryptMedium1, CryptMedium2, HouseInterior1, HouseInterior2, HouseInterior3, KitchenInteriorSmall, KitchenInteriorLarge, HauntedInterior1, HauntedInterior2, HauntedInterior3, BlackSmith, PitCries, MagicInteriorSmall, MagicInteriorMedium, MagicInteriorLarge, MagicInteriorEvil, MagicalInteriorFireLab, MagicalInteriorEarthLab, MagicalInteriorAirLab, MagicalInteriorWaterLab, WinterDayWetXp1, WinterDayWindyXp1, DesertDayXp1, DesertNightXp1, MonasteryInteriorXp1, RuinWetXp1, RuinRumblingXp1, RuinHauntedXp1, SandStormLightXp1, SandStormExtremeXp1, EvilDroneXp2, PlainOfFireXp2, FrozenHellXp2, CaveEvil1Xp2, CaveEvil2Xp2, CaveEvil3Xp2, TavernRowdy

## Anvil.API.AnimalCompanionCreatureType  [enum]
- values: Badger, Wolf, Bear, Boar, Hawk, Panther, Spider, DireWolf, DireRat, None

## Anvil.API.Animation  [enum]
- values: LoopingPause, LoopingPause2, LoopingListen, LoopingMeditate, LoopingWorship, LoopingLookFar, LoopingSitChair, LoopingSitCross, LoopingTalkNormal, LoopingTalkPleading, LoopingTalkForceful, LoopingTalkLaughing, LoopingGetLow, LoopingGetMid, LoopingPauseTired, LoopingPauseDrunk, LoopingDeadFront, LoopingDeadBack, LoopingConjure1, LoopingConjure2, LoopingSpasm, LoopingCustom1, LoopingCustom2, LoopingCustom3, LoopingCustom4, LoopingCustom5, LoopingCustom6, LoopingCustom7, LoopingCustom8, LoopingCustom9, LoopingCustom10, LoopingCustom11, LoopingCustom12, LoopingCustom13, LoopingCustom14, LoopingCustom15, LoopingCustom16, LoopingCustom17, LoopingCustom18, LoopingCustom19, LoopingCustom20, LoopingCustom21, LoopingCustom22, LoopingCustom23, LoopingCustom24, LoopingCustom25, LoopingCustom26, LoopingCustom27, LoopingCustom28, LoopingCustom29, LoopingCustom30, LoopingCustom31, LoopingCustom32, LoopingCustom33, LoopingCustom34, LoopingCustom35, LoopingCustom36, LoopingCustom37, LoopingCustom38, LoopingCustom39, LoopingCustom40, LoopingCustom41, LoopingCustom42, LoopingCustom43, LoopingCustom44, LoopingCustom45, LoopingCustom46, LoopingCustom47, LoopingCustom48, LoopingCustom49, LoopingCustom50, LoopingCustom51, LoopingCustom52, LoopingCustom53, LoopingCustom54, LoopingCustom55, LoopingCustom56, LoopingCustom57, LoopingCustom58, LoopingCustom59, LoopingCustom60, LoopingCustom61, LoopingCustom62, LoopingCustom63, LoopingCustom64, LoopingCustom65, LoopingCustom66, LoopingCustom67, LoopingCustom68, LoopingCustom69, LoopingCustom70, Mount1, Dismount1, FireForgetHeadTurnLeft, FireForgetHeadTurnRight, FireForgetPauseScratchHead, FireForgetPauseBored, FireForgetSalute, FireForgetBow, FireForgetSteal, FireForgetGreeting, FireForgetTaunt, FireForgetVictory1, FireForgetVictory2, FireForgetVictory3, FireForgetRead, FireForgetDrink, FireForgetDodgeSide, FireForgetDodgeDuck, FireForgetSpasm, PlaceableActivate, PlaceableDeactivate, PlaceableOpen, PlaceableClose, DoorClose, DoorOpen1, DoorOpen2, DoorDestroy

## Anvil.API.AnimationState  [enum]
- values: Pause, Ready, Walking, WalkingBackwards, Running, KnockdownFront, DeadFront, KnockdownButt, DeadButt, Attack, Throw, Dodge, Parry, Shield, Damage, Conjure1, Conjure2, Cast1, Cast2, Cast3, Cast4, Open, Closed, Spasm, CombatStepFront, CombatStepBack, CombatStepLeft, CombatStepRight, Taunt, OverlayGreeting, OverlayListen, Meditate, Worship, OverlaySalute, Bow, Sitting, Steal, OverlayTalkNormal, OverlayTalkPleading, OverlayTalkForceful, OverlayTalkLaugh, CombatStepDummy, AttackDummy, VictoryFighter, VictoryMage, VictoryThief, SitCrossLegs, LookFar, CombatStepDummyFbs, Opened1, Opened2, Pause2, HeadTurnLeft, HeadTurnRight, PauseScratchHead, PauseBored, PauseTired, PauseDrunk, GetLow, GetMid, Cast5, Flown, Arrived, OverlayDrink, OverlayRead, Destroyed, PlaceableActivated, PlaceableDeactivated, PlaceableOpened, PlaceableClosed, DamageStab, WalkingLeft, WalkingRight, TurnOnSpotRight, TurnOnSpotLeft, CombatTurnRight, CombatTurnLeft, WalkingForwardLeft, WalkingForwardRight, RunningForwardLeft, RunningForwardRight, DialogNoAnim, FakeAttack, FakeDodgeSide, FakeDodgeDuck, Whirlwind, SpasmLooping, Flown2, Arrived2, CastCreature, Custom1, Custom2, DamageLeft, DamageRight, Custom3, Custom4, Custom5, Custom6, Custom7, Custom8, Custom9, Custom10, Custom11, Custom12, Custom13, Custom14, Custom15, Custom16, Custom17, Custom18, Custom19, Custom20, Mount1, Dismount1

## Anvil.API.AppearanceType  [enum]
- values: Invalid, Allip, Aranea, ArchTarget, Aribeth, AsabiChieftain, AsabiShaman, AsabiWarrior, Badger, BadgerDire, Balor, Bartender, Basilisk, Bat, BatHorror, BearBlack, BearBrown, BearDire, BearKodiak, BearPolar, BeetleFire, BeetleSlicer, BeetleStag, BeetleStink, Begger, BloodSailor, Boar, BoarDire, Bodak, BugbearA, BugbearB, BugbearChieftainA, BugbearChieftainB, BugbearShamanA, BugbearShamanB, Bulette, CatCatDire, CatCougar, CatCragCat, CatJaguar, CatKrenshar, CatLeopard, CatLion, CatMpanther, CatPanther, Chicken, Cockatrice, CombatDummy, Convict, Cow, CultMember, Deer, DeerStag, Devil, Dog, DogBlinkDog, DogDireWolf, DogFenHound, DogHellHound, DogShadowMastif, DogWinterWolf, DogWolf, DogWorg, DoomKnight, DragonBlack, DragonBlue, DragonBrass, DragonBronze, DragonCopper, DragonGold, DragonGreen, DragonRed, DragonSilver, DragonWhite, DrowCleric, DrowFighter, DruegarCleric, DruegarFighter, Dryad, Dwarf, DwarfNpcFemale, DwarfNpcMale, ElementalAir, ElementalAirElder, ElementalEarth, ElementalEarthElder, ElementalFire, ElementalFireElder, ElementalWater, ElementalWaterElder, Elf, ElfNpcFemale, ElfNpcMale01, ElfNpcMale02, Ettercap, Ettin, FaerieDragon, Fairy, Falcon, Female01, Female02, Female03, Female04, FormianMyrmarch, FormianQueen, FormianWarrior, FormianWorker, Gargoyle, Ghast, Ghoul, GhoulLord, GiantFire, GiantFireFemale, GiantFrost, GiantFrostFemale, GiantHill, GiantMountain, GnollWarrior, GnollWiz, Gnome, GnomeNpcFemale, GnomeNpcMale, GoblinA, GoblinB, GoblinChiefA, GoblinChiefB, GoblinShamanA, GoblinShamanB, GolemBone, GolemClay, GolemFlesh, GolemIron, GolemStone, Gorgon, GrayOoze, GreyRender, Gynosphinx, Halfling, HalflingNpcFemale, HalflingNpcMale, HalfElf, HalfOrc, HalfOrcNpcFemale, HalfOrcNpcMale01, HalfOrcNpcMale02, HelmedHorror, HeurodisLich, HobgoblinWarrior, HobgoblinWizard, HookHorror, HouseGuard, Human, HumanNpcFemale01, HumanNpcFemale02, HumanNpcFemale03, HumanNpcFemale04, HumanNpcFemale05, HumanNpcFemale06, HumanNpcFemale07, HumanNpcFemale08, HumanNpcFemale09, HumanNpcFemale10, HumanNpcFemale11, HumanNpcFemale12, HumanNpcMale01, HumanNpcMale02, HumanNpcMale03, HumanNpcMale04, HumanNpcMale05, HumanNpcMale06, HumanNpcMale07, HumanNpcMale08, HumanNpcMale09, HumanNpcMale10, HumanNpcMale11, HumanNpcMale12, HumanNpcMale13, HumanNpcMale14, HumanNpcMale15, HumanNpcMale16, HumanNpcMale17, HumanNpcMale18, Imp, InnKeeper, IntellectDevourer, InvisibleHumanMale, InvisibleStalker, KidFemale, KidMale, KoboldA, KoboldB, KoboldChiefA, KoboldChiefB, KoboldShamanA, KoboldShamanB, LanternArchon, Lich, LizardfolkA, LizardfolkB, LizardfolkShamanA, LizardfolkShamanB, LizardfolkWarriorA, LizardfolkWarriorB, LuskanGuard, Male01, Male02, Male03, Male04, Male05, Manticore, Medusa, MephitAir, MephitDust, MephitEarth, MephitFire, MephitIce, MephitMagma, MephitOoze, MephitSalt, MephitSteam, MephitWater, Minogon, Minotaur, MinotaurChieftain, MinotaurShaman, Mohrg, MummyCommon, MummyFighter2, MummyGreater, MummyWarrior, NwnAarin, NwnAribethEvil, NwnHaedraline, NwnMaugrim, NwnMorag, NwnNasher, NwnSedos, NwMilitiaMember, Nymph, OchreJellyLarge, OchreJellyMedium, OchreJellySmall, Ogre, Ogreb, OgreChieftain, OgreChieftainb, OgreMage, OgreMageb, OldMan, OldWoman, OrcA, OrcB, OrcChieftainA, OrcChieftainB, OrcShamanA, OrcShamanB, Ox, Parrot, Penguin, PlagueVictim, Prostitute01, Prostitute02, Pseudodragon, Quasit, RakshasaBearMale, RakshasaTigerFemale, RakshasaTigerMale, RakshasaWolfMale, Rat, RatDire, Raven, Sahuagin, SahuaginLeader, SahuaginCleric, SeagullFlying, SeagullWalking, Shadow, ShadowFiend, SharkMako, SharkHammerhead, SharkGoblin, ShieldGuardian, ShopKeeper, SkeletalDevourer, SkeletonChieftain, SkeletonCommon, SkeletonMage, SkeletonPriest, SkeletonWarrior, SkeletonWarrior1, SkeletonWarrior2, SlaadBlue, SlaadDeath, SlaadGray, SlaadGreen, SlaadRed, Spectre, Sphinx, SpiderDire, SpiderGiant, SpiderPhase, SpiderSword, SpiderWraith, Stinger, StingerChieftain, StingerMage, StingerWarrior, Succubus, Troglodyte, TroglodyteWarrior, TroglodyteCleric, Troll, TrollChieftain, TrollShaman, Umberhulk, UthgardElkTribe, UthgardTigerTribe, VampireFemale, VampireMale, Vrock, Waitress, WarDevourer, Werecat, Wererat, Werewolf, Wight, WillOWisp, Wraith, WyrmlingBlack, WyrmlingBlue, WyrmlingBrass, WyrmlingBronze, WyrmlingCopper, WyrmlingGold, WyrmlingGreen, WyrmlingRed, WyrmlingSilver, WyrmlingWhite, YuanTi, YuanTiChieften, YuanTiWizard, Zombie, ZombieRotting, ZombieTyrantFog, ZombieWarrior1, ZombieWarrior2, Beholder, BeholderMage, BeholderEyeball, MephistoBig, Dracolich, Drider, DriderChief, DrowSlave, DrowWizard, DrowMatron, DuergarSlave, DuergarChief, Mindflayer, Mindflayer2, MindflayerAlhoon, DeepRothe, DragonShadow, Harpy, GolemMithral, GolemAdamantium, SpiderDemon, SvirfMale, SvirfFemale, DragonPris, SlaadBlack, SlaadWhite, AzerMale, AzerFemale, DemiLich, ObjectChair, ObjectTable, ObjectCandle, ObjectChest, ObjectWhite, ObjectBlue, ObjectCyan, ObjectGreen, ObjectYellow, ObjectOrange, ObjectRed, ObjectPurple, ObjectFlameSmall, ObjectFlameMedium, ObjectFlameLarge, DriderFemale, SeaHag, GolemDemonFlesh, AnimatedChest, GelatinousCube, MephistoNorm, BeholderMother, ObjectBoat, DwarfGolem, DwarfHalfOrc, DrowWarrior1, DrowWarrior2, DrowFemale1, DrowFemale2, DrowWarrior3

## Anvil.API.AreaDestroyResult  [enum]
- values: Occupied, IsSpawnArea, InvalidArea, Success

## Anvil.API.AreaLightColor  [enum]
- values: MoonAmbient, MoonDiffuse, SunAmbient, SunDiffuse

## Anvil.API.AreaLightDirection  [enum]
- values: Moon, Sun

## Anvil.API.AreaSizeDimension  [enum]
- values: Height, Width

## Anvil.API.AreaTransition  [enum]
- values: Random, UserDefined, City01, City02, City03, City04, City05, Crypt01, Crypt02, Crypt03, Crypt04, Crypt05, Dungeon01, Dungeon02, Dungeon03, Dungeon04, Dungeon05, Dungeon06, Dungeon07, Dungeon08, Mines01, Mines02, Mines03, Mines04, Mines05, Mines06, Mines07, Mines08, Mines09, Sewer01, Sewer02, Sewer03, Sewer04, Sewer05, Castle01, Castle02, Castle03, Castle04, Castle05, Castle06, Castle07, Castle08, Interior01, Interior02, Interior03, Interior04, Interior05, Interior06, Interior07, Interior08, Interior09, Interior10, Interior11, Interior12, Interior13, Interior14, Interior15, Interior16, Forest01, Forest02, Forest03, Forest04, Forest05, Rural01, Rural02, Rural03, Rural04, Rural05, Wrural01, Wrural02, Wrural03, Wrural04, Wrural05, Desert01, Desert02, Desert03, Desert04, Desert05, Ruins01, Ruins02, Ruins03, Ruins04, Ruins05, CaravanWinter, CaravanDesert, CaravanRural, Magical01, Magical02, Underdark01, Underdark02, Underdark03, Underdark04, Underdark05, Underdark06, Underdark07, Beholder01, Beholder02, Drow01, Drow02, Illithid01, Illithid02, Wasteland01, Wasteland02, Wasteland03, Drow03, Drow04, City, Crypt, Forest, Rural

## Anvil.API.AssociateCommand  [enum]
- values: StandGround, AttackNearest, HealMaster, FollowMaster, MasterFailedLockPick, GuardMaster, UnsummonFamiliar, UnsummonAnimalCompanion, UnsummonSummoned, MasterUnderAttack, ReleaseDomination, UnpossessFamiliar, MasterSawTrap, MasterAttackedOther, MasterGoingToBeAttacked, LeaveParty, PickLock, Inventory, DisarmTrap, ToggleCasting, ToggleStealth, ToggleSearch

## Anvil.API.AssociateType  [enum]
- values: None, Henchman, AnimalCompanion, Familiar, Summoned, Dominated

## Anvil.API.AttackBonus  [enum]
- values: Misc, OnHand, OffHand

## Anvil.API.Attitude  [enum]
- values: Neutral, Aggressive, Defensive, Special

## Anvil.API.AudioStreamIdentifier  [enum]
- values: Identifier0, Identifier1, Identifier2, Identifier3, Identifier4, Identifier5, Identifier6, Identifier7, Identifier8, Identifier9

## Anvil.API.BaseItemType  [enum]
- values: Shortsword, Longsword, Battleaxe, Bastardsword, LightFlail, Warhammer, HeavyCrossbow, LightCrossbow, Longbow, LightMace, Halberd, Shortbow, TwoBladedSword, Greatsword, SmallShield, Torch, Armor, Helmet, Greataxe, Amulet, Arrow, Belt, Dagger, MiscSmall, Bolt, Boots, Bullet, Club, MiscMedium, Dart, DireMace, Doubleaxe, MiscLarge, HeavyFlail, Gloves, LightHammer, Handaxe, HealersKit, Kama, Katana, Kukri, MiscTall, MagicRod, MagicStaff, MagicWand, Morningstar, Potions, Quarterstaff, Rapier, Ring, Scimitar, Scroll, Scythe, LargeShield, TowerShield, ShortSpear, Shuriken, Sickle, Sling, ThievesTools, ThrowingAxe, TrapKit, Key, LargeBox, MiscWide, CreatureSlashingWeapon, CreaturePiercingWeapon, CreatureBludgeoningWeapon, CreatureSlashingAndPiercingWeapon, CreatureItem, Book, SpellScroll, Gold, Gem, Bracer, MiscThin, Cloak, Grenade, Trident, BlankPotion, BlankScroll, BlankWand, EnchantedPotion, EnchantedScroll, EnchantedWand, DwarvenWaraxe, CraftMaterialMedium, CraftMaterialSmall, Whip, Invalid

## Anvil.API.BodyNode  [enum]
- values: Hand, Chest, Monster0, Monster1, Monster2, Monster3, Monster4, Monster5, Monster6, Monster7, Monster8, Monster9

## Anvil.API.CameraFlag  [enum]
- values: EnableCollision, DisableCollision, DisableShake, DisableScroll, DisableTurn, DisableTilt, DisableZoom

## Anvil.API.CameraMode  [enum]
- values: ChaseCamera, TopDown, StiffChaseCamera

## Anvil.API.CameraTransitionType  [enum]
- values: Snap, Crawl, VerySlow, Slow, Medium, Fast, VeryFast

## Anvil.API.ChatBarChannel  [enum]
- values: Shout, Whisper, Talk, Party, DM

## Anvil.API.ClassType  [enum]
- values: Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Wizard, Aberration, Animal, Construct, Humanoid, Monstrous, Elemental, Fey, Dragon, Undead, Commoner, Beast, Giant, MagicalBeast, Outsider, Shapechanger, Vermin, Shadowdancer, Harper, ArcaneArcher, Assassin, Blackguard, DivineChampion, WeaponMaster, PaleMaster, Shifter, DwarvenDefender, DragonDisciple, Ooze, EyeOfGruumsh, ShouDisciple, PurpleDragonKnight, Invalid

## Anvil.API.ColorChannel  [enum]
- values: Skin, Hair, Tattoo1, Tattoo2

## Anvil.API.CombatMode  [enum]
- values: None, Parry, PowerAttack, ImprovedPowerAttack, CounterSpell, FlurryOfBlows, RapidShot, Expertise, ImprovedExpertise, DefensiveCasting, DirtyFighting, DefensiveStance

## Anvil.API.CreatureModelNumber  [class]
- const int None = NWScript.CREATURE_MODEL_TYPE_NONE
- const int Skin = NWScript.CREATURE_MODEL_TYPE_SKIN
- const int Tattoo = NWScript.CREATURE_MODEL_TYPE_TATTOO
- const int Undead = NWScript.CREATURE_MODEL_TYPE_UNDEAD

## Anvil.API.CreaturePart  [enum]
- values: RightFoot, LeftFoot, RightShin, LeftShin, LeftThigh, RightThigh, Pelvis, Torso, Belt, Neck, RightForearm, LeftForearm, RightBicep, LeftBicep, RightShoulder, LeftShoulder, RightHand, LeftHand, Robe, Head

## Anvil.API.CreatureSize  [enum]
- values: Invalid, Tiny, Small, Medium, Large, Huge

## Anvil.API.CreatureTailType  [enum]
- values: None, Lizard, Bone, Devil

## Anvil.API.CreatureType  [enum]
- values: None, RacialType, PlayerChar, Class, Reputation, IsAlive, HasSpellEffect, DoesNotHaveSpellEffect, Perception

## Anvil.API.CreatureWingType  [enum]
- values: None, Demon, Angel, Bat, Dragon, Butterfly, Bird

## Anvil.API.DamageBonus  [enum]
- values: Plus1, Plus2, Plus3, Plus4, Plus5, Plus6, Plus7, Plus8, Plus9, Plus10, Plus11, Plus12, Plus13, Plus14, Plus15, Plus16, Plus17, Plus18, Plus19, Plus20, Plus1d4, Plus1d6, Plus1d8, Plus1d10, Plus1d12, Plus2d4, Plus2d6, Plus2d8, Plus2d10, Plus2d12

## Anvil.API.DamagePower  [enum]
- values: Normal, Plus1, Plus2, Plus3, Plus4, Plus5, Plus6, Plus7, Plus8, Plus9, Plus10, Plus11, Plus12, Plus13, Plus14, Plus15, Plus16, Plus17, Plus18, Plus19, Plus20, Energy

## Anvil.API.DamageType  [enum]
- values: Bludgeoning, Piercing, Slashing, Magical, Acid, Cold, Divine, Electrical, Fire, Negative, Positive, Sonic, BaseWeapon, Custom1, Custom2, Custom3, Custom4, Custom5, Custom6, Custom7, Custom8, Custom9, Custom10, Custom11, Custom12, Custom13, Custom14, Custom15, Custom16, Custom17, Custom18, Custom19

## Anvil.API.Direction  [class]
- const float East = NWScript.DIRECTION_EAST
- const float North = NWScript.DIRECTION_NORTH
- const float South = NWScript.DIRECTION_SOUTH
- const float West = NWScript.DIRECTION_WEST

## Anvil.API.DiseaseType  [enum]
- values: BlindingSickness, CackleFever, DevilChills, DemonFever, FilthFever, MindFire, MummyRot, RedAche, Shakes, SlimyDoom, RedSlaadEggs, GhoulRot, ZombieCreep, DreadBlisters, BurrowMaggots, SoldierShakes, VerminMadness

## Anvil.API.Domain  [enum]
- values: Error, Air, Animal, Death, Destruction, Earth, Evil, Fire, Good, Healing, Knowledge, Magic, Plant, Protection, Strength, Sun, Travel, Trickery, War, Water

## Anvil.API.DoorAction  [enum]
- values: Open, Unlock, Bash, Ignore, Knock

## Anvil.API.DoorOpenState  [enum]
- values: Closed, OpenForward, OpenBackward, Destroyed

## Anvil.API.EffectDuration  [enum]
- values: Instant, Temporary, Permanent

## Anvil.API.EffectIcon  [enum]
- values: Invalid, DamageResistance, Regenerate, DamageReduction, TemporaryHitpoints, Entangle, Invulnerable, Deaf, Fatigue, Immunity, Blind, EnemyAttackBonus, Charmed, Confused, Frightened, Dominated, Paralyze, Dazed, Stunned, Sleep, Poison, Disease, Curse, Silence, Turned, Haste, Slow, AbilityIncreaseStr, AbilityDecreaseStr, AttackIncrease, AttackDecrease, DamageIncrease, DamageDecrease, DamageImmunityIncrease, DamageImmunityDecrease, ACIncrease, ACDecrease, MovementSpeedIncrease, MovementSpeedDecrease, SavingThrowIncrease, SavingThrowDecrease, SpellResistanceIncrease, SpellResistanceDecrease, SkillIncrease, SkillDecrease, Invisibility, ImprovedInvisibility, Darkness, DispelMagical, ElementalShield, LevelDrain, Polymorph, Sanctuary, TrueSeeing, SeeInvisibility, TimeStop, Blindness, SpellLevelAbsorption, DispelMagicBest, AbilityIncreaseDex, AbilityDecreaseDex, AbilityIncreaseCon, AbilityDecreaseCon, AbilityIncreaseInt, AbilityDecreaseInt, AbilityIncreaseWis, AbilityDecreaseWis, AbilityIncreaseCha, AbilityDecreaseCha, ImmunityAll, ImmunityMind, ImmunityPoison, ImmunityDisease, ImmunityFear, ImmunityTrap, ImmunityParalysis, ImmunityBlindness, ImmunityDeafness, ImmunitySlow, ImmunityEntangle, ImmunitySilence, ImmunityStun, ImmunitySleep, ImmunityCharm, ImmunityDominate, ImmunityConfuse, ImmunityCurse, ImmunityDazed, ImmunityAbilityDecrease, ImmunityAttackDecrease, ImmunityDamageDecrease, ImmunityDamageImmunityDecrease, ImmunityACDecrease, ImmunityMovementSpeedDecrease, ImmunitySavingThrowDecrease, ImmunitySpellResistanceDecrease, ImmunitySkillDecrease, ImmunityKnockdown, ImmunityNegativeLevel, ImmunitySneakAttack, ImmunityCriticalHit, ImmunityDeathMagic, ReflexSaveIncreased, FortSaveIncreased, WillSaveIncreased, Taunted, SpellImmunity, Etherealness, Concealment, Petrified, EffectSpellFailure, DamageImmunityMagic, DamageImmunityAcid, DamageImmunityCold, DamageImmunityDivine, DamageImmunityElectrical, DamageImmunityFire, DamageImmunityNegative, DamageImmunityPositive, DamageImmunitySonic, DamageImmunityMagicDecrease, DamageImmunityAcidDecrease, DamageImmunityColdDecrease, DamageImmunityDivineDecrease, DamageImmunityElectricalDecrease, DamageImmunityFireDecrease, DamageImmunityNegativeDecrease, DamageImmunityPositiveDecrease, DamageImmunitySonicDecrease, Wounding

## Anvil.API.EffectRunScriptType  [enum]
- values: OnApplied, OnRemoved, OnInterval

## Anvil.API.EffectSubType  [enum]
- values: Magical, Supernatural, Extraordinary, Unyielding

## Anvil.API.EffectType  [enum]
- values: InvalidEffect, DamageResistance, Regenerate, DamageReduction, TemporaryHitpoints, Entangle, Invulnerable, Deaf, Resurrection, Immunity, EnemyAttackBonus, ArcaneSpellFailure, AreaOfEffect, Beam, Charmed, Confused, Frightened, Dominated, Paralyze, Dazed, Stunned, Sleep, Poison, Disease, Curse, Silence, Turned, Haste, Slow, AbilityIncrease, AbilityDecrease, AttackIncrease, AttackDecrease, DamageIncrease, DamageDecrease, DamageImmunityIncrease, DamageImmunityDecrease, AcIncrease, AcDecrease, MovementSpeedIncrease, MovementSpeedDecrease, SavingThrowIncrease, SavingThrowDecrease, SpellResistanceIncrease, SpellResistanceDecrease, SkillIncrease, SkillDecrease, Invisibility, ImprovedInvisibility, Darkness, DispelMagical, ElementalShield, NegativeLevel, Polymorph, Sanctuary, TrueSeeing, SeeInvisible, TimeStop, Blindness, SpellLevelAbsorption, DispelMagicBest, Ultravision, MissChance, Concealment, SpellImmunity, VisualEffect, DisappearAppear, Swarm, TurnResistanceDecrease, TurnResistanceIncrease, Petrify, CutsceneParalyze, Ethereal, SpellFailure, CutsceneGhost, CutsceneImmobilize, RunScript, Icon, Pacify, BonusFeat, TimeStopImmunity, ForceWalk, Appear, CutsceneDominated, Damage, Death, Disappear, Heal, HitpointChangeWhenDying, Knockdown, ModifyAttacks, SummonCreature, Taunt, Wounding

## Anvil.API.EncounterDifficulty  [enum]
- values: VeryEasy, Easy, Normal, Hard, Impossible

## Anvil.API.EquipmentSlots  [enum]
- values: None, Head, Chest, Boots, Arms, RightHand, LeftHand, Cloak, LeftRing, RightRing, Neck, Belt, Arrows, Bullets, Bolts, CreatureWeaponLeft, CreatureWeaponRight, CreatureWeaponBite, CreatureArmour, Rings

## Anvil.API.EventScriptType  [enum]
- values: None, ModuleOnHeartbeat, ModuleOnUserDefinedEvent, ModuleOnModuleLoad, ModuleOnModuleStart, ModuleOnClientEnter, ModuleOnClientExit, ModuleOnActivateItem, ModuleOnAcquireItem, ModuleOnLoseItem, ModuleOnPlayerDeath, ModuleOnPlayerDying, ModuleOnRespawnButtonPressed, ModuleOnPlayerRest, ModuleOnPlayerLevelUp, ModuleOnPlayerCancelCutscene, ModuleOnEquipItem, ModuleOnUnequipItem, ModuleOnPlayerChat, ModuleOnPlayerTarget, ModuleOnPlayerGuiEvent, ModuleOnPlayerTileAction, ModuleOnNuiEvent, AreaOnHeartbeat, AreaOnUserDefinedEvent, AreaOnEnter, AreaOnExit, AreaOfEffectOnHeartbeat, AreaOfEffectOnUserDefinedEvent, AreaOfEffectOnObjectEnter, AreaOfEffectOnObjectExit, CreatureOnHeartbeat, CreatureOnNotice, CreatureOnSpellCastAt, CreatureOnMeleeAttacked, CreatureOnDamaged, CreatureOnDisturbed, CreatureOnEndCombatRound, CreatureOnDialogue, CreatureOnSpawnIn, CreatureOnRested, CreatureOnDeath, CreatureOnUserDefinedEvent, CreatureOnBlockedByDoor, TriggerOnHeartbeat, TriggerOnObjectEnter, TriggerOnObjectExit, TriggerOnUserDefinedEvent, TriggerOnTrapTriggered, TriggerOnDisarmed, TriggerOnClicked, PlaceableOnClosed, PlaceableOnDamaged, PlaceableOnDeath, PlaceableOnDisarm, PlaceableOnHeartbeat, PlaceableOnInventoryDisturbed, PlaceableOnLock, PlaceableOnMeleeAttacked, PlaceableOnOpen, PlaceableOnSpellCastAt, PlaceableOnTrapTriggered, PlaceableOnUnlock, PlaceableOnUsed, PlaceableOnUserDefinedEvent, PlaceableOnDialogue, PlaceableOnLeftClick, DoorOnOpen, DoorOnClose, DoorOnDamage, DoorOnDeath, DoorOnDisarm, DoorOnHeartbeat, DoorOnLock, DoorOnMeleeAttacked, DoorOnSpellCastAt, DoorOnTrapTriggered, DoorOnUnlock, DoorOnUserDefined, DoorOnClicked, DoorOnDialogue, DoorOnFailToOpen, EncounterOnObjectEnter, EncounterOnObjectExit, EncounterOnHeartbeat, EncounterOnEncounterExhausted, EncounterOnUserDefinedEvent, StoreOnOpen, StoreOnClose

## Anvil.API.EventType  [enum]
- values: Heartbeat, Perceive, EndCombatRound, Dialogue, Attacked, Damaged, Disturbed, SpellCastAt

## Anvil.API.FadeSpeed  [class]
- const float Fast = NWScript.FADE_SPEED_FAST
- const float Fastest = NWScript.FADE_SPEED_FASTEST
- const float Medium = NWScript.FADE_SPEED_MEDIUM
- const float Slow = NWScript.FADE_SPEED_SLOW
- const float Slowest = NWScript.FADE_SPEED_SLOWEST

## Anvil.API.FamiliarCreatureType  [enum]
- values: Bat, CragCat, HellHound, Imp, FireMephit, IceMephit, Pixie, Raven, FairyDragon, PseudoDragon, Eyeball, None

## Anvil.API.Feat  [enum]
- values: Alertness, Ambidexterity, ArmorProficiencyHeavy, ArmorProficiencyLight, ArmorProficiencyMedium, CalledShot, Cleave, CombatCasting, DeflectArrows, Disarm, Dodge, EmpowerSpell, ExtendSpell, ExtraTurning, GreatFortitude, ImprovedCriticalClub, ImprovedDisarm, ImprovedKnockdown, ImprovedParry, ImprovedPowerAttack, ImprovedTwoWeaponFighting, ImprovedUnarmedStrike, IronWill, Knockdown, LightningReflexes, MaximizeSpell, Mobility, PointBlankShot, PowerAttack, QuickenSpell, RapidShot, Sap, ShieldProficiency, SilenceSpell, SkillFocusAnimalEmpathy, SpellFocusAbjuration, SpellPenetration, StillSpell, StunningFist, Toughness, TwoWeaponFighting, WeaponFinesse, WeaponFocusClub, WeaponProficiencyExotic, WeaponProficiencyMartial, WeaponProficiencySimple, WeaponSpecializationClub, WeaponProficiencyDruid, WeaponProficiencyMonk, WeaponProficiencyRogue, WeaponProficiencyWizard, ImprovedCriticalDagger, ImprovedCriticalDart, ImprovedCriticalHeavyCrossbow, ImprovedCriticalLightCrossbow, ImprovedCriticalLightMace, ImprovedCriticalMorningStar, ImprovedCriticalStaff, ImprovedCriticalSpear, ImprovedCriticalSickle, ImprovedCriticalSling, ImprovedCriticalUnarmedStrike, ImprovedCriticalLongbow, ImprovedCriticalShortbow, ImprovedCriticalShortSword, ImprovedCriticalRapier, ImprovedCriticalScimitar, ImprovedCriticalLongSword, ImprovedCriticalGreatSword, ImprovedCriticalHandAxe, ImprovedCriticalThrowingAxe, ImprovedCriticalBattleAxe, ImprovedCriticalGreatAxe, ImprovedCriticalHalberd, ImprovedCriticalLightHammer, ImprovedCriticalLightFlail, ImprovedCriticalWarHammer, ImprovedCriticalHeavyFlail, ImprovedCriticalKama, ImprovedCriticalKukri, ImprovedCriticalShuriken, ImprovedCriticalScythe, ImprovedCriticalKatana, ImprovedCriticalBastardSword, ImprovedCriticalDireMace, ImprovedCriticalDoubleAxe, ImprovedCriticalTwoBladedSword, WeaponFocusDagger, WeaponFocusDart, WeaponFocusHeavyCrossbow, WeaponFocusLightCrossbow, WeaponFocusLightMace, WeaponFocusMorningStar, WeaponFocusStaff, WeaponFocusSpear, WeaponFocusSickle, WeaponFocusSling, WeaponFocusUnarmedStrike, WeaponFocusLongbow, WeaponFocusShortbow, WeaponFocusShortSword, WeaponFocusRapier, WeaponFocusScimitar, WeaponFocusLongSword, WeaponFocusGreatSword, WeaponFocusHandAxe, WeaponFocusThrowingAxe, WeaponFocusBattleAxe, WeaponFocusGreatAxe, WeaponFocusHalberd, WeaponFocusLightHammer, WeaponFocusLightFlail, WeaponFocusWarHammer, WeaponFocusHeavyFlail, WeaponFocusKama, WeaponFocusKukri, WeaponFocusShuriken, WeaponFocusScythe, WeaponFocusKatana, WeaponFocusBastardSword, WeaponFocusDireMace, WeaponFocusDoubleAxe, WeaponFocusTwoBladedSword, WeaponSpecializationDagger, WeaponSpecializationDart, WeaponSpecializationHeavyCrossbow, WeaponSpecializationLightCrossbow, WeaponSpecializationLightMace, WeaponSpecializationMorningStar, WeaponSpecializationStaff, WeaponSpecializationSpear, WeaponSpecializationSickle, WeaponSpecializationSling, WeaponSpecializationUnarmedStrike, WeaponSpecializationLongbow, WeaponSpecializationShortbow, WeaponSpecializationShortSword, WeaponSpecializationRapier, WeaponSpecializationScimitar, WeaponSpecializationLongSword, WeaponSpecializationGreatSword, WeaponSpecializationHandAxe, WeaponSpecializationThrowingAxe, WeaponSpecializationBattleAxe, WeaponSpecializationGreatAxe, WeaponSpecializationHalberd, WeaponSpecializationLightHammer, WeaponSpecializationLightFlail, WeaponSpecializationWarHammer, WeaponSpecializationHeavyFlail, WeaponSpecializationKama, WeaponSpecializationKukri, WeaponSpecializationShuriken, WeaponSpecializationScythe, WeaponSpecializationKatana, WeaponSpecializationBastardSword, WeaponSpecializationDireMace, WeaponSpecializationDoubleAxe, WeaponSpecializationTwoBladedSword, SpellFocusConjuration, SpellFocusDivination, SpellFocusEnchantment, SpellFocusEvocation, SpellFocusIllusion, SpellFocusNecromancy, SpellFocusTransmutation, SkillFocusConcentration, SkillFocusDisableTrap, SkillFocusDiscipline, SkillFocusHeal, SkillFocusHide, SkillFocusListen, SkillFocusLore, SkillFocusMoveSilently, SkillFocusOpenLock, SkillFocusParry, SkillFocusPerform, SkillFocusPersuade, SkillFocusPickPocket, SkillFocusSearch, SkillFocusSetTrap, SkillFocusSpellcraft, SkillFocusSpot, SkillFocusTaunt, SkillFocusUseMagicDevice, BarbarianEndurance, UncannyDodge1, DamageReduction, BardicKnowledge, NatureSense, AnimalCompanion, WoodlandStride, TracklessStep, ResistNaturesLure, VenomImmunity, FlurryOfBlows, Evasion, MonkEndurance, StillMind, PurityOfBody, WholenessOfBody, ImprovedEvasion, KiStrike, DiamondBody, DiamondSoul, PerfectSelf, DivineGrace, DivineHealth, SneakAttack, CripplingStrike, DefensiveRoll, Opportunist, SkillMastery, UncannyReflex, Stonecunning, Darkvision, HardinessVersusPoisons, HardinessVersusSpells, BattleTrainingVersusOrcs, BattleTrainingVersusGoblins, BattleTrainingVersusGiants, SkillAffinityLore, ImmunityToSleep, HardinessVersusEnchantments, SkillAffinityListen, SkillAffinitySearch, SkillAffinitySpot, KeenSense, HardinessVersusIllusions, BattleTrainingVersusReptilians, SkillAffinityConcentration, PartialSkillAffinityListen, PartialSkillAffinitySearch, PartialSkillAffinitySpot, SkillAffinityMoveSilently, Lucky, Fearless, GoodAim, UncannyDodge2, UncannyDodge3, UncannyDodge4, UncannyDodge5, UncannyDodge6, WeaponProficiencyElf, BardSongs, QuickToMaster, SlipperyMind, MonkAcBonus, FavoredEnemyDwarf, FavoredEnemyElf, FavoredEnemyGnome, FavoredEnemyHalfling, FavoredEnemyHalfelf, FavoredEnemyHalforc, FavoredEnemyHuman, FavoredEnemyAberration, FavoredEnemyAnimal, FavoredEnemyBeast, FavoredEnemyConstruct, FavoredEnemyDragon, FavoredEnemyGoblinoid, FavoredEnemyMonstrous, FavoredEnemyOrc, FavoredEnemyReptilian, FavoredEnemyElemental, FavoredEnemyFey, FavoredEnemyGiant, FavoredEnemyMagicalBeast, FavoredEnemyOutsider, FavoredEnemyShapechanger, FavoredEnemyUndead, FavoredEnemyVermin, WeaponProficiencyCreature, WeaponSpecializationCreature, WeaponFocusCreature, ImprovedCriticalCreature, BarbarianRage, BarbarianRage2, BarbarianRage3, BarbarianRage4, BarbarianRage5, BarbarianRage6, BarbarianRage7, TurnUndead, QuiveringPalm, EmptyBody, LayOnHands, AuraOfCourage, SmiteEvil, RemoveDisease, SummonFamiliar, ElementalShape, ElementalShape2, ElementalShape3, ElementalShape4, WildShape, WildShape2, WildShape3, WildShape4, WildShape5, WildShape6, WarDomainPower, StrengthDomainPower, ProtectionDomainPower, LuckDomainPower, DeathDomainPower, AirDomainPower, AnimalDomainPower, DestructionDomainPower, EarthDomainPower, EvilDomainPower, FireDomainPower, GoodDomainPower, HealingDomainPower, KnowledgeDomainPower, MagicDomainPower, PlantDomainPower, SunDomainPower, TravelDomainPower, TrickeryDomainPower, WaterDomainPower, Lowlightvision, ImprovedInitiative, Artist, Blooded, Bullheaded, CourtlyMagocracy, LuckOfHeroes, ResistPoison, SilverPalm, Snakeblood, Stealthy, Strongsoul, Expertise, ImprovedExpertise, GreatCleave, SpringAttack, GreaterSpellFocusAbjuration, GreaterSpellFocusConjuration, GreaterSpellFocusDiviniation, GreaterSpellFocusDivination, GreaterSpellFocusEnchantment, GreaterSpellFocusEvocation, GreaterSpellFocusIllusion, GreaterSpellFocusNecromancy, GreaterSpellFocusTransmutation, GreaterSpellPenetration, Thug, SkillfocusAppraise, SkillFocusTumble, SkillFocusCraftTrap, BlindFight, CircleKick, ExtraStunningAttack, RapidReload, ZenArchery, DivineMight, DivineShield, ArcaneDefenseAbjuration, ArcaneDefenseConjuration, ArcaneDefenseDivination, ArcaneDefenseEnchantment, ArcaneDefenseEvocation, ArcaneDefenseIllusion, ArcaneDefenseNecromancy, ArcaneDefenseTransmutation, ExtraMusic, LingeringSong, DirtyFighting, ResistDisease, ResistEnergyCold, ResistEnergyAcid, ResistEnergyFire, ResistEnergyElectrical, ResistEnergySonic, HideInPlainSight, ShadowDaze, SummonShadow, ShadowEvade, DeneirsEye, TymorasSmile, LliirasHeart, CraftHarperItem, HarperSleep, HarperCatsGrace, HarperEaglesSplendor, HarperInvisibility, PrestigeEnchantArrow1, PrestigeEnchantArrow2, PrestigeEnchantArrow3, PrestigeEnchantArrow4, PrestigeEnchantArrow5, PrestigeImbueArrow, PrestigeSeekerArrow1, PrestigeSeekerArrow2, PrestigeHailOfArrows, PrestigeArrowOfDeath, PrestigeDeathAttack1, PrestigeDeathAttack2, PrestigeDeathAttack3, PrestigeDeathAttack4, PrestigeDeathAttack5, BlackguardSneakAttack1D6, BlackguardSneakAttack2D6, BlackguardSneakAttack3D6, PrestigePoisonSave1, PrestigePoisonSave2, PrestigePoisonSave3, PrestigePoisonSave4, PrestigePoisonSave5, PrestigeSpellGhostlyVisage, PrestigeDarkness, PrestigeInvisibility1, PrestigeInvisibility2, SmiteGood, PrestigeDarkBlessing, InflictLightWounds, InflictModerateWounds, InflictSeriousWounds, InflictCriticalWounds, BullsStrength, Contagion, EyeOfGruumshBlindingSpittle, EyeOfGruumshBlindingSpittle2, EyeOfGruumshCommandTheHorde, EyeOfGruumshSwingBlindly, EyeOfGruumshRitualScarring, Blindsight5Feet, Blindsight10Feet, EyeOfGruumshSightOfGruumsh, Blindsight60Feet, ShouDiscipleDodge2, EpicArmorSkin, EpicBlindingSpeed, EpicDamageReduction3, EpicDamageReduction6, EpicDamageReduction9, EpicDevastatingCriticalClub, EpicDevastatingCriticalDagger, EpicDevastatingCriticalDart, EpicDevastatingCriticalHeavycrossbow, EpicDevastatingCriticalLightcrossbow, EpicDevastatingCriticalLightmace, EpicDevastatingCriticalMorningstar, EpicDevastatingCriticalQuarterstaff, EpicDevastatingCriticalShortspear, EpicDevastatingCriticalSickle, EpicDevastatingCriticalSling, EpicDevastatingCriticalUnarmed, EpicDevastatingCriticalLongbow, EpicDevastatingCriticalShortbow, EpicDevastatingCriticalShortsword, EpicDevastatingCriticalRapier, EpicDevastatingCriticalScimitar, EpicDevastatingCriticalLongsword, EpicDevastatingCriticalGreatsword, EpicDevastatingCriticalHandaxe, EpicDevastatingCriticalThrowingaxe, EpicDevastatingCriticalBattleaxe, EpicDevastatingCriticalGreataxe, EpicDevastatingCriticalHalberd, EpicDevastatingCriticalLighthammer, EpicDevastatingCriticalLightflail, EpicDevastatingCriticalWarhammer, EpicDevastatingCriticalHeavyflail, EpicDevastatingCriticalKama, EpicDevastatingCriticalKukri, EpicDevastatingCriticalShuriken, EpicDevastatingCriticalScythe, EpicDevastatingCriticalKatana, EpicDevastatingCriticalBastardsword, EpicDevastatingCriticalDiremace, EpicDevastatingCriticalDoubleaxe, EpicDevastatingCriticalTwobladedsword, EpicDevastatingCriticalCreature, EpicEnergyResistanceCold1, EpicEnergyResistanceCold2, EpicEnergyResistanceCold3, EpicEnergyResistanceCold4, EpicEnergyResistanceCold5, EpicEnergyResistanceCold6, EpicEnergyResistanceCold7, EpicEnergyResistanceCold8, EpicEnergyResistanceCold9, EpicEnergyResistanceCold10, EpicEnergyResistanceAcid1, EpicEnergyResistanceAcid2, EpicEnergyResistanceAcid3, EpicEnergyResistanceAcid4, EpicEnergyResistanceAcid5, EpicEnergyResistanceAcid6, EpicEnergyResistanceAcid7, EpicEnergyResistanceAcid8, EpicEnergyResistanceAcid9, EpicEnergyResistanceAcid10, EpicEnergyResistanceFire1, EpicEnergyResistanceFire2, EpicEnergyResistanceFire3, EpicEnergyResistanceFire4, EpicEnergyResistanceFire5, EpicEnergyResistanceFire6, EpicEnergyResistanceFire7, EpicEnergyResistanceFire8, EpicEnergyResistanceFire9, EpicEnergyResistanceFire10, EpicEnergyResistanceElectrical1, EpicEnergyResistanceElectrical2, EpicEnergyResistanceElectrical3, EpicEnergyResistanceElectrical4, EpicEnergyResistanceElectrical5, EpicEnergyResistanceElectrical6, EpicEnergyResistanceElectrical7, EpicEnergyResistanceElectrical8, EpicEnergyResistanceElectrical9, EpicEnergyResistanceElectrical10, EpicEnergyResistanceSonic1, EpicEnergyResistanceSonic2, EpicEnergyResistanceSonic3, EpicEnergyResistanceSonic4, EpicEnergyResistanceSonic5, EpicEnergyResistanceSonic6, EpicEnergyResistanceSonic7, EpicEnergyResistanceSonic8, EpicEnergyResistanceSonic9, EpicEnergyResistanceSonic10, EpicFortitude, EpicProwess, EpicReflexes, EpicReputation, EpicSkillFocusAnimalEmpathy, EpicSkillFocusAppraise, EpicSkillFocusConcentration, EpicSkillFocusCraftTrap, EpicSkillFocusDisabletrap, EpicSkillFocusDiscipline, EpicSkillFocusHeal, EpicSkillFocusHide, EpicSkillFocusListen, EpicSkillFocusLore, EpicSkillFocusMovesilently, EpicSkillFocusOpenlock, EpicSkillFocusParry, EpicSkillFocusPerform, EpicSkillFocusPersuade, EpicSkillFocusPickpocket, EpicSkillFocusSearch, EpicSkillFocusSettrap, EpicSkillFocusSpellcraft, EpicSkillFocusSpot, EpicSkillFocusTaunt, EpicSkillFocusTumble, EpicSkillFocusUsemagicdevice, EpicSpellFocusAbjuration, EpicSpellFocusConjuration, EpicSpellFocusDivination, EpicSpellFocusEnchantment, EpicSpellFocusEvocation, EpicSpellFocusIllusion, EpicSpellFocusNecromancy, EpicSpellFocusTransmutation, EpicSpellPenetration, EpicWeaponFocusClub, EpicWeaponFocusDagger, EpicWeaponFocusDart, EpicWeaponFocusHeavycrossbow, EpicWeaponFocusLightcrossbow, EpicWeaponFocusLightmace, EpicWeaponFocusMorningstar, EpicWeaponFocusQuarterstaff, EpicWeaponFocusShortspear, EpicWeaponFocusSickle, EpicWeaponFocusSling, EpicWeaponFocusUnarmed, EpicWeaponFocusLongbow, EpicWeaponFocusShortbow, EpicWeaponFocusShortsword, EpicWeaponFocusRapier, EpicWeaponFocusScimitar, EpicWeaponFocusLongsword, EpicWeaponFocusGreatsword, EpicWeaponFocusHandaxe, EpicWeaponFocusThrowingaxe, EpicWeaponFocusBattleaxe, EpicWeaponFocusGreataxe, EpicWeaponFocusHalberd, EpicWeaponFocusLighthammer, EpicWeaponFocusLightflail, EpicWeaponFocusWarhammer, EpicWeaponFocusHeavyflail, EpicWeaponFocusKama, EpicWeaponFocusKukri, EpicWeaponFocusShuriken, EpicWeaponFocusScythe, EpicWeaponFocusKatana, EpicWeaponFocusBastardsword, EpicWeaponFocusDiremace, EpicWeaponFocusDoubleaxe, EpicWeaponFocusTwobladedsword, EpicWeaponFocusCreature, EpicWeaponSpecializationClub, EpicWeaponSpecializationDagger, EpicWeaponSpecializationDart, EpicWeaponSpecializationHeavycrossbow, EpicWeaponSpecializationLightcrossbow, EpicWeaponSpecializationLightmace, EpicWeaponSpecializationMorningstar, EpicWeaponSpecializationQuarterstaff, EpicWeaponSpecializationShortspear, EpicWeaponSpecializationSickle, EpicWeaponSpecializationSling, EpicWeaponSpecializationUnarmed, EpicWeaponSpecializationLongbow, EpicWeaponSpecializationShortbow, EpicWeaponSpecializationShortsword, EpicWeaponSpecializationRapier, EpicWeaponSpecializationScimitar, EpicWeaponSpecializationLongsword, EpicWeaponSpecializationGreatsword, EpicWeaponSpecializationHandaxe, EpicWeaponSpecializationThrowingaxe, EpicWeaponSpecializationBattleaxe, EpicWeaponSpecializationGreataxe, EpicWeaponSpecializationHalberd, EpicWeaponSpecializationLighthammer, EpicWeaponSpecializationLightflail, EpicWeaponSpecializationWarhammer, EpicWeaponSpecializationHeavyflail, EpicWeaponSpecializationKama, EpicWeaponSpecializationKukri, EpicWeaponSpecializationShuriken, EpicWeaponSpecializationScythe, EpicWeaponSpecializationKatana, EpicWeaponSpecializationBastardsword, EpicWeaponSpecializationDiremace, EpicWeaponSpecializationDoubleaxe, EpicWeaponSpecializationTwobladedsword, EpicWeaponSpecializationCreature, EpicWill, EpicImprovedCombatCasting, EpicImprovedKiStrike4, EpicImprovedKiStrike5, EpicImprovedSpellResistance1, EpicImprovedSpellResistance2, EpicImprovedSpellResistance3, EpicImprovedSpellResistance4, EpicImprovedSpellResistance5, EpicImprovedSpellResistance6, EpicImprovedSpellResistance7, EpicImprovedSpellResistance8, EpicImprovedSpellResistance9, EpicImprovedSpellResistance10, EpicOverwhelmingCriticalClub, EpicOverwhelmingCriticalDagger, EpicOverwhelmingCriticalDart, EpicOverwhelmingCriticalHeavycrossbow, EpicOverwhelmingCriticalLightcrossbow, EpicOverwhelmingCriticalLightmace, EpicOverwhelmingCriticalMorningstar, EpicOverwhelmingCriticalQuarterstaff, EpicOverwhelmingCriticalShortspear, EpicOverwhelmingCriticalSickle, EpicOverwhelmingCriticalSling, EpicOverwhelmingCriticalUnarmed, EpicOverwhelmingCriticalLongbow, EpicOverwhelmingCriticalShortbow, EpicOverwhelmingCriticalShortsword, EpicOverwhelmingCriticalRapier, EpicOverwhelmingCriticalScimitar, EpicOverwhelmingCriticalLongsword, EpicOverwhelmingCriticalGreatsword, EpicOverwhelmingCriticalHandaxe, EpicOverwhelmingCriticalThrowingaxe, EpicOverwhelmingCriticalBattleaxe, EpicOverwhelmingCriticalGreataxe, EpicOverwhelmingCriticalHalberd, EpicOverwhelmingCriticalLighthammer, EpicOverwhelmingCriticalLightflail, EpicOverwhelmingCriticalWarhammer, EpicOverwhelmingCriticalHeavyflail, EpicOverwhelmingCriticalKama, EpicOverwhelmingCriticalKukri, EpicOverwhelmingCriticalShuriken, EpicOverwhelmingCriticalScythe, EpicOverwhelmingCriticalKatana, EpicOverwhelmingCriticalBastardsword, EpicOverwhelmingCriticalDiremace, EpicOverwhelmingCriticalDoubleaxe, EpicOverwhelmingCriticalTwobladedsword, EpicOverwhelmingCriticalCreature, EpicPerfectHealth, EpicSelfConcealment10, EpicSelfConcealment20, EpicSelfConcealment30, EpicSelfConcealment40, EpicSelfConcealment50, EpicSuperiorInitiative, EpicToughness1, EpicToughness2, EpicToughness3, EpicToughness4, EpicToughness5, EpicToughness6, EpicToughness7, EpicToughness8, EpicToughness9, EpicToughness10, EpicGreatCharisma1, EpicGreatCharisma2, EpicGreatCharisma3, EpicGreatCharisma4, EpicGreatCharisma5, EpicGreatCharisma6, EpicGreatCharisma7, EpicGreatCharisma8, EpicGreatCharisma9, EpicGreatCharisma10, EpicGreatConstitution1, EpicGreatConstitution2, EpicGreatConstitution3, EpicGreatConstitution4, EpicGreatConstitution5, EpicGreatConstitution6, EpicGreatConstitution7, EpicGreatConstitution8, EpicGreatConstitution9, EpicGreatConstitution10, EpicGreatDexterity1, EpicGreatDexterity2, EpicGreatDexterity3, EpicGreatDexterity4, EpicGreatDexterity5, EpicGreatDexterity6, EpicGreatDexterity7, EpicGreatDexterity8, EpicGreatDexterity9, EpicGreatDexterity10, EpicGreatIntelligence1, EpicGreatIntelligence2, EpicGreatIntelligence3, EpicGreatIntelligence4, EpicGreatIntelligence5, EpicGreatIntelligence6, EpicGreatIntelligence7, EpicGreatIntelligence8, EpicGreatIntelligence9, EpicGreatIntelligence10, EpicGreatWisdom1, EpicGreatWisdom2, EpicGreatWisdom3, EpicGreatWisdom4, EpicGreatWisdom5, EpicGreatWisdom6, EpicGreatWisdom7, EpicGreatWisdom8, EpicGreatWisdom9, EpicGreatWisdom10, EpicGreatStrength1, EpicGreatStrength2, EpicGreatStrength3, EpicGreatStrength4, EpicGreatStrength5, EpicGreatStrength6, EpicGreatStrength7, EpicGreatStrength8, EpicGreatStrength9, EpicGreatStrength10, EpicGreatSmiting1, EpicGreatSmiting2, EpicGreatSmiting3, EpicGreatSmiting4, EpicGreatSmiting5, EpicGreatSmiting6, EpicGreatSmiting7, EpicGreatSmiting8, EpicGreatSmiting9, EpicGreatSmiting10, EpicImprovedSneakAttack1, EpicImprovedSneakAttack2, EpicImprovedSneakAttack3, EpicImprovedSneakAttack4, EpicImprovedSneakAttack5, EpicImprovedSneakAttack6, EpicImprovedSneakAttack7, EpicImprovedSneakAttack8, EpicImprovedSneakAttack9, EpicImprovedSneakAttack10, EpicImprovedStunningFist1, EpicImprovedStunningFist2, EpicImprovedStunningFist3, EpicImprovedStunningFist4, EpicImprovedStunningFist5, EpicImprovedStunningFist6, EpicImprovedStunningFist7, EpicImprovedStunningFist8, EpicImprovedStunningFist9, EpicImprovedStunningFist10, EpicBaneOfEnemies, EpicDodge, EpicAutomaticQuicken1, EpicAutomaticQuicken2, EpicAutomaticQuicken3, EpicAutomaticSilentSpell1, EpicAutomaticSilentSpell2, EpicAutomaticSilentSpell3, EpicAutomaticStillSpell1, EpicAutomaticStillSpell2, EpicAutomaticStillSpell3, ShouDiscipleMartialFlurryLight, WhirlwindAttack, ImprovedWhirlwind, MightyRage, EpicLastingInspiration, CurseSong, EpicWildShapeUndead, EpicWildShapeDragon, EpicSpellMummyDust, EpicSpellDragonKnight, EpicSpellHellball, EpicSpellMageArmour, EpicSpellRuin, WeaponOfChoiceSickle, WeaponOfChoiceKama, WeaponOfChoiceKukri, KiDamage, IncreaseMultiplier, SuperiorWeaponFocus, KiCritical, BoneSkin2, BoneSkin4, BoneSkin6, AnimateDead, SummonUndead, DeathlessVigor, UndeadGraft1, UndeadGraft2, ToughAsBone, SummonGreaterUndead, DeathlessMastery, DeathlessMasterTouch, GreaterWildshape1, ShouDiscipleMartialFlurryAny, GreaterWildshape2, GreaterWildshape3, HumanoidShape, GreaterWildshape4, SacredDefense1, SacredDefense2, SacredDefense3, SacredDefense4, SacredDefense5, DivineWrath, ExtraSmiting, SkillFocusCraftArmor, SkillFocusCraftWeapon, EpicSkillFocusCraftArmor, EpicSkillFocusCraftWeapon, SkillFocusBluff, SkillFocusIntimidate, EpicSkillFocusBluff, EpicSkillFocusIntimidate, WeaponOfChoiceClub, WeaponOfChoiceDagger, WeaponOfChoiceLightmace, WeaponOfChoiceMorningstar, WeaponOfChoiceQuarterstaff, WeaponOfChoiceShortspear, WeaponOfChoiceShortsword, WeaponOfChoiceRapier, WeaponOfChoiceScimitar, WeaponOfChoiceLongsword, WeaponOfChoiceGreatsword, WeaponOfChoiceHandaxe, WeaponOfChoiceBattleaxe, WeaponOfChoiceGreataxe, WeaponOfChoiceHalberd, WeaponOfChoiceLighthammer, WeaponOfChoiceLightflail, WeaponOfChoiceWarhammer, WeaponOfChoiceHeavyflail, WeaponOfChoiceScythe, WeaponOfChoiceKatana, WeaponOfChoiceBastardsword, WeaponOfChoiceDiremace, WeaponOfChoiceDoubleaxe, WeaponOfChoiceTwobladedsword, BrewPotion, ScribeScroll, CraftWand, DwarvenDefenderDefensiveStance, DamageReduction6, PrestigeDefensiveAwareness1, PrestigeDefensiveAwareness2, PrestigeDefensiveAwareness3, WeaponFocusDwaxe, WeaponSpecializationDwaxe, ImprovedCriticalDwaxe, EpicDevastatingCriticalDwaxe, EpicWeaponFocusDwaxe, EpicWeaponSpecializationDwaxe, EpicOverwhelmingCriticalDwaxe, WeaponOfChoiceDwaxe, UsePoison, DragonArmor, DragonAbilities, DragonImmuneParalysis, DragonImmuneFire, DragonDisBreath, EpicFighter, EpicBarbarian, EpicBard, EpicCleric, EpicDruid, EpicMonk, EpicPaladin, EpicRanger, EpicRogue, EpicSorcerer, EpicWizard, EpicArcaneArcher, EpicAssassin, EpicBlackguard, EpicShadowdancer, EpicHarperScout, EpicDivineChampion, EpicWeaponMaster, EpicPaleMaster, EpicDwarvenDefender, EpicShifter, EpicRedDragonDisc, EpicThunderingRage, EpicTerrifyingRage, EpicSpellEpicWarding, WeaponFocusWhip, WeaponSpecializationWhip, ImprovedCriticalWhip, EpicDevastatingCriticalWhip, EpicWeaponFocusWhip, EpicWeaponSpecializationWhip, EpicOverwhelmingCriticalWhip, WeaponOfChoiceWhip, EpicCharacter, EpicEpicShadowlord, EpicEpicFiend, PrestigeDeathAttack6, PrestigeDeathAttack7, PrestigeDeathAttack8, BlackguardSneakAttack4D6, BlackguardSneakAttack5D6, BlackguardSneakAttack6D6, BlackguardSneakAttack7D6, BlackguardSneakAttack8D6, BlackguardSneakAttack9D6, BlackguardSneakAttack10D6, BlackguardSneakAttack11D6, BlackguardSneakAttack12D6, BlackguardSneakAttack13D6, BlackguardSneakAttack14D6, BlackguardSneakAttack15D6, PrestigeDeathAttack9, PrestigeDeathAttack10, PrestigeDeathAttack11, PrestigeDeathAttack12, PrestigeDeathAttack13, PrestigeDeathAttack14, PrestigeDeathAttack15, PrestigeDeathAttack16, PrestigeDeathAttack17, PrestigeDeathAttack18, PrestigeDeathAttack19, PrestigeDeathAttack20, ShouDiscipleDodge3, DragonHdincreaseD6, DragonHdincreaseD8, DragonHdincreaseD10, PrestigeEnchantArrow6, PrestigeEnchantArrow7, PrestigeEnchantArrow8, PrestigeEnchantArrow9, PrestigeEnchantArrow10, PrestigeEnchantArrow11, PrestigeEnchantArrow12, PrestigeEnchantArrow13, PrestigeEnchantArrow14, PrestigeEnchantArrow15, PrestigeEnchantArrow16, PrestigeEnchantArrow17, PrestigeEnchantArrow18, PrestigeEnchantArrow19, PrestigeEnchantArrow20, EpicOutsiderShape, EpicConstructShape, EpicShifterInfiniteWildshape1, EpicShifterInfiniteWildshape2, EpicShifterInfiniteWildshape3, EpicShifterInfiniteWildshape4, EpicShifterInfiniteHumanoidShape, EpicBarbarianDamageReduction, EpicDruidInfiniteWildshape, EpicDruidInfiniteElementalShape, PrestigePoisonSaveEpic, EpicSuperiorWeaponFocus, WeaponFocusTrident, WeaponSpecializationTrident, ImprovedCriticalTrident, EpicDevastatingCriticalTrident, EpicWeaponFocusTrident, EpicWeaponSpecializationTrident, EpicOverwhelmingCriticalTrident, WeaponOfChoiceTrident, PdkRally, PdkShield, PdkFear, PdkWrath, PdkStand, PdkInspire1, PdkInspire2, MountedCombat, MountedArchery, HorseMenu, HorseMount, HorseDismount, HorsePartyMount, HorsePartyDismount, HorseAssignMount, PaladinSummonMount, PlayerTool01, PlayerTool02, PlayerTool03, PlayerTool04, PlayerTool05, PlayerTool06, PlayerTool07, PlayerTool08, PlayerTool09, PlayerTool10

## Anvil.API.FogColor  [enum]
- values: Red, RedDark, Green, GreenDark, Blue, BlueDark, Black, White, Grey, Yellow, YellowDark, Cyan, Magenta, Orange, OrangeDark, Brown, BrownDark

## Anvil.API.FogType  [enum]
- values: All, Sun, Moon

## Anvil.API.FootstepType  [enum]
- values: Invalid, Normal, Large, Dragon, Soft, Hoof, HoofLarge, Beetle, Spider, Skeleton, LeatherWing, FeatherWing, None, Seagull, Shark, WaterNormal, WaterLarge, Horse, Default

## Anvil.API.GUIPanel  [enum]
- values: Death, Minimap, Compass, Inventory, PlayerList, Journal, SpellBook, CharacterSheet, LevelUp, GoldInventory, GoldBarter, ExamineCreature, ExamineItem, ExaminePlaceable, ExamineDoor, Tile, Trigger, Creature, Item, Placeable, Door, Quickbar

## Anvil.API.GameDifficulty  [enum]
- values: VeryEasy, Easy, Normal, CoreRules, Difficult

## Anvil.API.Gender  [enum]
- values: Male, Female, Both, Other, None

## Anvil.API.GuiEventType  [enum]
- values: ChatBarFocus, ChatBarUnFocus, CharacterSheetSkillClick, CharacterSheetFeatClick, EffectIconClick, DeathPanelWaitForHelpClick, MinimapMapPinClick, MinimapOpen, MinimapClose, JournalOpen, JournalClose, PlayerListPlayerClick, PartyBarPortraitClick, DisabledPanelAttemptOpen, CompassClick, LevelUpCancelled, AreaLoadScreenFinished, QuickChatActivate, QuickChatSelect, QuickChatClose, SelectCreature, UnselectCreature, ExamineObject, OptionsOpen, OptionsClose, RadialOpen, ChatlogPortraitClick, PlayerlistPlayerTell

## Anvil.API.ImmunityType  [enum]
- values: None, MindSpells, Poison, Disease, Fear, Trap, Paralysis, Blindness, Deafness, Slow, Entangle, Silence, Stun, Sleep, Charm, Dominate, Confused, Cursed, Dazed, AbilityDecrease, AttackDecrease, DamageDecrease, DamageImmunityDecrease, AcDecrease, MovementSpeedDecrease, SavingThrowDecrease, SpellResistanceDecrease, SkillDecrease, Knockdown, NegativeLevel, SneakAttack, CriticalHit, Death

## Anvil.API.InventoryDisturbType  [enum]
- values: Added, Removed, Stolen

## Anvil.API.InventorySlot  [enum]
- values: Arms, Arrows, Belt, Bolts, Boots, Bullets, CreatureSkin, Chest, Cloak, CreatureBiteWeapon, CreatureLeftWeapon, CreatureRightWeapon, Head, LeftHand, LeftRing, Neck, RightHand, RightRing

## Anvil.API.InvisibilityType  [enum]
- values: Normal, Darkness, Improved

## Anvil.API.ItemAppearanceArmorColor  [enum]
- values: Leather1, Leather2, Cloth1, Cloth2, Metal1, Metal2

## Anvil.API.ItemAppearanceType  [enum]
- values: SimpleModel, WeaponColor, WeaponModel, ArmorModel, ArmorColor

## Anvil.API.ItemAppearanceWeaponColor  [enum]
- values: Bottom, Middle, Top

## Anvil.API.ItemAppearanceWeaponModel  [enum]
- values: Bottom, Middle, Top

## Anvil.API.IPACModifierType  [enum]
- values: Dodge, Natural, Armor, Shield, Deflection

## Anvil.API.IPAbility  [enum]
- values: Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma

## Anvil.API.IPAdditional  [enum]
- values: Unknown, Cursed

## Anvil.API.IPAlignment  [enum]
- values: LawfulGood, LawfulNeutral, LawfulEvil, NeutralGood, TrueNeutral, NeutralEvil, ChaoticGood, ChaoticNeutral, ChaoticEvil

## Anvil.API.IPAlignmentGroup  [enum]
- values: All, Neutral, Lawful, Chaotic, Good, Evil

## Anvil.API.IPAmmoType  [enum]
- values: Arrow, Bolt, Bullet

## Anvil.API.IPArcaneSpellFailure  [enum]
- values: Minus50Pct, Minus45Pct, Minus40Pct, Minus35Pct, Minus30Pct, Minus25Pct, Minus20Pct, Minus15Pct, Minus10Pct, Minus5Pct, Plus5Pct, Plus10Pct, Plus15Pct, Plus20Pct, Plus25Pct, Plus30Pct, Plus35Pct, Plus40Pct, Plus45Pct, Plus50Pct

## Anvil.API.IPCastSpell  [enum]
- values: AcidFog11, AcidSplash1, ActivateItem, Aid3, Amplify5, AnimateDead10, AnimateDead15, AnimateDead5, AuraOfVitality13, AuraVersusAlignment15, Auraofglory7, Awaken9, Balagarnsironhorn7, Bane5, Banishment15, Barkskin12, Barkskin3, Barkskin6, BestowCurse5, BigbysClenchedFist20, BigbysCrushingHand20, BigbysForcefulHand15, BigbysGraspingHand17, BigbysInterposingHand15, BladeBarrier11, BladeBarrier15, Bless2, BlindnessDeafness3, BloodFrenzy7, Bombardment20, BullsStrength10, BullsStrength15, BullsStrength3, BurningHands2, BurningHands5, CallLightning10, CallLightning5, Camoflage5, CatsGrace10, CatsGrace15, CatsGrace3, ChainLightning11, ChainLightning15, ChainLightning20, CharmMonster10, CharmMonster5, CharmPerson10, CharmPerson2, CharmPersonOrAnimal10, CharmPersonOrAnimal3, CircleOfDeath11, CircleOfDeath15, CircleOfDeath20, CircleOfDoom15, CircleOfDoom20, CircleOfDoom9, ClairaudienceClairvoyance10, ClairaudienceClairvoyance15, ClairaudienceClairvoyance5, Clarity3, Cloudkill9, ColorSpray2, ConeOfCold15, ConeOfCold9, Confusion10, Confusion5, Contagion5, ContinualFlame7, ControlUndead13, ControlUndead20, CreateGreaterUndead15, CreateGreaterUndead16, CreateGreaterUndead18, CreateUndead11, CreateUndead14, CreateUndead16, CreepingDoom13, CureCriticalWounds12, CureCriticalWounds15, CureCriticalWounds7, CureLightWounds2, CureLightWounds5, CureMinorWounds1, CureModerateWounds10, CureModerateWounds3, CureModerateWounds6, CureSeriousWounds10, CureSeriousWounds5, Darkness3, Darkvision3, Darkvision6, Daze1, DeathWard7, DelayedBlastFireball13, DelayedBlastFireball15, DelayedBlastFireball20, Destruction13, Dirge15, Dismissal12, Dismissal18, Dismissal7, DispelMagic10, DispelMagic5, Displacement9, DivineFavor5, DivineMight5, DivinePower7, DivineShield5, DominateAnimal5, DominateMonster17, DominatePerson7, Doom2, Doom5, DragonBreathAcid10, DragonBreathCold10, DragonBreathFear10, DragonBreathFire10, DragonBreathGas10, DragonBreathLightning10, DragonBreathParalyze10, DragonBreathSleep10, DragonBreathSlow10, DragonBreathWeaken10, Drown15, EagleSplendor10, EagleSplendor15, EagleSplendor3, Earthquake20, ElectricJolt1, ElementalShield12, ElementalShield7, ElementalSwarm17, Endurance10, Endurance15, Endurance3, EndureElements2, EnergyBuffer11, EnergyBuffer15, EnergyBuffer20, EnergyDrain17, Enervation7, Entangle2, Entangle5, EntropicShield5, EtherealVisage15, EtherealVisage9, Etherealness18, EvardsBlackTentacles15, EvardsBlackTentacles7, ExpeditiousRetreat5, Fear5, Feeblemind9, FindTraps3, FingerOfDeath13, FireStorm13, FireStorm18, Fireball10, Fireball5, Firebrand15, FlameArrow12, FlameArrow18, FlameArrow5, FlameLash10, FlameLash3, FlameStrike12, FlameStrike18, FlameStrike7, Flare1, FleshToStone5, FoxsCunning10, FoxsCunning15, FoxsCunning3, FreedomOfMovement7, Gate17, GhostlyVisage15, GhostlyVisage3, GhostlyVisage9, GhoulTouch3, GlobeOfInvulnerability11, Grease2, GreaterBullsStrength11, GreaterCatsGrace11, GreaterDispelling15, GreaterDispelling7, GreaterEaglesSplendor11, GreaterEndurance11, GreaterFoxsCunning11, GreaterMagicFang9, GreaterOwlsWisdom11, GreaterPlanarBinding15, GreaterRestoration13, GreaterShadowConjuration9, GreaterSpellBreach11, GreaterSpellMantle17, GreaterStoneskin11, GrenadeAcid1, GrenadeCaltrops1, GrenadeChicken1, GrenadeChoking1, GrenadeFire1, GrenadeHoly1, GrenadeTangle1, GrenadeThunderstone1, GustOfWind10, HammerOfTheGods12, HammerOfTheGods7, Harm11, Haste10, Haste5, Heal11, HealingCircle16, HealingCircle9, HoldAnimal3, HoldMonster7, HoldPerson3, HorridWilting15, HorridWilting20, IceStorm9, Identify3, Implosion17, ImprovedInvisibility7, IncendiaryCloud15, Inferno15, InflictCriticalWounds12, InflictLightWounds5, InflictMinorWounds1, InflictModerateWounds7, InflictSeriousWounds9, Invisibility3, InvisibilityPurge5, InvisibilitySphere5, IsaacsGreaterMissileStorm15, IsaacsLesserMissileStorm13, Knock3, LegendLore5, LesserDispel3, LesserDispel5, LesserMindBlank9, LesserPlanarBinding9, LesserRestoration3, LesserSpellBreach7, LesserSpellMantle9, Light1, Light5, LightningBolt10, LightningBolt5, MageArmor2, MagicCircleAgainstAlignment5, MagicFang5, MagicMissile3, MagicMissile5, MagicMissile9, ManipulatePortalStone, MassBlindnessDeafness15, MassCamouflage13, MassCharm15, MassHaste11, MassHeal15, MelfsAcidArrow3, MelfsAcidArrow6, MelfsAcidArrow9, MeteorSwarm17, MindBlank15, MindFog9, MinorGlobeOfInvulnerability15, MinorGlobeOfInvulnerability7, MordenkainensDisjunction17, MordenkainensSword13, MordenkainensSword18, NaturesBalance15, NegativeEnergyBurst10, NegativeEnergyBurst5, NegativeEnergyProtection10, NegativeEnergyProtection15, NegativeEnergyProtection5, NegativeEnergyRay1, NegativeEnergyRay3, NegativeEnergyRay5, NegativeEnergyRay7, NegativeEnergyRay9, NeutralizePoison5, OneWithTheLand7, OwlsInsight15, OwlsWisdom10, OwlsWisdom15, OwlsWisdom3, PhantasmalKiller7, PlanarAlly15, PlanarBinding11, Poison5, PolymorphSelf7, PowerWordKill17, PowerWordStun13, Prayer5, Premonition15, PrismaticSpray13, ProtectionFromAlignment2, ProtectionFromAlignment5, ProtectionFromElements10, ProtectionFromElements3, ProtectionFromSpells13, ProtectionFromSpells20, Quillfire8, RaiseDead9, RayOfEnfeeblement2, RayOfFrost1, Regenerate13, RemoveBlindnessDeafness5, RemoveCurse5, RemoveDisease5, RemoveFear2, RemoveParalysis3, ResistElements10, ResistElements3, Resistance2, Resistance5, Restoration7, Resurrection13, RoguesCunning3, Sanctuary2, Scare2, SearingLight5, SeeInvisibility3, Shades11, ShadowConjuration7, ShadowShield13, Shapechange17, Shield5, ShieldOfFaith5, Silence3, SlayLiving9, Sleep2, Sleep5, Slow5, SoundBurst3, SpecialAlcoholBeer, SpecialAlcoholSpirits, SpecialAlcoholWine, SpecialHerbBelladonna, SpecialHerbGarlic, SpellMantle13, SpellResistance15, SpellResistance9, SpikeGrowth9, StinkingCloud5, StoneToFlesh5, Stoneskin7, StormOfVengeance17, SummonCreatureI2, SummonCreatureI5, SummonCreatureIi3, SummonCreatureIii5, SummonCreatureIv7, SummonCreatureIx17, SummonCreatureV9, SummonCreatureVi11, SummonCreatureVii13, SummonCreatureViii15, Sunbeam13, Sunburst20, TashasHideousLaughter7, TensersTransformation11, TimeStop17, TrueSeeing9, TrueStrike5, UndeathsEternalFoe20, UniquePower, UniquePowerSelfOnly, VampiricTouch5, Virtue1, WailOfTheBanshee17, WallOfFire9, WarCry7, Web3, Weird17, WordOfFaith13, WoundingWhispers9

## Anvil.API.IPCastSpellNumUses  [enum]
- values: SingleUse, ChargesPerUse5, ChargesPerUse4, ChargesPerUse3, ChargesPerUse2, ChargePerUse1, ChargesPerUse0, UsePerDay1, UsesPerDay2, UsesPerDay3, UsesPerDay4, UsesPerDay5, UnlimitedUse

## Anvil.API.IPClass  [enum]
- values: Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Wizard

## Anvil.API.IPContainerWeightReduction  [enum]
- values: Reduction20Pct, Reduction40Pct, Reduction60Pct, Reduction80Pct, Reduction100Pct

## Anvil.API.IPDamageBonus  [enum]
- values: Plus1, Plus2, Plus3, Plus4, Plus5, Plus1d4, Plus1d6, Plus1d8, Plus1d10, Plus2d6, Plus2d8, Plus2d4, Plus2d10, Plus1d12, Plus2d12, Plus6, Plus7, Plus8, Plus9, Plus10

## Anvil.API.IPDamageImmunityType  [enum]
- values: Immunity5Pct, Immunity10Pct, Immunity25Pct, Immunity50Pct, Immunity75Pct, Immunity90Pct, Immunity100Pct

## Anvil.API.IPDamageReduction  [enum]
- values: DR1, DR2, DR3, DR4, DR5, DR6, DR7, DR8, DR9, DR10, DR11, DR12, DR13, DR14, DR15, DR16, DR17, DR18, DR19, DR20

## Anvil.API.IPDamageResist  [enum]
- values: Resist5, Resist10, Resist15, Resist20, Resist25, Resist30, Resist35, Resist40, Resist45, Resist50

## Anvil.API.IPDamageSoak  [enum]
- values: HP5, HP10, HP15, HP20, HP25, HP30, HP35, HP40, HP45, HP50

## Anvil.API.IPDamageType  [enum]
- values: Bludgeoning, Piercing, Slashing, Subdual, Physical, Magical, Acid, Cold, Divine, Electrical, Fire, Negative, Positive, Sonic

## Anvil.API.IPDamageVulnerabilityType  [enum]
- values: Vulnerable5Pct, Vulnerable10Pct, Vulnerable25Pct, Vulnerable50Pct, Vulnerable75Pct, Vulnerable90Pct, Vulnerable100Pct

## Anvil.API.IPFeat  [enum]
- values: Alertness, Ambidextrous, Cleave, CombatCasting, Dodge, ExtraTurning, Knockdown, PointBlank, SpellFocusAbjuration, SpellFocusConstitution, SpellFocusDivination, SpellFocusEnchantment, SpellFocusEvocation, SpellFocusIllusion, SpellFocusNecromancy, SpellPenetration, PowerAttack, TwoWeaponFighting, WeaponSpecializationUnarmed, WeaponFinesse, ImprovedCriticalUnarmed, WeaponProfExotic, WeaponProfMartial, WeaponProfSimple, ArmorProfHeavy, ArmorProfLight, ArmorProfMedium, Mobility, Disarm, Whirlwind, RapidShot, HideInPlainSight, SneakAttack1D6, SneakAttack2D6, SneakAttack3D6, ShieldProficiency, UsePoison, DisarmWhip, WeaponProfCreature, SneakAttack5D6, PlayerTool01, PlayerTool02, PlayerTool03, PlayerTool04, PlayerTool05, PlayerTool06, PlayerTool07, PlayerTool08, PlayerTool09, PlayerTool10

## Anvil.API.IPLightBrightness  [enum]
- values: Dim, Low, Normal, Bright

## Anvil.API.IPLightColor  [enum]
- values: Blue, Yellow, Purple, Red, Green, Orange, White

## Anvil.API.IPMiscImmunity  [enum]
- values: BackStab, LevelAbilityDrain, MindSpells, Poison, Disease, Fear, Knockdown, Paralysis, CriticalHits, DeathMagic

## Anvil.API.IPMonsterDamage  [enum]
- values: Damage1d2, Damage1d3, Damage1d4, Damage2d4, Damage3d4, Damage4d4, Damage5d4, Damage1d6, Damage2d6, Damage3d6, Damage4d6, Damage5d6, Damage6d6, Damage7d6, Damage8d6, Damage9d6, Damage10d6, Damage1d8, Damage2d8, Damage3d8, Damage4d8, Damage5d8, Damage6d8, Damage7d8, Damage8d8, Damage9d8, Damage10d8, Damage1d10, Damage2d10, Damage3d10, Damage4d10, Damage5d10, Damage6d10, Damage7d10, Damage8d10, Damage9d10, Damage10d10, Damage1d12, Damage2d12, Damage3d12, Damage4d12, Damage5d12, Damage6d12, Damage7d12, Damage8d12, Damage9d12, Damage10d12, Damage1d20, Damage2d20, Damage3d20, Damage4d20, Damage5d20, Damage6d20, Damage7d20, Damage8d20, Damage9d20, Damage10d20

## Anvil.API.IPOnHit  [enum]
- values: Sleep, Stun, Hold, Confusion, Daze, Doom, Fear, Knock, Slow, LesserDispel, DispelMagic, GreaterDispel, MordsDisjunction, Silence, Deafness, Blindness, LevelDrain, AbilityDrain, ItemPoison, Disease, SlayRace, SlayAlignmentGroup, SlayAlignment, Vorpal, Wounding

## Anvil.API.IPOnHitCastSpell  [enum]
- values: AcidFog, BestowCurse, BladeBarrier, BlindnessAndDeafness, CallLightning, ChainLightning, Cloudkill, Confusion, Contagion, Darkness, Daze, DelayedBlastFireball, Dismissal, DispelMagic, Doom, EnergyDrain, Enervation, Entangle, Fear, Feeblemind, FireStorm, Fireball, FlameLash, FlameStrike, GhoulTouch, Grease, GreaterDispelling, GreaterSpellBreach, GustOfWind, HammerOfTheGods, Harm, HoldAnimal, HoldMonster, HoldPerson, Implosion, IncendiaryCloud, LesserDispel, LesserSpellBreach, Light, LightningBolt, MagicMissile, MassBlindnessAndDeafness, MassCharm, MelfsAcidArrow, MeteorSwarm, MindFog, PhantasmalKiller, Poison, PowerWordKill, PowerWordStun, Scare, SearingLight, Silence, SlayLiving, Sleep, Slow, SoundBurst, StinkingCloud, StormOfVengeance, Sunbeam, VampiricTouch, WailOfTheBanshee, WallOfFire, Web, Weird, WordOfFaith, CreepingDoom, Destruction, HorridWilting, IceStorm, NegativeEnergyBurst, EvardsBlackTentacles, ActivateItem, Flare, Bombardment, AcidSplash, Quillfire, Earthquake, Sunburst, Banishment, InflictMinorWounds, InflictLightWounds, InflictModerateWounds, InflictSeriousWounds, InflictCriticalWounds, Balagarnsironhorn, Drown, ElectricJolt, Firebrand, WoundingWhispers, UndeathsEternalFoe, Inferno, IsaacsLesserMissileStorm, IsaacsGreaterMissileStorm, Bane, SpikeGrowth, TashasHideousLaughter, BigbysInterposingHand, BigbysForcefulHand, BigbysGraspingHand, BigbysClenchedFist, BigbysCrushingHand, FleshToStone, StoneToFlesh, Crumble, InfestationOfMaggots, GreatThunderclap, BallLightning, GedleesElectricLoop, HorizikaulsBoom, MestilsAcidBreath, ScintillatingSphere, UndeathToDeath, Stonehold, EvilBlight, Teleport, Slayrakshasa, FireDamage, UniquePower, PlanarRift, Darkfire, ExtractBrain, FlamingSkin, ChaosShield, ConstrictWeapon, RuinArmorBebilith, DemilichTouch, DracolichTouch, IntelligentWeapon, Paralyze2, DeafeningClang, Knockdown, Freeze, Combust

## Anvil.API.IPOnHitDuration  [enum]
- values: Duration5Pct5Rounds, Duration10Pct4Rounds, Duration25Pct3Rounds, Duration50Pct2Rounds, Duration75Pct1Round

## Anvil.API.IPOnHitSaveDC  [enum]
- values: DC14, DC16, DC18, DC20, DC22, DC24, DC26

## Anvil.API.IPOnMonsterHit  [enum]
- values: AbilityDrain, Confusion, Disease, Doom, Fear, LevelDrain, Poison, Slow, Stun, Wounding

## Anvil.API.IPPoisonDamage  [enum]
- values: Strength1d2, Dexterity1d2, Constitution1d2, Intelligence1d2, Wisdom1d2, Charisma1d2

## Anvil.API.IPQuality  [enum]
- values: Unknown, Destroyed, Ruined, VeryPoor, Poor, BelowAverage, Average, AboveAverage, Good, VeryGood, Excellent, Masterwork, GodLike, Raw, Cut, Polished

## Anvil.API.IPRacialType  [enum]
- values: Dwarf, Elf, Gnome, Halfling, HalfElf, HalfOrc, Human, Aberration, Animal, Beast, Construct, Dragon, HumanoidGoblinoid, HumanoidMonstrous, HumanoidOrc, HumanoidReptilian, Elemental, Fey, Giant, MagicalBeast, Outsider, ShapeChanger, Undead, Vermin

## Anvil.API.IPReducedWeight  [enum]
- values: Minus80Pct, Minus60Pct, Minus40Pct, Minus20Pct, Minus10Pct

## Anvil.API.IPSaveBaseType  [enum]
- values: Fortitude, Will, Reflex

## Anvil.API.IPSaveVs  [enum]
- values: Acid, Cold, Death, Disease, Divine, Electrical, Fear, Fire, MindAffecting, Negative, Poison, Positive, Sonic, Universal

## Anvil.API.IPSpellImmunity  [enum]
- values: AcidFog, Aid, Barkskin, BestowCurse, BlindnessAndDeafness, BurningHands, CallLightning, ChainLightning, CharmMonster, CharmPerson, CharmPersonOrAnimal, CircleOfDeath, CircleOfDoom, CloudKill, ColorSpray, ConeOfCold, Confusion, Contagion, ControlUndead, CureCriticalWounds, CureLightWounds, CureMinorWounds, CureModerateWounds, CureSeriousWounds, Darkness, Daze, DeathWard, DelayedBlastFireball, Dismissal, DispelMagic, DominateAnimal, DominateMonster, DominatePerson, Doom, EnergyDrain, Enervation, Entangle, Fear, Feeblemind, FingerOfDeath, FireStorm, Fireball, FlameArrow, FlameLash, FlameStrike, FreedomOfMovement, Grease, GreaterDispelling, GreaterPlanarBinding, GreaterShadowConjuration, GreaterSpellBreach, HammerOfTheGods, Harm, Heal, HealingCircle, HoldAnimal, HoldMonster, HoldPerson, Implosion, ImprovedInvisibility, IncendiaryCloud, InvisibilityPurge, LesserDispel, LesserPlanarBinding, LesserSpellBreach, LightningBolt, MagicMissile, MassBlindnessAndDeafness, MassCharm, MassHeal, MelfsAcidArrow, MeteorSwarm, MindFog, MordenkainensDisjunction, PhantasmalKiller, PlanarBinding, Poison, PowerWordKill, PowerWordStun, PrismaticSpray, RayOfEnfeeblement, RayOfFrost, Scare, SearingLight, Shades, ShadowConjuration, Silence, SlayLiving, Sleep, Slow, SoundBurst, StinkingCloud, Stoneskin, StormOfVengeance, Sunbeam, Virtue, WailOfTheBanshee, Web, Weird, WordOfFaith, MagicCircleAgainstAlignment, EagleSplendor, OwlsWisdom, FoxsCunning, GreaterEaglesSplendor, GreaterOwlsWisdom, GreaterFoxsCunning, GreaterBullsStrength, GreaterCatsGrace, GreaterEndurance, AuraOfVitality, WarCry, Regenerate, EvardsBlackTentacles, LegendLore, FindTraps

## Anvil.API.IPSpellLevel  [enum]
- values: SL0, SL1, SL2, SL3, SL4, SL5, SL6, SL7, SL8, SL9

## Anvil.API.IPSpellResistanceBonus  [enum]
- values: Plus10, Plus12, Plus14, Plus16, Plus18, Plus20, Plus22, Plus24, Plus26, Plus28, Plus30, Plus32

## Anvil.API.IPSpellSchool  [enum]
- values: Abjuration, Conjuration, Divination, Enchantment, Evocation, Illusion, Necromancy, Transmutation

## Anvil.API.IPTrapStrength  [enum]
- values: Minor, Average, Strong, Deadly

## Anvil.API.IPTrapType  [enum]
- values: Spike, Holy, Tangle, BlobOfAcid, Fire, Electrical, Gas, Frost, AcidSplash, Sonic, Negative

## Anvil.API.IPUnlimitedAmmoType  [enum]
- values: Basic, Fire1d6, Cold1d6, Light1d6, Plus1, Plus2, Plus3, Plus4, Plus5

## Anvil.API.IPWeightIncrease  [enum]
- values: Plus5Lbs, Plus10Lbs, Plus15Lbs, Plus30Lbs, Plus50Lbs, Plus100Lbs

## Anvil.API.ItemPropertyType  [enum]
- values: AbilityBonus, AcBonus, AcBonusVsAlignmentGroup, AcBonusVsDamageType, AcBonusVsRacialGroup, AcBonusVsSpecificAlignment, EnhancementBonus, EnhancementBonusVsAlignmentGroup, EnhancementBonusVsRacialGroup, EnhancementBonusVsSpecificAlignment, DecreasedEnhancementModifier, BaseItemWeightReduction, BonusFeat, BonusSpellSlotOfLevelN, CastSpell, DamageBonus, DamageBonusVsAlignmentGroup, DamageBonusVsRacialGroup, DamageBonusVsSpecificAlignment, ImmunityDamageType, DecreasedDamage, DamageReduction, DamageResistance, DamageVulnerability, Darkvision, DecreasedAbilityScore, DecreasedAc, DecreasedSkillModifier, EnhancedContainerReducedWeight, ExtraMeleeDamageType, ExtraRangedDamageType, Haste, HolyAvenger, ImmunityMiscellaneous, ImprovedEvasion, SpellResistance, SavingThrowBonus, SavingThrowBonusSpecific, Keen, Light, Mighty, MindBlank, NoDamage, OnHitProperties, DecreasedSavingThrows, DecreasedSavingThrowsSpecific, Regeneration, SkillBonus, ImmunitySpecificSpell, ImmunitySpellSchool, ThievesTools, AttackBonus, AttackBonusVsAlignmentGroup, AttackBonusVsRacialGroup, AttackBonusVsSpecificAlignment, DecreasedAttackModifier, UnlimitedAmmunition, UseLimitationAlignmentGroup, UseLimitationClass, UseLimitationRacialType, UseLimitationSpecificAlignment, UseLimitationTileset, RegenerationVampiric, Trap, TrueSeeing, OnMonsterHit, TurnResistance, MassiveCriticals, FreedomOfMovement, Poison, MonsterDamage, ImmunitySpellsByLevel, SpecialWalk, HealersKit, WeightIncrease, OnHitCastSpell, VisualEffect, ArcaneSpellFailure, Material, Quality, Additional

## Anvil.API.ItemVisual  [enum]
- values: Acid, Cold, Electrical, Fire, Sonic, Holy, Evil

## Anvil.API.LastAttackMode  [enum]
- values: Invalid, Parry, PowerAttack, ImprovedPowerAttack, FlurryOfBlows, RapidShot, Expertise, ImprovedExpertise, DefensiveCasting, DirtyFighting, DefensiveStance

## Anvil.API.MetaMagic  [enum]
- values: None, Empower, Extend, Maximize, Quicken, Silent, Still, Any

## Anvil.API.MissChanceType  [enum]
- values: Normal, VsRanged, VsMelee

## Anvil.API.MouseCursor  [enum]
- values: Default, DefaultDown, Walk, WalkDown, NoWalk, NoWalkDown, Attack, AttackDown, NoAttack, NoAttackDown, Talk, TalkDown, NoTalk, NoTalkDown, Follow, FollowDown, Examine, ExamineDown, NoExamine, NoExamineDown, Transition, TransitionDown, Door, DoorDown, Use, UseDown, Nouse, NouseDown, Magic, MagicDown, NoMagic, NoMagicDown, Disarm, DisarmDown, NoDisarm, NoDisarmDown, Action, ActionDown, NoAction, NoActionDown, Lock, LockDown, NoLock, NoLockDown, Pushpin, PushpinDown, Create, CreateDown, Nocreate, NocreateDown, Kill, KillDown, NoKill, NoKillDown, Heal, HealDown, NoHeal, NoHealDown, RunArrow, WalkArrow, Pickup, PickupDown, Custom00, Custom00Down, Custom99, Custom99Down

## Anvil.API.MovementRate  [enum]
- values: PC, Immobile, VerySlow, Slow, Normal, Fast, VeryFast, CreatureDefault, DM

## Anvil.API.NameTable  [enum]
- values: FirstGenericMale, Animal, Familiar, FirstDwarfMale, FirstDwarfFemale, LastDwarf, FirstElfMale, FirstElfFemale, LastElf, FirstGnomeMale, FirstGnomeFemale, LastGnome, FirstHalfElfMale, FirstHalfElfFemale, LastHalfElf, FirstHalflingMale, FirstHalflingFemale, LastHalfling, FirstHalfOrcMale, FirstHalfOrcFemale, LastHalfOrc, FirstHumanMale, FirstHumanFemale, LastHuman

## Anvil.API.NuiEventType  [enum]
- values: Unknown, Click, Watch, Open, Close, Focus, Blur, MouseDown, MouseUp

## Anvil.API.ObjectTypes  [enum]
- values: Creature, Item, Trigger, Door, AreaOfEffect, Waypoint, Placeable, Store, Encounter, Tile, All, Invalid

## Anvil.API.ObjectUiDiscovery  [enum]
- values: Default, None, HiliteMouseover, HiliteTab, TextbubbleMouseover, TextbubbleTab

## Anvil.API.ObjectUiTextBubbleOverride  [enum]
- values: None, Replace, Prepend, Append

## Anvil.API.ObjectVisualTransform  [enum]
- values: Scale, RotateX, RotateY, RotateZ, TranslateX, TranslateY, TranslateZ, AnimationSpeed

## Anvil.API.ObjectVisualTransformBehavior  [enum]
- values: Default, Bounce

## Anvil.API.ObjectVisualTransformDataScope  [enum]
- values: AllScopes, Base, CreatureHead, CreatureTail, CreatureWings, CreatureCloak, ItemPart1, ItemPart2, ItemPart3, ItemPart4, ItemPart5

## Anvil.API.PVPSetting  [enum]
- values: None, Party, Full, Default

## Anvil.API.PackageType  [enum]
- values: Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, WizardGeneralist, DruidInterloper, DruidGray, DruidDeath, DruidHawkmaster, BarbarianBrute, BarbarianSlayer, BarbarianSavage, BarbarianOrcBlood, ClericShaman, ClericDeadWalker, ClericElementalist, ClericBattlePriest, FighterFinesse, FighterPirate, FighterGladiator, FighterCommander, WizardAbjuration, WizardConjuration, WizardDivination, WizardEnchantment, WizardEvocation, WizardIllusion, WizardNecromancy, WizardTransmutation, SorcererAbjuration, SorcererConjuration, SorcererDivination, SorcererEnchantment, SorcererEvocation, SorcererIllusion, SorcererNecromancy, SorcererTransmutation, BardBlade, BardGallant, BardJester, BardLoremaster, MonkSpirit, MonkGifted, MonkDevout, MonkPeasant, PaladinErrant, PaladinUndead, PaladinInquisitor, PaladinChampion, RangerMarksman, RangerWarden, RangerStalker, RangerGiantkiller, RogueGypsy, RogueBandit, RogueScout, RogueSwashbuckler, Shadowdancer, Harper, ArcaneArcher, Assassin, Blackguard, NpcSorcerer, NpcRogue, NpcBard, Aberration, Animal, Construct, Humanoid, Monstrous, Elemental, Fey, Dragon, Undead, Commoner, Beast, Giant, Magicbeast, Outsider, Shapechanger, Vermin, DwarvenDefender, BarbarianBlackguard, BardHarper, ClericDivine, DruidShifter, FighterWeaponmaster, MonkAssassin, PaladinDivine, RangerArcanearcher, RogueShadowdancer, SorcererDragondisciple, WizardPalemaster, NpcWizassassin, NpcFtWeaponmaster, NpcRgShadowdancer, NpcClericLinu, NpcBarbarianDaelan, NpcBardFighter, NpcPaladinFalling, Shifter, DivineChampion, PaleMaster, DragonDisciple, Weaponmaster, NpcFtWeaponmasterValen2, NpcBardFighterSharwyn2, NpcWizassassinNathyrra, NpcRgTomi2, NpcBardDeekin2, BarbarianBlackguard2Ndclass, BardHarper2Ndclass, ClericDivine2Ndclass, DruidShifter2Ndclass, FighterWeaponmaster2Ndclass, MonkAssassin2Ndclass, PaladinDivine2Ndclass, RangerArcanearcher2Ndclass, RogueShadowdancer2Ndclass, SorcererDragondisciple2Ndclass, WizardPalemaster2Ndclass, NpcAribethPaladin, NpcAribethBlackguard, Invalid

## Anvil.API.PanelButton  [enum]
- values: Map, Inventory, Journal, Character, Options, Spells, Rest, PlayerVersusPlayer

## Anvil.API.PerceptionEventType  [enum]
- values: Unknown, Seen, Vanished, Heard, Inaudible

## Anvil.API.PerceptionType  [enum]
- values: SeenAndHeard, NotSeenAndNotHeard, HeardAndNotSeen, SeenAndNotHeard, NotHeard, Heard, NotSeen, Seen

## Anvil.API.PersistentVfxType  [enum]
- values: PerFogacid, PerFogfire, PerFogstink, PerFogkill, PerFogmind, PerWallfire, PerWallwind, PerWallblade, PerWeb, PerEntangle, PerDarkness, MobCircevil, MobCircgood, MobCirclaw, MobCircchaos, MobFear, MobBlinding, MobUnearthly, MobMenace, MobUnnatural, MobStun, MobProtection, MobFire, MobFrost, MobElectrical, PerFogghoul, MobTyrantFog, PerStorm, PerInvisSphere, MobSilence, PerDelayBlastFireball, PerGrease, PerCreepingDoom, PerEvardsBlackTentacles, MobInvisibilityPurge, MobDragonFear, PerCustomAoe, PerGlyphOfWarding, PerFogOfBewilderment, PerVineMineCamouflage, MobTideOfBattle, PerStonehold, PerOvermind, MobHorrificappearance, MobTroglodyteStench

## Anvil.API.PersistentZone  [enum]
- values: Active, Follow

## Anvil.API.Phenotype  [enum]
- values: Normal, Big, Custom1, Custom2, Custom3, Custom4, Custom5, Custom6, Custom7, Custom8, Custom9, Custom10, Custom11, Custom12, Custom13, Custom14, Custom15, Custom16, Custom17, Custom18

## Anvil.API.PlaceableAction  [enum]
- values: Use, Unlock, Bash, Knock

## Anvil.API.PlayerDeviceProperty  [class]
- static readonly PlayerDeviceProperty GuiHeight = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GUI_HEIGHT)
- static readonly PlayerDeviceProperty GuiScale = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GUI_SCALE)
- static readonly PlayerDeviceProperty GuiWidth = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GUI_WIDTH)
- static readonly PlayerDeviceProperty GraphicsAntialiasingMode = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_ANTIALIASING_MODE)
- static readonly PlayerDeviceProperty GraphicsAnisotropicFiltering = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_ANISOTROPIC_FILTERING)
- static readonly PlayerDeviceProperty GraphicsGamma = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_GAMMA)
- static readonly PlayerDeviceProperty GraphicsTextureAnimations = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_TEXTURE_ANIMATIONS)
- static readonly PlayerDeviceProperty GraphicsSkyboxes = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_SKYBOXES)
- static readonly PlayerDeviceProperty GraphicsCreatureWind = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_CREATURE_WIND)
- static readonly PlayerDeviceProperty GraphicsSecondStoryTiles = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_SECOND_STORY_TILES)
- static readonly PlayerDeviceProperty GraphicsTileBorders = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_TILE_BORDERS)
- static readonly PlayerDeviceProperty GraphicsSpellTargetingEffect = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_SPELL_TARGETING_EFFECT)
- static readonly PlayerDeviceProperty GraphicsTexturesPack = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_TEXTURES_PACK)
- static readonly PlayerDeviceProperty GraphicsGrass = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_GRASS)
- static readonly PlayerDeviceProperty GraphicsGrassRenderDistance = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_GRASS_RENDER_DISTANCE)
- static readonly PlayerDeviceProperty GraphicsShinyWater = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_SHINY_WATER)
- static readonly PlayerDeviceProperty GraphicsLightingMaxLights = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_LIGHTING_MAX_LIGHTS)
- static readonly PlayerDeviceProperty GraphicsLightingEnhanced = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_LIGHTING_ENHANCED)
- static readonly PlayerDeviceProperty GraphicsShadowsEnvironment = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_SHADOWS_ENVIRONMENT)
- static readonly PlayerDeviceProperty GraphicsShadowsCreatures = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_SHADOWS_CREATURES)
- static readonly PlayerDeviceProperty GraphicsShadowsMaxCastingLights = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_SHADOWS_MAX_CASTING_LIGHTS)
- static readonly PlayerDeviceProperty GraphicsEffectsHighQuality = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_EFFECTS_HIGH_QUALITY)
- static readonly PlayerDeviceProperty GraphicsEffectsCreatureEnvironmentMapping = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_EFFECTS_CREATURE_ENVIRONMENT_MAPPING)
- static readonly PlayerDeviceProperty GraphicsKeyholing = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_KEYHOLING)
- static readonly PlayerDeviceProperty GraphicsKeyholingWithTooltip = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_KEYHOLING_WITH_TOOLTIP)
- static readonly PlayerDeviceProperty GraphicsKeyholingDisablesCameraCollisions = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_KEYHOLING_DISABLES_CAMERA_COLLISIONS)
- static readonly PlayerDeviceProperty GraphicsFboSsao = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_FBO_SSAO)
- static readonly PlayerDeviceProperty GraphicsFboHighContrast = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_FBO_HIGH_CONTRAST)
- static readonly PlayerDeviceProperty GraphicsFboVibrance = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_FBO_VIBRANCE)
- static readonly PlayerDeviceProperty GraphicsFboToon = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_FBO_TOON)
- static readonly PlayerDeviceProperty GraphicsFboDof = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_FBO_DOF)
- static readonly PlayerDeviceProperty GraphicsLOD = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_LOD)
- static readonly PlayerDeviceProperty GraphicsRenderCloaks = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_RENDER_CLOAKS)
- static readonly PlayerDeviceProperty GraphicsGeneratePLTWithShaders = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_GENERATE_PLT_WITH_SHADERS)
- static readonly PlayerDeviceProperty GraphicsHilite = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_HILITE)
- static readonly PlayerDeviceProperty GraphicsHiliteGlow = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GRAPHICS_HILITE_GLOW)
- static readonly PlayerDeviceProperty InputKeyboardShiftWalkInverted = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_INPUT_KEYBOARD_SHIFT_WALK_INVERTED)
- static readonly PlayerDeviceProperty InputMouseHardwarePointer = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_INPUT_MOUSE_HARDWARE_POINTER)
- static readonly PlayerDeviceProperty UiScale = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_SCALE)
- static readonly PlayerDeviceProperty UiLargeFont = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_LARGE_FONT)
- static readonly PlayerDeviceProperty UiTooltipDelay = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_TOOLTIP_DELAY)
- static readonly PlayerDeviceProperty UiMouseoverFeedback = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_MOUSEOVER_FEEDBACK)
- static readonly PlayerDeviceProperty UiTextBubble = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_TEXT_BUBBLE)
- static readonly PlayerDeviceProperty UiTargetingFeedback = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_TARGETING_FEEDBACK)
- static readonly PlayerDeviceProperty UiCanClickSelfWhileWalking = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_CAN_CLICK_SELF_WHILE_WALKING)
- static readonly PlayerDeviceProperty UiFloatingTextFeedback = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_FLOATING_TEXT_FEEDBACK)
- static readonly PlayerDeviceProperty UiFloatingTextFeedbackDamageTotalsOnly = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_FLOATING_TEXT_FEEDBACK_DAMAGE_TOTALS_ONLY)
- static readonly PlayerDeviceProperty UiHideQuickchatTextInChatWindow = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_HIDE_QUICKCHAT_TEXT_IN_CHAT_WINDOW)
- static readonly PlayerDeviceProperty UiConfirmSelfcastSpells = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_CONFIRM_SELFCAST_SPELLS)
- static readonly PlayerDeviceProperty UiConfirmSelfcastFeats = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_CONFIRM_SELFCAST_FEATS)
- static readonly PlayerDeviceProperty UiConfirmSelfcastItems = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_CONFIRM_SELFCAST_ITEMS)
- static readonly PlayerDeviceProperty UiChargenSortClasses = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_CHARGEN_SORT_CLASSES)
- static readonly PlayerDeviceProperty UiChatPanePrimaryHeight = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_CHAT_PANE_PRIMARY_HEIGHT)
- static readonly PlayerDeviceProperty UiChatPaneSecondaryHeight = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_CHAT_PANE_SECONDARY_HEIGHT)
- static readonly PlayerDeviceProperty UiChatSwearFilter = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_CHAT_SWEAR_FILTER)
- static readonly PlayerDeviceProperty UiPartyInvitePopup = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_PARTY_INVITE_POPUP)
- static readonly PlayerDeviceProperty UiSpellbookSortSpells = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_SPELLBOOK_SORT_SPELLS)
- static readonly PlayerDeviceProperty UiRadialSpellcastingAlwaysSubradial = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_RADIAL_SPELLCASTING_ALWAYS_SUBRADIAL)
- static readonly PlayerDeviceProperty UiRadialClassAbilitiesAlwaysSubradial = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_RADIAL_CLASS_ABILITIES_ALWAYS_SUBRADIAL)
- static readonly PlayerDeviceProperty UiDisplayLoadscreenHintsInChatlog = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_DISPLAY_LOADSCREEN_HINTS_IN_CHATLOG)
- static readonly PlayerDeviceProperty UiMouseScale = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_MOUSE_SCALE)
- static readonly PlayerDeviceProperty UiMouseScaleValue = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_UI_MOUSE_SCALE_VALUE)
- static readonly PlayerDeviceProperty CameraMode = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_CAMERA_MODE)
- static readonly PlayerDeviceProperty CameraEdgeTurning = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_CAMERA_EDGE_TURNING)
- static readonly PlayerDeviceProperty CameraDialogZoom = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_CAMERA_DIALOG_ZOOM)
- static readonly PlayerDeviceProperty GameGore = new PlayerDeviceProperty(NWScript.PLAYER_DEVICE_PROPERTY_GAME_GORE)

## Anvil.API.PlayerIdConstants  [class]
- const uint AllClients = 0x0FFFFFFFF
- const uint AllGameMasters = 0x0FFFFFFF6
- const uint AllPlayers = 0x0FFFFFFF7
- const uint AllServerAdmins = 0x0FFFFFFF5
- const uint Invalid = 0x0FFFFFFFE
- const uint Server = 0x0FFFFFFFD

## Anvil.API.PlayerLanguage  [enum]
- values: Invalid, English, French, German, Italian, Spanish, Polish

## Anvil.API.PlayerPlatform  [enum]
- values: Invalid, WindowsX86, WindowsX64, LinuxX86, LinuxX64, LinuxArm32, LinuxArm64, MacX86, MacX64, MacArm64, Ios, AndroidArm32, AndroidArm64, AndroidX64, NintendoSwitch, MicrosoftXboxOne, SonyPs4

## Anvil.API.PoisonType  [enum]
- values: Nightshade, SmallCentipedePoison, BladeBane, GreenbloodOil, Bloodroot, PurpleWormPoison, LargeScorpionVenom, WyvernPoison, BlueWhinnis, GiantWaspPoison, ShadowEssence, BlackAdderVenom, Deathblade, MalyssRootPaste, Nitharit, DragonBile, SassoneLeafResidue, TerinavRoot, CarrionCrawlerBrainJuice, BlackLotusExtract, OilOfTaggit, IdMoss, StripedToadstool, Arsenic, LichDust, DarkReaverPowder, UngolDust, BurntOthurFumes, ChaosMist, BebilithVenom, QuasitVenom, PitFiendIchor, EttercapVenom, AraneaVenom, TinySpiderVenom, SmallSpiderVenom, MediumSpiderVenom, LargeSpiderVenom, HugeSpiderVenom, GargantuanSpiderVenom, ColossalSpiderVenom, PhaseSpiderVenom, WraithSpiderVenom, IronGolem

## Anvil.API.PolymorphType  [enum]
- values: Werewolf, Wererat, Werecat, GiantSpider, Troll, UmberHulk, Pixie, Zombie, RedDragon, FireGiant, Balor, DeathSlaad, IronGolem, HugeFireElemental, HugeWaterElemental, HugeEarthElemental, HugeAirElemental, ElderFireElemental, ElderWaterElemental, ElderEarthElemental, ElderAirElemental, BrownBear, Panther, Wolf, Boar, Badger, Penguin, Cow, DoomKnight, Yuanti, Imp, Quasit, Succubus, DireBrownBear, DirePanther, DireWolf, DireBoar, DireBadger, CelestialAvenger, Vrock, Chicken, FrostGiantMale, FrostGiantFemale, Heurodis, JnahGiantMale, JnahGiantFemale, WyrmlingWhite, WyrmlingBlue, WyrmlingRed, WyrmlingGreen, WyrmlingBlack, GolemAutomaton, Manticore, MaleDrow, Harpy, Basilisk, Drider, Beholder, Medusa, Gargoyle, Minotaur, SuperChicken, Mindflayer, DireTiger, FemaleDrow, AncientBlueDragon, AncientRedDragon, AncientGreenDragon, VampireMale, RisenLord, Spectre, VampireFemale, NullHuman

## Anvil.API.ProjectilePathType  [enum]
- values: Default, Homing, Ballistic, HighBallistic, BurstUp, Accelerating, Spiral, Linked, Bounce, Burst, LinkedBurstUp, TripleBallisticHit, TripleBallisticMiss, DoubleBallistic

## Anvil.API.QuickBarButtonType  [enum]
- values: Empty, Item, Spell, Skill, Feat, Dialog, Attack, Emote, ItemPropertyCastSpell, ModeToggle, Command, PossessFamiliar, AssociateCommand, Examine, Barter, QuickChat, CancelPolymorph, SpellLikeAbility

## Anvil.API.RacialType  [enum]
- values: Dwarf, Elf, Gnome, Halfling, HalfElf, HalfOrc, Human, Aberration, Animal, Beast, Construct, Dragon, HumanoidGoblinoid, HumanoidMonstrous, HumanoidOrc, HumanoidReptilian, Elemental, Fey, Giant, MagicalBeast, Outsider, ShapeChanger, Undead, Vermin, All, Invalid, Ooze

## Anvil.API.RadiusSize  [class]
- const float Colossal = NWScript.RADIUS_SIZE_COLOSSAL
- const float Gargantuan = NWScript.RADIUS_SIZE_GARGANTUAN
- const float Huge = NWScript.RADIUS_SIZE_HUGE
- const float Large = NWScript.RADIUS_SIZE_LARGE
- const float Medium = NWScript.RADIUS_SIZE_MEDIUM
- const float Small = NWScript.RADIUS_SIZE_SMALL

## Anvil.API.RegexpFormat  [enum]
- values: Default, Sed, NoCopy, FirstOnly

## Anvil.API.RegexpMatch  [enum]
- values: NotBol, NotEol, NotBow, NotEow, Any, NotNull, Continuous, PrevAvail

## Anvil.API.RegexpType  [enum]
- values: Ecmascript, Basic, Extended, Awk, Grep, Egrep, Icase, Nosubs

## Anvil.API.ReputationType  [enum]
- values: Friend, Enemy, Neutral

## Anvil.API.ResRefType  [enum]
- values: BMP, MVE, TGA, WAV, PLT, INI, BMU, MPG, TXT, PLH, TEX, MDL, THG, FNT, LUA, SLT, NSS, NCS, MOD, ARE, SET, IFO, BIC, WOK, TWODA, TLK, TXI, GIT, BTI, UTI, BTC, UTC, DLG, ITP, BTT, UTT, DDS, BTS, UTS, LTR, GFF, FAC, BTE, UTE, BTD, UTD, BTP, UTP, DFT, GIC, GUI, CSS, CCS, BTM, UTM, DWK, PWK, BTG, UTG, JRL, SAV, UTW, FOURPC, SSF, HAK, NWM, BIK, NDB, PTM, PTT, BAK, DAT, SHD, XBC, WBM, MTR, KTX, TTF, SQL, TML, SQ3, LOD, GIF, PNG, JPG, CAF, JUI, IDS, ERF, BIF, KEY

## Anvil.API.ResistSpellResult  [enum]
- values: NonPlayerSpell, Failed, Resisted, ResistedMagicImmune, ResistedSpellAbsorbed

## Anvil.API.RestEventType  [enum]
- values: Invalid, Started, Finished, Cancelled

## Anvil.API.SavingThrow  [enum]
- values: All, Fortitude, Reflex, Will

## Anvil.API.SavingThrowResult  [enum]
- values: Failure, Success, Immune

## Anvil.API.SavingThrowType  [enum]
- values: All, None, MindSpells, Poison, Disease, Fear, Sonic, Acid, Fire, Electricity, Positive, Negative, Death, Cold, Divine, Trap, Spell, Good, Evil, Law, Chaos, Paralysis

## Anvil.API.ScreenAnchor  [enum]
- values: TopLeft, TopRight, BottomLeft, BottomRight, Center

## Anvil.API.ScriptConstants  [class]
- const string GameEventScriptName = "____anvil_event"
- const int MaxScriptNameSize = ResourceManager.MaxNameLength
- const string NWNXEventScriptName = "___anvilx_event"

## Anvil.API.SettleFlags  [enum]
- values: ReloadGrass, ReloadBorder, RecomputeLighting

## Anvil.API.ShaderUniform  [enum]
- values: Uniform1, Uniform2, Uniform3, Uniform4, Uniform5, Uniform6, Uniform7, Uniform8, Uniform9, Uniform10, Uniform11, Uniform12, Uniform13, Uniform14, Uniform15, Uniform16

## Anvil.API.Shape  [enum]
- values: SpellCylinder, Cone, Cube, SpellCone, Sphere

## Anvil.API.Skill  [enum]
- values: AnimalEmpathy, Concentration, DisableTrap, Discipline, Heal, Hide, Listen, Lore, MoveSilently, OpenLock, Parry, Perform, Persuade, PickPocket, Search, SetTrap, Spellcraft, Spot, Taunt, UseMagicDevice, Appraise, Tumble, CraftTrap, Bluff, Intimidate, CraftArmor, CraftWeapon, Ride, AllSkills

## Anvil.API.SkillResult  [enum]
- values: Failure, Success, CriticalFailure, SuccessNotPossible, AutomaticSuccess, SuccessNeverPossible

## Anvil.API.Skybox  [enum]
- values: None, GrassClear, GrassStorm, DesertClear, WinterClear, Icy

## Anvil.API.SpecialAttack  [enum]
- values: Invalid, CalledShotLeg, CalledShotArm, Sap, Disarm, ImprovedDisarm, Knockdown, ImprovedKnockdown, StunningFist, FlurryOfBlows, RapidShot

## Anvil.API.Spell  [enum]
- values: AllSpells, AcidFog, Aid, AnimateDead, Barkskin, BestowCurse, BladeBarrier, Bless, BlessWeapon, BlindnessAndDeafness, BullsStrength, BurningHands, CallLightning, CatsGrace, ChainLightning, CharmMonster, CharmPerson, CharmPersonOrAnimal, CircleOfDeath, CircleOfDoom, ClairaudienceAndClairvoyance, Clarity, CloakOfChaos, Cloudkill, ColorSpray, ConeOfCold, Confusion, Contagion, ControlUndead, CreateGreaterUndead, CreateUndead, CureCriticalWounds, CureLightWounds, CureMinorWounds, CureModerateWounds, CureSeriousWounds, Darkness, Daze, DeathWard, DelayedBlastFireball, Dismissal, DispelMagic, DivinePower, DominateAnimal, DominateMonster, DominatePerson, Doom, ElementalShield, ElementalSwarm, Endurance, EndureElements, EnergyDrain, Enervation, Entangle, Fear, Feeblemind, FingerOfDeath, FireStorm, Fireball, FlameArrow, FlameLash, FlameStrike, FreedomOfMovement, Gate, GhoulTouch, GlobeOfInvulnerability, Grease, GreaterDispelling, GreaterPlanarBinding, GreaterRestoration, GreaterSpellBreach, GreaterSpellMantle, GreaterStoneskin, GustOfWind, HammerOfTheGods, Harm, Haste, Heal, HealingCircle, HoldAnimal, HoldMonster, HoldPerson, HolyAura, HolySword, Identify, Implosion, ImprovedInvisibility, IncendiaryCloud, Invisibility, InvisibilityPurge, InvisibilitySphere, Knock, LesserDispel, LesserMindBlank, LesserPlanarBinding, LesserRestoration, LesserSpellBreach, LesserSpellMantle, Light, LightningBolt, MageArmor, MagicCircleAgainstChaos, MagicCircleAgainstEvil, MagicCircleAgainstGood, MagicCircleAgainstLaw, MagicMissile, MagicVestment, MassBlindnessAndDeafness, MassCharm, MassHaste, MassHeal, MelfsAcidArrow, MeteorSwarm, MindBlank, MindFog, MinorGlobeOfInvulnerability, GhostlyVisage, EtherealVisage, MordenkainensDisjunction, MordenkainensSword, NaturesBalance, NegativeEnergyProtection, NeutralizePoison, PhantasmalKiller, PlanarBinding, Poison, PolymorphSelf, PowerWordKill, PowerWordStun, Prayer, Premonition, PrismaticSpray, ProtectionFromChaos, ProtectionFromElements, ProtectionFromEvil, ProtectionFromGood, ProtectionFromLaw, ProtectionFromSpells, RaiseDead, RayOfEnfeeblement, RayOfFrost, RemoveBlindnessAndDeafness, RemoveCurse, RemoveDisease, RemoveFear, RemoveParalysis, ResistElements, Resistance, Restoration, Resurrection, Sanctuary, Scare, SearingLight, SeeInvisibility, ShadowShield, Shapechange, ShieldOfLaw, Silence, SlayLiving, Sleep, Slow, SoundBurst, SpellResistance, SpellMantle, SphereOfChaos, StinkingCloud, Stoneskin, StormOfVengeance, SummonCreatureI, SummonCreatureIi, SummonCreatureIii, SummonCreatureIv, SummonCreatureIx, SummonCreatureV, SummonCreatureVi, SummonCreatureVii, SummonCreatureViii, Sunbeam, TensersTransformation, TimeStop, TrueSeeing, UnholyAura, VampiricTouch, Virtue, WailOfTheBanshee, WallOfFire, Web, Weird, WordOfFaith, AbilityAuraBlinding, AbilityAuraCold, AbilityAuraElectricity, AbilityAuraFear, AbilityAuraFire, AbilityAuraMenace, AbilityAuraProtection, AbilityAuraStun, AbilityAuraUnearthlyVisage, AbilityAuraUnnatural, AbilityBoltAbilityDrainCharisma, AbilityBoltAbilityDrainConstitution, AbilityBoltAbilityDrainDexterity, AbilityBoltAbilityDrainIntelligence, AbilityBoltAbilityDrainStrength, AbilityBoltAbilityDrainWisdom, AbilityBoltAcid, AbilityBoltCharm, AbilityBoltCold, AbilityBoltConfuse, AbilityBoltDaze, AbilityBoltDeath, AbilityBoltDisease, AbilityBoltDominate, AbilityBoltFire, AbilityBoltKnockdown, AbilityBoltLevelDrain, AbilityBoltLightning, AbilityBoltParalyze, AbilityBoltPoison, AbilityBoltShards, AbilityBoltSlow, AbilityBoltStun, AbilityBoltWeb, AbilityConeAcid, AbilityConeCold, AbilityConeDisease, AbilityConeFire, AbilityConeLightning, AbilityConePoison, AbilityConeSonic, AbilityDragonBreathAcid, AbilityDragonBreathCold, AbilityDragonBreathFear, AbilityDragonBreathFire, AbilityDragonBreathGas, AbilityDragonBreathLightning, AbilityDragonBreathParalyze, AbilityDragonBreathSleep, AbilityDragonBreathSlow, AbilityDragonBreathWeaken, AbilityDragonWingBuffet, AbilityFerocity1, AbilityFerocity2, AbilityFerocity3, AbilityGazeCharm, AbilityGazeConfusion, AbilityGazeDaze, AbilityGazeDeath, AbilityGazeDestroyChaos, AbilityGazeDestroyEvil, AbilityGazeDestroyGood, AbilityGazeDestroyLaw, AbilityGazeDominate, AbilityGazeDoom, AbilityGazeFear, AbilityGazeParalysis, AbilityGazeStunned, AbilityGolemBreathGas, AbilityHellHoundFirebreath, AbilityHowlConfuse, AbilityHowlDaze, AbilityHowlDeath, AbilityHowlDoom, AbilityHowlFear, AbilityHowlParalysis, AbilityHowlSonic, AbilityHowlStun, AbilityIntensity1, AbilityIntensity2, AbilityIntensity3, AbilityKrensharScare, AbilityLesserBodyAdjustment, AbilityMephitSaltBreath, AbilityMephitSteamBreath, AbilityMummyBolsterUndead, AbilityPulseDrown, AbilityPulseSpores, AbilityPulseWhirlwind, AbilityPulseFire, AbilityPulseLightning, AbilityPulseCold, AbilityPulseNegative, AbilityPulseHoly, AbilityPulseDeath, AbilityPulseLevelDrain, AbilityPulseAbilityDrainIntelligence, AbilityPulseAbilityDrainCharisma, AbilityPulseAbilityDrainConstitution, AbilityPulseAbilityDrainDexterity, AbilityPulseAbilityDrainStrength, AbilityPulseAbilityDrainWisdom, AbilityPulsePoison, AbilityPulseDisease, AbilityRage3, AbilityRage4, AbilityRage5, AbilitySmokeClaw, AbilitySummonSlaad, AbilitySummonTanarri, AbilityTrumpetBlast, AbilityTyrantFogMist, AbilityBarbarianRage, AbilityTurnUndead, AbilityWholenessOfBody, AbilityQuiveringPalm, AbilityEmptyBody, AbilityDetectEvil, AbilityLayOnHands, AbilityAuraOfCourage, AbilitySmiteEvil, AbilityRemoveDisease, AbilitySummonAnimalCompanion, AbilitySummonFamiliar, AbilityElementalShape, AbilityWildShape, ShadesSummonShadow, ShadesConeOfCold, ShadesFireball, ShadesStoneskin, ShadesWallOfFire, ShadowConjurationSummonShadow, ShadowConjurationDarkness, ShadowConjurationInivsibility, ShadowConjurationMageArmor, ShadowConjurationMagicMissile, GreaterShadowConjurationSummonShadow, GreaterShadowConjurationAcidArrow, GreaterShadowConjurationMirrorImage, GreaterShadowConjurationWeb, GreaterShadowConjurationMinorGlobe, EagleSpledor, OwlsWisdom, FoxsCunning, GreaterEagleSplendor, GreaterOwlsWisdom, GreaterFoxsCunning, GreaterBullsStrength, GreaterCatsGrace, GreaterEndurance, Awaken, CreepingDoom, Darkvision, Destruction, HorridWilting, IceStorm, EnergyBuffer, NegativeEnergyBurst, NegativeEnergyRay, AuraOfVitality, WarCry, Regenerate, EvardsBlackTentacles, LegendLore, FindTraps, AbilitySummonMephit, AbilitySummonCelestial, AbilityBattleMastery, AbilityDivineStrength, AbilityDivineProtection, AbilityNegativePlaneAvatar, AbilityDivineTrickery, AbilityRoguesCunning, AbilityActivateItem, AbilityDragonFear, DivineFavor, TrueStrike, Flare, Shield, EntropicShield, ContinualFlame, OneWithTheLand, Camoflage, BloodFrenzy, Bombardment, AcidSplash, Quillfire, Earthquake, Sunburst, ActivateItemSelf2, Auraofglory, Banishment, InflictMinorWounds, InflictLightWounds, InflictModerateWounds, InflictSeriousWounds, InflictCriticalWounds, Balagarnsironhorn, Drown, OwlsInsight, ElectricJolt, Firebrand, WoundingWhispers, Amplify, Etherealness, UndeathsEternalFoe, Dirge, Inferno, IsaacsLesserMissileStorm, IsaacsGreaterMissileStorm, Bane, ShieldOfFaith, PlanarAlly, MagicFang, GreaterMagicFang, SpikeGrowth, MassCamoflage, ExpeditiousRetreat, TashasHideousLaughter, Displacement, BigbysInterposingHand, BigbysForcefulHand, BigbysGraspingHand, BigbysClenchedFist, BigbysCrushingHand, GrenadeFire, GrenadeTangle, GrenadeHoly, GrenadeChoking, GrenadeThunderstone, GrenadeAcid, GrenadeChicken, GrenadeCaltrops, ActivateItemPortal, DivineMight, DivineShield, ShadowDaze, SummonShadow, ShadowEvade, TymorasSmile, CraftHarperItem, FleshToStone, StoneToFlesh, TrapArrow, TrapBolt, TrapDart, TrapShuriken, AbilityBreathPetrify, AbilityTouchPetrify, AbilityGazePetrify, AbilityManticoreSpikes, RodOfWonder, DeckOfManyThings, ElementalSummoningItem, DeckAvatar, DeckGemspray, DeckButterflyspray, Healingkit, Powerstone, Spellstaff, Charger, Decharger, KoboldJump, Crumble, InfestationOfMaggots, HealingSting, GreatThunderclap, BallLightning, Battletide, Combust, DeathArmor, GedleesElectricLoop, HorizikaulsBoom, Ironguts, MestilsAcidBreath, MestilsAcidSheath, MonstrousRegeneration, ScintillatingSphere, StoneBones, UndeathToDeath, VineMine, VineMineEntangle, VineMineHamperMovement, VineMineCamouflage, BlackBladeOfDisaster, ShelgarnsPersistentBlade, BladeThirst, DeafeningClang, CloudOfBewilderment, KeenEdge, Blackstaff, FlameWeapon, IceDagger, MagicWeapon, GreaterMagicWeapon, Stonehold, Darkfire, GlyphOfWarding, AbilityMindblast, AbilityCharmmonster, IounStoneDustyRose, IounStonePaleBlue, IounStoneScarletBlue, IounStoneBlue, IounStoneDeepRed, IounStonePink, IounStonePinkGreen, AbilityWhirlwind, AbilityCommandTheHorde, AbilityAaImbueArrow, AbilityAaSeekerArrow1, AbilityAaSeekerArrow2, AbilityAaHailOfArrows, AbilityAaArrowOfDeath, AbilityAsGhostlyVisage, AbilityAsDarkness, AbilityAsInvisibility, AbilityAsImprovedInvisiblity, AbilityBgCreatedead, AbilityBgFiendishServant, AbilityBgInflictSeriousWounds, AbilityBgInflictCriticalWounds, AbilityBgContagion, AbilityBgBullsStrength, FlyingDebris, AbilityDcDivineWrath, AbilityPmAnimateDead, AbilityPmSummonUndead, AbilityPmUndeadGraft1, AbilityPmUndeadGraft2, AbilityPmSummonGreaterUndead, AbilityPmDeathlessMasterTouch, EpicHellball, EpicMummyDust, EpicDragonKnight, EpicMageArmor, EpicRuin, AbilityDwDefensiveStance, AbilityEpicMightyRage, AbilityEpicCurseSong, AbilityEpicImprovedWhirlwind, AbilityEpicShapeDragonkin, AbilityEpicShapeDragon, CraftDyeClothcolor1, CraftDyeClothcolor2, CraftDyeLeathercolor1, CraftDyeLeathercolor2, CraftDyeMetalcolor1, CraftDyeMetalcolor2, CraftAddItemProperty, CraftPoisonWeaponOrAmmo, CraftCraftWeaponSkill, CraftCraftArmorSkill, AbilityDragonBreathNegative, AbilitySeahagEvileye, AbilityAuraHorrificappearance, AbilityTroglodyteStench, HorseMenu, HorseMount, HorseDismount, HorsePartyMount, HorsePartyDismount, HorseAssignMount, PaladinSummonMount

## Anvil.API.SpellFailureType  [enum]
- values: All, Arcane

## Anvil.API.SpellSchool  [enum]
- values: Unknown, General, Abjuration, Conjuration, Divination, Enchantment, Evocation, Illusion, Necromancy, Transmutation

## Anvil.API.SpellTargetingFlags  [enum]
- values: None, HarmsEnemies, HarmsAllies, HelpsAllies, IgnoresSelf, OriginOnSelf, SuppressWithTarget

## Anvil.API.SpellTargetingShape  [enum]
- values: None, Sphere, Rect, Cone, Hsphere

## Anvil.API.StandardFaction  [enum]
- values: Hostile, Commoner, Merchant, Defender

## Anvil.API.StoreCategory  [enum]
- values: ArmorClothing, Weapons, PotionsScrolls, WandsMagicItems, Miscellaneous

## Anvil.API.SubSkill  [enum]
- values: None, FlagTrap, RecoverTrap, ExamineTrap

## Anvil.API.Subfeat  [enum]
- values: None, CalledShotLeg, CalledShotArms, ElementalShapeEarth, ElementalShapeWater, ElementalShapeFire, ElementalShapeAir, WildShapeBrownBear, WildShapePanther, WildShapeWolf, WildShapeBoar, WildShapeBadger

## Anvil.API.TalentCategory  [enum]
- values: HarmfulAreaEffectDiscriminant, HarmfulRanged, HarmfulTouch, BeneficialHealingAreaEffect, BeneficialHealingTouch, BeneficialConditionalAreaEffect, BeneficialConditionalSingle, BeneficialEnhancementAreaEffect, BeneficialEnhancementSingle, BeneficialEnhancementSelf, HarmfulAreaEffectIndiscriminant, BeneficialProtectionSelf, BeneficialProtectionSingle, BeneficialProtectionAreaEffect, BeneficialObtainAllies, PersistentAreaOfEffect, BeneficialHealingPotion, BeneficialConditionalPotion, DragonsBreath, BeneficialProtectionPotion, BeneficialEnhancementPotion, HarmfulMelee

## Anvil.API.TalentType  [enum]
- values: Spell, Feat, Skill

## Anvil.API.TalkVolume  [enum]
- values: Talk, Whisper, Shout, SilentTalk, SilentShout, Party, Tell

## Anvil.API.TileMainLightColor  [enum]
- values: Black, DimWhite, White, BrightWhite, PaleDarkYellow, DarkYellow, PaleYellow, Yellow, PaleDarkGreen, DarkGreen, PaleGreen, Green, PaleDarkAqua, DarkAqua, PaleAqua, Aqua, PaleDarkBlue, DarkBlue, PaleBlue, Blue, PaleDarkPurple, DarkPurple, PalePurple, Purple, PaleDarkRed, DarkRed, PaleRed, Red, PaleDarkOrange, DarkOrange, PaleOrange, Orange

## Anvil.API.TileRotation  [enum]
- values: Rotate0, Rotate90, Rotate180, Rotate270

## Anvil.API.TileSourceLightColor  [enum]
- values: Black, White, PaleDarkYellow, PaleYellow, PaleDarkGreen, PaleGreen, PaleDarkAqua, PaleAqua, PaleDarkBlue, PaleBlue, PaleDarkPurple, PalePurple, PaleDarkRed, PaleRed, PaleDarkOrange, PaleOrange

## Anvil.API.TilesetResRef  [class]
- const string BarrowsInterior = NWScript.TILESET_RESREF_BARROWS_INTERIOR
- const string BeholderCaves = NWScript.TILESET_RESREF_BEHOLDER_CAVES
- const string CastleExteriorRural = NWScript.TILESET_RESREF_CASTLE_EXTERIOR_RURAL
- const string CastleInterior = NWScript.TILESET_RESREF_CASTLE_INTERIOR
- const string CastleInterior2 = NWScript.TILESET_RESREF_CASTLE_INTERIOR_2
- const string CityExterior = NWScript.TILESET_RESREF_CITY_EXTERIOR
- const string CityInterior = NWScript.TILESET_RESREF_CITY_INTERIOR
- const string CityInterior2 = NWScript.TILESET_RESREF_CITY_INTERIOR_2
- const string Crypt = NWScript.TILESET_RESREF_CRYPT
- const string Desert = NWScript.TILESET_RESREF_DESERT
- const string DrowInterior = NWScript.TILESET_RESREF_DROW_INTERIOR
- const string Dungeon = NWScript.TILESET_RESREF_DUNGEON
- const string EarlyWinter2 = NWScript.TILESET_RESREF_EARLY_WINTER_2
- const string Forest = NWScript.TILESET_RESREF_FOREST
- const string ForestFacelift = NWScript.TILESET_RESREF_FOREST_FACELIFT
- const string FortInterior = NWScript.TILESET_RESREF_FORT_INTERIOR
- const string FrozenWastes = NWScript.TILESET_RESREF_FROZEN_WASTES
- const string IllithidInterior = NWScript.TILESET_RESREF_ILLITHID_INTERIOR
- const string LizardfolkInterior = NWScript.TILESET_RESREF_LIZARDFOLK_INTERIOR
- const string MedievalCity2 = NWScript.TILESET_RESREF_MEDIEVAL_CITY_2
- const string MedievalRural2 = NWScript.TILESET_RESREF_MEDIEVAL_RURAL_2
- const string Microset = NWScript.TILESET_RESREF_MICROSET
- const string MinesAndCaverns = NWScript.TILESET_RESREF_MINES_AND_CAVERNS
- const string Ruins = NWScript.TILESET_RESREF_RUINS
- const string Rural = NWScript.TILESET_RESREF_RURAL
- const string RuralWinter = NWScript.TILESET_RESREF_RURAL_WINTER
- const string RuralWinterFacelift = NWScript.TILESET_RESREF_RURAL_WINTER_FACELIFT
- const string SeaCaves = NWScript.TILESET_RESREF_SEA_CAVES
- const string Seaships = NWScript.TILESET_RESREF_SEASHIPS
- const string Sewers = NWScript.TILESET_RESREF_SEWERS
- const string Steamworks = NWScript.TILESET_RESREF_STEAMWORKS
- const string Tropical = NWScript.TILESET_RESREF_TROPICAL
- const string Underdark = NWScript.TILESET_RESREF_UNDERDARK

## Anvil.API.TouchAttackResult  [enum]
- values: Miss, Hit, CriticalHit

## Anvil.API.Track  [enum]
- values: RuralDay1, RuralDay2, RuralNight, ForestDay1, ForestDay2, ForestNight, Dungeon1, Sewer, Mines1, Mines2, Crypt1, Crypt2, DesertDay, DesertNight, WinterDay, EvilDungeon1, EvilDungeon2, CitySlumDay, CitySlumNight, CityDockDay, CityDockNight, CityWealthy, CityMarket, CityNight, Tavern1, Tavern2, Tavern3, Tavern4, RichHouse, Store, TempleGood, TempleGood2, TempleEvil, ThemeNwn, ThemeChapter1, ThemeChapter2, ThemeChapter3, ThemeChapter4, BattleRural1, BattleForest1, BattleForest2, BattleDungeon1, BattleDungeon2, BattleDungeon3, BattleCity1, BattleCity2, BattleCity3, BattleCityBoss, BattleForestBoss, BattleLizardBoss, BattleDragon, BattleAribeth, BattleEndBoss, BattleDesert, BattleWinter, Castle, ThemeAribeth1, ThemeAribeth2, ThemeGend, ThemeMaugrim, ThemeMorag, HotuTheme, HotuWaterdeep, HotuUndermountain, HotuRebelcamp, HotuFireplane, HotuQueen, HotuHellfrozeover, HotuDracolich, HotuBattleSmall, HotuBattleMed, HotuBattleLarge, HotuBattleHell, HotuBattleBoss1, HotuBattleBoss2

## Anvil.API.TrapBaseType  [enum]
- values: MinorSpike, AverageSpike, StrongSpike, DeadlySpike, MinorHoly, AverageHoly, StrongHoly, DeadlyHoly, MinorTangle, AverageTangle, StrongTangle, DeadlyTangle, MinorAcid, AverageAcid, StrongAcid, DeadlyAcid, MinorFire, AverageFire, StrongFire, DeadlyFire, MinorElectrical, AverageElectrical, StrongElectrical, DeadlyElectrical, MinorGas, AverageGas, StrongGas, DeadlyGas, MinorFrost, AverageFrost, StrongFrost, DeadlyFrost, MinorNegative, AverageNegative, StrongNegative, DeadlyNegative, MinorSonic, AverageSonic, StrongSonic, DeadlySonic, MinorAcidSplash, AverageAcidSplash, StrongAcidSplash, DeadlyAcidSplash, EpicElectrical, EpicFire, EpicFrost, EpicSonic

## Anvil.API.VfxType  [enum]
- values: None, DurBlur, DurDarkness, DurEntangle, DurFreedomOfMovement, DurGlobeInvulnerability, DurBlackout, DurInvisibility, DurMindAffectingNegative, DurMindAffectingPositive, DurGhostlyVisage, DurEtherealVisage, DurProtBarkskin, DurProtGreaterStoneskin, DurProtPremonition, DurProtShadowArmor, DurProtStoneskin, DurSanctuary, DurWeb, FnfBlinddeaf, FnfDispel, FnfDispelDisjunction, FnfDispelGreater, FnfFireball, FnfFirestorm, FnfImplosion, FnfMassHeal, FnfMassMindAffecting, FnfMeteorSwarm, FnfNaturesBalance, FnfPwkill, FnfPwstun, FnfSummonGate, FnfSummonMonster1, FnfSummonMonster2, FnfSummonMonster3, FnfSummonUndead, FnfSunbeam, FnfTimeStop, FnfWailOBanshees, FnfWeird, FnfWord, ImpAcBonus, ImpAcidL, ImpAcidS, ImpBlindDeafM, ImpBreach, ImpConfusionS, ImpDazedS, ImpDeath, ImpDiseaseS, ImpDispel, ImpDispelDisjunction, ImpDivineStrikeFire, ImpDivineStrikeHoly, ImpDominateS, ImpDoom, ImpFearS, ImpFlameM, ImpFlameS, ImpFrostL, ImpFrostS, ImpGrease, ImpHaste, ImpHealingG, ImpHealingL, ImpHealingM, ImpHealingS, ImpHealingX, ImpHolyAid, ImpKnock, BeamLightning, ImpLightningM, ImpLightningS, ImpMagblue, ImpNegativeEnergy, DurParalyzeHold, ImpPoisonL, ImpPoisonS, ImpPolymorph, ImpPulseCold, ImpPulseFire, ImpPulseHoly, ImpPulseNegative, ImpRaiseDead, ImpReduceAbilityScore, ImpRemoveCondition, ImpSilence, ImpSleep, ImpSlow, ImpSonic, ImpStun, ImpSunstrike, ImpUnsummon, ComSpecialBlueRed, ComSpecialPinkOrange, ComSpecialRedWhite, ComSpecialRedOrange, ComSpecialWhiteBlue, ComSpecialWhiteOrange, ComBloodRegWimp, ComBloodLrgWimp, ComBloodCrtWimp, ComBloodRegRed, ComBloodRegGreen, ComBloodRegYellow, ComBloodLrgRed, ComBloodLrgGreen, ComBloodLrgYellow, ComBloodCrtRed, ComBloodCrtGreen, ComBloodCrtYellow, ComSparksParry, ComUnloadModel, ComChunkRedSmall, ComChunkRedMedium, ComChunkGreenSmall, ComChunkGreenMedium, ComChunkYellowSmall, ComChunkYellowMedium, DurSpellturning, ImpImproveAbilityScore, ImpCharm, ImpMagicalVision, ImpEvilHelp, ImpGoodHelp, ImpDeathWard, DurElementalShield, DurLight, ImpMagicProtection, ImpSuperHeroism, FnfStorm, ImpElementalProtection, DurLightBlue5, DurLightBlue10, DurLightBlue15, DurLightBlue20, DurLightYellow5, DurLightYellow10, DurLightYellow15, DurLightYellow20, DurLightPurple5, DurLightPurple10, DurLightPurple15, DurLightPurple20, DurLightRed5, DurLightRed10, DurLightRed15, DurLightRed20, DurLightOrange5, DurLightOrange10, DurLightOrange15, DurLightOrange20, DurLightWhite5, DurLightWhite10, DurLightWhite15, DurLightWhite20, DurLightGrey5, DurLightGrey10, DurLightGrey15, DurLightGrey20, ImpMirv, DurDarkvision, FnfSoundBurst, FnfStrikeHoly, FnfLosEvil10, FnfLosEvil20, FnfLosEvil30, FnfLosHoly10, FnfLosHoly20, FnfLosHoly30, FnfLosNormal10, FnfLosNormal20, FnfLosNormal30, ImpHeadAcid, ImpHeadFire, ImpHeadSonic, ImpHeadElectricity, ImpHeadCold, ImpHeadHoly, ImpHeadNature, ImpHeadHeal, ImpHeadMind, ImpHeadEvil, ImpHeadOdd, DurCessateNeutral, DurCessatePositive, DurCessateNegative, DurMindAffectingDisabled, DurMindAffectingDominated, BeamFire, BeamCold, BeamHoly, BeamMind, BeamEvil, BeamOdd, BeamFireLash, ImpDeathL, DurMindAffectingFear, FnfSummonCelestial, DurGlobeMinor, ImpRestorationLesser, ImpRestoration, ImpRestorationGreater, DurProtectionElements, DurProtectionGoodMinor, DurProtectionGoodMajor, DurProtectionEvilMinor, DurProtectionEvilMajor, DurMagicalSight, DurWebMass, FnfIcestorm, DurParalyzed, ImpMirvFlame, ImpDestruction, ComChunkRedLarge, ComChunkBoneMedium, ComBloodSparkSmall, ComBloodSparkMedium, ComBloodSparkLarge, DurGhostlyPulse, FnfHorridWilting, DurBlindvision, DurLowlightvision, DurUltravision, DurMirvAcid, ImpHarm, DurBlind, DurAntiLight10, DurMagicResistance, ImpMagicResistanceUse, ImpGlobeUse, ImpWillSavingThrowUse, ImpSpikeTrap, ImpSpellMantleUse, ImpFortitudeSavingThrowUse, ImpReflexSaveThrowUse, FnfGasExplosionAcid, FnfGasExplosionEvil, FnfGasExplosionNature, FnfGasExplosionFire, FnfGasExplosionGrease, FnfGasExplosionMind, FnfSmokePuff, ImpPulseWater, ImpPulseWind, ImpPulseNature, DurAuraCold, DurAuraFire, DurAuraPoison, DurAuraDisease, DurAuraOdd, DurAuraSilence, ImpAuraHoly, ImpAuraUnearthly, ImpAuraFear, ImpAuraNegativeEnergy, DurBardSong, FnfHowlMind, FnfHowlOdd, ComHitFire, ComHitFrost, ComHitElectrical, ComHitAcid, ComHitSonic, FnfHowlWarCry, FnfScreenShake, FnfScreenBump, ComHitNegative, ComHitDivine, FnfHowlWarCryFemale, DurAuraDragonFear, DurFlagRed, DurFlagBlue, DurFlagGold, DurFlagPurple, DurFlagGoldFixed, DurFlagPurpleFixed, DurTentacle, DurPetrify, DurFreezeAnimation, ComChunkStoneSmall, ComChunkStoneMedium, BeamSilentLightning, BeamSilentFire, BeamSilentCold, BeamSilentHoly, BeamSilentMind, BeamSilentEvil, BeamSilentOdd, DurBigbysInterposingHand, ImpBigbysForcefulHand, DurBigbysClenchedFist, DurBigbysCrushingHand, DurBigbysGraspingHand, DurCaltrops, DurSmoke, DurPixiedust, FnfDeck, DurCutsceneInvisibility, EyesRedFlameHumanMale, EyesRedFlameHumanFemale, EyesRedFlameHalfelfMale, EyesRedFlameHalfelfFemale, EyesRedFlameDwarfMale, EyesRedFlameDwarfFemale, EyesRedFlameElfMale, EyesRedFlameElfFemale, EyesRedFlameGnomeMale, EyesRedFlameGnomeFemale, EyesRedFlameHalflingMale, EyesRedFlameHalflingFemale, EyesRedFlameHalforcMale, EyesRedFlameHalforcFemale, EyesRedFlameTroglodyte, EyesYelHumanMale, EyesYelHumanFemale, EyesYelDwarfMale, EyesYelDwarfFemale, EyesYelElfMale, EyesYelElfFemale, EyesYelGnomeMale, EyesYelGnomeFemale, EyesYelHalflingMale, EyesYelHalflingFemale, EyesYelHalforcMale, EyesYelHalforcFemale, EyesYelTroglodyte, EyesOrgHumanMale, EyesOrgHumanFemale, EyesOrgDwarfMale, EyesOrgDwarfFemale, EyesOrgElfMale, EyesOrgElfFemale, EyesOrgGnomeMale, EyesOrgGnomeFemale, EyesOrgHalflingMale, EyesOrgHalflingFemale, EyesOrgHalforcMale, EyesOrgHalforcFemale, EyesOrgTroglodyte, DurIounstone, ImpTornado, DurGlowLightBlue, DurGlowPurple, DurGlowBlue, DurGlowRed, DurGlowLightRed, DurGlowYellow, DurGlowLightYellow, DurGlowGreen, DurGlowLightGreen, DurGlowOrange, DurGlowLightOrange, DurGlowBrown, DurGlowLightBrown, DurGlowGrey, DurGlowWhite, DurGlowLightPurple, DurGhostTransparent, DurGhostSmoke, DurGlyphOfWarding, FnfSoundBurstSilent, BeamDisintegrate, FnfElectricExplosion, ImpDustExplosion, ImpPulseHolySilent, DurDeathArmor, DurIceskin, FnfSwingingBlade, DurInferno, FnfDemonHand, DurStonehold, FnfMysticalExplosion, DurGhostlyVisageNoSound, DurGhostSmoke2, DurFlies, FnfSummondragon, BeamFireW, BeamFireWSilent, BeamChain, BeamBlack, ImpWallspike, FnfGreaterRuin, FnfUndeadDragon, DurProtEpicArmor, FnfSummonEpicUndead, DurProtEpicArmor2, DurInfernoChest, DurIounstoneRed, DurIounstoneBlue, DurIounstoneYellow, DurIounstoneGreen, ImpMirvElectric, ComChunkRedBallista, DurInfernoNoSound, DurAuraPulseRedWhite, DurAuraPulseBlueWhite, DurAuraPulseGreenWhite, DurAuraPulseYellowWhite, DurAuraPulseMagentaWhite, DurAuraPulseCyanWhite, DurAuraPulseOrangeWhite, DurAuraPulseBrownWhite, DurAuraPulsePurpleWhite, DurAuraPulseGreyWhite, DurAuraPulseGreyBlack, DurAuraPulseBlueGreen, DurAuraPulseRedBlue, DurAuraPulseRedYellow, DurAuraPulseGreenYellow, DurAuraPulseRedGreen, DurAuraPulseBlueYellow, DurAuraPulseBlueBlack, DurAuraPulseRedBlack, DurAuraPulseGreenBlack, DurAuraPulseYellowBlack, DurAuraPulseMagentaBlack, DurAuraPulseCyanBlack, DurAuraPulseOrangeBlack, DurAuraPulseBrownBlack, DurAuraPulsePurpleBlack, DurAuraPulseCyanGreen, DurAuraPulseCyanBlue, DurAuraPulseCyanRed, DurAuraPulseCyanYellow, DurAuraPulseMagentaBlue, DurAuraPulseMagentaRed, DurAuraPulseMagentaGreen, DurAuraPulseMagentaYellow, DurAuraPulseRedOrange, DurAuraPulseYellowOrange, DurAuraRed, DurAuraGreen, DurAuraBlue, DurAuraMagenta, DurAuraYellow, DurAuraWhite, DurAuraOrange, DurAuraBrown, DurAuraPurple, DurAuraCyan, DurAuraGreenDark, DurAuraGreenLight, DurAuraRedDark, DurAuraRedLight, DurAuraBlueDark, DurAuraBlueLight, DurAuraYellowDark, DurAuraYellowLight, DurBubbles, EyesGreenHumanMale, EyesGreenHumanFemale, EyesGreenHalfelfMale, EyesGreenHalfelfFemale, EyesGreenDwarfMale, EyesGreenDwarfFemale, EyesGreenElfMale, EyesGreenElfFemale, EyesGreenGnomeMale, EyesGreenGnomeFemale, EyesGreenHalflingMale, EyesGreenHalflingFemale, EyesGreenHalforcMale, EyesGreenHalforcFemale, EyesGreenTroglodyte, EyesPurHumanMale, EyesPurHumanFemale, EyesPurDwarfMale, EyesPurDwarfFemale, EyesPurElfMale, EyesPurElfFemale, EyesPurGnomeMale, EyesPurGnomeFemale, EyesPurHalflingMale, EyesPurHalflingFemale, EyesPurHalforcMale, EyesPurHalforcFemale, EyesPurTroglodyte, EyesCynHumanMale, EyesCynHumanFemale, EyesCynDwarfMale, EyesCynDwarfFemale, EyesCynElfMale, EyesCynElfFemale, EyesCynGnomeMale, EyesCynGnomeFemale, EyesCynHalflingMale, EyesCynHalflingFemale, EyesCynHalforcMale, EyesCynHalforcFemale, EyesCynTroglodyte, EyesWhtHumanMale, EyesWhtHumanFemale, EyesWhtDwarfMale, EyesWhtDwarfFemale, EyesWhtElfMale, EyesWhtElfFemale, EyesWhtGnomeMale, EyesWhtGnomeFemale, EyesWhtHalflingMale, EyesWhtHalflingFemale, EyesWhtHalforcMale, EyesWhtHalforcFemale, EyesWhtTroglodyte, ImpPdkGenericPulse, ImpPdkGenericHeadHit, ImpPdkRallyingCry, ImpPdkHeroicShield, ImpPdkInspireCourage, DurPdkFear, ImpPdkWrath, ImpPdkOath, ImpPdkFinalStand, DurArrowInSternum, DurArrowInChestLeft, DurArrowInChestRight, DurArrowInBack, DurArrowInTemples, DurArrowInFace, DurArrowInHead, DurQuillInChest, ImpStarburstGreen, ImpStarburstRed, ImpNightmareHeadHit

## Anvil.API.VibratorMotor  [enum]
- values: Any, Left, Right

## Anvil.API.VisualTransformLerpType  [enum]
- values: None, Linear, SmoothStep, InverseSmoothStep, EaseIn, EaseOut, Quadratic, SmootherStep

## Anvil.API.VoiceChatType  [enum]
- values: Attack, BattleCry1, BattleCry2, BattleCry3, HealMe, Help, Enemies, Flee, Taunt, GuardMe, Hold, GAttack1, GAttack2, GAttack3, Pain1, Pain2, Pain3, NearDeath, Death, Poisoned, SpellFailed, WeaponSucks, FollowMe, LookHere, Group, MoveOver, PickLock, Search, Hide, CanDo, CantDo, TaskComplete, Encumbered, Selected, Hello, Yes, No, Stop, Rest, Bored, Goodbye, Thanks, Laugh, Cuss, Cheer, TalkToMe, GoodIdea, BadIdea, Threaten

## Anvil.API.WeatherType  [enum]
- values: Invalid, Clear, Rain, Snow, UseAreaSettings

## Anvil.API.Cassowary  [class]
- Cassowary() : base(CreateNew(), true)
- string DebugState
- static implicit operator Cassowary?(IntPtr intPtr)
- void AddConstraint(string constraintExpression, float strength = CassowaryStrength.Required)
- float GetValue(string varName)
- void Reset()
- void SuggestValue(string varName, float value, float strength = CassowaryStrength.Strong)

## Anvil.API.CassowaryStrength  [class]
- const float Medium = NWScript.CASSOWARY_STRENGTH_MEDIUM
- const float Required = NWScript.CASSOWARY_STRENGTH_REQUIRED
- const float Strong = NWScript.CASSOWARY_STRENGTH_STRONG
- const float Weak = NWScript.CASSOWARY_STRENGTH_WEAK

## Anvil.API.Effect  [class]
- static Effect AbilityDecrease(Ability ability, int amount)
- static Effect AbilityIncrease(Ability ability, int amount)
- static Effect ACDecrease(int amount, ACBonus acType = ACBonus.Dodge)
- static Effect ACIncrease(int amount, ACBonus acType = ACBonus.Dodge)
- static Effect Appear()
- static Effect AreaOfEffect(PersistentVfxTableEntry vfxType, ScriptCallbackHandle? onEnterHandle = null, ScriptCallbackHandle? heartbeatHandle = null, ScriptCallbackHandle? onExitHandle = null)
- static Effect AttackDecrease(int amount, AttackBonus penaltyType = AttackBonus.Misc)
- static Effect AttackIncrease(int amount, AttackBonus bonusType = AttackBonus.Misc)
- static Effect Beam(VfxType fxType, NwGameObject emitter, BodyNode origin, bool missTarget = false)
- static Effect Blindness()
- static Effect BonusFeat(NwFeat feat)
- static Effect Charmed()
- static Effect Concealment(int percentage, MissChanceType missChanceType = MissChanceType.Normal)
- static Effect Confused()
- static Effect Curse(int strMod = 1, int dexMod = 1, int conMod = 1, int intMod = 1, int wisMod = 1, int chaMod = 1)
- static Effect CutsceneDominated()
- static Effect CutsceneGhost()
- static Effect CutsceneImmobilize()
- static Effect CutsceneParalyze()
- static Effect Damage(int amount, DamageType damageType = DamageType.Magical, DamagePower damagePower = DamagePower.Normal)
- static Effect DamageDecrease(int penalty, DamageType damageType = DamageType.Magical)
- static Effect DamageImmunityDecrease(DamageType damageType, int pctImmunity)
- static Effect DamageImmunityIncrease(DamageType damageType, int pctImmunity)
- static Effect DamageIncrease(int bonus, DamageType damageType = DamageType.Magical)
- static Effect DamageIncrease(DamageBonus bonus, DamageType damageType = DamageType.Magical)
- static Effect DamageReduction(int amount, DamagePower damagePower, int totalAbsorb = 0, bool rangedOnly = false)
- static Effect DamageResistance(DamageType damageType, int amount, int totalAbsorb = 0, bool rangedOnly = false)
- static Effect DamageShield(int damageAmount, DamageBonus randomAmount, DamageType damageType)
- static Effect Darkness()
- static Effect Dazed()
- static Effect Deaf()
- static Effect Death(bool spectacularDeath = false, bool feedback = true)
- static Effect Disappear()
- static Effect DisappearAppear(Location location, int animationType = 1)
- static Effect Disease(DiseaseType diseaseType)
- static Effect DispelMagicAll(int casterLevel)
- static Effect DispelMagicBest(int casterLevel)
- static Effect Dominated()
- static Effect Entangle()
- static Effect Ethereal()
- static Effect Frightened()
- static Effect ForceWalk()
- static Effect Haste()
- static Effect Heal(int damageToHeal)
- static Effect HitPointChangeWhenDying(float hpChangePerRound)
- static Effect Icon(EffectIconTableEntry icon)
- static Effect Immunity(ImmunityType immunityType)
- static Effect Invisibility(InvisibilityType invisibilityType)
- static Effect Knockdown()
- static Effect LinkEffects(Effect baseEffect, params Effect[] effects)
- static Effect LinkEffects(Effect baseEffect, IEnumerable<Effect> effects)
- static Effect MissChance(int missPct, MissChanceType missChanceType = MissChanceType.Normal)
- static Effect ModifyAttacks(int numAttacks)
- static Effect MovementSpeedDecrease(int pctChange)
- static Effect MovementSpeedIncrease(int pctChange)
- static Effect NegativeLevel(int numLevels)
- static Effect Pacified()
- static Effect Paralyze()
- static Effect Petrify()
- static Effect Poison(PoisonType poisonType)
- static Effect Polymorph(PolymorphTableEntry polymorphType, bool locked = false, VfxType? unPolymorphVfx = VfxType.ImpPolymorph, int spellAbilityModifier = -1, int spellAbilityCasterLevel = 0)
- static Effect Regenerate(int amountPerInterval, TimeSpan interval)
- static Effect Resurrection()
- static Effect RunAction(ScriptCallbackHandle? onAppliedHandle = null, ScriptCallbackHandle? onRemovedHandle = null, ScriptCallbackHandle? onIntervalHandle = null, TimeSpan interval = default, string data = "")
- static Effect Sanctuary(int difficultyClass)
- static Effect SavingThrowDecrease(SavingThrow savingThrow, int amount, SavingThrowType savingThrowType = SavingThrowType.All)
- static Effect SavingThrowIncrease(SavingThrow savingThrow, int amount, SavingThrowType savingThrowType = SavingThrowType.All)
- static Effect SeeInvisible()
- static Effect Silence()
- static Effect SkillDecrease(NwSkill skill, int amount)
- static Effect SkillDecreaseAll(int amount)
- static Effect SkillIncrease(NwSkill skill, int amount)
- static Effect SkillIncreaseAll(int amount)
- static Effect Sleep()
- static Effect Slow()
- static Effect SpellFailure(int failPct, SpellSchool spellSchool = SpellSchool.General, SpellFailureType failureType = SpellFailureType.All)
- static Effect SpellImmunity(Spell spell = API.Spell.AllSpells)
- static Effect SpellLevelAbsorption(int maxSpellLevel, int totalSpellsAbsorbed = 0, SpellSchool spellSchool = SpellSchool.General)
- static Effect SpellResistanceDecrease(int amount)
- static Effect SpellResistanceIncrease(int amount)
- static Effect Stunned()
- static Effect SummonCreature(string creatureResRef, VisualEffectTableEntry summonVfx, TimeSpan delay = default, int appearType = 0, VisualEffectTableEntry? unsummonVfx = default)
- static Effect SummonCreature(NwCreature summonCreature, VisualEffectTableEntry summonVfx, VisualEffectTableEntry? unsummonVfx = default)
- static Effect Swarm(bool loop, string creatureTemplate1, string creatureTemplate2 = "", string creatureTemplate3 = "", string creatureTemplate4 = "")
- static Effect TemporaryHitpoints(int hitPoints)
- static Effect TimeStop()
- static Effect TimeStopImmunity()
- static Effect TrueSeeing()
- static Effect Turned()
- static Effect TurnResistanceDecrease(int hitDiceDecrease)
- static Effect TurnResistanceIncrease(int hitDiceIncrease)
- static Effect Ultravision()
- static Effect VisualEffect(VfxType visualEffectId, bool missEffect = false, float fScale = 1.0f, System.Numerics.Vector3 vTranslate = default, System.Numerics.Vector3 vRotate = default)
- static Effect VisualEffect(VisualEffectTableEntry visualEffect, bool missEffect = false, float fScale = 1.0f, System.Numerics.Vector3 vTranslate = default, System.Numerics.Vector3 vRotate = default)
- static Effect EnemyAttackBonus(int bonus)
- float DurationRemaining
- EffectDuration DurationType
- EffectType EffectType
- EffectSubType SubType
- string? Tag
- string LinkId
- bool IgnoreImmunity
- float TotalDuration
- static implicit operator Effect?(IntPtr intPtr)
- Effect Clone()

## Anvil.API.EffectBase  [class]
- int CasterLevel
- NwObject? Creator
- bool Expose
- EffectParams<float> FloatParams
- EffectParams<int> IntParams
- EffectParams<NwObject> ObjectParams
- bool ShowIcon
- NwSpell? Spell
- EffectParams<string> StringParams
- EffectParams<Vector3> VectorParams
- static implicit operator CGameEffect(EffectBase effect)

## Anvil.API.EffectParams<T>  [class]
- int Count
- T? this[int index]
- IEnumerator<T?> GetEnumerator()

## Anvil.API.EngineStructure  [class]
- bool IsValid
- void Dispose()
- static implicit operator IntPtr(EngineStructure engineStructure)

## Anvil.API.HitEffect  [struct]
- static HitEffect AbilityDrain(IPAbility ability)
- static HitEffect Blindness(IPOnHitDuration duration)
- static HitEffect Confusion(IPOnHitDuration duration)
- static HitEffect Daze(IPOnHitDuration duration)
- static HitEffect Deafness(IPOnHitDuration duration)
- static HitEffect Disease(DiseaseType diseaseType)
- static HitEffect DispelMagic()
- static HitEffect Doom(IPOnHitDuration duration)
- static HitEffect Fear(IPOnHitDuration duration)
- static HitEffect GreaterDispel()
- static HitEffect Hold(IPOnHitDuration duration)
- static HitEffect ItemPoison(IPPoisonDamage poisonType)
- static HitEffect Knock()
- static HitEffect LesserDispel()
- static HitEffect LevelDrain(int levelDrain = 1)
- static HitEffect MordsDisjunction()
- static HitEffect Silence(IPOnHitDuration duration)
- static HitEffect SlayAlignment(IPAlignment alignment)
- static HitEffect SlayAlignmentGroup(IPAlignmentGroup alignmentGroup)
- static HitEffect SlayRace(IPRacialType racialType)
- static HitEffect SlayRace(NwRace race)
- static HitEffect Sleep(IPOnHitDuration duration)
- static HitEffect Slow(IPOnHitDuration duration)
- static HitEffect Stun(IPOnHitDuration duration)
- static HitEffect Vorpal()
- static HitEffect Wounding(int bleedDamage)

## Anvil.API.ItemProperty  [class]
- static ItemProperty AbilityBonus(IPAbility ability, int bonus)
- static ItemProperty ACBonus(int bonus)
- static ItemProperty ACBonusVsAlign(IPAlignmentGroup alignmentGroup, int bonus)
- static ItemProperty ACBonusVsDmgType(IPDamageType damageType, int bonus)
- static ItemProperty ACBonusVsRace(IPRacialType racialType, int bonus)
- static ItemProperty ACBonusVsRace(NwRace race, int bonus)
- static ItemProperty ACBonusVsSAlign(IPAlignment alignment, int bonus)
- static ItemProperty Additional(IPAdditional additional)
- static ItemProperty ArcaneSpellFailure(IPArcaneSpellFailure spellFailure)
- static ItemProperty AttackBonus(int bonus)
- static ItemProperty AttackBonusVsAlign(IPAlignmentGroup alignmentGroup, int bonus)
- static ItemProperty AttackBonusVsRace(IPRacialType racialType, int bonus)
- static ItemProperty AttackBonusVsRace(NwRace race, int bonus)
- static ItemProperty AttackBonusVsSAlign(IPAlignment alignment, int bonus)
- static ItemProperty AttackPenalty(int penalty)
- static ItemProperty BonusFeat(IPFeat feat)
- static ItemProperty BonusLevelSpell(IPClass classType, IPSpellLevel spellLevel)
- static ItemProperty BonusSavingThrow(IPSaveBaseType saveType, int bonus)
- static ItemProperty BonusSavingThrowVsX(IPSaveVs saveType, int bonus)
- static ItemProperty BonusSpellResistance(IPSpellResistanceBonus resistBonus)
- static ItemProperty CastSpell(IPCastSpell spell, IPCastSpellNumUses uses)
- static ItemProperty ContainerReducedWeight(IPContainerWeightReduction weightReduction)
- static ItemProperty Custom(int type, int subType = -1, int costTableValue = -1, int param1Value = -1)
- static ItemProperty Custom(ItemPropertyTableEntry property, ItemPropertySubTypeTableEntry? subType = null, ItemPropertyCostTableEntry? costTableValue = null, ItemPropertyParamTableEntry? paramTableValue = null)
- static ItemProperty DamageBonus(IPDamageType damageType, IPDamageBonus damageBonus)
- static ItemProperty DamageBonusVsAlign(IPAlignmentGroup alignmentGroup, IPDamageType damageType, IPDamageBonus damageBonus)
- static ItemProperty DamageBonusVsRace(IPRacialType racialType, IPDamageType damageType, IPDamageBonus damageBonus)
- static ItemProperty DamageBonusVsRace(NwRace race, IPDamageType damageType, IPDamageBonus damageBonus)
- static ItemProperty DamageBonusVsSAlign(IPAlignment alignment, IPDamageType damageType, IPDamageBonus damageBonus)
- static ItemProperty DamageImmunity(IPDamageType damageType, IPDamageImmunityType immunityType)
- static ItemProperty DamagePenalty(int penalty)
- static ItemProperty DamageReduction(IPDamageReduction damageReduction, IPDamageSoak damageSoak)
- static ItemProperty DamageResistance(IPDamageType damageType, IPDamageResist damageResist)
- static ItemProperty DamageVulnerability(IPDamageType damageType, IPDamageVulnerabilityType damageVulnerability)
- static ItemProperty Darkvision()
- static ItemProperty DecreaseAbility(IPAbility ability, int penalty)
- static ItemProperty DecreaseAC(IPACModifierType modifierType, int penalty)
- static ItemProperty DecreaseSkill(NwSkill skill, int penalty)
- static ItemProperty EnhancementBonus(int bonus)
- static ItemProperty EnhancementBonusVsAlign(IPAlignmentGroup alignmentGroup, int bonus)
- static ItemProperty EnhancementBonusVsRace(IPRacialType racialType, int bonus)
- static ItemProperty EnhancementBonusVsRace(NwRace race, int bonus)
- static ItemProperty EnhancementBonusVsSAlign(IPAlignment alignment, int bonus)
- static ItemProperty EnhancementPenalty(int penalty)
- static ItemProperty ExtraMeleeDamageType(IPDamageType damageType)
- static ItemProperty ExtraRangeDamageType(IPDamageType damageType)
- static ItemProperty FreeAction()
- static ItemProperty Haste()
- static ItemProperty HealersKit(int level)
- static ItemProperty HolyAvenger()
- static ItemProperty ImmunityMisc(IPMiscImmunity immunityType)
- static ItemProperty ImmunityToSpellLevel(IPSpellLevel spellLevel)
- static ItemProperty ImprovedEvasion()
- static ItemProperty Keen()
- static ItemProperty Light(IPLightBrightness brightness, IPLightColor color)
- static ItemProperty LimitUseByAlign(IPAlignmentGroup alignmentGroup)
- static ItemProperty LimitUseByClass(IPClass classType)
- static ItemProperty LimitUseByClass(NwClass classType)
- static ItemProperty LimitUseByRace(IPRacialType racialType)
- static ItemProperty LimitUseByRace(NwRace race)
- static ItemProperty LimitUseBySAlign(IPAlignment alignment)
- static ItemProperty MassiveCritical(IPDamageBonus damageBonus)
- static ItemProperty Material(int materialType)
- static ItemProperty MaxRangeStrengthMod(int modifier)
- static ItemProperty MonsterDamage(IPMonsterDamage monsterDamage)
- static ItemProperty NoDamage()
- static ItemProperty OnHitCastSpell(IPCastSpell spell, int casterLevel)
- static ItemProperty OnHitCastSpell(IPCastSpell spell, IPSpellLevel spellLevel)
- static ItemProperty OnHitEffect(IPOnHitSaveDC saveDC, HitEffect effect)
- static ItemProperty OnMonsterHitProperties(MonsterHitEffect effect)
- static ItemProperty Quality(IPQuality quality)
- static ItemProperty ReducedSavingThrow(IPSaveBaseType saveType, int penalty)
- static ItemProperty ReducedSavingThrowVsX(IPSaveVs saveType, int penalty)
- static ItemProperty Regeneration(int regenAmount)
- static ItemProperty SkillBonus(NwSkill skill, int bonus)
- static ItemProperty SpecialWalk()
- static ItemProperty SpellImmunitySchool(IPSpellSchool spellSchool)
- static ItemProperty SpellImmunitySpecific(IPSpellImmunity spell)
- static ItemProperty ThievesTools(int modifier)
- static ItemProperty Trap(IPTrapStrength trapStrength, IPTrapType trapType)
- static ItemProperty TrueSeeing()
- static ItemProperty TurnResistance(int modifier)
- static ItemProperty UnlimitedAmmo(IPUnlimitedAmmoType ammoType = IPUnlimitedAmmoType.Basic)
- static ItemProperty VampiricRegeneration(int regenAmount)
- static ItemProperty VisualEffect(ItemVisual itemVisual)
- static ItemProperty WeightIncrease(IPWeightIncrease weightIncrease)
- static ItemProperty WeightReduction(IPReducedWeight weightReduction)
- TwoDimArray<ItemPropertyCostTableEntry>? CostTable
- ItemPropertyCostTableEntry? CostTableValue
- EffectDuration DurationType
- TwoDimArray<ItemPropertyParamTableEntry>? Param1Table
- ItemPropertyParamTableEntry? Param1TableValue
- ItemPropertyTableEntry Property
- TimeSpan RemainingDuration
- TwoDimArray<ItemPropertySubTypeTableEntry>? SubTypeTable
- ItemPropertySubTypeTableEntry? SubType
- string? Tag
- TimeSpan TotalDuration
- bool Usable
- int UsesPerDay
- bool Valid
- static implicit operator ItemProperty?(IntPtr intPtr)

## Anvil.API.Json  [class]
- static implicit operator Json(IntPtr intPtr)
- static Json Parse(string jsonString)
- string Dump()
- NwObject? ToNwObject(Location location, NwGameObject? owner = null, bool loadObjectState = true)
- T? ToNwObject<T>(Location location, NwGameObject? owner = null, bool loadObjectState = true) where T : NwObject

## Anvil.API.Location  [class]
- NwArea Area
- float FlippedRotation
- float GroundHeight
- bool IsWalkable
- Vector3 Position
- float Rotation
- int SurfaceMaterial
- TileMainLightColor TileMainLightColorOne
- TileMainLightColor TileMainLightColorTwo
- TileSourceLightColor TileSourceLightColorOne
- TileSourceLightColor TileSourceLightColorTwo
- int TileId
- TileRotation TileRotation
- int TileHeight
- TileInfo? TileInfo
- static Location? Create(NwArea area, Vector3 position, float orientation)
- static implicit operator Location?(IntPtr intPtr)
- void ApplyEffect(EffectDuration durationType, Effect effect, TimeSpan duration = default)
- void CreateTrap(TrapBaseType trap, float size = 2.0f, string tag = "", string disarm = "", string triggered = "")
- float Distance(Location target)
- float DistanceSquared(Location target)
- IEnumerable<NwCreature> GetNearestCreatures()
- IEnumerable<NwCreature> GetNearestCreatures(CreatureTypeFilter filter1)
- IEnumerable<NwCreature> GetNearestCreatures(CreatureTypeFilter filter1, CreatureTypeFilter filter2)
- IEnumerable<NwCreature> GetNearestCreatures(CreatureTypeFilter filter1, CreatureTypeFilter filter2, CreatureTypeFilter filter3)
- IEnumerable<T> GetNearestObjectsByType<T>() where T : NwGameObject
- IEnumerable<NwGameObject> GetObjectsInShape(Shape shape, float size, bool losCheck, ObjectTypes objTypes = ObjectTypes.Creature, Vector3 origin = default)
- IEnumerable<T> GetObjectsInShapeByType<T>(Shape shape, float size, bool losCheck, Vector3 origin = default) where T : NwGameObject
- void SetTile(int tileId, TileRotation rotation, int height = 0, SettleFlags flags = SettleFlags.RecomputeLighting)
- void SetTileAnimationLoops(bool animLoop1, bool animLoop2, bool animLoop3)

## Anvil.API.MonsterHitEffect  [struct]
- static MonsterHitEffect AbilityDrain(IPAbility ability)
- static MonsterHitEffect Confusion(IPOnHitDuration duration)
- static MonsterHitEffect Disease(DiseaseType diseaseType)
- static MonsterHitEffect Doom(IPOnHitDuration duration)
- static MonsterHitEffect Fear(IPOnHitDuration duration)
- static MonsterHitEffect LevelDrain(int levelDrain = 1)
- static MonsterHitEffect Poison(PoisonType poisonType)
- static MonsterHitEffect Slow(IPOnHitDuration duration)
- static MonsterHitEffect Stun(IPOnHitDuration duration)
- static MonsterHitEffect Wounding(int bleedDamage)

## Anvil.API.SQLQuery  [class]
- string Error
- SQLResult? Result
- IEnumerable<SQLResult> Results
- string[] Columns
- static implicit operator SQLQuery(IntPtr intPtr)
- void BindParam(string param, int value)
- void BindParam(string param, float value)
- void BindParam(string param, string value)
- void BindParam(string param, Vector3 value)
- void BindParam(string param, NwObject value)
- void Execute()
- void Reset(bool clearBinds = false)

## Anvil.API.SQLResult  [class]
- float GetFloat(int columnIndex)
- float GetFloat(string columnName)
- int GetInt(int columnIndex)
- float GetInt(string columnName)
- T? GetObject<T>(int columnIndex, Location spawnLocation, NwGameObject? targetInventory = null) where T : NwObject
- T? GetObject<T>(string columnName, Location spawnLocation, NwGameObject? targetInventory = null) where T : NwObject
- string GetString(int columnIndex)
- string GetString(string columnName)
- Vector3 GetVector3(int columnIndex)
- Vector3 GetVector3(string columnName)

## Anvil.API.Talent  [class]
- static implicit operator Talent(NwSkill skill)
- static implicit operator Talent(NwSpell spell)
- static implicit operator Talent(NwFeat feat)
- static implicit operator Talent(Skill skill)
- static implicit operator Talent(Spell spell)
- static implicit operator Talent(Feat feat)
- NwFeat Feat
- NwSkill Skill
- NwSpell Spell
- TalentType Type
- bool Valid
- static implicit operator Talent(IntPtr intPtr)

## Anvil.API.TalentExtensions  [class]
- static Talent ToTalent(this NwSkill skill)
- static Talent ToTalent(this NwSpell spell)
- static Talent ToTalent(this NwFeat feat)

## Anvil.API.TileData  [class]
- int Index
- int TileId
- TileRotation Orientation
- int Height
- int AnimationLoop1
- int AnimationLoop2
- int AnimationLoop3

## Anvil.API.Events.AreaEvents  [class]

## Anvil.API.Events.OnEnter  [class]
- NwArea Area
- NwGameObject EnteringObject
- NwAreaOfEffect Effect
- NwGameObject Entering
- int SpellSaveDC
- NwEncounter Encounter
- NwTrigger Trigger

## Anvil.API.NwArea  [class]
- event Action<AreaEvents.OnEnter> OnEnter
- event Action<AreaEvents.OnExit> OnExit
- event Action<AreaEvents.OnHeartbeat> OnHeartbeat
- event Action<AreaEvents.OnUserDefined> OnUserDefined
- override bool IsValid
- int AmbientDayTrack
- int AmbientDayVolume
- int AmbientNightTrack
- int AmbientNightVolume
- AreaFlags AreaFlags
- DayNightMode DayNightMode
- float FogClipDistance
- bool IsAboveGround
- bool IsBattleMusicPlaying
- bool IsExterior
- bool IsInterior
- bool IsMusicPlaying
- bool IsNatural
- bool IsUnderGround
- bool IsUrban
- NwGameObject? LastEntered
- NwGameObject? LastLeft
- int LightningChance
- int ListenModifier
- LoadScreenTableEntry LoadScreen
- Color MoonAmbientColor
- Color MoonDiffuseColor
- int MoonFogAmount
- Color MoonFogColor
- bool MoonShadows
- int MusicBackgroundDayTrack
- int MusicBackgroundNightTrack
- int MusicBattleTrack
- IEnumerable<NwGameObject> Objects
- int PlayerCount
- PVPSetting PVPSetting
- int RainChance
- bool RestingAllowed
- byte ShadowOpacity
- Vector2Int Size
- Skybox SkyBox
- int SnowChance
- int SpotModifier
- Color SunAmbientColor
- Color SunDiffuseColor
- int SunFogAmount
- Color SunFogColor
- bool SunShadows
- string Tileset
- IReadOnlyList<TileInfo> TileInfo
- WeatherType Weather
- byte WindPower
- static NwArea? Create(string resRef, string newTag = "", string newName = "")
- static NwArea? Deserialize(byte[] serializedARE, byte[] serializedGIT, string newTag = "", string newName = "")
- static NwArea? Deserialize(string resRef, byte[] serializedARE, byte[] serializedGIT, string newTag = "", string newName = "")
- static implicit operator CNWSArea?(NwArea? area)
- void ApplyEnvironmentPreset(EnvironmentPreset preset)
- NwArea? Clone()
- EnvironmentPreset CreateEnvironmentPreset()
- AreaDestroyResult Destroy()
- IEnumerable<T> FindObjectsOfTypeInArea<T>() where T : NwObject
- string GetLocalizedName(PlayerLanguage language, Gender gender = Gender.Male)
- TileInfo GetTileInfo(int tileX, int tileY)
- TileInfo GetTileInfoByIndex(int index)
- override Guid? PeekUUID()
- void PlayAmbient()
- void PlayBackgroundMusic()
- void PlayBattleMusic()
- void RecomputeStaticLighting()
- void ReloadAreaGrass()
- void ReloadAreaBorder()
- void SetLocalizedName(string name, PlayerLanguage language, Gender gender = Gender.Male)
- void SetTiles(List<TileData> data, SettleFlags flags = SettleFlags.RecomputeLighting, string tileSet = "")
- unsafe byte[]? SerializeARE(string? areaName = null, string? resRef = null)
- byte[]? SerializeGIT(ObjectTypes objectFilter = ObjectTypes.All, ICollection<NwGameObject>? exclusionList = null, bool exportVarTable = true, bool exportUUID = true, string? resRef = null)
- void SetAreaTileBorderDisabled(bool disabled)
- void SetAreaGrassOverride(SurfaceMaterialTableEntry material, string texture, float density, float height, Color ambientColor, Color diffuseColor)
- void RemoveAreaGrassOverride(SurfaceMaterialTableEntry material)
- void SetAreaDefaultGrassDisabled(bool disabled)
- int GetAreaLightColor(AreaLightColor colorType)
- void SetAreaLightColor(AreaLightColor colorType, int color, TimeSpan fadeTime = default)
- Vector3 GetAreaLightDirection(AreaLightDirection lightType)
- void SetAreaLightDirection(AreaLightDirection lightType, Vector3 direction, TimeSpan fadeTime = default)
- void SetAreaWind(Vector3 direction, float magnitude, float yaw, float pitch)
- void SetFogAmount(FogType fogType, int fogAmount)
- void SetFogColor(FogType fogType, FogColor fogColor, TimeSpan fadeTime = default)
- void StopAmbient()
- void StopBackgroundMusic()
- void StopBattleMusic()

## Anvil.API.Events.OnExit  [class]
- NwArea Area
- NwGameObject ExitingObject
- NwAreaOfEffect Effect
- NwGameObject Exiting
- int SpellSaveDC
- NwEncounter Encounter
- NwTrigger Trigger

## Anvil.API.Events.OnHeartbeat  [class]
- NwArea Area
- NwAreaOfEffect Effect
- int SpellSaveDC
- NwCreature Creature
- NwDoor Door
- NwEncounter Encounter
- NwPlaceable Placeable
- NwTrigger Trigger

## Anvil.API.Events.OnUserDefined  [class]
- NwArea Area
- int EventNumber
- static void Signal(NwArea area, int eventId)
- NwAreaOfEffect Effect
- static void Signal(NwAreaOfEffect areaOfEffect, int eventId)
- NwCreature Creature
- static void Signal(NwCreature creature, int eventId)
- NwDoor Door
- static void Signal(NwDoor door, int eventId)
- NwEncounter Encounter
- static void Signal(NwEncounter encounter, int eventId)
- static void Signal(int eventId)
- NwPlaceable Placeable
- static void Signal(NwPlaceable placeable, int eventId)
- NwTrigger Trigger
- static void Signal(NwTrigger trigger, int eventId)

## Anvil.API.Events.AreaOfEffectEvents  [class]

## Anvil.API.NwAreaOfEffect  [class]
- event Action<AreaOfEffectEvents.OnEnter> OnEnter
- event Action<AreaOfEffectEvents.OnExit> OnExit
- event Action<AreaOfEffectEvents.OnHeartbeat> OnHeartbeat
- event Action<AreaOfEffectEvents.OnUserDefined> OnUserDefined
- override bool IsValid
- NwGameObject? Creator
- float Radius
- TimeSpan RemainingDuration
- NwSpell? Spell
- static implicit operator CNWSAreaOfEffectObject?(NwAreaOfEffect? areaOfEffect)
- override NwAreaOfEffect Clone(Location location, string? newTag = null, bool copyLocalState = true)
- IEnumerable<T> GetObjectsInEffectArea<T>() where T : NwGameObject
- IEnumerable<NwGameObject> GetObjectsInEffectArea(ObjectTypes objectTypes)
- override byte[] Serialize()
- void SetRadius(float radius)

## Anvil.API.Events.CreatureEvents  [class]

## Anvil.API.Events.OnBlocked  [class]
- NwDoor BlockingDoor
- NwCreature Creature

## Anvil.API.NwCreature  [class]
- event Action<CreatureEvents.OnBlocked> OnBlocked
- event Action<CreatureEvents.OnCombatRoundEnd> OnCombatRoundEnd
- event Action<CreatureEvents.OnConversation> OnConversation
- event Action<CreatureEvents.OnDamaged> OnDamaged
- event Action<CreatureEvents.OnDeath> OnDeath
- event Action<CreatureEvents.OnDisturbed> OnDisturbed
- event Action<CreatureEvents.OnHeartbeat> OnHeartbeat
- event Action<CreatureEvents.OnPerception> OnPerception
- event Action<CreatureEvents.OnPhysicalAttacked> OnPhysicalAttacked
- event Action<CreatureEvents.OnRested> OnRested
- event Action<CreatureEvents.OnSpawn> OnSpawn
- event Action<CreatureEvents.OnSpellCastAt> OnSpellCastAt
- event Action<CreatureEvents.OnUserDefined> OnUserDefined
- event Action<ModuleEvents.OnActivateItem> OnActivateItem
- override bool IsValid
- int AC
- int Age
- AiLevel AiLevel
- bool AlwaysWalk
- string AnimalCompanionName
- AnimalCompanionCreatureType AnimalCompanionType
- AppearanceTableEntry Appearance
- int ArcaneSpellFailure
- sbyte ArmorCheckPenalty
- IEnumerable<NwCreature> Associates
- AssociateType AssociateType
- NwGameObject? AttackTarget
- NwGameObject? AttemptedAttackTarget
- NwGameObject? AttemptedSpellTarget
- sbyte BaseAC
- byte BaseArmorArcaneSpellFailure
- int BaseAttackBonus
- int BaseAttackCount
- byte BaseShieldArcaneSpellFailure
- NwPlaceable? BodyBag
- BodyBagTableEntry BodyBagTemplate
- float ChallengeRating
- byte InitiativeRoll
- IReadOnlyList<CreatureClassInfo> Classes
- CombatMode CombatMode
- bool Commandable
- NwPlayer? ControllingPlayer
- TimeSpan CorpseDecayTime
- Action CurrentAction
- DamageLevelEntry DamageLevel
- bool DefensiveCastingModeActive
- string Deity
- bool DetectModeActive
- string? DialogResRef
- bool Disarmable
- NwEncounter? Encounter
- bool ExploresMinimap
- NwFaction Faction
- string FamiliarName
- FamiliarCreatureType FamiliarType
- int FeatCount
- IReadOnlyList<NwFeat> Feats
- bool FlatFooted
- FootstepType FootstepType
- Gender Gender
- uint Gold
- Alignment GoodEvilAlignment
- int GoodEvilValue
- IEnumerable<NwCreature> Henchmen
- bool Immortal
- Inventory Inventory
- bool IsBartering
- bool IsDead
- bool IsDMPossessed
- bool IsDMAvatar
- bool IsEncounterCreature
- bool IsInCombat
- bool IsLoginPlayerCharacter
- bool IsPlayableRace
- bool IsPlayerControlled
- bool IsPossessedFamiliar
- bool IsRangedWeaponEquipped
- bool IsResting
- LastAttackMode LastAttackMode
- AssociateCommand LastCommandFromMaster
- SpecialAttack LastSpecialAttackType
- NwTrappable? LastTrapDetected
- Alignment LawChaosAlignment
- int LawChaosValue
- int Level
- IReadOnlyList<CreatureLevelInfo> LevelInfo
- NwPlayer? LoginPlayer
- bool Lootable
- NwCreature? Master
- MovementRate MovementRate
- float MovementRateFactor
- MovementType MovementType
- string OriginalFirstName
- string OriginalLastName
- string OriginalName
- Phenotype Phenotype
- override Vector3 Position
- NwRace Race
- ushort RemainingSkillPoints
- sbyte ShieldCheckPenalty
- NwPlaceable? SittingObject
- CreatureSize Size
- ushort SoundSet
- IEnumerable<CreatureSpellAbility> SpellAbilities
- IReadOnlyList<SpecialAbility> SpecialAbilities
- sbyte SpellResistance
- PackageType StartingPackage
- bool StealthModeActive
- string SubRace
- CreatureTailType TailType
- decimal TotalWeight
- int TurnResistanceHitDice
- float? WalkRateCap
- CreatureWingType WingType
- int Xp
- static NwCreature? Create(string template, Location location, bool useAppearAnim = false, string newTag = "")
- static NwCreature? Deserialize(byte[] serialized)
- static implicit operator CNWSCreature?(NwCreature? creature)
- unsafe void AcquireItem(NwItem item, bool displayFeedback = true)
- async Task ActionAttackTarget(NwGameObject target, bool passive = false)
- async Task ActionCastFakeSpellAt(NwSpell spell, Location location, ProjectilePathType pathType = ProjectilePathType.Default)
- async Task ActionCastFakeSpellAt(NwSpell spell, NwGameObject target, ProjectilePathType pathType = ProjectilePathType.Default)
- async Task ActionCloseDoor(NwDoor door, bool run = false)
- async Task ActionCounterspell(NwGameObject counterSpellTarget)
- void ForceLevelUp(NwClass classType, byte hitDie, Ability? abilityGain = default, bool epic = false, ushort skillPointsRemaining = 0, NwDomain? domain1 = default, NwDomain? domain2 = default, SpellSchool school = SpellSchool.Unknown, bool addStatsToList = true)
- async Task ActionEquipItem(NwItem item, InventorySlot slot)
- async Task ActionEquipMostDamagingMelee(NwGameObject? verses = null, bool offhand = false)
- async Task ActionEquipMostDamagingRanged(NwGameObject? verses = null)
- async Task ActionEquipMostEffectiveArmor()
- async Task ActionForceFollowObject(NwGameObject target, float distance)
- async Task ActionForceMoveTo(Location target, bool run = false, TimeSpan? timeOut = null)
- async Task ActionForceMoveTo(NwObject target, bool run = false, float range = 1.0f, TimeSpan? timeOut = null)
- async Task ActionInteractObject(NwPlaceable placeable)
- Task ActionLockObject(NwDoor door)
- Task ActionLockObject(NwPlaceable placeable)
- async Task ActionMoveAwayFrom(NwObject target, bool run, float range = 40.0f)
- async Task ActionMoveAwayFrom(Location location, bool run, float range = 40.0f)
- async Task ActionMoveTo(Location target, bool run = false)
- async Task ActionMoveTo(NwObject target, bool run = false, float range = 1.0f)
- async Task ActionOpenDoor(NwDoor door, bool run = false)
- async Task ActionPickUpItem(NwItem item)
- async Task ActionPutDownItem(NwItem item)
- async Task ActionRandomWalk()
- async Task ActionRest(bool enemyLineOfSightCheck = false)
- async Task ActionSit(NwPlaceable sitPlaceable, bool alignToPlaceable = true)
- async Task ActionUnequipItem(NwItem item)
- Task ActionUnlockObject(NwDoor door)
- Task ActionUnlockObject(NwPlaceable placeable)
- async Task ActionUseFeat(NwFeat feat, NwGameObject target, Subfeat subFeat = Subfeat.None)
- async Task ActionUseFeat(NwFeat feat, Location target, Subfeat subFeat = Subfeat.None)
- async Task ActionUseItem(NwItem item, ItemProperty itemProperty, Location location, bool decrementCharges = true, int subPropertyIndex = 0)
- async Task ActionUseItem(NwItem item, ItemProperty itemProperty, NwGameObject gameObject, bool decrementCharges = true, int subPropertyIndex = 0)
- async Task ActionUseSkill(NwSkill skill, NwGameObject target, SubSkill subSkill = SubSkill.None, NwItem? itemUsed = null)
- async Task ActionUseTalent(Talent talent, Location target)
- async Task ActionUseTalent(Talent talent, NwGameObject target)
- void AddFeat(NwFeat feat)
- void AddFeat(NwFeat feat, int level)
- void AddSpecialAbility(SpecialAbility ability)
- void AdjustPartyAlignment(Alignment alignment, int shift)
- void BroadcastSkillRoll(int diceRoll, NwSkill skill, int modifier, int difficultyClass, bool take20, SkillResult result)
- ResistSpellResult CheckResistSpell(NwGameObject target)
- void ClearDamageLevelOverride()
- void ClearInitiativeModifier()
- override NwCreature Clone(Location location, string? newTag = null, bool copyLocalState = true)
- void DecrementRemainingFeatUses(NwFeat feat, int amount = 1)
- bool DeserializeQuickbar(byte[] serialized)
- async Task DoDoorAction(NwDoor door, DoorAction doorAction)
- async Task DoPlaceableAction(NwPlaceable placeable, PlaceableAction placeableAction)
- bool DoSkillCheck(NwSkill skill, int difficultyClass)
- NwItem? FindItemWithTag(string itemTag)
- void ForceRest()
- int GetAbilityModifier(Ability ability)
- int CalculateAbilityModifierFromScore(byte abilityScore)
- int GetAbilityScore(Ability ability, bool baseOnly = false)
- bool GetActionMode(ActionMode actionMode)
- NwCreature? GetAssociate(AssociateType associateType)
- int GetAttackBonus(bool isMelee = false, bool isTouchAttack = false, bool isOffHand = false, bool includeBaseAttackBonus = true)
- int GetBaseSavingThrow(SavingThrow savingThrow)
- IEnumerable<NwDomain> GetClassDomains(NwClass? nwClass = null)
- CreatureClassInfo? GetClassInfo(NwClass? nwClass)
- int GetCreatureBodyPart(CreaturePart creaturePart)
- DamageLevelEntry? GetDamageLevelOverride()
- int GetFeatGainLevel(NwFeat feat)
- int GetFeatRemainingUses(NwFeat feat)
- int GetFeatTotalUses(NwFeat feat)
- int? GetInitiativeModifier()
- NwItem? GetItemInSlot(InventorySlot slot)
- CreatureLevelInfo GetLevelStats(int level)
- byte GetPrePolymorphAbilityScore(Ability ability)
- PlayerQuickBarButton GetQuickBarButton(byte index)
- PlayerQuickBarButton[] GetQuickBarButtons()
- byte GetRawAbilityScore(Ability ability)
- int GetSavingThrow(SavingThrow savingThrow)
- int GetSkillRank(NwSkill skill, bool ranksOnly = false)
- EquipmentSlots GetSlotFromItem(NwItem item)
- SpellSchool GetSpecialization(NwClass? nwClass = null)
- int GetSpellUsesLeft(NwClass nwClass, NwSpell spell, MetaMagic metaMagic = MetaMagic.None, int domain = 0)
- bool GetTileExplored(NwArea area, int x, int y)
- void GiveGold(int amount, bool showFeedback = true)
- async Task GiveItem(NwItem item)
- async Task GiveItem(NwItem item, int amount)
- bool HasFeatEffect(NwFeat feat)
- bool HasFeatPrepared(NwFeat feat)
- bool HasSkill(NwSkill skill)
- bool HasSpellEffect(NwSpell spell)
- bool HasSpellUse(NwSpell spell)
- bool HasTalent(Talent talent)
- void IncrementRemainingFeatUses(NwFeat feat, int amount = 1)
- bool IsCreatureHeard(NwCreature creature)
- bool IsCreatureSeen(NwCreature creature)
- bool IsEnemy(NwCreature target)
- bool IsFlanking(NwCreature target)
- bool IsFriend(NwCreature target)
- bool IsImmuneTo(ImmunityType immunityType, NwGameObject? verses = null)
- bool IsNeutral(NwCreature target)
- bool IsReactionTypeFriendly(NwCreature creature)
- bool IsReactionTypeHostile(NwCreature creature)
- bool IsReactionTypeNeutral(NwCreature creature)
- async Task<bool> IsWeaponEffective(NwGameObject target, bool offHand = false)
- async Task JumpToObject(NwGameObject gameObject, bool walkStraightLineToPoint = true)
- bool KnowsFeat(NwFeat feat)
- int LevelUpHenchman(NwClass nwClass, PackageType package, bool spellsReady = false)
- void LevelUp(NwClass nwClass, int count)
- bool MeetsFeatRequirements(NwFeat feat)
- void PlayVoiceChat(VoiceChatType voiceChatType)
- void RemoveFeat(NwFeat feat, bool removeFeatFromLevelList = false)
- void RemoveSpecialAbilityAt(int index)
- int Reputation(NwCreature creature)
- void RestoreAllSpells()
- void RestoreBaseAttackBonus()
- void RestoreSpells(byte level)
- bool RunEquip(NwItem item, InventorySlot inventorySlot)
- bool RunEquip(NwItem item, EquipmentSlots equipmentSlot)
- bool RunUnequip(NwItem item)
- override byte[]? Serialize()
- byte[]? SerializeQuickbar()
- void SetActionMode(ActionMode actionMode, bool status)
- void SetBaseSavingThrow(SavingThrow savingThrow, sbyte newValue)
- void SetCreatureBodyPart(CreaturePart creaturePart, int modelNumber)
- void SetDamageLevelOverride(DamageLevelEntry damageLevel)
- void SetEffectIconFlashing(EffectIconTableEntry effectIcon, bool flashing)
- void SetInitiativeModifier(int modifier)
- void SetFeatRemainingUses(NwFeat feat, byte remainingUses)
- void SetAssociateListenPatterns()
- void SetQuickBarButton(byte index, PlayerQuickBarButton data)
- void SetQuickBarButtons(PlayerQuickBarButton[] buttons)
- void SetSkillRank(NwSkill skill, sbyte rank)
- void SetSpecialAbilityAt(int index, SpecialAbility ability)
- void SetsRawAbilityScore(Ability ability, byte value)
- bool SetTileExplored(NwArea area, int x, int y, bool newState)
- async Task SpeakOneLinerConversation(string dialogResRef = "", NwGameObject? tokenTarget = null)
- bool SpellResistanceCheck(NwGameObject target, NwSpell? spell = null, int? casterLevel = null, int? spellResistance = null, bool feedback = true)
- bool SpellImmunityCheck(NwGameObject target, NwSpell? spell = null, bool feedback = true)
- bool SpellAbsorptionLimitedCheck(NwGameObject target, NwSpell? spell = null, SpellSchool? spellSchool = null, int? spellLevel = null, bool removeLevels = true, bool feedback = true)
- bool SpellAbsorptionUnlimitedCheck(NwGameObject target, NwSpell? spell = null, SpellSchool? spellSchool = null, int? spellLevel = null, bool feedback = true)
- void SummonAnimalCompanion()
- void SummonAnimalCompanion(string resRef)
- void UnsummonAnimalCompanion()
- void SummonFamiliar()
- void SummonFamiliar(string resRef)
- void UnsummonFamiliar()
- void Unsummon()
- void TakeGold(int amount, bool showFeedback = true)
- Talent TalentBest(TalentCategory category, int maxCr)
- Talent TalentRandom(TalentCategory category)
- TouchAttackResult TouchAttackMelee(NwGameObject target, bool displayFeedback = true)
- TouchAttackResult TouchAttackRanged(NwGameObject target, bool displayFeedback)
- void UnpossessFamiliar()
- int GetArmorClassVersus(NwCreature creature)

## Anvil.API.Events.OnCombatRoundEnd  [class]
- NwCreature Creature

## Anvil.API.Events.OnConversation  [class]
- NwCreature Creature
- NwGameObject? LastSpeaker
- NwPlayer? PlayerSpeaker
- int ListenPattern
- AssociateCommand AssociateCommand
- static void Signal(NwCreature creature)
- void PauseConversation()
- void ResumeConversation()
- NwDoor Door
- static void Signal(NwDoor door)
- NwPlaceable Placeable
- static void Signal(NwPlaceable placeable)

## Anvil.API.Events.OnDamaged  [class]
- NwCreature Creature
- int DamageAmount
- NwGameObject Damager
- int GetDamageDealtByType(DamageType damageType)
- OnDamaged()
- NwCreature DamagedBy
- NwDoor Door
- int TotalDamageDealt
- NwPlaceable DamagedObject
- NwGameObject? Damager

## Anvil.API.Events.OnDeath  [class]
- NwCreature KilledCreature
- NwObject? Killer
- NwDoor Door
- NwCreature Killer
- NwPlaceable KilledObject
- NwCreature? Killer

## Anvil.API.Events.OnDisturbed  [class]
- NwCreature CreatureDisturbed
- NwItem DisturbedItem
- NwCreature Disturber
- InventoryDisturbType DisturbType
- OnDisturbed()
- NwItem? DisturbedItem
- NwGameObject? Disturber
- NwPlaceable Placeable

## Anvil.API.Events.OnPerception  [class]
- NwCreature Creature
- NwCreature PerceivedCreature
- PerceptionEventType PerceptionEventType

## Anvil.API.Events.OnPhysicalAttacked  [class]
- NwCreature Attacker
- NwCreature Creature
- SpecialAttack AttackType
- NwDoor Door
- ActionMode AttackMode(NwCreature attacker)
- NwItem WeaponUsed(NwCreature attacker)
- OnPhysicalAttacked()
- NwCreature? Attacker
- NwPlaceable Placeable
- NwItem? WeaponUsed(NwCreature attacker)

## Anvil.API.Events.OnRested  [class]
- NwCreature Creature

## Anvil.API.Events.OnSpawn  [class]
- NwCreature Creature

## Anvil.API.Events.OnSpellCastAt  [class]
- NwGameObject Caster
- NwCreature Creature
- bool Harmful
- NwSpell Spell
- static void Signal(NwObject caster, NwCreature target, NwSpell spell, bool harmful = true)
- NwDoor Door
- static void Signal(NwObject caster, NwDoor target, NwSpell spell, bool harmful = true)
- NwGameObject? Caster
- NwPlaceable Placeable
- static void Signal(NwObject caster, NwPlaceable target, NwSpell spell, bool harmful = true)

## Anvil.API.Events.DoorEvents  [class]

## Anvil.API.Events.OnAreaTransitionClick  [class]
- NwPlayer ClickedBy
- NwDoor Door
- NwStationary TransitionTarget
- void SetAreaTransitionBMP(AreaTransition transition)
- void SetAreaTransitionBMP(string transition)

## Anvil.API.NwDoor  [class]
- event Action<DoorEvents.OnAreaTransitionClick> OnAreaTransitionClick
- event Action<DoorEvents.OnClose> OnClose
- event Action<DoorEvents.OnConversation> OnConversation
- event Action<DoorEvents.OnDamaged> OnDamaged
- event Action<DoorEvents.OnDeath> OnDeath
- event Action<DoorEvents.OnDisarm> OnDisarm
- event Action<DoorEvents.OnFailToOpen> OnFailToOpen
- event Action<DoorEvents.OnHeartbeat> OnHeartbeat
- event Action<DoorEvents.OnLock> OnLock
- event Action<DoorEvents.OnOpen> OnOpen
- event Action<DoorEvents.OnPhysicalAttacked> OnPhysicalAttacked
- event Action<DoorEvents.OnSpellCastAt> OnSpellCastAt
- event Action<DoorEvents.OnTrapTriggered> OnTrapTriggered
- event Action<DoorEvents.OnUnlock> OnUnlock
- event Action<DoorEvents.OnUserDefined> OnUserDefined
- override bool IsValid
- string? DialogResRef
- override bool KeyAutoRemoved
- DoorOpenState DoorOpenState
- static NwDoor? Create(string template, Location location, string? newTag = null)
- static NwDoor? Deserialize(byte[] serialized)
- static implicit operator CNWSDoor?(NwDoor? door)
- override NwDoor Clone(Location location, string? newTag = null, bool copyLocalState = true)
- async Task Close()
- int GetBaseSavingThrow(SavingThrow savingThrow)
- bool IsDoorActionPossible(DoorAction action)
- async Task Open()
- override byte[]? Serialize()
- void SetBaseSavingThrow(SavingThrow savingThrow, sbyte newValue)

## Anvil.API.Events.OnClose  [class]
- NwGameObject ClosedBy
- NwDoor Door
- OnClose()
- NwCreature? ClosedBy
- NwPlaceable Placeable
- NwCreature Creature
- NwStore Store

## Anvil.API.Events.OnDisarm  [class]
- NwDoor Door
- NwPlaceable Placeable

## Anvil.API.Events.OnFailToOpen  [class]
- NwDoor Door
- NwCreature WhoFailed

## Anvil.API.Events.OnLock  [class]
- NwDoor Door
- NwCreature LockedBy
- OnLock()
- NwCreature? LockedBy
- NwPlaceable LockedPlaceable

## Anvil.API.Events.OnOpen  [class]
- NwDoor Door
- NwGameObject OpenedBy
- OnOpen()
- NwCreature? OpenedBy
- NwPlaceable Placeable
- NwPlayer Player
- NwStore Store

## Anvil.API.Events.OnTrapTriggered  [class]
- NwDoor Door
- NwGameObject TriggeredBy
- NwPlaceable Placeable
- NwTrigger Trigger

## Anvil.API.Events.OnUnlock  [class]
- NwDoor Door
- NwCreature UnlockedBy
- OnUnlock()
- NwPlaceable Placeable
- NwCreature? UnlockedBy

## Anvil.API.Events.EncounterEvents  [class]

## Anvil.API.NwEncounter  [class]
- event Action<EncounterEvents.OnEnter> OnEnter
- event Action<EncounterEvents.OnExhausted> OnExhausted
- event Action<EncounterEvents.OnExit> OnExit
- event Action<EncounterEvents.OnHeartbeat> OnHeartbeat
- event Action<EncounterEvents.OnUserDefined> OnUserDefined
- override bool IsValid
- bool Active
- bool CanReset
- IReadOnlyList<EncounterListEntry> CreatureList
- EncounterDifficulty Difficulty
- NwFaction Faction
- int MaxSpawnedCreatures
- int MaxSpawns
- int MinSpawnedCreatures
- int NumSpawnedCreatures
- bool PlayerTriggeredOnly
- TimeSpan ResetTime
- IReadOnlyList<EncounterSpawnPoint> SpawnPointList
- int Spawns
- static NwEncounter? Create(string template, Location location, string? newTag = null)
- static NwEncounter? Deserialize(byte[] serialized)
- static implicit operator CNWSEncounter?(NwEncounter? encounter)
- override NwEncounter Clone(Location location, string? newTag = null, bool copyLocalState = true)
- override void Destroy()
- IEnumerable<T> GetObjectsInEncounterArea<T>() where T : NwGameObject
- IEnumerable<NwGameObject> GetObjectsInEncounterArea(ObjectTypes objectTypes = ObjectTypes.All)
- override byte[]? Serialize()

## Anvil.API.Events.OnExhausted  [class]
- NwEncounter Encounter

## Anvil.API.Events.GameEventFactory  [class]
- readonly EventScriptType EventScriptType = eventScriptType
- readonly uint GameObject = gameObject
- static bool operator ==(EventKey left, EventKey right)
- static bool operator !=(EventKey left, EventKey right)
- bool Equals(EventKey other)
- override bool Equals(object? obj)
- override int GetHashCode()
- sealed class RegistrationData(NwObject nwObject, bool callOriginal = true)
- bool CallOriginal
- NwObject NwObject

## Anvil.API.Events.ModuleEvents  [class]

## Anvil.API.Events.OnAcquireItem  [class]
- OnAcquireItem()
- NwGameObject? AcquiredBy
- NwGameObject? AcquiredFrom
- int AmountAcquired
- NwItem? Item

## Anvil.API.NwModule  [class]
- event Action<ModuleEvents.OnAcquireItem> OnAcquireItem
- event Action<ModuleEvents.OnActivateItem> OnActivateItem
- event Action<ModuleEvents.OnClientEnter> OnClientEnter
- event Action<ModuleEvents.OnClientLeave> OnClientLeave
- event Action<ModuleEvents.OnCutsceneAbort> OnCutsceneAbort
- event Action<ModuleEvents.OnHeartbeat> OnHeartbeat
- event Action<ModuleEvents.OnModuleLoad> OnModuleLoad
- event Action<ModuleEvents.OnModuleStart> OnModuleStart
- event Action<ModuleEvents.OnNuiEvent> OnNuiEvent
- event Action<ModuleEvents.OnPlayerChat> OnPlayerChat
- event Action<ModuleEvents.OnPlayerDeath> OnPlayerDeath
- event Action<ModuleEvents.OnPlayerDying> OnPlayerDying
- event Action<ModuleEvents.OnPlayerEquipItem> OnPlayerEquipItem
- event Action<ModuleEvents.OnPlayerGuiEvent> OnPlayerGuiEvent
- event Action<ModuleEvents.OnPlayerLevelUp> OnPlayerLevelUp
- event Action<ModuleEvents.OnPlayerRespawn> OnPlayerRespawn
- event Action<ModuleEvents.OnPlayerRest> OnPlayerRest
- event Action<ModuleEvents.OnPlayerTarget> OnPlayerTarget
- event Action<ModuleEvents.OnPlayerTileAction> OnPlayerTileAction
- event Action<ModuleEvents.OnPlayerUnequipItem> OnPlayerUnequipItem
- event Action<ModuleEvents.OnUnacquireItem> OnUnacquireItem
- event Action<ModuleEvents.OnUserDefined> OnUserDefined
- static readonly NwModule Instance = new NwModule(LowLevel.ServerExoApp.GetModule())
- override bool IsValid
- int AbilityPenaltyLimit
- IEnumerable<NwArea> Areas
- int AttackBonusLimit
- int DamageBonusLimit
- GameDifficulty GameDifficulty
- int GetAbilityBonusLimit
- bool IsDawn
- bool IsDay
- bool IsDusk
- bool IsNight
- IEnumerable<NwGameObject> LimboGameObjects
- int MaxHenchmen
- int PlayerCount
- IEnumerable<NwPlayer> Players
- int SavingThrowBonusLimit
- int SkillBonusLimit
- Location StartingLocation
- int XPScale
- static implicit operator CNWSModule?(NwModule? module)
- void AddJournalQuestEntry(string categoryTag, int entryId, bool allowOverrideHigher = false)
- void ClearTextureOverride(string texName)
- void DestroyCampaignDatabase(string campaign)
- void EndGame(string endMovie)
- void ExportAllCharacters()
- T GetCampaignVariable<T>(string campaign, string name) where T : CampaignVariable, new()
- IEnumerable<NwObject> GetLastCreatedObjects()
- NwWaypoint? GetWaypointByTag(string tag)
- void MoveObjectToLimbo(NwGameObject gameObject)
- override Guid? PeekUUID()
- SQLQuery PrepareCampaignSQLQuery(string database, string query)
- SQLQuery PrepareSQLQuery(string query)
- void RefreshClientObjects(NwGameObject gameObject)
- void SendMessageToAllDMs(string message, Color color)
- void SendMessageToAllDMs(string message)
- void SetTextureOverride(string oldTexName, string newName)

## Anvil.API.NwGameObject  [class]
- event Action<ModuleEvents.OnAcquireItem> OnAcquireItem
- event Action<ModuleEvents.OnUnacquireItem> OnUnacquireItem
- IEnumerable<Effect> ActiveEffects
- AnimationState AnimationState
- NwArea? Area
- int CasterLevel
- Color HighlightColor
- int HP
- bool IsDestroyable
- bool IsRaiseable
- bool IsSelectableWhenDead
- bool IsInConversation
- virtual Location? Location
- bool IsListening
- int MaxHP
- MouseCursor MouseCursor
- bool PlotFlag
- PortraitTableEntry? PortraitId
- string PortraitResRef
- virtual Vector3 Position
- virtual float Rotation
- NwGameObject? TransitionTarget
- bool Useable
- VisibilityMode VisibilityOverride
- float VisibleDistance
- VisualTransform VisualTransform
- ObjectUiDiscovery UiDiscoveryFlags
- async Task ActionCastSpellAt(NwSpell spell, NwGameObject target, MetaMagic metaMagic = MetaMagic.Any, bool cheat = false, int domainLevel = 0, ProjectilePathType projectilePathType = ProjectilePathType.Default, bool instant = false, NwClass? spellClass = null, bool spontaneousCast = false)
- async Task ActionCastSpellAt(NwSpell spell, Location target, MetaMagic metaMagic = MetaMagic.Any, bool cheat = false, ProjectilePathType projectilePathType = ProjectilePathType.Default, bool instant = false, NwClass? spellClass = null, bool spontaneousCast = false, int domainLevel = 0)
- async Task ActionJumpToLocation(Location location)
- async Task ActionWait(TimeSpan duration)
- void ApplyEffect(EffectDuration durationType, Effect effect, TimeSpan duration = default)
- abstract NwGameObject Clone(Location location, string? newTag = null, bool copyLocalState = true)
- virtual void Destroy()
- float Distance(NwGameObject target)
- float DistanceSquared(NwGameObject target)
- async Task EndConversation()
- void FaceToObject(NwGameObject target)
- virtual void FaceToPoint(Vector3 point)
- int GetColor(ColorChannel colorChannel)
- string GetLocalizedName(PlayerLanguage language, Gender gender = Gender.Male)
- IEnumerable<NwCreature> GetNearestCreatures()
- IEnumerable<NwCreature> GetNearestCreatures(CreatureTypeFilter filter1)
- IEnumerable<NwCreature> GetNearestCreatures(CreatureTypeFilter filter1, CreatureTypeFilter filter2)
- IEnumerable<NwCreature> GetNearestCreatures(CreatureTypeFilter filter1, CreatureTypeFilter filter2, CreatureTypeFilter filter3)
- IEnumerable<T> GetNearestObjectsByType<T>() where T : NwGameObject
- VisualTransform GetVisualTransform(ObjectVisualTransformDataScope scope)
- bool HasLineOfSight(NwGameObject target)
- override Guid? PeekUUID()
- async Task PlayAnimation(Animation animation, float animSpeed, bool queueAsAction = false, TimeSpan duration = default)
- async Task PlaySound(string soundName)
- async Task PlaySoundByStrRef(StrRef strRef, bool runAsAction = true)
- void RemoveEffect(Effect effect)
- void ReplaceObjectAnimation(string anim, string newAnim)
- void ClearObjectAnimationOverride(string anim)
- void ReplaceObjectTexture(string texture, string newTexture)
- void ResetMaterialShaderUniforms()
- void ResetMaterialShaderUniforms(string material)
- void ResetMaterialShaderUniforms(string material, string param)
- SavingThrowResult RollSavingThrow(SavingThrow savingThrow, int dc, SavingThrowType saveType, NwGameObject? saveVs = null)
- abstract byte[]? Serialize()
- void SetColor(ColorChannel colorChannel, int newColor)
- void SetFacing(float facing)
- void SetIsDestroyable(bool destroyable, bool raiseable = true, bool selectableWhenDead = false)
- void SetListenPattern(string pattern, int patternNumber)
- void SetLocalizedName(string name, PlayerLanguage language, Gender gender = Gender.Male)
- void SetMaterialShaderUniform(string material, string param, int value)
- void SetMaterialShaderUniform(string material, string param, Vector4 value)
- void SetMaterialShaderUniform(string material, string param, float value)
- void SetTextBubbleOverride(ObjectUiTextBubbleOverride mode, string text)

## Anvil.API.Events.OnActivateItem  [class]
- NwItem ActivatedItem
- NwCreature ItemActivator
- Location? TargetLocation
- NwGameObject? TargetObject
- static void Signal(NwItem item, Location targetLocation, NwGameObject? targetObject = null)

## Anvil.API.Events.OnClientEnter  [class]
- NwPlayer Player

## Anvil.API.NwPlayer  [class]
- event Action<ModuleEvents.OnClientEnter> OnClientEnter
- event Action<ModuleEvents.OnClientLeave> OnClientLeave
- event Action<ModuleEvents.OnCutsceneAbort> OnCutsceneAbort
- event Action<ModuleEvents.OnNuiEvent> OnNuiEvent
- event Action<ModuleEvents.OnPlayerChat> OnPlayerChat
- event Action<ModuleEvents.OnPlayerDeath> OnPlayerDeath
- event Action<ModuleEvents.OnPlayerDying> OnPlayerDying
- event Action<ModuleEvents.OnPlayerEquipItem> OnPlayerEquipItem
- event Action<ModuleEvents.OnPlayerGuiEvent> OnPlayerGuiEvent
- event Action<ModuleEvents.OnPlayerLevelUp> OnPlayerLevelUp
- event Action<ModuleEvents.OnPlayerRespawn> OnPlayerRespawn
- event Action<ModuleEvents.OnPlayerRest> OnPlayerRest
- event Action<ModuleEvents.OnPlayerTarget> OnPlayerTarget
- event Action<ModuleEvents.OnPlayerTileAction> OnPlayerTileAction
- event Action<ModuleEvents.OnPlayerUnequipItem> OnPlayerUnequipItem
- string BicFileName
- float CameraHeight
- CameraFlag CameraFlags
- string CDKey
- Version ClientVersion
- string ClientVersionCommitSha1
- NwCreature? ControlledCreature
- float CutsceneCameraMoveRate
- string IPAddress
- bool IsConnected
- bool IsConnectionRelayed
- bool IsDM
- bool IsInCursorTargetMode
- bool IsInCutsceneMode
- bool IsPlayerDM
- bool IsValid
- PlayerLanguage Language
- int Latency
- int LatencyAverage
- NwCreature? LoginCreature
- IEnumerable<NwPlayer> PartyMembers
- PlayerPlatform Platform
- uint PlayerId
- string PlayerName
- TimeSpan? RestDurationOverride
- Location? SpawnLocation
- static bool operator ==(NwPlayer? left, NwPlayer? right)
- static implicit operator CNWSPlayer?(NwPlayer? player)
- static bool operator !=(NwPlayer? left, NwPlayer? right)
- async Task ActionExamine(NwGameObject target)
- async Task ActionStartConversation(NwGameObject converseWith, string dialogResRef = "", bool isPrivate = false, bool playHello = true)
- int AddCustomJournalEntry(JournalEntry entryData, bool silentUpdate = false)
- void AddLoopingVisualEffect(NwGameObject gameObject, VisualEffectTableEntry visualEffect)
- void AddHenchmen(NwCreature henchmen)
- void AddJournalQuestEntry(string categoryTag, int entryId, bool allPartyMembers = true, bool allowOverrideHigher = false)
- void AddToParty(NwPlayer partyLeader)
- void ApplyInstantVisualEffectToObject(VfxType visualEffect, NwGameObject target)
- void AttachCamera(NwGameObject target, bool findCleanView = false)
- void BootPlayer(string reason = "")
- void CancelTargetMode()
- void ClearLoopingVisualEffects(NwGameObject gameObject)
- void ClearPlayerNameOverride(bool clearAll = false)
- void ClearPlayerNameOverride(NwPlayer observer)
- void ClearObjectNameOverride(NwGameObject gameObject)
- void ClearTextureOverride(string texName)
- async Task Delete(string kickMessage, bool preserveBackup = true)
- void DestroySQLDatabase()
- void DisplayFloatingTextStringOnCreature(NwCreature target, string text)
- void DMPossessCreature(NwCreature creature, bool impersonate = false)
- void PlayerPossessCreature(NwCreature creature, bool mindImmune = true, bool createDefaultQuickBar = false)
- void EnterCutsceneMode(bool allowLeftClick = false)
- void EnterTargetMode(Action<ModuleEvents.OnPlayerTarget> handler, TargetModeSettings? settings = null)
- bool Equals(NwPlayer? other)
- override bool Equals(object? obj)
- void ExitCutsceneMode()
- void ExportCharacter()
- void FadeFromBlack(float fadeSpeed)
- void FadeToBlack(float fadeSpeed)
- void FloatingTextString(string message, bool broadcastToParty = true, bool chatWindow = true)
- void FloatingTextStrRef(int strRef, bool broadcastToParty = true, bool chatWindow = true)
- void ForceAreaReload()
- void ForceExamine(NwGameObject target)
- unsafe byte[]? GetAreaExplorationState(NwArea? area)
- T GetCampaignVariable<T>(string campaign, string name) where T : CampaignVariable, new()
- int GetDeviceProperty(PlayerDeviceProperty property)
- override int GetHashCode()
- JournalEntry? GetJournalEntry(string questTag)
- Dictionary<NwPlayer, PlayerNameOverride> GetOverridesForObserver(bool includeGlobal = false)
- VisibilityMode GetPersonalVisibilityOverride(NwGameObject target)
- List<VisualEffectTableEntry>? GetLoopingVisualEffects(NwGameObject gameObject)
- PlayerNameOverride? GetPlayerNameOverride(NwPlayer? observer = null)
- string? GetObjectNameOverride(NwGameObject gameObject)
- void GiveXp(int xPAmount)
- void LockCameraDirection(bool isLocked = true)
- void LockCameraDistance(bool isLocked = true)
- void LockCameraPitch(bool isLocked = true)
- void NightToDay(TimeSpan delayTransitionTime = default)
- void OpenInventory()
- void OpenInventory(NwCreature target)
- void OpenInventory(NwPlaceable target)
- void PlaySound(string sound, NwGameObject? target = null)
- void PopUpDeathPanel(bool respawnButton = true, bool waitForHelp = true, int helpStringRef = 0, string helpString = "")
- void PopUpGUIPanel(GUIPanel panel = GUIPanel.Death)
- void PostString(string message, int xPos, int yPos, ScreenAnchor anchor, float life, Color? start = null, Color? end = null, int id = 0, string font = "")
- SQLQuery PrepareSQLQuery(string query)
- unsafe void RefreshClientObject(NwGameObject gameObject)
- void RefreshPlayerClientObject()
- void RemoveFromCurrentParty()
- async Task RestoreCameraFacing()
- void SendServerMessage(string message, Color color)
- void SendServerMessage(string message)
- void SendToServer(string ipAddress = "", string password = "", string waypointTag = "", bool seamless = false)
- byte[]? Serialize(bool stripPCFlags = false)
- void SetAreaExplorationState(NwArea area, bool explored)
- unsafe void SetAreaExplorationState(NwArea area, byte[] newState)
- async Task SetCameraFacing(float direction, float pitch = -1.0f, float distance = -1.0f, CameraTransitionType transitionType = CameraTransitionType.Snap)
- void SetCameraLimits(float minPitch = -1.0f, float maxPitch = -1.0f, float minDist = -1.0f, float maxDist = -1.0f)
- void SetCutsceneMode(bool inCutscene = true, bool leftClickEnabled = false)
- void SetGuiPanelDisabled(GUIPanel panel, bool disabled, NwGameObject? targetObject = null)
- void SetPCReputation(bool like, NwPlayer target)
- void SetPersonalVisibilityOverride(NwGameObject target, VisibilityMode visibilityMode)
- void SetPlayerNameOverride(PlayerNameOverride nameOverride)
- void SetPlayerNameOverride(PlayerNameOverride nameOverride, NwPlayer observer)
- void SetObjectNameOverride(NwGameObject gameObject, string name)
- void SetTextureOverride(string oldTexName, string newTexName)
- void SetShaderUniform(ShaderUniform uniform, float value)
- void SetShaderUniform(ShaderUniform uniform, int value)
- void SetShaderUniform(ShaderUniform uniform, Vector4 value)
- void SetSpellTargetingData(TargetingData data)
- void ShowVisualEffect(VfxType effectType, Vector3 position)
- void StartAudioStream(AudioStreamIdentifier streamIdentifier, string resRef, bool looping = false, TimeSpan fadeTime = default, float seekOffset = -1f, float volume = 1f)
- void StopAudioStream(AudioStreamIdentifier streamIdentifier, TimeSpan fadeTime = default)
- void SetAudioStreamPaused(AudioStreamIdentifier streamIdentifier, bool paused, TimeSpan fadeTime = default)
- void SetAudioStreamVolume(AudioStreamIdentifier streamIdentifier, float volume = 1.0f, TimeSpan fadeTime = default)
- void SeekAudioStream(AudioStreamIdentifier streamIdentifier, float seekOffset)
- void StopFade()
- async Task StoreCameraFacing()
- bool TryCreateNuiWindow(NuiWindow window, out NuiWindowToken token, string windowId = "")
- bool TryEnterTargetMode(Action<ModuleEvents.OnPlayerTarget> handler, TargetModeSettings? settings = null)
- void UnlockAchievement(string achievementId, int lastValue = 0, int currentValue = 0, int maxValue = 0)
- void UnpossessCreature()
- async Task UpdateCharacterSheet()
- void Vibrate(VibratorMotor motor, float strength, TimeSpan duration)

## Anvil.API.Events.OnClientLeave  [class]
- NwPlayer Player

## Anvil.API.Events.OnCutsceneAbort  [class]
- NwPlayer Player

## Anvil.API.Events.OnModuleLoad  [class]

## Anvil.API.Events.OnModuleStart  [class]

## Anvil.API.Events.OnNuiEvent  [class]
- OnNuiEvent()
- int ArrayIndex
- NwObject? Context
- string ElementId
- NuiEventType EventType
- NwPlayer Player
- NuiWindowToken Token
- T? GetEventPayload<T>()

## Anvil.API.NuiWindowToken  [struct]
- event Action<ModuleEvents.OnNuiEvent> OnNuiEvent
- static NuiWindowToken Invalid = new NuiWindowToken(null!, -1)
- NwPlayer Player
- int Token
- string WindowId
- static bool operator ==(NuiWindowToken left, NuiWindowToken right)
- static bool operator !=(NuiWindowToken left, NuiWindowToken right)
- void Close()
- void Dispose()
- bool Equals(NuiWindowToken other)
- override bool Equals(object? obj)
- T? GetBindValue<T>(NuiBind<T> bind)
- List<T>? GetBindValues<T>(NuiBind<T> bind)
- override int GetHashCode()
- T? GetUserData<T>()
- void SetBindValue<T>(NuiBind<T> bind, T value)
- void SetBindValues<T>(NuiBind<T> bind, IEnumerable<T> values)
- void SetBindWatch<T>(NuiBind<T> bind, bool watch)
- void SetGroupLayout(NuiGroup group, NuiLayout newLayout)
- void SetUserData<T>(T userData)

## Anvil.API.Events.OnPlayerChat  [class]
- string Message
- NwPlayer Sender
- TalkVolume Volume

## Anvil.API.Events.OnPlayerDeath  [class]
- OnPlayerDeath()
- NwPlayer DeadPlayer
- NwObject? Killer

## Anvil.API.Events.OnPlayerDying  [class]
- NwPlayer Player

## Anvil.API.Events.OnPlayerEquipItem  [class]
- OnPlayerEquipItem()
- NwItem? Item
- NwCreature? Player
- InventorySlot Slot

## Anvil.API.Events.OnPlayerGuiEvent  [class]
- ChatBarChannel ChatBarChannel
- EffectIconTableEntry? EffectIcon
- NwObject EventObject
- GuiEventType EventType
- NwFeat FeatSelection
- GUIPanel OpenedPanel
- NwPlayer Player
- NwSkill SkillSelection
- Vector3 Vector

## Anvil.API.Events.OnPlayerLevelUp  [class]
- NwPlayer Player

## Anvil.API.Events.OnPlayerRespawn  [class]
- NwPlayer Player

## Anvil.API.Events.OnPlayerRest  [class]
- NwPlayer Player
- RestEventType RestEventType

## Anvil.API.Events.OnPlayerTarget  [class]
- bool IsCancelled
- NwPlayer Player
- NwObject? TargetObject
- Vector3 TargetPosition

## Anvil.API.Events.OnPlayerTileAction  [class]
- int ActionId
- NwPlayer Player
- Vector3 TargetPosition

## Anvil.API.Events.OnPlayerUnequipItem  [class]
- NwItem Item
- NwCreature UnequippedBy
- InventorySlot Slot

## Anvil.API.Events.OnUnacquireItem  [class]
- NwItem? Item
- NwCreature LostBy

## Anvil.API.Events.PlaceableEvents  [class]

## Anvil.API.NwPlaceable  [class]
- event Action<PlaceableEvents.OnClose> OnClose
- event Action<PlaceableEvents.OnConversation> OnConversation
- event Action<PlaceableEvents.OnDamaged> OnDamaged
- event Action<PlaceableEvents.OnDeath> OnDeath
- event Action<PlaceableEvents.OnDisarm> OnDisarm
- event Action<PlaceableEvents.OnDisturbed> OnDisturbed
- event Action<PlaceableEvents.OnHeartbeat> OnHeartbeat
- event Action<PlaceableEvents.OnLeftClick> OnLeftClick
- event Action<PlaceableEvents.OnLock> OnLock
- event Action<PlaceableEvents.OnOpen> OnOpen
- event Action<PlaceableEvents.OnPhysicalAttacked> OnPhysicalAttacked
- event Action<PlaceableEvents.OnSpellCastAt> OnSpellCastAt
- event Action<PlaceableEvents.OnTrapTriggered> OnTrapTriggered
- event Action<PlaceableEvents.OnUnlock> OnUnlock
- event Action<PlaceableEvents.OnUsed> OnUsed
- event Action<PlaceableEvents.OnUserDefined> OnUserDefined
- override bool IsValid
- PlaceableTableEntry Appearance
- string? DialogResRef
- bool HasInventory
- bool Illumination
- Inventory Inventory
- bool IsBodyBag
- bool IsStatic
- override bool KeyAutoRemoved
- bool Occupied
- override float Rotation
- NwCreature? SittingCreature
- static NwPlaceable? Create(string template, Location location, bool useAppearAnim = false, string newTag = "")
- static NwPlaceable? Deserialize(byte[] serialized)
- static implicit operator CNWSPlaceable?(NwPlaceable? placeable)
- unsafe void AcquireItem(NwItem item, bool displayFeedback = true)
- override NwPlaceable Clone(Location location, string? newTag = null, bool copyLocalState = true)
- sbyte GetBaseSavingThrow(SavingThrow savingThrow)
- async Task GiveItem(NwItem item)
- async Task GiveItem(NwItem item, int amount)
- bool IsPlaceableActionPossible(PlaceableAction action)
- override byte[]? Serialize()
- void SetBaseSavingThrow(SavingThrow savingThrow, sbyte newValue)

## Anvil.API.Events.OnLeftClick  [class]
- NwPlayer ClickedBy
- NwPlaceable Placeable

## Anvil.API.Events.OnUsed  [class]
- NwPlaceable Placeable
- NwCreature UsedBy

## Anvil.API.Events.StoreEvents  [class]

## Anvil.API.NwStore  [class]
- event Action<StoreEvents.OnClose> OnClose
- event Action<StoreEvents.OnOpen> OnOpen
- override bool IsValid
- bool BuyStolenGoods
- IReadOnlyList<NwCreature> CurrentCustomers
- int CustomerCount
- int IdentifyCost
- IEnumerable<NwItem> Items
- int MarkDown
- int MarkDownStolen
- int MarkUp
- int MaxBuyPrice
- int StoreGold
- IList<NwBaseItem?> WillNotBuyItems
- IList<NwBaseItem?> WillOnlyBuyItems
- static NwStore? Create(string template, Location location, bool useAppearAnim = false, string newTag = "")
- static NwStore? Deserialize(byte[] serialized)
- static implicit operator CNWSStore?(NwStore? store)
- void AcquireItem(NwItem item)
- override NwStore Clone(Location location, string? newTag = null, bool copyLocalState = true)
- void Open(NwPlayer player, int bonusMarkup = 0, int bonusMarkDown = 0)
- override byte[]? Serialize()

## Anvil.API.Events.TriggerEvents  [class]

## Anvil.API.Events.OnClicked  [class]
- NwCreature ClickedBy
- NwTrigger Trigger

## Anvil.API.NwTrigger  [class]
- event Action<TriggerEvents.OnClicked> OnClicked
- event Action<TriggerEvents.OnDisarmed> OnDisarmed
- event Action<TriggerEvents.OnEnter> OnEnter
- event Action<TriggerEvents.OnExit> OnExit
- event Action<TriggerEvents.OnHeartbeat> OnHeartbeat
- event Action<TriggerEvents.OnTrapTriggered> OnTrapTriggered
- event Action<TriggerEvents.OnUserDefined> OnUserDefined
- override bool IsValid
- static NwTrigger? Create(string template, Location location, float size = 2.0f, string? newTag = null)
- static NwTrigger? Deserialize(byte[] serialized)
- static implicit operator CNWSTrigger?(NwTrigger? trigger)
- override NwTrigger Clone(Location location, string? newTag = null, bool copyLocalState = true)
- IEnumerable<T> GetObjectsInTrigger<T>() where T : NwGameObject
- IEnumerable<NwGameObject> GetObjectsInTrigger(ObjectTypes objectTypes = ObjectTypes.All)
- override byte[]? Serialize()

## Anvil.API.Events.OnDisarmed  [class]
- NwCreature? DisarmedBy
- NwTrigger Trigger

## Anvil.API.Events.IEvent  [interface]
- NwObject? Context

## Anvil.API.Events.IEventFactory  [interface]

## Anvil.API.Events.IEventFactory<in TRegisterData>  [interface]

## Anvil.API.Events.IEventSkippable  [interface]
- bool Skip

## Anvil.API.Events.DialogEvents  [class]

## Anvil.API.Events.ActionTaken  [class]
- NwGameObject? CurrentSpeaker
- NwGameObject? LastSpeaker
- NwPlayer? PlayerSpeaker
- void PauseConversation()
- void ResumeConversation()

## Anvil.API.Events.AppearsWhen  [class]
- NwGameObject? CurrentSpeaker
- NwGameObject? LastSpeaker
- NwPlayer? PlayerSpeaker

## Anvil.API.Events.EffectRunScriptEvent  [class]
- Effect? Effect
- NwObject? EffectTarget
- EffectRunScriptType EventType

## Anvil.API.Events.SpellEvents  [class]

## Anvil.API.Events.OnSpellCast  [class]
- NwGameObject? Caster
- bool Harmful
- NwItem? Item
- MetaMagic MetaMagicFeat
- int SaveDC
- NwSpell Spell
- NwClass? SpellCastClass
- int SpellLevel
- bool IsSpontaneousCast
- Location? TargetLocation
- NwGameObject? TargetObject

## Anvil.API.CollectionExtensions  [class]
- static void AddElement<TKey, TValue, TCollection>(this IDictionary<TKey, TCollection> mutableLookup, TKey key, TValue value) where TCollection : ICollection<TValue>, new()
- static bool ContainsElement<TKey, TValue, TCollection>(this IDictionary<TKey, TCollection> mutableLookup, TKey key, TValue value) where TCollection : ICollection<TValue>
- static void AddRange<T>(this IList<T> list, IEnumerable<T> values)
- static void DisposeAll(this IEnumerable<IDisposable?>? disposables)
- static int InsertOrdered<T>(this List<T> sortedList, T item, IComparer<T>? comparer = null)
- static bool RemoveElement<TKey, TValue, TCollection>(this IDictionary<TKey, TCollection> mutableLookup, TKey key, TValue value) where TCollection : ICollection<TValue>, new()
- static TValue? SafeGet<TKey, TValue>(this IDictionary<TKey, TValue> dictionary, TKey key)
- static IEnumerable<T> SafeYield<T>(this T? item)
- static IEnumerable<T> Yield<T>(this T item)

## Anvil.API.GuidExtensions  [class]
- static T? ToNwObject<T>(this Guid objectId) where T : NwObject
- static NwObject? ToNwObject(this Guid objectId)
- static T? ToNwObjectSafe<T>(this Guid objectId) where T : NwObject
- static string ToUUIDString(this Guid guid)

## Anvil.API.IntegerExtensions  [class]
- static byte AsByte(this sbyte value)
- static int AsInt(this uint value)
- static long AsLong(this ulong value)
- static sbyte AsSByte(this byte value)
- static short AsShort(this ushort value)
- static uint AsUInt(this int value)
- static ulong AsULong(this long value)
- static ushort AsUShort(this short value)
- static bool ToBool(this int value)
- static int ToInt(this bool value)
- static T? ToNwObject<T>(this uint objectId) where T : NwObject
- static NwObject? ToNwObject(this uint objectId)
- static T? ToNwObjectSafe<T>(this uint objectId) where T : NwObject
- static NwPlayer? ToNwPlayer(this uint objectId, PlayerSearch playerSearch = PlayerSearch.All)

## Anvil.API.ObjectExtensions  [class]
- static bool IsLoginPlayerCharacter(this NwObject? gameObject, [NotNullWhen(true)] out NwPlayer? player)
- static bool IsPlayerControlled(this NwObject? gameObject, [NotNullWhen(true)] out NwPlayer? player)

## Anvil.API.PlayerSearch  [enum]
- values: None, Controlled, Login, All

## Anvil.API.RandomExtensions  [class]
- static double NextDouble(this Random random, double minValue, double maxValue)
- static float NextFloat(this Random random)
- static float NextFloat(this Random random, float minValue, float maxValue)

## Anvil.API.ReflectionExtensions  [class]
- static T[] GetCustomAttributes<T>(this Type type, bool inherit = true) where T : Attribute
- static T[] GetCustomAttributes<T>(this MemberInfo member, bool inherit = true) where T : Attribute
- static string GetFullName(this MemberInfo member)
- static T? SafeGetCustomAttribute<T>(this MemberInfo memberInfo, bool inherit = true)

## Anvil.API.StringExtensions  [class]
- static void AppendColored(this StringBuilder stringBuilder, string text, Color color)
- static string ColorString(this string input, Color color)
- static bool IsReservedScriptName(this string scriptName)
- static bool IsValidScriptName(this string? scriptName, bool allowEmpty)
- static float ParseFloat(this string floatString)
- static float ParseFloat(this string floatString, float defaultValue)
- static int ParseInt(this string intString)
- static int ParseInt(this string intString, int defaultValue)
- static bool ParseIntBool(this string intBoolString)
- static bool ParseIntBool(this string intBoolString, bool defaultValue)
- static NwObject? ParseObject(this string objectIdString)
- static T? ParseObject<T>(this string objectIdString) where T : NwObject
- static bool TryParseObject(this string objectIdString, [NotNullWhen(true)] out NwObject? result)
- static bool TryParseObject<T>(this string objectIdString, [NotNullWhen(true)] out T? result) where T : NwObject
- static string ReadBlock(this StringReader stringReader, int length)
- static string ReadUntilChar(this StringReader stringReader, char character)
- static void Skip(this StringReader stringReader, int count)
- static string StripColors(this string input)
- static string ToBase64EncodedString(this byte[] data)
- static byte[] ToByteArray(this string base64String)
- static bool TryParseFloat(this string floatString, out float result)
- static bool TryParseInt(this string intString, out int result)
- static bool TryParseIntBool(this string intBoolString, out bool result)

## Anvil.API.NuiProperty<T>  [class]
- static NuiBind<T> CreateBind(string key)
- static NuiValue<T> CreateValue(T value)
- static implicit operator NuiProperty<T>(T value)

## Anvil.API.NuiValue<T>  [class]
- NuiValue(T value)
- T? Value
- static implicit operator T?(NuiValue<T>? value)

## Anvil.API.NuiValueConverter  [class]
- override bool CanConvert(Type objectType)
- override object? ReadJson(JsonReader reader, Type objectType, object? existingValue, JsonSerializer serializer)
- override void WriteJson(JsonWriter writer, object? value, JsonSerializer serializer)

## Anvil.API.NuiValueStrRef  [class]
- NuiValueStrRef(StrRef? value)
- StrRef? Value
- static implicit operator StrRef?(NuiValueStrRef? value)

## Anvil.API.NuiValueStrRefConverter  [class]
- override NuiValueStrRef? ReadJson(JsonReader reader, Type objectType, NuiValueStrRef? existingValue, bool hasExistingValue, JsonSerializer serializer)
- override void WriteJson(JsonWriter writer, NuiValueStrRef? value, JsonSerializer serializer)

## Anvil.API.NuiAspect  [enum]
- values: Fit, Fill, Fit100, Exact, ExactScaled, Stretch

## Anvil.API.NuiChartType  [enum]
- values: Lines, Column

## Anvil.API.NuiDirection  [enum]
- values: Horizontal, Vertical

## Anvil.API.NuiDrawListItemOrder  [enum]
- values: Before, Default, After

## Anvil.API.NuiDrawListItemRender  [enum]
- values: Always, MouseOff, MouseHover, MouseLeft, MouseRight, MouseMiddle

## Anvil.API.NuiDrawListItemType  [enum]
- values: PolyLine, Curve, Circle, Arc, Text, Image, Line

## Anvil.API.NuiHAlign  [enum]
- values: Center, Left, Right

## Anvil.API.NuiMouseButton  [enum]
- values: Left, Middle, Right

## Anvil.API.NuiScrollbars  [enum]
- values: None, X, Y, Both, Auto

## Anvil.API.NuiStyle  [class]
- const float PrimaryHeight = 50.0f
- const float PrimaryWidth = 150.0f
- const float RowHeight = 25.0f
- const float SecondaryHeight = 35.0f
- const float SecondaryWidth = 150.0f
- const float TertiaryHeight = 30.0f
- const float TertiaryWidth = 100.0f

## Anvil.API.NuiVAlign  [enum]
- values: Middle, Top, Bottom

## Anvil.API.NuiColumn  [class]
- List<NuiElement> Children
- override string Type

## Anvil.API.NuiGroup  [class]
- bool Border
- NuiLayout? Layout
- NuiElement? Element
- NuiScrollbars Scrollbars
- override string Type
- void SetLayout(NwPlayer player, int token, NuiLayout newLayout)

## Anvil.API.NuiLayout  [class]

## Anvil.API.NuiRow  [class]
- List<NuiElement> Children
- override string Type

## Anvil.API.NuiElement  [class]
- float? Aspect
- NuiProperty<bool>? Enabled
- NuiProperty<Color>? ForegroundColor
- float? Height
- string? Id
- float? Margin
- float? Padding
- NuiProperty<string>? Tooltip
- abstract string Type
- NuiProperty<bool>? Visible
- float? Width
- List<NuiDrawListItem>? DrawList
- NuiProperty<bool>? Scissor
- NuiProperty<string>? DisabledTooltip
- NuiProperty<bool>? Encouraged

## Anvil.API.NuiDrawListArc  [class]
- NuiDrawListArc(NuiProperty<Color> color, NuiProperty<bool> fill, NuiProperty<float> lineThickness, NuiProperty<NuiVector> center, NuiProperty<float> radius,
- NuiProperty<float> AngleMax
- NuiProperty<float> AngleMin
- NuiProperty<NuiVector> Center
- NuiProperty<float> Radius
- override NuiDrawListItemType Type

## Anvil.API.NuiDrawListCircle  [class]
- NuiDrawListCircle(NuiProperty<Color> color, NuiProperty<bool> fill, NuiProperty<float> lineThickness, NuiProperty<NuiRect> rect)
- NuiProperty<NuiRect> Rect
- override NuiDrawListItemType Type

## Anvil.API.NuiDrawListCurve  [class]
- NuiDrawListCurve(NuiProperty<Color> color, NuiProperty<float> lineThickness, NuiProperty<NuiVector> pointA, NuiProperty<NuiVector> pointB, NuiProperty<NuiVector> control0, NuiProperty<NuiVector> control1)
- NuiProperty<NuiVector> Control0
- NuiProperty<NuiVector> Control1
- NuiProperty<NuiVector> PointA
- NuiProperty<NuiVector> PointB
- override NuiDrawListItemType Type

## Anvil.API.NuiDrawListItem  [class]
- NuiProperty<Color>? Color
- NuiProperty<bool> Enabled
- NuiProperty<bool>? Fill
- NuiProperty<float>? LineThickness
- abstract NuiDrawListItemType Type
- NuiDrawListItemOrder Order
- NuiDrawListItemRender Render

## Anvil.API.NuiDrawListLine  [class]
- NuiDrawListLine(NuiProperty<Color> color, NuiProperty<bool> fill, NuiProperty<float> lineThickness, NuiProperty<NuiVector> pointA, NuiProperty<NuiVector> pointB)
- NuiProperty<NuiVector> PointA
- NuiProperty<NuiVector> PointB
- override NuiDrawListItemType Type

## Anvil.API.NuiDrawListPolyLine  [class]
- NuiDrawListPolyLine(NuiProperty<Color> color, NuiProperty<bool> fill, NuiProperty<float> lineThickness, List<float> points)
- List<float> Points
- override NuiDrawListItemType Type

## Anvil.API.NuiDrawListText  [class]
- NuiDrawListText(NuiProperty<Color> color, NuiProperty<NuiRect> rect, NuiProperty<string> text)
- NuiProperty<NuiRect> Rect
- NuiProperty<string> Text
- override NuiDrawListItemType Type

## Anvil.API.NuiChart  [class]
- List<NuiChartSlot>? ChartSlots
- override string Type

## Anvil.API.NuiCombo  [class]
- NuiProperty<List<NuiComboEntry>> Entries
- NuiProperty<int> Selected
- override string Type

## Anvil.API.NuiOptions  [class]
- NuiDirection Direction
- List<string> Options
- NuiProperty<int> Selection
- override string Type

## Anvil.API.NuiSpacer  [class]
- override string Type

## Anvil.API.NuiWidget  [class]

## Anvil.API.NwMath  [class]
- const float DegToRad = (float)(Math.PI * 2f / 360f)
- const float FeetToMeters = 0.3048f
- const float MetersToFeet = 1f / FeetToMeters
- const float MetersToYards = 1f / YardsToMeters
- const float RadToDeg = 1f / DegToRad
- const float YardsToMeters = 0.9144f
- static Vector2 AngleToVector2(float angle)
- static Vector3 AngleToVector3(float angle)
- static float VectorToAngle(Vector2 direction)
- static float VectorToAngle(Vector3 direction)

## Anvil.API.NwRandom  [class]
- static string RandomName(NameTable name = NameTable.FirstGenericMale)
- static int Roll(this Random random, int sides, int amount = 1)

## Anvil.API.AreaFlags  [enum]
- values: Interior, UnderGround, Natural

## Anvil.API.CreatureClassInfo  [class]
- NwClass Class
- IArray<NwDomain?> Domains
- IReadOnlyList<IList<NwSpell>> KnownSpells
- byte Level
- byte NegativeLevels
- SpellSchool School
- void ClearMemorizedKnownSpells(NwSpell spell)
- int GetMemorizedSpellSlotCountByLevel(byte spellLevel)
- IReadOnlyList<MemorizedSpellSlot> GetMemorizedSpellSlots(byte spellLevel)
- byte GetRemainingSpellSlots(byte spellLevel)
- void SetRemainingSpellSlots(byte spellLevel, byte slotsRemaining)

## Anvil.API.CreatureLevelInfo  [class]
- CreatureClassInfo ClassInfo
- int FeatCount
- IList<NwFeat> Feats
- IReadOnlyList<IList<NwSpell>> AddedKnownSpells
- IReadOnlyList<IList<NwSpell>> RemovedKnownSpells
- byte HitDie
- ushort SkillPointsRemaining
- Ability? AbilityGained
- sbyte GetSkillRank(NwSkill skill)
- void SetSkillRank(NwSkill skill, sbyte rank)

## Anvil.API.CreatureSpellAbility  [class]
- int Index
- NwSpell Spell
- int CasterLevel
- bool Ready

## Anvil.API.CreatureTypeFilter  [struct]
- static readonly CreatureTypeFilter None = new CreatureTypeFilter(CreatureType.None, -1)
- static CreatureTypeFilter Alive(bool alive)
- static CreatureTypeFilter Class(NwClass nwClass)
- static CreatureTypeFilter DoesNotHaveSpellEffect(NwSpell spellEffect)
- static CreatureTypeFilter HasSpellEffect(NwSpell spellEffect)
- static CreatureTypeFilter Perception(PerceptionType perceptionType)
- static CreatureTypeFilter PlayerChar(bool isPc)
- static CreatureTypeFilter Race(NwRace race)
- static CreatureTypeFilter Reputation(ReputationType reputationType)

## Anvil.API.DayNightMode  [enum]
- values: EnableDayNightCycle, AlwaysNight, AlwaysDay

## Anvil.API.Inventory  [class]
- IEnumerable<NwItem> Items
- bool CheckFit(NwItem item)
- bool CheckFit(NwBaseItem baseItem)

## Anvil.API.ItemAppearance  [class]
- NwItem ChangeAppearance(Action<ItemAppearance> changes)
- void ClearArmorPieceColor(CreaturePart modelSlot, ItemAppearanceArmorColor colorSlot)
- void CopyTo(NwItem otherItem)
- void Deserialize(string serialized)
- byte GetArmorColor(ItemAppearanceArmorColor slot)
- ushort GetArmorModel(CreaturePart slot)
- byte GetArmorPieceColor(CreaturePart modelSlot, ItemAppearanceArmorColor colorSlot)
- ushort GetSimpleModel()
- byte GetWeaponColor(ItemAppearanceWeaponColor slot)
- ushort GetWeaponModel(ItemAppearanceWeaponModel slot)
- string Serialize()
- void SetArmorColor(ItemAppearanceArmorColor slot, byte value)
- void SetArmorModel(CreaturePart slot, ushort value)
- void SetArmorPieceColor(CreaturePart modelSlot, ItemAppearanceArmorColor colorSlot, byte value)
- void SetSimpleModel(ushort value)
- void SetWeaponColor(ItemAppearanceWeaponColor slot, byte value)
- void SetWeaponModel(ItemAppearanceWeaponModel slot, ushort value)

## Anvil.API.JournalEntry  [class]
- uint CalendarDay
- string Name
- uint Priority
- bool QuestCompleted
- bool QuestDisplayed
- string QuestTag
- uint State
- string Text
- uint TimeOfDay
- bool Updated

## Anvil.API.MemorizedSpellSlot  [class]
- bool IsDomainSpell
- bool IsPopulated
- bool IsReady
- MetaMagic MetaMagic
- NwSpell Spell
- void ClearMemorizedSpell()

## Anvil.API.MovementType  [enum]
- values: Stationary, Walk, Run, Sidestep, WalkBackwards

## Anvil.API.NwItem  [class]
- override bool IsValid
- int ACValue
- int AddGoldValue
- ItemAppearance Appearance
- int BaseACValue
- uint BaseGoldValue
- NwBaseItem BaseItem
- bool CursedFlag
- bool Droppable
- int GoldValue
- bool HasInventory
- int HiddenWhenEquipped
- bool Identified
- bool Infinite
- Inventory Inventory
- bool IsRangedWeapon
- int ItemCharges
- IEnumerable<ItemProperty> ItemProperties
- byte MinEquipLevel
- string OriginalUnidentifiedDescription
- bool Pickpocketable
- NwGameObject? Possessor
- int StackSize
- bool Stolen
- string UnidentifiedDescription
- NwGameObject? RootPossessor
- decimal Weight
- static NwItem? Create(string template, Location location, bool useAppearAnim = false, int stackSize = 1, string? newTag = null)
- static async Task<NwItem?> Create(string template, NwGameObject? target = null, int stackSize = 1, string newTag = "")
- static NwItem? Deserialize(byte[] serialized)
- static implicit operator CNWSItem?(NwItem? item)
- unsafe void AcquireItem(NwItem item, bool displayFeedback = true)
- void AddItemProperty(ItemProperty itemProperty, EffectDuration durationType, TimeSpan duration = default, AddPropPolicy policy = AddPropPolicy.IgnoreExisting, bool ignoreDuration = false, bool ignoreSubType = false, bool ignoreTag = false)
- void ClearMinEquipLevelOverride()
- NwItem Clone(NwGameObject targetInventory, string? newTag = null, bool copyLocalState = true, bool preserveDropFlag = true)
- override NwItem Clone(Location location, string? newTag = null, bool copyLocalState = true)
- NwItem Clone(Location location, bool preserveDropFlag, string? newTag = null, bool copyLocalState = true)
- bool CompareItem(NwItem otherItem)
- byte? GetMinEquipLevelOverride()
- int GetUsesPerDayRemaining(ItemProperty property)
- bool HasItemProperty(ItemPropertyType property)
- bool HasItemProperty(ItemPropertyTableEntry? propertyType = null, ItemPropertySubTypeTableEntry? subType = null, EffectDuration? durationType = null, string? tag = null)
- void RemoveItemProperty(ItemProperty itemProperty)
- void RemoveItemProperties(ItemPropertyTableEntry? propertyType = null, ItemPropertySubTypeTableEntry? subType = null, EffectDuration? durationType = null, string? tag = null)
- override byte[]? Serialize()
- void SetMinEquipLevelOverride(byte equipLevel)
- void SetUsesPerDayRemaining(ItemProperty property, int numUses)

## Anvil.API.NwObject  [class]
- static IEnumerable<T> FindObjectsOfType<T>() where T : NwObject
- static IEnumerable<NwObject> FindObjectsWithTag(params string[] tags)
- static IEnumerable<T> FindObjectsWithTag<T>(params string[] tags) where T : NwObject
- readonly uint ObjectId
- string Description
- bool HasUUID
- abstract bool IsValid
- IEnumerable<ObjectVariable> LocalVariables
- string Name
- string OriginalDescription
- string ResRef
- string Tag
- Guid UUID
- static bool operator ==(NwObject? left, NwObject? right)
- static implicit operator uint(NwObject? gameObject)
- static bool operator !=(NwObject? left, NwObject? right)
- async Task AddActionToQueue(System.Action action)
- void ClearActionQueue(bool clearCombatState = false)
- void ClearEventSubscriptions()
- bool Equals(NwObject? other)
- override bool Equals(object? obj)
- void ForceRefreshUUID()
- string GetEventScript(EventScriptType eventType)
- override int GetHashCode()
- T GetObjectVariable<T>(string name) where T : ObjectVariable, new()
- bool IsEventLocked(EventScriptType eventType)
- abstract Guid? PeekUUID()
- void SetEventScript(EventScriptType eventType, string? script)
- async Task SpeakString(string message, TalkVolume talkVolume = TalkVolume.Talk, bool queueAsAction = false)
- override string ToString()
- bool TryGetUUID(out Guid uid)
- Json SerializeToJson(bool saveObjectState)
- async Task WaitForObjectContext()

## Anvil.API.NwSound  [class]
- override bool IsValid
- sbyte Volume
- static NwSound? Create(string template, Location location, string? newTag = null)
- static NwSound? Deserialize(byte[] serialized)
- static implicit operator CNWSSoundObject?(NwSound? sound)
- override NwGameObject Clone(Location location, string? newTag = null, bool copyLocalState = true)
- void Play()
- override byte[]? Serialize()
- void Stop()

## Anvil.API.NwStationary  [class]
- int Hardness
- bool IsOpen
- abstract bool KeyAutoRemoved
- string KeyRequiredFeedback
- override Location Location
- bool Lockable
- int LockDC
- bool Locked
- NwGameObject? LockedBy
- bool LockKeyRequired
- string LockKeyTag
- int UnlockDC
- NwGameObject? UnlockedBy
- void CreateTrap(TrapBaseType trap, string disarm = "", string triggered = "")
- override void FaceToPoint(Vector3 point)
- void SetSavingThrow(SavingThrow savingThrow, int amount)

## Anvil.API.NwTrappable  [class]
- bool IsTrapFlagged
- bool IsTrapped
- bool OneShotTrap
- bool TrapActive
- TrapBaseType TrapBaseType
- NwPlayer? TrapCreator
- bool TrapDetectable
- int TrapDetectDC
- bool TrapDisarmable
- int TrapDisarmDC
- string TrapKeyTag
- bool TrapRecoverable
- void DisableTrap()
- async Task<NwCreature?> GetLastDisarmedBy()
- bool IsTrapDetectedBy(NwCreature creature)
- void SetTrapDetectedBy(bool detected, params NwCreature[] creatures)

## Anvil.API.NwWaypoint  [class]
- override bool IsValid
- static NwWaypoint? Create(string template, Location location, bool useAppearAnim = false, string newTag = "")
- static NwWaypoint? Create(Location location, bool useAppearAnim = false, string newTag = "")
- static NwWaypoint? Deserialize(byte[] serialized)
- static implicit operator CNWSWaypoint?(NwWaypoint? waypoint)
- override NwWaypoint Clone(Location location, string? newTag = null, bool copyLocalState = true)
- override byte[]? Serialize()

## Anvil.API.PlayerQuickBarButton  [class]
- PlayerQuickBarButton()
- PlayerQuickBarButton(CNWSQuickbarButton button)
- NwObject? Associate
- int AssociateType
- string? CommandLabel
- string? CommandLine
- byte DomainLevel
- NwObject? Item
- byte MetaType
- int MultiClass
- QuickBarButtonType ObjectType
- int Param1
- string? ResRef
- NwObject? SecondaryItem
- string? ToolTip

## Anvil.API.TileInfo  [class]
- int GridX
- int GridY
- int Height
- int Id
- int Orientation

## Anvil.API.GffResourceFieldList  [class]
- override int Count
- override GffResourceFieldType FieldType
- override IEnumerable<GffResourceFieldStruct> Values
- override GffResourceFieldStruct this[int index]
- IEnumerator<GffResourceFieldStruct> GetEnumerator()

## Anvil.API.GffResourceFieldStruct  [class]
- override int Count
- override IEnumerable<KeyValuePair<string, GffResourceField>> EntrySet
- override GffResourceFieldType FieldType
- override IEnumerable<string> Keys
- override IEnumerable<GffResourceField> Values
- override GffResourceField this[int index]
- override GffResourceField this[string key]
- override bool ContainsKey(string key)
- IEnumerator<KeyValuePair<string, GffResourceField>> GetEnumerator()
- override bool TryGetValue(string key, [NotNullWhen(true)] out GffResourceField? value)

## Anvil.API.GffResourceFieldType  [enum]
- values: Byte, Char, Word, Short, DWord, Int, DWord64, Int64, Float, Double, CExoString, CResRef, CExoLocString, Void, Struct, List

## Anvil.API.GffResourceFieldValue  [class]
- override GffResourceFieldType FieldType
- bool TryReadByte(out byte value)
- bool TryReadCExoLocString(out string value, int id = 0, Gender gender = Gender.Male)
- bool TryReadCExoString(out string value)
- bool TryReadChar(out byte value)
- bool TryReadCResRef(out string value)
- bool TryReadDouble(out double value)
- bool TryReadDWord(out uint value)
- bool TryReadDWord64(out ulong value)
- bool TryReadFloat(out float value)
- bool TryReadInt(out int value)
- bool TryReadInt64(out long value)
- bool TryReadShort(out short value)
- bool TryReadWord(out ushort value)

## Anvil.API.GffResource  [class]
- string FileType
- GffResourceField? this[int index]
- GffResourceField? this[string index]
- void Dispose()

## Anvil.API.BaseItemAmmunitionType  [enum]
- values: None, Arrow, Bolt, Bullet, Dart, Shuriken, ThrowingAxe

## Anvil.API.BaseItemCategory  [enum]
- values: None, Melee, Ranged, Shield, Armor, Helmet, Ammo, Thrown, Staves, Potion, Scroll, ThievesTools, Misc, Wands, Rods, Traps, MiscUnequippable, Container, Healers, Torches

## Anvil.API.BaseItemModelType  [enum]
- values: Simple, Layered, Composite, Armor

## Anvil.API.BaseItemQBBehaviour  [enum]
- values: Default, SelectSpellNormal, SelectSpellTargetSelf

## Anvil.API.BaseItemRotation  [enum]
- values: NoRotation, YAxis, XAxis

## Anvil.API.BaseItemWeaponSize  [enum]
- values: Unknown, Tiny, Small, Medium, Large, Huge

## Anvil.API.BaseItemWeaponWieldType  [enum]
- values: Standard, CannotWield, TwoHanded, Bow, Crossbow, Shield, DoubleSided, Creature, Sling, Throwing

## Anvil.API.CRulesKeyHash  [struct]
- ulong Hash
- CRulesKeyHash(string key)
- static implicit operator CRulesKeyHash(string key)
- static implicit operator ulong(CRulesKeyHash hash)

## Anvil.API.ClassAbilityGainList  [class]
- int Count
- IEnumerable<Ability> Keys
- IEnumerable<sbyte> Values
- sbyte this[Ability key]
- bool ContainsKey(Ability key)
- IEnumerator<KeyValuePair<Ability, sbyte>> GetEnumerator()
- bool TryGetValue(Ability key, out sbyte value)

## Anvil.API.ClassFeatListTypes  [enum]
- values: Granted, Normal, Bonus

## Anvil.API.ClassRestrictionTypes  [enum]
- values: None, LawChaos, GoodEvil, Both

## Anvil.API.ClassRestrictions  [enum]
- values: None, Neutral, Lawful, Chaotic, Good, Evil

## Anvil.API.NwBaseItem  [class]
- ACBonus ACBonusType
- BaseItemAmmunitionType AmmunitionType
- byte AnimSlashL
- byte AnimSlashR
- byte AnimSlashS
- byte ArcaneSpellFailure
- sbyte ArmorCheckPenalty
- byte BaseAC
- float BaseCost
- StrRef BaseItemStatsText
- bool CanRotateIcon
- BaseItemCategory Category
- float CostMultiplier
- byte CritMultiplier
- byte CritThreat
- string? DefaultIcon
- string? DefaultModel
- StrRef Description
- byte DieToRoll
- NwFeat? EpicDevastatingCriticalFeat
- NwFeat? EpicOverwhelmingCriticalFeat
- NwFeat? EpicWeaponFocusFeat
- NwFeat? EpicWeaponSpecializationFeat
- EquipmentSlots EquipmentSlots
- uint Id
- byte ILRStackSize
- NwFeat? ImprovedCriticalFeat
- Vector2Int InventorySlotSize
- byte InvSoundTypeIndex
- bool IsContainer
- bool IsGenderSpecific
- bool IsMonkWeapon
- bool IsRangedWeapon
- bool IsStackable
- string ItemClass
- byte ItemPropertiesMax
- byte ItemPropertiesMin
- byte ItemPropertyColumnId
- BaseItemType ItemType
- int MaxStackSize
- float ModelRangeMax
- float ModelRangeMin
- BaseItemModelType ModelType
- StrRef Name
- byte NumDamageDice
- float PreferredAttackDistance
- IEnumerable<NwFeat> PrerequisiteFeats
- BaseItemQBBehaviour QBBehaviour
- BaseItemRotation RotateOnGround
- byte StartingCharges
- StoreCategory StoreCategory
- byte StoreSortOrder
- CreatureSize WeaponFinesseMinimumCreatureSize
- NwFeat? WeaponFocusFeat
- byte WeaponMaterialTypeIndex
- NwFeat? WeaponOfChoiceFeat
- BaseItemWeaponSize WeaponSize
- NwFeat? WeaponSpecializationFeat
- IEnumerable<DamageType> WeaponType
- BaseItemWeaponWieldType WeaponWieldType
- decimal Weight
- static NwBaseItem? FromItemId(int itemId)
- static NwBaseItem FromItemType(BaseItemType itemType)
- static implicit operator NwBaseItem(BaseItemType itemType)
- bool IsPartUsingEnvMap(int partIndex)

## Anvil.API.NwClass  [class]
- IReadOnlyList<ClassAbilityGainList> AbilityGainTable
- int ArcaneSpellUsePerDayLevel
- IReadOnlyList<byte> AttackBonusTable
- IReadOnlyList<byte> BonusFeatsTable
- bool CanCastSpontaneously
- bool CanLearnFromScrolls
- float CasterLevelMultiplier
- ClassType ClassType
- StrRef Description
- int DivineSpellUsePerDayLevel
- IReadOnlyList<byte> EffectiveCRTable
- byte EpicLevel
- IReadOnlyList<ClassFeat> Feats
- bool HasArcaneSpellFailure
- bool HasDomains
- bool HasMemorizedSpells
- bool HasMulticlassPenalty
- bool HasSpecialization
- byte HitDie
- string? IconResRef
- byte Id
- bool InvertRestrictions
- bool IsArcaneCaster
- bool IsPlayerClass
- bool IsSpellbookRestricted
- bool IsSpellCaster
- byte MaxLevel
- byte MinAssociateLevel
- int MinCastingLevel
- StrRef Name
- StrRef NameLower
- StrRef NamePlural
- IReadOnlyList<sbyte> NaturalACGainTable
- uint PackageIndex
- TwoDimArray<ClassPreReqTableEntry>? PreReqTable
- Ability PrimaryAbility
- ClassRestrictions Restrictions
- ClassRestrictionTypes RestrictionTypes
- byte SkillPointBase
- IReadOnlyList<ClassSkill> Skills
- Ability SpellCastingAbility
- IReadOnlyList<ClassSpellGainList> SpellGainTable
- IReadOnlyList<ClassSpellGainList> SpellKnownTable
- string? SpellTableColumn
- static NwClass? FromClassId(int classId)
- static NwClass FromClassType(ClassType classType)
- static implicit operator NwClass(ClassType classType)
- byte GetRecommendedAbilityScore(Ability ability)
- IReadOnlyList<byte> GetSavingThrowTable(SavingThrow savingThrow)

## Anvil.API.NwDomain  [class]
- bool CastableFeat
- StrRef Description
- Domain DomainType
- NwFeat? GrantedFeat
- string? Icon
- byte Id
- bool IsValidDomain
- StrRef Name
- IReadOnlyList<NwSpell?> Spells
- static NwDomain FromDomainType(Domain domainType)
- static implicit operator NwDomain(Domain domainType)
- static NwDomain? FromDomainId(int domainId)

## Anvil.API.NwFaction  [class]
- static IReadOnlyList<NwFaction> Factions
- int AverageGoodEvilAlignment
- int AverageLawChaosAlignment
- int AverageLevel
- int AverageXP
- int Gold
- int Id
- NwPlayer? Leader
- NwClass MostFrequentClass
- StandardFaction StandardFactionType
- static NwFaction? FromFactionId(int factionId)
- static NwFaction FromStandardFaction(StandardFaction factionType)
- static bool operator ==(NwFaction? left, NwFaction? right)
- static implicit operator NwFaction(StandardFaction faction)
- static bool operator !=(NwFaction left, NwFaction right)
- void AdjustReputation(NwCreature creature, int adjustment)
- bool Equals(NwFaction? other)
- override bool Equals(object? obj)
- int GetAverageReputation(NwGameObject target)
- NwCreature GetBestACMember(NwCreature? referenceCreature = null, bool visible = false)
- override int GetHashCode()
- NwCreature GetLeastDamagedMember(NwCreature? referenceCreature = null, bool visible = false)
- List<NwCreature> GetMembers()
- NwCreature GetMostDamagedMember(NwCreature? referenceCreature = null, bool visible = false)
- int GetReputation(NwGameObject target)
- NwCreature GetStrongestMember(NwCreature? referenceCreature = null, bool visible = false)
- NwCreature GetWeakestMember(NwCreature? referenceCreature = null, bool visible = false)
- NwCreature GetWorstACMember(NwCreature? referenceCreature = null, bool visible = false)
- void SetReputation(NwGameObject target, int newReputation)

## Anvil.API.NwFeat  [class]
- bool AllClassesCanUse
- StrRef Description
- Feat FeatType
- string? IconResRef
- ushort Id
- bool IsHostileFeat
- byte MasterFeat
- byte MaxLevel
- byte MinAttackBonus
- byte MinFortSave
- byte MinLevel
- NwClass? MinLevelClass
- byte MinSpellLevel
- StrRef Name
- IEnumerable<NwFeat> RequiredFeatsAll
- IReadOnlyList<NwFeat> RequiredFeatsSome
- NwSkill? RequiredSkill1
- ushort RequiredSkill1MinRanks
- NwSkill? RequiredSkill2
- ushort RequiredSkill2MinRanks
- bool RequiresAction
- bool RequiresEpic
- NwSpell? Spell
- NwFeat? SuccessorFeat
- TalentCategory TalentCategory
- int TalentMaxCR
- bool TargetSelf
- byte UsesPerDay
- static NwFeat? FromFeatId(int featId)
- static NwFeat FromFeatType(Feat featType)
- static implicit operator NwFeat(Feat featType)
- byte GetRequiredAbilityScore(Ability ability)

## Anvil.API.NwRace  [class]
- int AbilityPointBuyAmount
- int DefaultAge
- string? DefaultCharacterDescription
- string? Description
- int ExtraFeatsAtFirstLevel
- int ExtraSkillPointsPerLevel
- NwClass? FavoredClass
- int FirstLevelSkillPointsMultiplier
- ushort Id
- bool IsPlayerRace
- string? Name
- int NormalFeatEveryNthLevel
- int NumberNormalFeatsEveryNthLevel
- string? PluralName
- RacialType RacialType
- Ability SkillPointModifierAbility
- static NwRace? FromRaceId(ushort? raceId)
- static NwRace? FromRaceId(int? raceId)
- static NwRace FromRacialType(RacialType racialType)
- static implicit operator NwRace(RacialType racialType)
- sbyte GetAbilityAdjustment(Ability ability)
- bool IsFirstLevelGrantedFeat(NwFeat feat)
- NwFeat? GetFavoredEnemyFeat()

## Anvil.API.NwRuleset  [class]
- static IReadOnlyList<NwBaseItem> BaseItems
- static IReadOnlyList<NwClass> Classes
- static IReadOnlyList<NwDomain> Domains
- static IReadOnlyList<NwFeat> Feats
- static IReadOnlyList<NwRace> Races
- static IReadOnlyList<NwSkill> Skills
- static IReadOnlyList<NwSpell> Spells
- static void ReloadRules()
- Factory(HookService hookService)

## Anvil.API.NwSkill  [class]
- bool AllClassesCanUse
- bool ArmorCheckPenalty
- StrRef Description
- string? IconResRef
- byte Id
- bool IsHostileSkill
- bool IsUntrained
- Ability KeyAbility
- StrRef Name
- Skill SkillType
- static NwSkill? FromSkillId(int skillId)
- static NwSkill FromSkillType(Skill skillType)
- static implicit operator NwSkill(Skill skillType)

## Anvil.API.NwSpell  [class]
- MetaMagic AllowedMetaMagic
- StrRef AltMessage
- SpellCastAnimType CastAnim
- string? CastGroundVisual
- string? CastHandVisual
- string? CastHeadVisual
- string? CastSound
- TimeSpan CastTime
- SpellConjureAnimType ConjureAnim
- string? ConjureGroundVisual
- string? ConjureHandVisual
- string? ConjureHeadVisual
- string? ConjureSound
- TimeSpan ConjureTime
- IReadOnlyList<NwSpell> CounterSpells
- StrRef Description
- NwFeat? FeatReference
- bool HasProjectile
- string? IconResRef
- int Id
- string? ImpactScript
- byte InnateSpellLevel
- bool IsHostileSpell
- NwSpell? MasterSpell
- StrRef Name
- string? ProjectileModel
- SpellProjectileOrientation ProjectileOrientation
- ProjectilePathType ProjectilePathType
- string? ProjectileSound
- SpellProjectileSpawnPoint ProjectileSpawnPoint
- IReadOnlyList<NwSpell> RadialSpells
- SpellRange Range
- SpellComponents SpellComponents
- SpellSchool SpellSchool
- Spell SpellType
- bool SpontaneouslyCast
- TalentCategory TalentCategory
- SpellTargetTypes TargetTypes
- bool UseConcentration
- SpellUserType UserType
- static NwSpell? FromSpellId(int? spellId)
- static NwSpell? FromSpellId(uint? spellId)
- static NwSpell FromSpellType(Spell spellType)
- static implicit operator NwSpell(Spell spellType)
- string? GetConjureSound(Gender gender)
- byte GetSpellLevelForClass(NwClass nwClass)
- int? GetSpellLevelByClass(NwClass classType, bool includeMasterSpell = true)

## Anvil.API.RulesetKeys  [class]
- static readonly CRulesKeyHash CALLED_SHOT_TO_HIT_MODIFIER = new CRulesKeyHash("CALLED_SHOT_TO_HIT_MODIFIER")
- static readonly CRulesKeyHash CALLED_SHOT_EFFECT_DURATION = new CRulesKeyHash("CALLED_SHOT_EFFECT_DURATION")
- static readonly CRulesKeyHash CALLED_SHOT_ARM_ATTACK_PENALTY = new CRulesKeyHash("CALLED_SHOT_ARM_ATTACK_PENALTY")
- static readonly CRulesKeyHash CALLED_SHOT_LEG_ABILITY_PENALTY = new CRulesKeyHash("CALLED_SHOT_LEG_ABILITY_PENALTY")
- static readonly CRulesKeyHash CALLED_SHOT_LEG_MOVEMENT_PENALTY = new CRulesKeyHash("CALLED_SHOT_LEG_MOVEMENT_PENALTY")
- static readonly CRulesKeyHash SAP_TO_HIT_MODIFIER = new CRulesKeyHash("SAP_TO_HIT_MODIFIER")
- static readonly CRulesKeyHash SAP_EFFECT_DURATION = new CRulesKeyHash("SAP_EFFECT_DURATION")
- static readonly CRulesKeyHash DISARM_TO_HIT_MODIFIER = new CRulesKeyHash("DISARM_TO_HIT_MODIFIER")
- static readonly CRulesKeyHash IMPROVED_DISARM_TO_HIT_MODIFIER = new CRulesKeyHash("IMPROVED_DISARM_TO_HIT_MODIFIER")
- static readonly CRulesKeyHash DISARM_WEAPON_SIZE_MODIFIER = new CRulesKeyHash("DISARM_WEAPON_SIZE_MODIFIER")
- static readonly CRulesKeyHash KNOCKDOWN_TO_HIT_MODIFIER = new CRulesKeyHash("KNOCKDOWN_TO_HIT_MODIFIER")
- static readonly CRulesKeyHash KNOCKDOWN_EFFECT_DURATION = new CRulesKeyHash("KNOCKDOWN_EFFECT_DURATION")
- static readonly CRulesKeyHash KNOCKDOWN_CREATURE_SIZE_MODIFIER = new CRulesKeyHash("KNOCKDOWN_CREATURE_SIZE_MODIFIER")
- static readonly CRulesKeyHash IMPROVED_PARRY_MODIFIER = new CRulesKeyHash("IMPROVED_PARRY_MODIFIER")
- static readonly CRulesKeyHash GOOD_AIM_MODIFIER = new CRulesKeyHash("GOOD_AIM_MODIFIER")
- static readonly CRulesKeyHash STUNNING_FIST_TO_HIT_MODIFIER = new CRulesKeyHash("STUNNING_FIST_TO_HIT_MODIFIER")
- static readonly CRulesKeyHash STUNNING_FIST_DAMAGE_MODIFIER = new CRulesKeyHash("STUNNING_FIST_DAMAGE_MODIFIER")
- static readonly CRulesKeyHash STUNNING_FIST_EFFECT_DURATION = new CRulesKeyHash("STUNNING_FIST_EFFECT_DURATION")
- static readonly CRulesKeyHash STUNNING_FIST_BASE_SAVE_DC = new CRulesKeyHash("STUNNING_FIST_BASE_SAVE_DC")
- static readonly CRulesKeyHash CRIPPLING_STRIKE_STRENGTH_MODIFIER = new CRulesKeyHash("CRIPPLING_STRIKE_STRENGTH_MODIFIER")
- static readonly CRulesKeyHash PARRY_RIPOSTE_DIFFERENCE = new CRulesKeyHash("PARRY_RIPOSTE_DIFFERENCE")
- static readonly CRulesKeyHash TAUNT_EFFECT_DURATION = new CRulesKeyHash("TAUNT_EFFECT_DURATION")
- static readonly CRulesKeyHash TAUNT_ARCANE_SPELL_FAILURE = new CRulesKeyHash("TAUNT_ARCANE_SPELL_FAILURE")
- static readonly CRulesKeyHash TAUNT_MAX_MODIFIER = new CRulesKeyHash("TAUNT_MAX_MODIFIER")
- static readonly CRulesKeyHash ALERTNESS_SKILL_BONUS = new CRulesKeyHash("ALERTNESS_SKILL_BONUS")
- static readonly CRulesKeyHash STONECUNNING_SEARCH_SKILL_BONUS = new CRulesKeyHash("STONECUNNING_SEARCH_SKILL_BONUS")
- static readonly CRulesKeyHash TRACKLESS_STEP_SKILL_BONUS = new CRulesKeyHash("TRACKLESS_STEP_SKILL_BONUS")
- static readonly CRulesKeyHash RESIST_NATURES_LURE_SAVE_BONUS = new CRulesKeyHash("RESIST_NATURES_LURE_SAVE_BONUS")
- static readonly CRulesKeyHash BLIND_PENALTY_TO_SKILL_CHECK = new CRulesKeyHash("BLIND_PENALTY_TO_SKILL_CHECK")
- static readonly CRulesKeyHash PICKPOCKET_HOSTILE_CREATURE_DC = new CRulesKeyHash("PICKPOCKET_HOSTILE_CREATURE_DC")
- static readonly CRulesKeyHash PICKPOCKET_NEUTRAL_CREATURE_DC = new CRulesKeyHash("PICKPOCKET_NEUTRAL_CREATURE_DC")
- static readonly CRulesKeyHash PICKPOCKET_CREATURE_DEAD = new CRulesKeyHash("PICKPOCKET_CREATURE_DEAD")
- static readonly CRulesKeyHash MAX_NON_ROGUE_DISARM_LEVEL = new CRulesKeyHash("MAX_NON_ROGUE_DISARM_LEVEL")
- static readonly CRulesKeyHash MAX_NON_ROGUE_DETECT_LEVEL = new CRulesKeyHash("MAX_NON_ROGUE_DETECT_LEVEL")
- static readonly CRulesKeyHash ASSESSTRAP_EFORTLESS_MODIFIER = new CRulesKeyHash("ASSESSTRAP_EFORTLESS_MODIFIER")
- static readonly CRulesKeyHash ASSESSTRAP_EASY_MODIFIER = new CRulesKeyHash("ASSESSTRAP_EASY_MODIFIER")
- static readonly CRulesKeyHash ASSESSTRAP_CHALLENGING_MODIFIER = new CRulesKeyHash("ASSESSTRAP_CHALLENGING_MODIFIER")
- static readonly CRulesKeyHash ASSESSTRAP_DIFFICULT_MODIFIER = new CRulesKeyHash("ASSESSTRAP_DIFFICULT_MODIFIER")
- static readonly CRulesKeyHash SKILL_DISABLETRAP_SYNERGY_LEVEL = new CRulesKeyHash("SKILL_DISABLETRAP_SYNERGY_LEVEL")
- static readonly CRulesKeyHash SKILL_DISABLE_TRAP_SYNERGY_BONUS = new CRulesKeyHash("SKILL_DISABLE_TRAP_SYNERGY_BONUS")
- static readonly CRulesKeyHash SKILL_SETTRAP_SYNERGY_LEVEL = new CRulesKeyHash("SKILL_SETTRAP_SYNERGY_LEVEL")
- static readonly CRulesKeyHash SKILL_SETTRAP_SYNERGY_BONUS = new CRulesKeyHash("SKILL_SETTRAP_SYNERGY_BONUS")
- static readonly CRulesKeyHash SKILL_PICKPOCKET_HOSTILE_SPOT_BONUS = new CRulesKeyHash("SKILL_PICKPOCKET_HOSTILE_SPOT_BONUS")
- static readonly CRulesKeyHash CONCENTRATION_CHECK_RANGE = new CRulesKeyHash("CONCENTRATION_CHECK_RANGE")
- static readonly CRulesKeyHash CONCENTRATION_CHECK_MELEE_PENALTY = new CRulesKeyHash("CONCENTRATION_CHECK_MELEE_PENALTY")
- static readonly CRulesKeyHash CONCENTRATION_BASE_DC = new CRulesKeyHash("CONCENTRATION_BASE_DC")
- static readonly CRulesKeyHash ANIMAL_EMPATHY_ANIMAL_DC = new CRulesKeyHash("ANIMAL_EMPATHY_ANIMAL_DC")
- static readonly CRulesKeyHash ANIMAL_EMPATHY_BEAST_DC = new CRulesKeyHash("ANIMAL_EMPATHY_BEAST_DC")
- static readonly CRulesKeyHash MAX_MELEE_DISTANCE = new CRulesKeyHash("MAX_MELEE_DISTANCE")
- static readonly CRulesKeyHash MIN_RANGED_DISTANCE = new CRulesKeyHash("MIN_RANGED_DISTANCE")
- static readonly CRulesKeyHash MAX_RANGED_SNEAK_ATTACK_DISTANCE = new CRulesKeyHash("MAX_RANGED_SNEAK_ATTACK_DISTANCE")
- static readonly CRulesKeyHash MAX_RANGED_FLANK_ATTACK_DISTANCE = new CRulesKeyHash("MAX_RANGED_FLANK_ATTACK_DISTANCE")
- static readonly CRulesKeyHash RANGED_MISS_DISTANCE_MODIFIER = new CRulesKeyHash("RANGED_MISS_DISTANCE_MODIFIER")
- static readonly CRulesKeyHash CROSSBOW_ATTACKS = new CRulesKeyHash("CROSSBOW_ATTACKS")
- static readonly CRulesKeyHash SLOWED_ATTACKS = new CRulesKeyHash("SLOWED_ATTACKS")
- static readonly CRulesKeyHash HASTED_BONUS_ATTACKS = new CRulesKeyHash("HASTED_BONUS_ATTACKS")
- static readonly CRulesKeyHash NUM_ATTACKS_OF_OPPORTUNITY = new CRulesKeyHash("NUM_ATTACKS_OF_OPPORTUNITY")
- static readonly CRulesKeyHash DEFENSIVE_CASTING_BASE_DC = new CRulesKeyHash("DEFENSIVE_CASTING_BASE_DC")
- static readonly CRulesKeyHash COUNTERSPELL_LESSER_DISPEL_THRESHOLD = new CRulesKeyHash("COUNTERSPELL_LESSER_DISPEL_THRESHOLD")
- static readonly CRulesKeyHash COUNTERSPELL_DISPEL_THRESHOLD = new CRulesKeyHash("COUNTERSPELL_DISPEL_THRESHOLD")
- static readonly CRulesKeyHash COUNTERSPELL_GREATER_DISPEL_THRESHOLD = new CRulesKeyHash("COUNTERSPELL_GREATER_DISPEL_THRESHOLD")
- static readonly CRulesKeyHash COUNTERSPELL_MORDENKAINENS_DISJUNCTION = new CRulesKeyHash("COUNTERSPELL_MORDENKAINENS_DISJUNCTION")
- static readonly CRulesKeyHash BLIND_TARGET_BONUS = new CRulesKeyHash("BLIND_TARGET_BONUS")
- static readonly CRulesKeyHash BLIND_MISS_CHANCE = new CRulesKeyHash("BLIND_MISS_CHANCE")
- static readonly CRulesKeyHash PRONE_MELEE_TARGET_BONUS = new CRulesKeyHash("PRONE_MELEE_TARGET_BONUS")
- static readonly CRulesKeyHash FLANK_ATTACK_BONUS = new CRulesKeyHash("FLANK_ATTACK_BONUS")
- static readonly CRulesKeyHash PRONE_RANGED_TARGET_BONUS = new CRulesKeyHash("PRONE_RANGED_TARGET_BONUS")
- static readonly CRulesKeyHash STUNNED_TARGET_BONUS = new CRulesKeyHash("STUNNED_TARGET_BONUS")
- static readonly CRulesKeyHash MOVING_TARGET_PENALTY = new CRulesKeyHash("MOVING_TARGET_PENALTY")
- static readonly CRulesKeyHash INVISIBILITY_CONCEALMENT_CHANCE = new CRulesKeyHash("INVISIBILITY_CONCEALMENT_CHANCE")
- static readonly CRulesKeyHash INVISIBILITY_ATTACK_BONUS = new CRulesKeyHash("INVISIBILITY_ATTACK_BONUS")
- static readonly CRulesKeyHash AMMUNITION_WARNING_LIMIT = new CRulesKeyHash("AMMUNITION_WARNING_LIMIT")
- static readonly CRulesKeyHash AMMUNITION_WARNING_DECREMENT = new CRulesKeyHash("AMMUNITION_WARNING_DECREMENT")
- static readonly CRulesKeyHash NOSIGHT_TARGET_PENALTY = new CRulesKeyHash("NOSIGHT_TARGET_PENALTY")
- static readonly CRulesKeyHash NUM_CLEAVE_ATTACKS = new CRulesKeyHash("NUM_CLEAVE_ATTACKS")
- static readonly CRulesKeyHash NUM_CIRCLE_KICK_ATTACKS = new CRulesKeyHash("NUM_CIRCLE_KICK_ATTACKS")
- static readonly CRulesKeyHash FAST_SPELLCAST_ROUND = new CRulesKeyHash("FAST_SPELLCAST_ROUND")
- static readonly CRulesKeyHash FLANK_LEVEL_RANGE = new CRulesKeyHash("FLANK_LEVEL_RANGE")
- static readonly CRulesKeyHash COUP_DE_GRACE_LEVEL_LIMIT = new CRulesKeyHash("COUP_DE_GRACE_LEVEL_LIMIT")
- static readonly CRulesKeyHash MAX_RANGED_COUP_DE_GRACE = new CRulesKeyHash("MAX_RANGED_COUP_DE_GRACE")
- static readonly CRulesKeyHash SPOT_NO_LIGHT_MODIFIER = new CRulesKeyHash("SPOT_NO_LIGHT_MODIFIER")
- static readonly CRulesKeyHash HIDING_LIGHT_MODIFIER = new CRulesKeyHash("HIDING_LIGHT_MODIFIER")
- static readonly CRulesKeyHash CREATURE_SIZE_TINY_AC_BONUS = new CRulesKeyHash("CREATURE_SIZE_TINY_AC_BONUS")
- static readonly CRulesKeyHash CREATURE_SIZE_SMALL_AC_BONUS = new CRulesKeyHash("CREATURE_SIZE_SMALL_AC_BONUS")
- static readonly CRulesKeyHash CREATURE_SIZE_LARGE_AC_PENALTY = new CRulesKeyHash("CREATURE_SIZE_LARGE_AC_PENALTY")
- static readonly CRulesKeyHash CREATURE_SIZE_HUGE_AC_PENALTY = new CRulesKeyHash("CREATURE_SIZE_HUGE_AC_PENALTY")
- static readonly CRulesKeyHash CREATURE_SIZE_TINY_ATTACK_BONUS = new CRulesKeyHash("CREATURE_SIZE_TINY_ATTACK_BONUS")
- static readonly CRulesKeyHash CREATURE_SIZE_SMALL_ATTACK_BONUS = new CRulesKeyHash("CREATURE_SIZE_SMALL_ATTACK_BONUS")
- static readonly CRulesKeyHash CREATURE_SIZE_LARGE_ATTACK_PENALTY = new CRulesKeyHash("CREATURE_SIZE_LARGE_ATTACK_PENALTY")
- static readonly CRulesKeyHash CREATURE_SIZE_HUGE_ATTACK_PENALTY = new CRulesKeyHash("CREATURE_SIZE_HUGE_ATTACK_PENALTY")
- static readonly CRulesKeyHash WHIRLWIND_ATTACK_RANGE = new CRulesKeyHash("WHIRLWIND_ATTACK_RANGE")
- static readonly CRulesKeyHash IMPROVED_WHIRLWIND_ATTACK_RANGE = new CRulesKeyHash("IMPROVED_WHIRLWIND_ATTACK_RANGE")
- static readonly CRulesKeyHash HOLY_AVENGER_ITEM_PROPERTY_SR_BONUS = new CRulesKeyHash("HOLY_AVENGER_ITEM_PROPERTY_SR_BONUS")
- static readonly CRulesKeyHash MAX_NEGATIVE_LEVELS = new CRulesKeyHash("MAX_NEGATIVE_LEVELS")
- static readonly CRulesKeyHash BONUS_HP_PER_LEVEL_DRAINED = new CRulesKeyHash("BONUS_HP_PER_LEVEL_DRAINED")
- static readonly CRulesKeyHash MAX_MASTER_DETECTION_DISTANCE_FROM_ASSOCIATE = new CRulesKeyHash("MAX_MASTER_DETECTION_DISTANCE_FROM_ASSOCIATE")
- static readonly CRulesKeyHash REST_ENEMY_CHECK_DISTANCE = new CRulesKeyHash("REST_ENEMY_CHECK_DISTANCE")
- static readonly CRulesKeyHash MIN_TRAP_FIRE_DISTANCE = new CRulesKeyHash("MIN_TRAP_FIRE_DISTANCE")
- static readonly CRulesKeyHash ONHIT_EFFECT_DC = new CRulesKeyHash("ONHIT_EFFECT_DC")
- static readonly CRulesKeyHash KI_STRIKE_LEVEL_5 = new CRulesKeyHash("KI_STRIKE_LEVEL_5")
- static readonly CRulesKeyHash KI_STRIKE_LEVEL_4 = new CRulesKeyHash("KI_STRIKE_LEVEL_4")
- static readonly CRulesKeyHash KI_STRIKE_LEVEL_3 = new CRulesKeyHash("KI_STRIKE_LEVEL_3")
- static readonly CRulesKeyHash KI_STRIKE_LEVEL_2 = new CRulesKeyHash("KI_STRIKE_LEVEL_2")
- static readonly CRulesKeyHash KI_STRIKE_LEVEL_1 = new CRulesKeyHash("KI_STRIKE_LEVEL_1")
- static readonly CRulesKeyHash DODGE_AC_BONUS = new CRulesKeyHash("DODGE_AC_BONUS")
- static readonly CRulesKeyHash SHOU_DISCIPLE_DODGE_AC_BONUS_2 = new CRulesKeyHash("SHOU_DISCIPLE_DODGE_AC_BONUS_2")
- static readonly CRulesKeyHash SHOU_DISCIPLE_DODGE_AC_BONUS_3 = new CRulesKeyHash("SHOU_DISCIPLE_DODGE_AC_BONUS_3")
- static readonly CRulesKeyHash UNCANNY_DODGE_LEVEL_6 = new CRulesKeyHash("UNCANNY_DODGE_LEVEL_6")
- static readonly CRulesKeyHash UNCANNY_DODGE_LEVEL_5 = new CRulesKeyHash("UNCANNY_DODGE_LEVEL_5")
- static readonly CRulesKeyHash UNCANNY_DODGE_LEVEL_4 = new CRulesKeyHash("UNCANNY_DODGE_LEVEL_4")
- static readonly CRulesKeyHash UNCANNY_DODGE_LEVEL_3 = new CRulesKeyHash("UNCANNY_DODGE_LEVEL_3")
- static readonly CRulesKeyHash UNCANNY_DODGE_LEVEL_2 = new CRulesKeyHash("UNCANNY_DODGE_LEVEL_2")
- static readonly CRulesKeyHash DEFENSIVE_AWARENESS_SAVE_BONUS = new CRulesKeyHash("DEFENSIVE_AWARENESS_SAVE_BONUS")
- static readonly CRulesKeyHash ONHAND_NORMAL_OFFHAND_ATTACK_PENALTY = new CRulesKeyHash("ONHAND_NORMAL_OFFHAND_ATTACK_PENALTY")
- static readonly CRulesKeyHash OFFHAND_NORMAL_OFFHAND_ATTACK_PENALTY = new CRulesKeyHash("OFFHAND_NORMAL_OFFHAND_ATTACK_PENALTY")
- static readonly CRulesKeyHash LIGHT_OFFHAND_WEAPON_BONUS = new CRulesKeyHash("LIGHT_OFFHAND_WEAPON_BONUS")
- static readonly CRulesKeyHash AMBIDEXTERITY_BONUS = new CRulesKeyHash("AMBIDEXTERITY_BONUS")
- static readonly CRulesKeyHash TWO_WEAPON_FIGHTING_BONUS = new CRulesKeyHash("TWO_WEAPON_FIGHTING_BONUS")
- static readonly CRulesKeyHash OFFENSIVE_TRAINING_MODIFIER = new CRulesKeyHash("OFFENSIVE_TRAINING_MODIFIER")
- static readonly CRulesKeyHash DEFENSIVE_TRAINING_MODIFIER = new CRulesKeyHash("DEFENSIVE_TRAINING_MODIFIER")
- static readonly CRulesKeyHash DWARVEN_DEFENDER_DAMAGE_REDUCTION = new CRulesKeyHash("DWARVEN_DEFENDER_DAMAGE_REDUCTION")
- static readonly CRulesKeyHash EPIC_BARBARIAN_DAMAGE_REDUCTION = new CRulesKeyHash("EPIC_BARBARIAN_DAMAGE_REDUCTION")
- static readonly CRulesKeyHash BARBARIAN_DAMAGE_REDUCTION_LEVEL_4 = new CRulesKeyHash("BARBARIAN_DAMAGE_REDUCTION_LEVEL_4")
- static readonly CRulesKeyHash BARBARIAN_DAMAGE_REDUCTION_LEVEL_3 = new CRulesKeyHash("BARBARIAN_DAMAGE_REDUCTION_LEVEL_3")
- static readonly CRulesKeyHash BARBARIAN_DAMAGE_REDUCTION_LEVEL_2 = new CRulesKeyHash("BARBARIAN_DAMAGE_REDUCTION_LEVEL_2")
- static readonly CRulesKeyHash BARBARIAN_DAMAGE_REDUCTION_LEVEL_1 = new CRulesKeyHash("BARBARIAN_DAMAGE_REDUCTION_LEVEL_1")
- static readonly CRulesKeyHash DIAMOND_SOUL_SPELL_RESISTANCE_BASE = new CRulesKeyHash("DIAMOND_SOUL_SPELL_RESISTANCE_BASE")
- static readonly CRulesKeyHash PERFECT_SELF_DAMAGE_REDUCTION_POWER = new CRulesKeyHash("PERFECT_SELF_DAMAGE_REDUCTION_POWER")
- static readonly CRulesKeyHash PERFECT_SELF_DAMAGE_REDUCTION = new CRulesKeyHash("PERFECT_SELF_DAMAGE_REDUCTION")
- static readonly CRulesKeyHash STILL_MIND_COMPETANCE_BONUS = new CRulesKeyHash("STILL_MIND_COMPETANCE_BONUS")
- static readonly CRulesKeyHash FEARLESS_MORALE_BONUS = new CRulesKeyHash("FEARLESS_MORALE_BONUS")
- static readonly CRulesKeyHash RANGED_ATTACK_IN_MELEE_RANGE = new CRulesKeyHash("RANGED_ATTACK_IN_MELEE_RANGE")
- static readonly CRulesKeyHash POINT_BLANK_SHOT_MAX_RANGE = new CRulesKeyHash("POINT_BLANK_SHOT_MAX_RANGE")
- static readonly CRulesKeyHash POINT_BLANK_SHOT_ATTACK_BONUS = new CRulesKeyHash("POINT_BLANK_SHOT_ATTACK_BONUS")
- static readonly CRulesKeyHash POINT_BLANK_SHOT_DAMAGE_BONUS = new CRulesKeyHash("POINT_BLANK_SHOT_DAMAGE_BONUS")
- static readonly CRulesKeyHash MOBILITY_DODGE_BONUS = new CRulesKeyHash("MOBILITY_DODGE_BONUS")
- static readonly CRulesKeyHash OPPORTUNIST_TO_HIT_MODIFIER = new CRulesKeyHash("OPPORTUNIST_TO_HIT_MODIFIER")
- static readonly CRulesKeyHash NATURE_SENSE_TO_HIT_MODIFIER = new CRulesKeyHash("NATURE_SENSE_TO_HIT_MODIFIER")
- static readonly CRulesKeyHash HARDINESS_SAVE_BONUS = new CRulesKeyHash("HARDINESS_SAVE_BONUS")
- static readonly CRulesKeyHash DEFLECT_ARROWS_DC = new CRulesKeyHash("DEFLECT_ARROWS_DC")
- static readonly CRulesKeyHash SKILL_FOCUS_SKILL_BONUS = new CRulesKeyHash("SKILL_FOCUS_SKILL_BONUS")
- static readonly CRulesKeyHash SKILL_AFFINITY_SKILL_BONUS = new CRulesKeyHash("SKILL_AFFINITY_SKILL_BONUS")
- static readonly CRulesKeyHash PARTIAL_SKILL_FOCUS_SKILL_BONUS = new CRulesKeyHash("PARTIAL_SKILL_FOCUS_SKILL_BONUS")
- static readonly CRulesKeyHash FEAT_EXTRA_TURNING_BONUS_TURNS = new CRulesKeyHash("FEAT_EXTRA_TURNING_BONUS_TURNS")
- static readonly CRulesKeyHash FEAT_SPELL_FOCUS_BONUS = new CRulesKeyHash("FEAT_SPELL_FOCUS_BONUS")
- static readonly CRulesKeyHash FEAT_GREATER_SPELL_FOCUS_BONUS = new CRulesKeyHash("FEAT_GREATER_SPELL_FOCUS_BONUS")
- static readonly CRulesKeyHash FEAT_SPELL_PENETRATION_LEVEL_BONUS = new CRulesKeyHash("FEAT_SPELL_PENETRATION_LEVEL_BONUS")
- static readonly CRulesKeyHash FEAT_GREATER_SPELL_PENETRATION_LEVEL_BONUS = new CRulesKeyHash("FEAT_GREATER_SPELL_PENETRATION_LEVEL_BONUS")
- static readonly CRulesKeyHash TURN_UNDEAD_BASE_USES_PER_DAY = new CRulesKeyHash("TURN_UNDEAD_BASE_USES_PER_DAY")
- static readonly CRulesKeyHash QUIVERING_PALM_BASE_DC = new CRulesKeyHash("QUIVERING_PALM_BASE_DC")
- static readonly CRulesKeyHash IMPROVED_INITIATIVE_BONUS = new CRulesKeyHash("IMPROVED_INITIATIVE_BONUS")
- static readonly CRulesKeyHash ARTIST_PERFORM_BONUS = new CRulesKeyHash("ARTIST_PERFORM_BONUS")
- static readonly CRulesKeyHash ARTIST_PERSUADE_BONUS = new CRulesKeyHash("ARTIST_PERSUADE_BONUS")
- static readonly CRulesKeyHash ARTIST_SPOT_BONUS = new CRulesKeyHash("ARTIST_SPOT_BONUS")
- static readonly CRulesKeyHash BLOODED_INITIATIVE_BONUS = new CRulesKeyHash("BLOODED_INITIATIVE_BONUS")
- static readonly CRulesKeyHash THUG_INITIATIVE_BONUS = new CRulesKeyHash("THUG_INITIATIVE_BONUS")
- static readonly CRulesKeyHash THUG_PERSUADE_BONUS = new CRulesKeyHash("THUG_PERSUADE_BONUS")
- static readonly CRulesKeyHash BLOODED_SPOT_BONUS = new CRulesKeyHash("BLOODED_SPOT_BONUS")
- static readonly CRulesKeyHash BULLHEADED_WILL_SAVE_BONUS = new CRulesKeyHash("BULLHEADED_WILL_SAVE_BONUS")
- static readonly CRulesKeyHash BULLHEADED_BONUS_VS_TAUNT = new CRulesKeyHash("BULLHEADED_BONUS_VS_TAUNT")
- static readonly CRulesKeyHash COURTEOUS_MAGOCRACY_LORE_BONUS = new CRulesKeyHash("COURTEOUS_MAGOCRACY_LORE_BONUS")
- static readonly CRulesKeyHash LUCKOFHEROES_SAVE_BONUS = new CRulesKeyHash("LUCKOFHEROES_SAVE_BONUS")
- static readonly CRulesKeyHash RESIST_POISON_BONUS = new CRulesKeyHash("RESIST_POISON_BONUS")
- static readonly CRulesKeyHash SILVER_PALM_PERSUADE_BONUS = new CRulesKeyHash("SILVER_PALM_PERSUADE_BONUS")
- static readonly CRulesKeyHash SILVER_PALM_APPRAISE_BONUS = new CRulesKeyHash("SILVER_PALM_APPRAISE_BONUS")
- static readonly CRulesKeyHash SMOOTH_TALK_PERSUADE_BONUS = new CRulesKeyHash("SMOOTH_TALK_PERSUADE_BONUS")
- static readonly CRulesKeyHash SNAKE_BLOOOD_POISON_BONUS = new CRulesKeyHash("SNAKE_BLOOOD_POISON_BONUS")
- static readonly CRulesKeyHash SNAKE_BLOOD_REFLEX_BONUS = new CRulesKeyHash("SNAKE_BLOOD_REFLEX_BONUS")
- static readonly CRulesKeyHash STEALTHY_MOVE_SILENTLY_BONUS = new CRulesKeyHash("STEALTHY_MOVE_SILENTLY_BONUS")
- static readonly CRulesKeyHash STEALTHY_HIDE_BONUS = new CRulesKeyHash("STEALTHY_HIDE_BONUS")
- static readonly CRulesKeyHash STRONG_SOUL_SAVE_BONUS = new CRulesKeyHash("STRONG_SOUL_SAVE_BONUS")
- static readonly CRulesKeyHash STRONG_SOUL_SAVE_VS_DEATH_BONUS = new CRulesKeyHash("STRONG_SOUL_SAVE_VS_DEATH_BONUS")
- static readonly CRulesKeyHash STRONG_SOULD_SAVE_VS_NEG_BONUS = new CRulesKeyHash("STRONG_SOULD_SAVE_VS_NEG_BONUS")
- static readonly CRulesKeyHash MERCANTILE_BACKGROUND_APPRAISE_BONUS = new CRulesKeyHash("MERCANTILE_BACKGROUND_APPRAISE_BONUS")
- static readonly CRulesKeyHash FEAT_EXTRA_STUNNING_ATTACK_USES = new CRulesKeyHash("FEAT_EXTRA_STUNNING_ATTACK_USES")
- static readonly CRulesKeyHash ARCANE_DEFENSE_SAVE_BONUS = new CRulesKeyHash("ARCANE_DEFENSE_SAVE_BONUS")
- static readonly CRulesKeyHash EXTRA_MUSIC_BONUS_USES = new CRulesKeyHash("EXTRA_MUSIC_BONUS_USES")
- static readonly CRulesKeyHash RESIST_DISEASE_BONUS = new CRulesKeyHash("RESIST_DISEASE_BONUS")
- static readonly CRulesKeyHash FIRING_INTO_MELEE_MODIFIER = new CRulesKeyHash("FIRING_INTO_MELEE_MODIFIER")
- static readonly CRulesKeyHash RESISTANCE_TO_ENERGY = new CRulesKeyHash("RESISTANCE_TO_ENERGY")
- static readonly CRulesKeyHash TUMBLE_NUM_RANKS_PER_AC_BONUS = new CRulesKeyHash("TUMBLE_NUM_RANKS_PER_AC_BONUS")
- static readonly CRulesKeyHash DIRTY_FIGHTING_NUM_ATTACKS_PER_ROUND = new CRulesKeyHash("DIRTY_FIGHTING_NUM_ATTACKS_PER_ROUND")
- static readonly CRulesKeyHash DENEIRS_EYE_SAVE_BONUS = new CRulesKeyHash("DENEIRS_EYE_SAVE_BONUS")
- static readonly CRulesKeyHash LLIIRAS_HEART_SAVE_BONUS = new CRulesKeyHash("LLIIRAS_HEART_SAVE_BONUS")
- static readonly CRulesKeyHash EXTRA_SMITING_BONUS_USES = new CRulesKeyHash("EXTRA_SMITING_BONUS_USES")
- static readonly CRulesKeyHash SPELLCRAFT_NUM_RANKS_PER_SAVE_BONUS = new CRulesKeyHash("SPELLCRAFT_NUM_RANKS_PER_SAVE_BONUS")
- static readonly CRulesKeyHash MAX_AC_DODGE_MOD = new CRulesKeyHash("MAX_AC_DODGE_MOD")
- static readonly CRulesKeyHash PRESTIGE_ENCHANT_ARROW_1_BONUS = new CRulesKeyHash("PRESTIGE_ENCHANT_ARROW_1_BONUS")
- static readonly CRulesKeyHash PRESTIGE_ENCHANT_ARROW_2_BONUS = new CRulesKeyHash("PRESTIGE_ENCHANT_ARROW_2_BONUS")
- static readonly CRulesKeyHash PRESTIGE_ENCHANT_ARROW_3_BONUS = new CRulesKeyHash("PRESTIGE_ENCHANT_ARROW_3_BONUS")
- static readonly CRulesKeyHash PRESTIGE_ENCHANT_ARROW_4_BONUS = new CRulesKeyHash("PRESTIGE_ENCHANT_ARROW_4_BONUS")
- static readonly CRulesKeyHash PRESTIGE_ENCHANT_ARROW_5_BONUS = new CRulesKeyHash("PRESTIGE_ENCHANT_ARROW_5_BONUS")
- static readonly CRulesKeyHash PRESTIGE_ENCHANT_ARROW_6_BONUS = new CRulesKeyHash("PRESTIGE_ENCHANT_ARROW_6_BONUS")
- static readonly CRulesKeyHash PRESTIGE_ENCHANT_ARROW_7_BONUS = new CRulesKeyHash("PRESTIGE_ENCHANT_ARROW_7_BONUS")
- static readonly CRulesKeyHash PRESTIGE_ENCHANT_ARROW_8_BONUS = new CRulesKeyHash("PRESTIGE_ENCHANT_ARROW_8_BONUS")
- static readonly CRulesKeyHash PRESTIGE_ENCHANT_ARROW_9_BONUS = new CRulesKeyHash("PRESTIGE_ENCHANT_ARROW_9_BONUS")
- static readonly CRulesKeyHash PRESTIGE_ENCHANT_ARROW_10_BONUS = new CRulesKeyHash("PRESTIGE_ENCHANT_ARROW_10_BONUS")
- static readonly CRulesKeyHash PRESTIGE_ENCHANT_ARROW_11_BONUS = new CRulesKeyHash("PRESTIGE_ENCHANT_ARROW_11_BONUS")
- static readonly CRulesKeyHash PRESTIGE_ENCHANT_ARROW_12_BONUS = new CRulesKeyHash("PRESTIGE_ENCHANT_ARROW_12_BONUS")
- static readonly CRulesKeyHash PRESTIGE_ENCHANT_ARROW_13_BONUS = new CRulesKeyHash("PRESTIGE_ENCHANT_ARROW_13_BONUS")
- static readonly CRulesKeyHash PRESTIGE_ENCHANT_ARROW_14_BONUS = new CRulesKeyHash("PRESTIGE_ENCHANT_ARROW_14_BONUS")
- static readonly CRulesKeyHash PRESTIGE_ENCHANT_ARROW_15_BONUS = new CRulesKeyHash("PRESTIGE_ENCHANT_ARROW_15_BONUS")
- static readonly CRulesKeyHash PRESTIGE_ENCHANT_ARROW_16_BONUS = new CRulesKeyHash("PRESTIGE_ENCHANT_ARROW_16_BONUS")
- static readonly CRulesKeyHash PRESTIGE_ENCHANT_ARROW_17_BONUS = new CRulesKeyHash("PRESTIGE_ENCHANT_ARROW_17_BONUS")
- static readonly CRulesKeyHash PRESTIGE_ENCHANT_ARROW_18_BONUS = new CRulesKeyHash("PRESTIGE_ENCHANT_ARROW_18_BONUS")
- static readonly CRulesKeyHash PRESTIGE_ENCHANT_ARROW_19_BONUS = new CRulesKeyHash("PRESTIGE_ENCHANT_ARROW_19_BONUS")
- static readonly CRulesKeyHash PRESTIGE_ENCHANT_ARROW_20_BONUS = new CRulesKeyHash("PRESTIGE_ENCHANT_ARROW_20_BONUS")
- static readonly CRulesKeyHash EPIC_ARMOR_SKIN_NATURAL_AC_BONUS = new CRulesKeyHash("EPIC_ARMOR_SKIN_NATURAL_AC_BONUS")
- static readonly CRulesKeyHash EPIC_DAMAGE_REDUCTION_3 = new CRulesKeyHash("EPIC_DAMAGE_REDUCTION_3")
- static readonly CRulesKeyHash EPIC_DAMAGE_REDUCTION_6 = new CRulesKeyHash("EPIC_DAMAGE_REDUCTION_6")
- static readonly CRulesKeyHash EPIC_DAMAGE_REDUCTION_9 = new CRulesKeyHash("EPIC_DAMAGE_REDUCTION_9")
- static readonly CRulesKeyHash DEVASTATING_CRITICAL_BASE_DC = new CRulesKeyHash("DEVASTATING_CRITICAL_BASE_DC")
- static readonly CRulesKeyHash EPIC_FORTITUDE_SAVE_BONUS = new CRulesKeyHash("EPIC_FORTITUDE_SAVE_BONUS")
- static readonly CRulesKeyHash EPIC_ENERGY_RESISTANCE_AMOUNT_1 = new CRulesKeyHash("EPIC_ENERGY_RESISTANCE_AMOUNT_1")
- static readonly CRulesKeyHash EPIC_ENERGY_RESISTANCE_AMOUNT_2 = new CRulesKeyHash("EPIC_ENERGY_RESISTANCE_AMOUNT_2")
- static readonly CRulesKeyHash EPIC_ENERGY_RESISTANCE_AMOUNT_3 = new CRulesKeyHash("EPIC_ENERGY_RESISTANCE_AMOUNT_3")
- static readonly CRulesKeyHash EPIC_ENERGY_RESISTANCE_AMOUNT_4 = new CRulesKeyHash("EPIC_ENERGY_RESISTANCE_AMOUNT_4")
- static readonly CRulesKeyHash EPIC_ENERGY_RESISTANCE_AMOUNT_5 = new CRulesKeyHash("EPIC_ENERGY_RESISTANCE_AMOUNT_5")
- static readonly CRulesKeyHash EPIC_ENERGY_RESISTANCE_AMOUNT_6 = new CRulesKeyHash("EPIC_ENERGY_RESISTANCE_AMOUNT_6")
- static readonly CRulesKeyHash EPIC_ENERGY_RESISTANCE_AMOUNT_7 = new CRulesKeyHash("EPIC_ENERGY_RESISTANCE_AMOUNT_7")
- static readonly CRulesKeyHash EPIC_ENERGY_RESISTANCE_AMOUNT_8 = new CRulesKeyHash("EPIC_ENERGY_RESISTANCE_AMOUNT_8")
- static readonly CRulesKeyHash EPIC_ENERGY_RESISTANCE_AMOUNT_9 = new CRulesKeyHash("EPIC_ENERGY_RESISTANCE_AMOUNT_9")
- static readonly CRulesKeyHash EPIC_ENERGY_RESISTANCE_AMOUNT_10 = new CRulesKeyHash("EPIC_ENERGY_RESISTANCE_AMOUNT_10")
- static readonly CRulesKeyHash EPIC_PROWESS_ATTACK_BONUS = new CRulesKeyHash("EPIC_PROWESS_ATTACK_BONUS")
- static readonly CRulesKeyHash EPIC_REFLEXES_REFLEX_BONUS = new CRulesKeyHash("EPIC_REFLEXES_REFLEX_BONUS")
- static readonly CRulesKeyHash EPIC_REPUTATION_SKILL_BONUS = new CRulesKeyHash("EPIC_REPUTATION_SKILL_BONUS")
- static readonly CRulesKeyHash EPIC_SKILL_FOCUS_SKILL_BONUS = new CRulesKeyHash("EPIC_SKILL_FOCUS_SKILL_BONUS")
- static readonly CRulesKeyHash FEAT_EPIC_SPELL_FOCUS_BONUS = new CRulesKeyHash("FEAT_EPIC_SPELL_FOCUS_BONUS")
- static readonly CRulesKeyHash FEAT_EPIC_SPELL_PENETRATION_LEVEL_BONUS = new CRulesKeyHash("FEAT_EPIC_SPELL_PENETRATION_LEVEL_BONUS")
- static readonly CRulesKeyHash EPIC_WILL_SAVE_BONUS = new CRulesKeyHash("EPIC_WILL_SAVE_BONUS")
- static readonly CRulesKeyHash EPIC_SPELL_RESISTANCE_1 = new CRulesKeyHash("EPIC_SPELL_RESISTANCE_1")
- static readonly CRulesKeyHash EPIC_SPELL_RESISTANCE_2 = new CRulesKeyHash("EPIC_SPELL_RESISTANCE_2")
- static readonly CRulesKeyHash EPIC_SPELL_RESISTANCE_3 = new CRulesKeyHash("EPIC_SPELL_RESISTANCE_3")
- static readonly CRulesKeyHash EPIC_SPELL_RESISTANCE_4 = new CRulesKeyHash("EPIC_SPELL_RESISTANCE_4")
- static readonly CRulesKeyHash EPIC_SPELL_RESISTANCE_5 = new CRulesKeyHash("EPIC_SPELL_RESISTANCE_5")
- static readonly CRulesKeyHash EPIC_SPELL_RESISTANCE_6 = new CRulesKeyHash("EPIC_SPELL_RESISTANCE_6")
- static readonly CRulesKeyHash EPIC_SPELL_RESISTANCE_7 = new CRulesKeyHash("EPIC_SPELL_RESISTANCE_7")
- static readonly CRulesKeyHash EPIC_SPELL_RESISTANCE_8 = new CRulesKeyHash("EPIC_SPELL_RESISTANCE_8")
- static readonly CRulesKeyHash EPIC_SPELL_RESISTANCE_9 = new CRulesKeyHash("EPIC_SPELL_RESISTANCE_9")
- static readonly CRulesKeyHash EPIC_SPELL_RESISTANCE_10 = new CRulesKeyHash("EPIC_SPELL_RESISTANCE_10")
- static readonly CRulesKeyHash EPIC_OVERWHELMING_CRITICAL_DIE = new CRulesKeyHash("EPIC_OVERWHELMING_CRITICAL_DIE")
- static readonly CRulesKeyHash EPIC_OVERHWLEMING_CRITICAL_NUM_DICE = new CRulesKeyHash("EPIC_OVERHWLEMING_CRITICAL_NUM_DICE")
- static readonly CRulesKeyHash EPIC_SELF_CONCEALMENT_50 = new CRulesKeyHash("EPIC_SELF_CONCEALMENT_50")
- static readonly CRulesKeyHash EPIC_SELF_CONCEALMENT_40 = new CRulesKeyHash("EPIC_SELF_CONCEALMENT_40")
- static readonly CRulesKeyHash EPIC_SELF_CONCEALMENT_30 = new CRulesKeyHash("EPIC_SELF_CONCEALMENT_30")
- static readonly CRulesKeyHash EPIC_SELF_CONCEALMENT_20 = new CRulesKeyHash("EPIC_SELF_CONCEALMENT_20")
- static readonly CRulesKeyHash EPIC_SELF_CONCEALMENT_10 = new CRulesKeyHash("EPIC_SELF_CONCEALMENT_10")
- static readonly CRulesKeyHash EPIC_SUPERIOR_INITIATIVE_BONUS = new CRulesKeyHash("EPIC_SUPERIOR_INITIATIVE_BONUS")
- static readonly CRulesKeyHash EPIC_GREAT_STAT_BONUS = new CRulesKeyHash("EPIC_GREAT_STAT_BONUS")
- static readonly CRulesKeyHash EPIC_GREAT_SMITING_1 = new CRulesKeyHash("EPIC_GREAT_SMITING_1")
- static readonly CRulesKeyHash EPIC_GREAT_SMITING_2 = new CRulesKeyHash("EPIC_GREAT_SMITING_2")
- static readonly CRulesKeyHash EPIC_GREAT_SMITING_3 = new CRulesKeyHash("EPIC_GREAT_SMITING_3")
- static readonly CRulesKeyHash EPIC_GREAT_SMITING_4 = new CRulesKeyHash("EPIC_GREAT_SMITING_4")
- static readonly CRulesKeyHash EPIC_GREAT_SMITING_5 = new CRulesKeyHash("EPIC_GREAT_SMITING_5")
- static readonly CRulesKeyHash EPIC_GREAT_SMITING_6 = new CRulesKeyHash("EPIC_GREAT_SMITING_6")
- static readonly CRulesKeyHash EPIC_GREAT_SMITING_7 = new CRulesKeyHash("EPIC_GREAT_SMITING_7")
- static readonly CRulesKeyHash EPIC_GREAT_SMITING_8 = new CRulesKeyHash("EPIC_GREAT_SMITING_8")
- static readonly CRulesKeyHash EPIC_GREAT_SMITING_9 = new CRulesKeyHash("EPIC_GREAT_SMITING_9")
- static readonly CRulesKeyHash EPIC_GREAT_SMITING_10 = new CRulesKeyHash("EPIC_GREAT_SMITING_10")
- static readonly CRulesKeyHash EPIC_IMPROVED_STUNNING_FIST_DC_BONUS_1 = new CRulesKeyHash("EPIC_IMPROVED_STUNNING_FIST_DC_BONUS_1")
- static readonly CRulesKeyHash EPIC_IMPROVED_STUNNING_FIST_DC_BONUS_2 = new CRulesKeyHash("EPIC_IMPROVED_STUNNING_FIST_DC_BONUS_2")
- static readonly CRulesKeyHash EPIC_IMPROVED_STUNNING_FIST_DC_BONUS_3 = new CRulesKeyHash("EPIC_IMPROVED_STUNNING_FIST_DC_BONUS_3")
- static readonly CRulesKeyHash EPIC_IMPROVED_STUNNING_FIST_DC_BONUS_4 = new CRulesKeyHash("EPIC_IMPROVED_STUNNING_FIST_DC_BONUS_4")
- static readonly CRulesKeyHash EPIC_IMPROVED_STUNNING_FIST_DC_BONUS_5 = new CRulesKeyHash("EPIC_IMPROVED_STUNNING_FIST_DC_BONUS_5")
- static readonly CRulesKeyHash EPIC_IMPROVED_STUNNING_FIST_DC_BONUS_6 = new CRulesKeyHash("EPIC_IMPROVED_STUNNING_FIST_DC_BONUS_6")
- static readonly CRulesKeyHash EPIC_IMPROVED_STUNNING_FIST_DC_BONUS_7 = new CRulesKeyHash("EPIC_IMPROVED_STUNNING_FIST_DC_BONUS_7")
- static readonly CRulesKeyHash EPIC_IMPROVED_STUNNING_FIST_DC_BONUS_8 = new CRulesKeyHash("EPIC_IMPROVED_STUNNING_FIST_DC_BONUS_8")
- static readonly CRulesKeyHash EPIC_IMPROVED_STUNNING_FIST_DC_BONUS_9 = new CRulesKeyHash("EPIC_IMPROVED_STUNNING_FIST_DC_BONUS_9")
- static readonly CRulesKeyHash EPIC_IMPROVED_STUNNING_FIST_DC_BONUS_10 = new CRulesKeyHash("EPIC_IMPROVED_STUNNING_FIST_DC_BONUS_10")
- static readonly CRulesKeyHash EPIC_BANE_OF_ENEMIES_ATTACK_BONUS = new CRulesKeyHash("EPIC_BANE_OF_ENEMIES_ATTACK_BONUS")
- static readonly CRulesKeyHash EPIC_BANE_OF_ENEMIES_DAMAGE_DIE = new CRulesKeyHash("EPIC_BANE_OF_ENEMIES_DAMAGE_DIE")
- static readonly CRulesKeyHash EPIC_BANE_OF_ENEMIES_DAMAGE_DICE = new CRulesKeyHash("EPIC_BANE_OF_ENEMIES_DAMAGE_DICE")
- static readonly CRulesKeyHash EPIC_AUTOMATIC_LESSER_STILL_LEVEL_CAP = new CRulesKeyHash("EPIC_AUTOMATIC_LESSER_STILL_LEVEL_CAP")
- static readonly CRulesKeyHash EPIC_AUTOMATIC_STILL_LEVEL_CAP = new CRulesKeyHash("EPIC_AUTOMATIC_STILL_LEVEL_CAP")
- static readonly CRulesKeyHash EPIC_AUTOMATIC_GREATER_STILL_LEVEL_CAP = new CRulesKeyHash("EPIC_AUTOMATIC_GREATER_STILL_LEVEL_CAP")
- static readonly CRulesKeyHash EPIC_AUTOMATIC_LESSER_SILENT_LEVEL_CAP = new CRulesKeyHash("EPIC_AUTOMATIC_LESSER_SILENT_LEVEL_CAP")
- static readonly CRulesKeyHash EPIC_AUTOMATIC_SILENT_LEVEL_CAP = new CRulesKeyHash("EPIC_AUTOMATIC_SILENT_LEVEL_CAP")
- static readonly CRulesKeyHash EPIC_AUTOMATIC_GREATER_SILENT_LEVEL_CAP = new CRulesKeyHash("EPIC_AUTOMATIC_GREATER_SILENT_LEVEL_CAP")
- static readonly CRulesKeyHash EPIC_AUTOMATIC_LESSER_QUICKEN_LEVEL_CAP = new CRulesKeyHash("EPIC_AUTOMATIC_LESSER_QUICKEN_LEVEL_CAP")
- static readonly CRulesKeyHash EPIC_AUTOMATIC_QUICKEN_LEVEL_CAP = new CRulesKeyHash("EPIC_AUTOMATIC_QUICKEN_LEVEL_CAP")
- static readonly CRulesKeyHash EPIC_AUTOMATIC_GREATER_QUICKEN_LEVEL_CAP = new CRulesKeyHash("EPIC_AUTOMATIC_GREATER_QUICKEN_LEVEL_CAP")
- static readonly CRulesKeyHash POISON_SAVE_BONUS_1 = new CRulesKeyHash("POISON_SAVE_BONUS_1")
- static readonly CRulesKeyHash POISON_SAVE_BONUS_2 = new CRulesKeyHash("POISON_SAVE_BONUS_2")
- static readonly CRulesKeyHash POISON_SAVE_BONUS_3 = new CRulesKeyHash("POISON_SAVE_BONUS_3")
- static readonly CRulesKeyHash POISON_SAVE_BONUS_4 = new CRulesKeyHash("POISON_SAVE_BONUS_4")
- static readonly CRulesKeyHash POISON_SAVE_BONUS_5 = new CRulesKeyHash("POISON_SAVE_BONUS_5")
- static readonly CRulesKeyHash KI_CRITICAL_BONUS = new CRulesKeyHash("KI_CRITICAL_BONUS")
- static readonly CRulesKeyHash BLINDSIGHT_RANGE_5_FEET = new CRulesKeyHash("BLINDSIGHT_RANGE_5_FEET")
- static readonly CRulesKeyHash BLINDSIGHT_RANGE_10_FEET = new CRulesKeyHash("BLINDSIGHT_RANGE_10_FEET")
- static readonly CRulesKeyHash BLINDSIGHT_RANGE_60_FEET = new CRulesKeyHash("BLINDSIGHT_RANGE_60_FEET")
- static readonly CRulesKeyHash BARBARIAN_ENDURANCE_BONUS = new CRulesKeyHash("BARBARIAN_ENDURANCE_BONUS")
- static readonly CRulesKeyHash COMPANION_LEVELS_STACK = new CRulesKeyHash("COMPANION_LEVELS_STACK")
- static readonly CRulesKeyHash DEATH_ATTACK_BASE_SAVE_DC = new CRulesKeyHash("DEATH_ATTACK_BASE_SAVE_DC")
- static readonly CRulesKeyHash QUICKENED_SPELL_MINIMUM_CONJURE_TIME = new CRulesKeyHash("QUICKENED_SPELL_MINIMUM_CONJURE_TIME")
- static readonly CRulesKeyHash HASTED_SPELL_CONJURE_TIME_MODIFIER = new CRulesKeyHash("HASTED_SPELL_CONJURE_TIME_MODIFIER")
- static readonly CRulesKeyHash FIX_EFFECTDAMAGEINCREASE_BYPASSING_DR_AND_DI = new CRulesKeyHash("FIX_EFFECTDAMAGEINCREASE_BYPASSING_DR_AND_DI")
- static readonly CRulesKeyHash TWO_HANDED_WEAPON_STRENGTH_MODIFIER = new CRulesKeyHash("TWO_HANDED_WEAPON_STRENGTH_MODIFIER")
- static readonly CRulesKeyHash OFFHAND_WEAPON_STRENGTH_MODIFIER = new CRulesKeyHash("OFFHAND_WEAPON_STRENGTH_MODIFIER")
- static readonly CRulesKeyHash HASTE_MOVEMENT_SPEED_INCREASE_BONUS = new CRulesKeyHash("HASTE_MOVEMENT_SPEED_INCREASE_BONUS")
- static readonly CRulesKeyHash HASTE_DODGE_AC_INCREASE_AMOUNT = new CRulesKeyHash("HASTE_DODGE_AC_INCREASE_AMOUNT")
- static readonly CRulesKeyHash ALL_ASSOCIATES_RUN_SCRIPTS = new CRulesKeyHash("ALL_ASSOCIATES_RUN_SCRIPTS")
- static readonly CRulesKeyHash MOVEMENT_SPEED_BONUS_DEFAULT_CAP = new CRulesKeyHash("MOVEMENT_SPEED_BONUS_DEFAULT_CAP")
- static readonly CRulesKeyHash MOVEMENT_SPEED_BONUS_MONK_CAP = new CRulesKeyHash("MOVEMENT_SPEED_BONUS_MONK_CAP")
- static readonly CRulesKeyHash MOVEMENT_SPEED_PENALTY_CAP = new CRulesKeyHash("MOVEMENT_SPEED_PENALTY_CAP")
- static readonly CRulesKeyHash MOVEMENT_STAGE_PENALTY_DETECT_MODE = new CRulesKeyHash("MOVEMENT_STAGE_PENALTY_DETECT_MODE")
- static readonly CRulesKeyHash MOVEMENT_STAGE_PENALTY_STEALTH_MODE = new CRulesKeyHash("MOVEMENT_STAGE_PENALTY_STEALTH_MODE")
- static readonly CRulesKeyHash MOVEMENT_STAGE_PENALTY_ENCUMBRANCE_HEAVY = new CRulesKeyHash("MOVEMENT_STAGE_PENALTY_ENCUMBRANCE_HEAVY")
- static readonly CRulesKeyHash MOVEMENT_STAGE_PENALTY_ENCUMBRANCE_OVERLOADED = new CRulesKeyHash("MOVEMENT_STAGE_PENALTY_ENCUMBRANCE_OVERLOADED")
- static readonly CRulesKeyHash MAX_CHARGES_FOR_ITEM_COST = new CRulesKeyHash("MAX_CHARGES_FOR_ITEM_COST")
- static readonly CRulesKeyHash TURN_RESISTANCE_AFFECTS_PCS = new CRulesKeyHash("TURN_RESISTANCE_AFFECTS_PCS")
- static readonly CRulesKeyHash SKILL_SET_TRAP_DURATION = new CRulesKeyHash("SKILL_SET_TRAP_DURATION")
- static readonly CRulesKeyHash SKILL_FLAG_TRAP_DURATION = new CRulesKeyHash("SKILL_FLAG_TRAP_DURATION")
- static readonly CRulesKeyHash SKILL_DISABLE_TRAP_DURATION = new CRulesKeyHash("SKILL_DISABLE_TRAP_DURATION")
- static readonly CRulesKeyHash SKILL_RECOVER_TRAP_DURATION = new CRulesKeyHash("SKILL_RECOVER_TRAP_DURATION")
- static readonly CRulesKeyHash SKILL_EXAMINE_TRAP_DURATION = new CRulesKeyHash("SKILL_EXAMINE_TRAP_DURATION")
- static readonly CRulesKeyHash SKILL_OPEN_LOCK_DURATION = new CRulesKeyHash("SKILL_OPEN_LOCK_DURATION")
- static readonly CRulesKeyHash SKILL_LOCK_DURATION = new CRulesKeyHash("SKILL_LOCK_DURATION")
- static readonly CRulesKeyHash SKILL_HIDE_IN_PLAIN_SIGHT_COOLDOWN = new CRulesKeyHash("SKILL_HIDE_IN_PLAIN_SIGHT_COOLDOWN")
- static readonly CRulesKeyHash SKILL_TAUNT_COOLDOWN = new CRulesKeyHash("SKILL_TAUNT_COOLDOWN")
- static readonly CRulesKeyHash SKILL_PICKPOCKET_COOLDOWN = new CRulesKeyHash("SKILL_PICKPOCKET_COOLDOWN")
- static readonly CRulesKeyHash SKILL_ANIMAL_EMPATHY_COOLDOWN = new CRulesKeyHash("SKILL_ANIMAL_EMPATHY_COOLDOWN")
- static readonly CRulesKeyHash WEAPON_FOCUS_BONUS = new CRulesKeyHash("WEAPON_FOCUS_BONUS")
- static readonly CRulesKeyHash WEAPON_SPECIALIZATION_BONUS = new CRulesKeyHash("WEAPON_SPECIALIZATION_BONUS")
- static readonly CRulesKeyHash EPIC_WEAPON_FOCUS_BONUS = new CRulesKeyHash("EPIC_WEAPON_FOCUS_BONUS")
- static readonly CRulesKeyHash EPIC_WEAPON_SPECIALIZATION_BONUS = new CRulesKeyHash("EPIC_WEAPON_SPECIALIZATION_BONUS")
- static readonly CRulesKeyHash POWER_ATTACK_TO_HIT_MODIFIER = new CRulesKeyHash("POWER_ATTACK_TO_HIT_MODIFIER")
- static readonly CRulesKeyHash POWER_ATTACK_DAMAGE_MODIFIER = new CRulesKeyHash("POWER_ATTACK_DAMAGE_MODIFIER")
- static readonly CRulesKeyHash IMPROVED_POWER_ATTACK_TO_HIT_MODIFIER = new CRulesKeyHash("IMPROVED_POWER_ATTACK_TO_HIT_MODIFIER")
- static readonly CRulesKeyHash IMPROVED_POWER_ATTACK_DAMAGE_MODIFIER = new CRulesKeyHash("IMPROVED_POWER_ATTACK_DAMAGE_MODIFIER")
- static readonly CRulesKeyHash RAPID_SHOT_TO_HIT_MODIFIER = new CRulesKeyHash("RAPID_SHOT_TO_HIT_MODIFIER")
- static readonly CRulesKeyHash FLURRY_OF_BLOWS_TO_HIT_MODIFIER = new CRulesKeyHash("FLURRY_OF_BLOWS_TO_HIT_MODIFIER")
- static readonly CRulesKeyHash EXPERTISE_TO_HIT_MODIFIER = new CRulesKeyHash("EXPERTISE_TO_HIT_MODIFIER")
- static readonly CRulesKeyHash IMPROVED_EXPERTISE_TO_HIT_MODIFIER = new CRulesKeyHash("IMPROVED_EXPERTISE_TO_HIT_MODIFIER")
- static readonly CRulesKeyHash EXPERTISE_AC_BONUS = new CRulesKeyHash("EXPERTISE_AC_BONUS")
- static readonly CRulesKeyHash IMPROVED_EXPERTISE_AC_BONUS = new CRulesKeyHash("IMPROVED_EXPERTISE_AC_BONUS")
- static readonly CRulesKeyHash LUCKY_SAVE_BONUS = new CRulesKeyHash("LUCKY_SAVE_BONUS")
- static readonly CRulesKeyHash GREAT_FORTITUDE_SAVE_BONUS = new CRulesKeyHash("GREAT_FORTITUDE_SAVE_BONUS")
- static readonly CRulesKeyHash IRON_WILL_SAVE_BONUS = new CRulesKeyHash("IRON_WILL_SAVE_BONUS")
- static readonly CRulesKeyHash LIGHTNING_REFLEXES_SAVE_BONUS = new CRulesKeyHash("LIGHTNING_REFLEXES_SAVE_BONUS")
- static readonly CRulesKeyHash FEAT_TOUGHNESS_HP_BONUS = new CRulesKeyHash("FEAT_TOUGHNESS_HP_BONUS")
- static readonly CRulesKeyHash FEAT_EPIC_TOUGHNESS_HP_BONUS_10 = new CRulesKeyHash("FEAT_EPIC_TOUGHNESS_HP_BONUS_10")
- static readonly CRulesKeyHash FEAT_EPIC_TOUGHNESS_HP_BONUS_9 = new CRulesKeyHash("FEAT_EPIC_TOUGHNESS_HP_BONUS_9")
- static readonly CRulesKeyHash FEAT_EPIC_TOUGHNESS_HP_BONUS_8 = new CRulesKeyHash("FEAT_EPIC_TOUGHNESS_HP_BONUS_8")
- static readonly CRulesKeyHash FEAT_EPIC_TOUGHNESS_HP_BONUS_7 = new CRulesKeyHash("FEAT_EPIC_TOUGHNESS_HP_BONUS_7")
- static readonly CRulesKeyHash FEAT_EPIC_TOUGHNESS_HP_BONUS_6 = new CRulesKeyHash("FEAT_EPIC_TOUGHNESS_HP_BONUS_6")
- static readonly CRulesKeyHash FEAT_EPIC_TOUGHNESS_HP_BONUS_5 = new CRulesKeyHash("FEAT_EPIC_TOUGHNESS_HP_BONUS_5")
- static readonly CRulesKeyHash FEAT_EPIC_TOUGHNESS_HP_BONUS_4 = new CRulesKeyHash("FEAT_EPIC_TOUGHNESS_HP_BONUS_4")
- static readonly CRulesKeyHash FEAT_EPIC_TOUGHNESS_HP_BONUS_3 = new CRulesKeyHash("FEAT_EPIC_TOUGHNESS_HP_BONUS_3")
- static readonly CRulesKeyHash FEAT_EPIC_TOUGHNESS_HP_BONUS_2 = new CRulesKeyHash("FEAT_EPIC_TOUGHNESS_HP_BONUS_2")
- static readonly CRulesKeyHash FEAT_EPIC_TOUGHNESS_HP_BONUS_1 = new CRulesKeyHash("FEAT_EPIC_TOUGHNESS_HP_BONUS_1")
- static readonly CRulesKeyHash FEAT_DEATHLESS_VIGOR_HP_BONUS = new CRulesKeyHash("FEAT_DEATHLESS_VIGOR_HP_BONUS")
- static readonly CRulesKeyHash FEAT_EPIC_DEATHLESS_VIGOR_HP_BONUS = new CRulesKeyHash("FEAT_EPIC_DEATHLESS_VIGOR_HP_BONUS")
- static readonly CRulesKeyHash FEAT_DEFENSIVES_STANCE_STR_BONUS = new CRulesKeyHash("FEAT_DEFENSIVES_STANCE_STR_BONUS")
- static readonly CRulesKeyHash FEAT_DEFENSIVES_STANCE_CON_BONUS = new CRulesKeyHash("FEAT_DEFENSIVES_STANCE_CON_BONUS")
- static readonly CRulesKeyHash FEAT_DEFENSIVES_STANCE_SAVE_BONUS = new CRulesKeyHash("FEAT_DEFENSIVES_STANCE_SAVE_BONUS")
- static readonly CRulesKeyHash FEAT_DEFENSIVES_STANCE_DODGE_BONUS = new CRulesKeyHash("FEAT_DEFENSIVES_STANCE_DODGE_BONUS")
- static readonly CRulesKeyHash FEAT_DRAGON_HD6 = new CRulesKeyHash("FEAT_DRAGON_HD6")
- static readonly CRulesKeyHash FEAT_DRAGON_HD8 = new CRulesKeyHash("FEAT_DRAGON_HD8")
- static readonly CRulesKeyHash FEAT_DRAGON_HD10 = new CRulesKeyHash("FEAT_DRAGON_HD10")
- static readonly CRulesKeyHash FEAT_DRAGON_HD12 = new CRulesKeyHash("FEAT_DRAGON_HD12")
- static readonly CRulesKeyHash DIRTY_FIGHTING_BONUS_DICE = new CRulesKeyHash("DIRTY_FIGHTING_BONUS_DICE")
- static readonly CRulesKeyHash MIN_LEVEL_FOR_MAX_HP = new CRulesKeyHash("MIN_LEVEL_FOR_MAX_HP")
- static readonly CRulesKeyHash SPELL_METAMAGIC_EMPOWER_COST = new CRulesKeyHash("SPELL_METAMAGIC_EMPOWER_COST")
- static readonly CRulesKeyHash SPELL_METAMAGIC_EXTEND_COST = new CRulesKeyHash("SPELL_METAMAGIC_EXTEND_COST")
- static readonly CRulesKeyHash SPELL_METAMAGIC_MAXIMIZE_COST = new CRulesKeyHash("SPELL_METAMAGIC_MAXIMIZE_COST")
- static readonly CRulesKeyHash SPELL_METAMAGIC_QUICKEN_COST = new CRulesKeyHash("SPELL_METAMAGIC_QUICKEN_COST")
- static readonly CRulesKeyHash SPELL_METAMAGIC_SILENT_COST = new CRulesKeyHash("SPELL_METAMAGIC_SILENT_COST")
- static readonly CRulesKeyHash SPELL_METAMAGIC_STILL_COST = new CRulesKeyHash("SPELL_METAMAGIC_STILL_COST")
- static readonly CRulesKeyHash MONK_DAMAGE_TIER_ONE_THRESHHOLD = new CRulesKeyHash("MONK_DAMAGE_TIER_ONE_THRESHHOLD")
- static readonly CRulesKeyHash MONK_DAMAGE_TIER_TWO_THRESHHOLD = new CRulesKeyHash("MONK_DAMAGE_TIER_TWO_THRESHHOLD")
- static readonly CRulesKeyHash MONK_DAMAGE_TIER_THREE_THRESHHOLD = new CRulesKeyHash("MONK_DAMAGE_TIER_THREE_THRESHHOLD")
- static readonly CRulesKeyHash MONK_DAMAGE_TIER_FOUR_THRESHHOLD = new CRulesKeyHash("MONK_DAMAGE_TIER_FOUR_THRESHHOLD")
- static readonly CRulesKeyHash MONK_DAMAGE_TIER_ZERO_SDAMAGE_DIE = new CRulesKeyHash("MONK_DAMAGE_TIER_ZERO_SDAMAGE_DIE")
- static readonly CRulesKeyHash MONK_DAMAGE_TIER_ONE_SDAMAGE_DIE = new CRulesKeyHash("MONK_DAMAGE_TIER_ONE_SDAMAGE_DIE")
- static readonly CRulesKeyHash MONK_DAMAGE_TIER_TWO_SDAMAGE_DIE = new CRulesKeyHash("MONK_DAMAGE_TIER_TWO_SDAMAGE_DIE")
- static readonly CRulesKeyHash MONK_DAMAGE_TIER_THREE_SDAMAGE_DIE = new CRulesKeyHash("MONK_DAMAGE_TIER_THREE_SDAMAGE_DIE")
- static readonly CRulesKeyHash MONK_DAMAGE_TIER_FOUR_SDAMAGE_DIE = new CRulesKeyHash("MONK_DAMAGE_TIER_FOUR_SDAMAGE_DIE")
- static readonly CRulesKeyHash MONK_DAMAGE_TIER_ZERO_SDAMAGE_DICE = new CRulesKeyHash("MONK_DAMAGE_TIER_ZERO_SDAMAGE_DICE")
- static readonly CRulesKeyHash MONK_DAMAGE_TIER_ONE_SDAMAGE_DICE = new CRulesKeyHash("MONK_DAMAGE_TIER_ONE_SDAMAGE_DICE")
- static readonly CRulesKeyHash MONK_DAMAGE_TIER_TWO_SDAMAGE_DICE = new CRulesKeyHash("MONK_DAMAGE_TIER_TWO_SDAMAGE_DICE")
- static readonly CRulesKeyHash MONK_DAMAGE_TIER_THREE_SDAMAGE_DICE = new CRulesKeyHash("MONK_DAMAGE_TIER_THREE_SDAMAGE_DICE")
- static readonly CRulesKeyHash MONK_DAMAGE_TIER_FOUR_SDAMAGE_DICE = new CRulesKeyHash("MONK_DAMAGE_TIER_FOUR_SDAMAGE_DICE")
- static readonly CRulesKeyHash MONK_DAMAGE_TIER_ZERO_DAMAGE_DIE = new CRulesKeyHash("MONK_DAMAGE_TIER_ZERO_DAMAGE_DIE")
- static readonly CRulesKeyHash MONK_DAMAGE_TIER_ONE_DAMAGE_DIE = new CRulesKeyHash("MONK_DAMAGE_TIER_ONE_DAMAGE_DIE")
- static readonly CRulesKeyHash MONK_DAMAGE_TIER_TWO_DAMAGE_DIE = new CRulesKeyHash("MONK_DAMAGE_TIER_TWO_DAMAGE_DIE")
- static readonly CRulesKeyHash MONK_DAMAGE_TIER_THREE_DAMAGE_DIE = new CRulesKeyHash("MONK_DAMAGE_TIER_THREE_DAMAGE_DIE")
- static readonly CRulesKeyHash MONK_DAMAGE_TIER_FOUR_DAMAGE_DIE = new CRulesKeyHash("MONK_DAMAGE_TIER_FOUR_DAMAGE_DIE")
- static readonly CRulesKeyHash MONK_DAMAGE_TIER_DICE = new CRulesKeyHash("MONK_DAMAGE_TIER_DICE")
- static readonly CRulesKeyHash UNARMED_SDAMAGE_DIE = new CRulesKeyHash("UNARMED_SDAMAGE_DIE")
- static readonly CRulesKeyHash UNARMED_DAMAGE_DIE = new CRulesKeyHash("UNARMED_DAMAGE_DIE")
- static readonly CRulesKeyHash UNARMED_DAMAGE_DICE = new CRulesKeyHash("UNARMED_DAMAGE_DICE")
- static readonly CRulesKeyHash SHOU_DISCIPLE_DAMAGE_TIER_ONE_DICE = new CRulesKeyHash("SHOU_DISCIPLE_DAMAGE_TIER_ONE_DICE")
- static readonly CRulesKeyHash SHOU_DISCIPLE_DAMAGE_TIER_TWO_DICE = new CRulesKeyHash("SHOU_DISCIPLE_DAMAGE_TIER_TWO_DICE")
- static readonly CRulesKeyHash SHOU_DISCIPLE_DAMAGE_TIER_ONE_THRESHHOLD = new CRulesKeyHash("SHOU_DISCIPLE_DAMAGE_TIER_ONE_THRESHHOLD")
- static readonly CRulesKeyHash SHOU_DISCIPLE_DAMAGE_TIER_TWO_THRESHHOLD = new CRulesKeyHash("SHOU_DISCIPLE_DAMAGE_TIER_TWO_THRESHHOLD")
- static readonly CRulesKeyHash SHOU_DISCIPLE_DAMAGE_TIER_THREE_THRESHHOLD = new CRulesKeyHash("SHOU_DISCIPLE_DAMAGE_TIER_THREE_THRESHHOLD")
- static readonly CRulesKeyHash SHOU_DISCIPLE_DAMAGE_TIER_ZERO_DAMAGE_DIE = new CRulesKeyHash("SHOU_DISCIPLE_DAMAGE_TIER_ZERO_DAMAGE_DIE")
- static readonly CRulesKeyHash SHOU_DISCIPLE_DAMAGE_TIER_ONE_DAMAGE_DIE = new CRulesKeyHash("SHOU_DISCIPLE_DAMAGE_TIER_ONE_DAMAGE_DIE")
- static readonly CRulesKeyHash SHOU_DISCIPLE_DAMAGE_TIER_TWO_DAMAGE_DIE = new CRulesKeyHash("SHOU_DISCIPLE_DAMAGE_TIER_TWO_DAMAGE_DIE")
- static readonly CRulesKeyHash SHOU_DISCIPLE_DAMAGE_TIER_THREE_DAMAGE_DIE = new CRulesKeyHash("SHOU_DISCIPLE_DAMAGE_TIER_THREE_DAMAGE_DIE")
- static readonly CRulesKeyHash SHOU_DISCIPLE_DAMAGE_TIER_ZERO_SDAMAGE_DIE = new CRulesKeyHash("SHOU_DISCIPLE_DAMAGE_TIER_ZERO_SDAMAGE_DIE")
- static readonly CRulesKeyHash SHOU_DISCIPLE_DAMAGE_TIER_ONE_SDAMAGE_DIE = new CRulesKeyHash("SHOU_DISCIPLE_DAMAGE_TIER_ONE_SDAMAGE_DIE")
- static readonly CRulesKeyHash SHOU_DISCIPLE_DAMAGE_TIER_TWO_SDAMAGE_DIE = new CRulesKeyHash("SHOU_DISCIPLE_DAMAGE_TIER_TWO_SDAMAGE_DIE")
- static readonly CRulesKeyHash SHOU_DISCIPLE_DAMAGE_TIER_THREE_SDAMAGE_DIE = new CRulesKeyHash("SHOU_DISCIPLE_DAMAGE_TIER_THREE_SDAMAGE_DIE")
- static readonly CRulesKeyHash MULTIPLE_ATTACKS_BAB_PENALTY_MULTIPLIER = new CRulesKeyHash("MULTIPLE_ATTACKS_BAB_PENALTY_MULTIPLIER")
- static readonly CRulesKeyHash MULTIPLE_ATTACKS_BAB_PENALTY_MULTIPLIER_MONK = new CRulesKeyHash("MULTIPLE_ATTACKS_BAB_PENALTY_MULTIPLIER_MONK")
- static readonly CRulesKeyHash CHARGEN_ENABLED_PHENOTYPES = new CRulesKeyHash("CHARGEN_ENABLED_PHENOTYPES")
- static readonly CRulesKeyHash CHARGEN_ABILITY_COST_INCREMENT2 = new CRulesKeyHash("CHARGEN_ABILITY_COST_INCREMENT2")
- static readonly CRulesKeyHash CHARGEN_ABILITY_COST_INCREMENT3 = new CRulesKeyHash("CHARGEN_ABILITY_COST_INCREMENT3")
- static readonly CRulesKeyHash CHARGEN_ABILITY_COST_INCREMENT4 = new CRulesKeyHash("CHARGEN_ABILITY_COST_INCREMENT4")
- static readonly CRulesKeyHash CHARGEN_BASE_ABILITY_MIN = new CRulesKeyHash("CHARGEN_BASE_ABILITY_MIN")
- static readonly CRulesKeyHash CHARGEN_BASE_ABILITY_MIN_PRIMARY = new CRulesKeyHash("CHARGEN_BASE_ABILITY_MIN_PRIMARY")
- static readonly CRulesKeyHash CHARGEN_BASE_ABILITY_MAX = new CRulesKeyHash("CHARGEN_BASE_ABILITY_MAX")
- static readonly CRulesKeyHash CHARGEN_ABILITY_NEUTRAL_VALUE = new CRulesKeyHash("CHARGEN_ABILITY_NEUTRAL_VALUE")
- static readonly CRulesKeyHash CHARGEN_ABILITY_MODIFIER_INCREMENT = new CRulesKeyHash("CHARGEN_ABILITY_MODIFIER_INCREMENT")
- static readonly CRulesKeyHash CHARGEN_SKILL_MAX_LEVEL_1_BONUS = new CRulesKeyHash("CHARGEN_SKILL_MAX_LEVEL_1_BONUS")
- static readonly CRulesKeyHash CHARGEN_ALLOW_CUSTOM_PORTRAITS = new CRulesKeyHash("CHARGEN_ALLOW_CUSTOM_PORTRAITS")
- static readonly CRulesKeyHash CHARGEN_ENABLE_RECOMMENDED_BUTTON = new CRulesKeyHash("CHARGEN_ENABLE_RECOMMENDED_BUTTON")
- static readonly CRulesKeyHash MULTICLASS_LIMIT = new CRulesKeyHash("MULTICLASS_LIMIT")
- static readonly CRulesKeyHash ALL_ASSOCIATES_CAN_INTERACT = new CRulesKeyHash("ALL_ASSOCIATES_CAN_INTERACT")

## Anvil.API.SpellCastAnimType  [enum]
- values: Unknown, Area, Attack, Out, Self, Touch, Up, Creature

## Anvil.API.SpellComponents  [enum]
- values: None, Verbal, Somatic, VerbalSomatic

## Anvil.API.SpellConjureAnimType  [enum]
- values: Unknown, Hand, Head

## Anvil.API.SpellProjectileOrientation  [enum]
- values: Unknown, Path, Target

## Anvil.API.SpellProjectileSpawnPoint  [enum]
- values: Unknown, Hand, Monster0, Monster1, Monster2, Monster3, Monster4

## Anvil.API.SpellRange  [enum]
- values: Unknown, Personal, Touch, Short, Medium, Long

## Anvil.API.SpellTargetTypes  [enum]
- values: Unknown, Self, Creature, Area, Item, Door, Placeable, Trigger

## Anvil.API.SpellUserType  [enum]
- values: Unknown, Spells, CreaturePower, Feats, ItemPower

## Anvil.API.ScriptParams  [class]
- string this[string paramName]
- bool IsSet(string paramName)

## Anvil.API.DebugOptions  [class]
- bool EnableCombatDebugging
- bool EnableHitDieDebugging
- bool EnableMovementSpeedDebugging
- bool EnableSavingThrowDebugging

## Anvil.API.JoiningRestrictions  [class]
- bool AllowLocalVaultCharacters
- int MaxLevel
- int MinLevel

## Anvil.API.NwServer  [class]
- static NwServer Instance
- NwServer()
- string BannedList
- bool DebugMode
- bool DebugCombat
- bool DebugSaveThrows
- bool DebugHitDie
- bool DebugMoveSpeed
- string DMPassword
- bool IsActivePaused
- bool IsTimestopPaused
- string PlayerPassword
- ServerInfo ServerInfo
- Version ServerVersion
- string UserDirectory
- WorldTimer WorldTimer
- void AddBannedCDKey(string cdKey)
- void AddBannedIP(string ip)
- void AddBannedPlayerName(string playerName)
- bool DeletePlayerTURD(string playerId, string characterName)
- string GetAliasPath(string alias)
- void RemoveBannedCDKey(string cdKey)
- void RemoveBannedIP(string ip)
- void RemoveBannedPlayer(string playerName)
- void ShutdownServer()

## Anvil.API.PersistentWorldOptions  [class]
- bool SaveCharactersInSaveGame
- bool ServerVaultByPlayerName
- bool StickyPlayerNames
- bool SuppressBaseServerVault
- bool VaultCharactersOnly

## Anvil.API.PlayOptions  [class]
- bool AllKillable
- bool AutoFailSaveOn1
- bool BackupSavedCharacters
- bool CdKeyBanlistAllowlist
- bool DisallowShouting
- bool EnforceLegalCharacters
- bool ExamineChallengeRating
- bool ExamineEffects
- bool HideHitpointsGained
- bool ItemLevelRestrictions
- bool LoseExp
- int LoseExpNum
- bool LoseGold
- int LoseGoldNum
- bool LoseItems
- int LoseItemsNum
- bool LoseStolenItems
- bool NonPartyKillable
- bool OnePartyOnly
- bool PauseAndPlay
- bool PlayerPartyControl
- PvPSetting PvPSetting
- bool RequireResurrection
- bool ResetEncounterSpawnPool
- bool RestoreSpellUses
- bool ShowDMJoinMessage
- bool UseMaxHPOnLevelUp
- bool ValidateSpells

## Anvil.API.ServerInfo  [class]
- DebugOptions DebugOptions
- JoiningRestrictions JoiningRestrictions
- string ModuleName
- PersistentWorldOptions PersistentWorldOptions
- PlayOptions PlayOptions
- string ServerName

## Anvil.API.NwDateTime  [struct]
- const int DaysInMonth = 28
- const long TicksPerDay = TicksPerHour * 24
- const long TicksPerHour = TicksPerMinute * 60
- const long TicksPerMillisecond = 1
- const long TicksPerMinute = TicksPerSecond * 60
- const long TicksPerMonth = TicksPerDay * 28
- const long TicksPerSecond = TicksPerMillisecond * 1000
- const long TicksPerYear = TicksPerMonth * 12
- static readonly NwDateTime MaxDate = new NwDateTime(GetTicks(30001)).AddMilliseconds(-1)
- static readonly NwDateTime MinDate = new NwDateTime(GetTicks())
- static NwDateTime Now
- static NwDateTime Today
- readonly long Ticks
- NwDateTime(int year = 0, int month = 1, int day = 1, int hour = 0, int minute = 0, int second = 0, int milliSecond = 0)
- NwDateTime Date
- int DayInMonth
- int DayInTenday
- int DayInYear
- int Hour
- int Millisecond
- int Minute
- int Month
- int Second
- int Year
- static NwDateTime FromTicks(long ticks)
- static implicit operator long(NwDateTime dateTime)
- NwDateTime Add(int value, long scale)
- NwDateTime AddDays(int days)
- NwDateTime AddHours(int hours)
- NwDateTime AddMilliseconds(int milliseconds)
- NwDateTime AddMinutes(int minutes)
- NwDateTime AddMonths(int months)
- NwDateTime AddSeconds(int seconds)
- NwDateTime AddYears(int years)
- override string ToString()

## Anvil.API.NwTimeSpan  [class]
- static TimeSpan FromHours(int hours)
- static TimeSpan FromRounds(int rounds)
- static TimeSpan FromTurns(int turns)

## Anvil.API.Time  [class]
- static TimeSpan DeltaTime
- static TimeSpan TimeSinceStartup
- Service()
- void Update()

## Anvil.API.VisualTransform  [class]
- float AnimSpeed
- Vector3 Rotation
- float Scale
- Vector3 Translation
- void Copy(VisualTransform other)
- void Lerp(VisualTransformLerpSettings settings, Action<VisualTransform> transforms)
- void Clear()

## Anvil.API.VisualTransformLerpSettings  [class]
- TimeSpan Duration
- VisualTransformLerpType LerpType
- bool PauseWithGame
- bool ReturnDestinationTransform
- ObjectVisualTransformBehavior BehaviorFlags
- int Repeats

## Anvil.API.ITwoDimArrayEntry  [interface]

## Anvil.API.AppearanceTableEntry  [class]
- bool? AbortOnParry
- int? AppearanceSoundSet
- string? BloodColor
- BodyBagTableEntry? BodyBag
- float? CreaturePersonalSpace
- string? EnvironmentMap
- int? FootstepType
- bool? HasArms
- bool? HasLegs
- int? HeadArcHorizontal
- int? HeadArcVertical
- string? HeadName
- bool? HeadTrack
- float? Height
- float? HelmetScaleF
- float? HelmetScaleM
- float? HitDistance
- string? Label
- string? ModelType
- string? MovementRate
- string? Name
- int? PerceptionDistance
- float? PersonalSpace
- string? Portrait
- float? PreferredAttackDistance
- string? Race
- int? RacialType
- int RowIndex
- float? RunDistance
- int? SizeCategory
- StrRef? StrRef
- bool? Targetable
- string? TargetHeight
- float? WalkDistance
- float? WeaponScale
- float? WingTailScale
- static implicit operator AppearanceTableEntry(AppearanceType appearanceType)

## Anvil.API.ArmorTableEntry  [class]
- int RowIndex
- int? ACBonus
- int? DexBonus
- int? ACCheck
- int? ArcaneFailurePct
- int? Weight
- int? Cost
- StrRef? Description
- StrRef? BaseItemStats
- void InterpretEntry(TwoDimArrayEntry entry)

## Anvil.API.BodyBagTableEntry  [class]
- PlaceableTableEntry? Appearance
- string? Label
- StrRef? Name
- int RowIndex

## Anvil.API.ClassPreReqTableEntry  [class]
- string? Label
- ClassPreReqType? ReqType
- string? ReqParam1
- string? ReqParam2
- int RowIndex

## Anvil.API.ClassPreReqType  [enum]
- values: ArcSpell, Bab, ClassOr, ClassNot, Feat, FeatOr, Race, Save, Skill, Spell, Var

## Anvil.API.DamageLevelEntry  [class]
- string? Label
- int RowIndex
- StrRef? StrRef
- void InterpretEntry(TwoDimArrayEntry entry)

## Anvil.API.EffectIconTableEntry  [class]
- int RowIndex
- string? Label
- StrRef? StrRef
- string? Icon
- void InterpretEntry(TwoDimArrayEntry entry)
- static implicit operator EffectIconTableEntry(EffectIcon effectIcon)

## Anvil.API.EnvironmentPreset  [class]
- DayNightMode DayNightMode
- float FogClipDistance
- string? Label
- int? LightningChance
- int? Main1Color1
- int? Main1Color2
- int? Main1Color3
- int? Main1Color4
- int? Main2Color1
- int? Main2Color2
- int? Main2Color3
- int? Main2Color4
- Color MoonAmbientColor
- Color MoonDiffuseColor
- int? MoonFogAmount
- Color MoonFogColor
- bool? MoonShadows
- int? RainChance
- int RowIndex
- int? SecondaryColor1
- int? SecondaryColor2
- int? SecondaryColor3
- int? SecondaryColor4
- float? ShadowAlpha
- int? SnowChance
- StrRef? StrRef
- Color SunAmbientColor
- Color SunDiffuseColor
- int? SunFogAmount
- Color SunFogColor
- bool? SunShadows
- int? WindPower

## Anvil.API.ExpTableEntry  [class]
- int? Level
- int RowIndex
- uint? XP
- void InterpretEntry(TwoDimArrayEntry entry)

## Anvil.API.ExpTableExtensions  [class]
- static int? GetLevelFromXP(this TwoDimArray<ExpTableEntry> table, int xp)
- static uint? GetXPFromLevel(this TwoDimArray<ExpTableEntry> table, int level)

## Anvil.API.ItemPropertyCostTableEntry  [class]
- int RowIndex
- StrRef? Name
- string? Label
- float? Cost

## Anvil.API.ItemPropertyCostTablesEntry  [class]
- int RowIndex
- TwoDimArray<ItemPropertyCostTableEntry>? Table
- string? TableResRef
- string? Label
- bool? ClientLoad
- void InterpretEntry(TwoDimArrayEntry entry)

## Anvil.API.ItemPropertyItemMapTableEntry  [class]
- IReadOnlyDictionary<NwBaseItem, bool> ValidItems
- StrRef? StrRef
- string? Label
- int RowIndex
- bool IsItemPropertyValidForItem(NwItem item)
- bool IsItemPropertyValidForItem(NwBaseItem item)

## Anvil.API.ItemPropertyParamTableEntry  [class]
- int RowIndex
- StrRef? Name
- string? Label

## Anvil.API.ItemPropertyParamTablesEntry  [class]
- int RowIndex
- StrRef? Name
- string? Label
- TwoDimArray<ItemPropertyParamTableEntry>? Table
- string? TableResRef

## Anvil.API.ItemPropertySubTypeTableEntry  [class]
- int RowIndex
- StrRef? Name
- string? Label

## Anvil.API.ItemPropertyTableEntry  [class]
- int RowIndex
- ItemPropertyItemMapTableEntry? ItemMap
- StrRef? Name
- string? Label
- TwoDimArray<ItemPropertySubTypeTableEntry>? SubTypeTable
- float? Cost
- TwoDimArray<ItemPropertyCostTableEntry>? CostTable
- TwoDimArray<ItemPropertyParamTableEntry>? Param1Table
- StrRef? GameStrRef
- StrRef? Description
- ItemPropertyType PropertyType
- static implicit operator ItemPropertyTableEntry(ItemPropertyType propertyType)

## Anvil.API.LightColorTableEntry  [class]
- float? Blue
- float? Green
- string? Label
- float? Red
- int RowIndex
- float? ToolsetBlue
- float? ToolsetGreen
- float? ToolsetRed

## Anvil.API.LoadScreenTableEntry  [class]
- int RowIndex
- string? Label
- string? ScriptingName
- string? BMPResRef
- string? TileSet
- StrRef? StrRef
- void InterpretEntry(TwoDimArrayEntry entry)

## Anvil.API.NwGameTables  [class]
- static TwoDimArray<T>? GetTable<T>(string? twoDimArrayName, bool useCache = true, bool checkCacheType = true) where T : class, ITwoDimArrayEntry, new()
- static TwoDimArray? GetTable(string twoDimArrayName)
- Factory(HookService hookService)
- void Dispose()
- static TwoDimArray<AppearanceTableEntry> AppearanceTable
- static TwoDimArray<ArmorTableEntry> ArmorTable
- static TwoDimArray<BodyBagTableEntry> BodyBagTable
- static TwoDimArray<DamageLevelEntry> DamageLevelTable
- static TwoDimArray<EffectIconTableEntry> EffectIconTable
- static TwoDimArray<EnvironmentPreset> EnvironmentPresetTable
- static TwoDimArray<ExpTableEntry> ExpTable
- static TwoDimArray<LightColorTableEntry> LightColorTable
- static TwoDimArray<LoadScreenTableEntry> LoadScreenTable
- static TwoDimArray<PartsTableEntry> PartsBeltTable
- static TwoDimArray<PartsTableEntry> PartsBicepTable
- static TwoDimArray<PartsTableEntry> PartsChestTable
- static TwoDimArray<PartsTableEntry> PartsFootTable
- static TwoDimArray<PartsTableEntry> PartsForearmTable
- static TwoDimArray<PartsTableEntry> PartsHandTable
- static TwoDimArray<PartsTableEntry> PartsLegTable
- static TwoDimArray<PartsTableEntry> PartsNeckTable
- static TwoDimArray<PartsTableEntry> PartsPelvisTable
- static TwoDimArray<PartsTableEntry> PartsRobeTable
- static TwoDimArray<PartsTableEntry> PartsShinTable
- static TwoDimArray<PartsTableEntry> PartsShoulderTable
- static TwoDimArray<PlaceableSoundTableEntry> PlaceableSoundTable
- static TwoDimArray<PlaceableTableEntry> PlaceableTable
- static TwoDimArray<PlaceableTypeTableEntry> PlaceableTypeTable
- static TwoDimArray<PolymorphTableEntry> PolymorphTable
- static TwoDimArray<PortraitTableEntry> PortraitTable
- static TwoDimArray<ProgrammedEffectTableEntry> ProgrammedEffectTable
- static TwoDimArray<PersistentVfxTableEntry> PersistentEffectTable
- static TwoDimArray<SkillItemCostTableEntry> SkillItemCostTable
- static TwoDimArray<SurfaceMaterialTableEntry> SurfaceMaterialTable
- static TwoDimArray<VisualEffectTableEntry> VisualEffectTable
- static TwoDimArray<ItemPropertyItemMapTableEntry> ItemPropertyItemMapTable
- static TwoDimArray<ItemPropertyTableEntry> ItemPropertyTable
- static TwoDimArray<ItemPropertyCostTablesEntry> ItemPropertyCostTables
- static TwoDimArray<ItemPropertyParamTablesEntry> ItemPropertyParamTables

## Anvil.API.PartsTableEntry  [class]
- int RowIndex
- int? CostModifier
- float? ACBonus
- ArmorTableEntry? ArmorTableEntry
- void InterpretEntry(TwoDimArrayEntry entry)

## Anvil.API.PersistentVfxTableEntry  [class]
- int RowIndex
- string? Label
- string? Shape
- float? Radius
- float? Width
- float? Length
- string? OnEnter
- string? OnExit
- string? OnHeartbeat
- bool? OrientWithGround
- VisualEffectTableEntry? DurationVfx
- string? Model01
- string? Model02
- string? Model03
- int? NumAct01
- int? NumAct02
- int? NumAct03
- TimeSpan? Duration01
- TimeSpan? Duration02
- TimeSpan? Duration03
- float? EdgeWeight01
- float? EdgeWeight02
- float? EdgeWeight03
- string? SoundImpact
- string? SoundDuration
- string? SoundCessation
- string? SoundOneShot
- float? SoundOneShotPercentage
- string? ModelMin01
- string? ModelMin02
- string? ModelMin03
- void InterpretEntry(TwoDimArrayEntry entry)
- static implicit operator PersistentVfxTableEntry(PersistentVfxType vfxType)

## Anvil.API.PlaceableSoundTableEntry  [class]
- string? ArmorType
- string? Closed
- string? Destroyed
- string? Label
- string? Locked
- string? Opened
- int RowIndex
- string? Used

## Anvil.API.PlaceableTableEntry  [class]
- bool? HasBodyBag
- string? Label
- LightColorTableEntry? LightColor
- Vector3? LightOffset
- string? LowGore
- string? ModelName
- string? Reflection
- int RowIndex
- ShadowSize? ShadowSize
- PlaceableSoundTableEntry? SoundType
- bool? StaticAllowed
- StrRef? StrRef

## Anvil.API.PlaceableTypeTableEntry  [class]
- int RowIndex
- string? Label
- StrRef? StrRef
- void InterpretEntry(TwoDimArrayEntry entry)

## Anvil.API.PolymorphTableEntry  [class]
- int RowIndex
- string? Name
- AppearanceTableEntry? AppearanceType
- NwRace? RacialType
- PortraitTableEntry? PortraitId
- string? PortraitCustom
- string? CreatureWeapon1
- string? CreatureWeapon2
- string? CreatureWeapon3
- string? CreatureHideItem
- string? EquippedItem
- int? Strength
- int? Constitution
- int? Dexterity
- int? NaturalAcBonus
- int? HpBonus
- NwSpell? Spell1
- NwSpell? Spell2
- NwSpell? Spell3
- bool? MergeW
- bool? MergeI
- bool? MergeA
- void InterpretEntry(TwoDimArrayEntry entry)
- static implicit operator PolymorphTableEntry(PolymorphType polymorphType)

## Anvil.API.PortraitTableEntry  [class]
- int RowIndex
- string? BaseResRef
- Gender? Gender
- NwRace? Race
- PlaceableTypeTableEntry? InanimateType
- bool? Plot
- string? BaseResRefLowGore
- void InterpretEntry(TwoDimArrayEntry entry)

## Anvil.API.ProgFxType  [enum]
- values: Unknown, SkinOverlay, EnvironmentMap, StaticGlow, Light, AlphaTransparency, PulsingAura, Beam, DisableRender, ChunkModel, Mirv, MirvVariant, SpellCastFailure, Freeze

## Anvil.API.ProgrammedEffectTableEntry  [class]
- string? Label
- int RowIndex
- ProgFxType? Type
- float? GetParamFloat(int param)
- int? GetParamInt(int param)
- string? GetParamString(int param)
- void InterpretEntry(TwoDimArrayEntry entry)
- static implicit operator ProgrammedEffectTableEntry(ProgFxType fxType)

## Anvil.API.ShadowSize  [enum]
- values: Small, Medium, Large

## Anvil.API.ShakeType  [enum]
- values: None, ShakeOnce, ShakeDuration

## Anvil.API.SkillItemCostTableEntry  [class]
- int? AlignmentSkillRequirement
- int? ClassSkillRequirement
- int? DeviceCostMax
- int? RaceSkillRequirement
- int RowIndex
- void InterpretEntry(TwoDimArrayEntry entry)

## Anvil.API.SurfaceMaterialTableEntry  [class]
- string? Label
- bool? Walk
- bool? WalkCheck
- bool? LineOfSight
- string? Sound
- string? Name
- bool? IsWater
- string? Visual
- string?[] ActionStrRefs
- string?[] ActionIcons
- int RowIndex
- void InterpretEntry(TwoDimArrayEntry entry)

## Anvil.API.VisualEffectTableEntry  [class]
- string? CesHeadConNode
- string? CesImpactNode
- string? CesRootHugeNode
- string? CesRootLargeNode
- string? CesRootMediumNode
- string? CesRootSmallNode
- string? ImpHeadConNode
- string? ImpImpactNode
- string? ImpRootHugeNode
- string? ImpRootLargeNode
- string? ImpRootMediumNode
- string? ImpRootSmallNode
- string? Label
- string? LowQualityVariant
- string? LowViolenceVariant
- bool? OrientWithGround
- bool? OrientWithObject
- ProgrammedEffectTableEntry? ProgFxCessastion
- ProgrammedEffectTableEntry? ProgFxDuration
- ProgrammedEffectTableEntry? ProgFxImpact
- int RowIndex
- float? ShakeDelay
- float? ShakeDuration
- ShakeType? ShakeType
- string? SoundCessastion
- string? SoundDuration
- string? SoundImpact
- string? TypeFd
- static implicit operator VisualEffectTableEntry(VfxType vfxType)

## Anvil.API.TwoDimArray  [class]
- int ColumnCount
- string[] Columns
- int RowCount
- bool? GetBool(int rowIndex, string columnName)
- bool? GetBool(int rowIndex, int columnIndex)
- int GetColumnIndex(string columnName)
- T? GetEnum<T>(int rowIndex, string columnName) where T : struct, Enum
- T? GetEnum<T>(int rowIndex, int columnIndex) where T : struct, Enum
- float? GetFloat(int rowIndex, string columnName)
- float? GetFloat(int rowIndex, int columnIndex)
- int? GetInt(int rowIndex, string columnName)
- int? GetInt(int rowIndex, int columnIndex)
- string? GetString(int rowIndex, string columnName)
- string? GetString(int rowIndex, int columnIndex)
- StrRef? GetStrRef(int rowIndex, string columnName)
- StrRef? GetStrRef(int rowIndex, int columnIndex)
- T? GetTableEntry<T>(int rowIndex, string columnName, TwoDimArray<T> table) where T : class, ITwoDimArrayEntry, new()
- T? GetTableEntry<T>(int rowIndex, int columnIndex, TwoDimArray<T> table) where T : class, ITwoDimArrayEntry, new()
- TwoDimArray<T>? GetTable<T>(int rowIndex, string columnName) where T : class, ITwoDimArrayEntry, new()
- TwoDimArray<T>? GetTable<T>(int rowIndex, int columnIndex) where T : class, ITwoDimArrayEntry, new()
- Vector3? GetVector3(int rowIndex, string columnNameX, string columnNameY, string columnNameZ)
- Vector3? GetVector3(int rowIndex, int columnIndexX, int columnIndexY, int columnIndexZ)

## Anvil.API.TwoDimArrayEntry  [class]
- int ColumnCount
- string[] Columns
- bool? GetBool(string columnName)
- bool? GetBool(int columnIndex)
- T? GetEnum<T>(string columnName) where T : struct, Enum
- T? GetEnum<T>(int columnIndex) where T : struct, Enum
- float? GetFloat(string columnName)
- float? GetFloat(int columnIndex)
- int? GetInt(string columnName)
- int? GetInt(int columnIndex)
- string? GetString(string columnName)
- string? GetString(int columnIndex)
- StrRef? GetStrRef(string columnName)
- StrRef? GetStrRef(int columnIndex)
- T? GetTableEntry<T>(string columnName, TwoDimArray<T> table) where T : class, ITwoDimArrayEntry, new()
- T? GetTableEntry<T>(int columnIndex, TwoDimArray<T> table) where T : class, ITwoDimArrayEntry, new()
- TwoDimArray<T>? GetTable<T>(string columnName) where T : class, ITwoDimArrayEntry, new()
- TwoDimArray<T>? GetTable<T>(int columnIndex) where T : class, ITwoDimArrayEntry, new()
- Vector3? GetVector3(string columnNameX, string columnNameY, string columnNameZ)
- Vector3? GetVector3(int columnIndexX, int columnIndexY, int columnIndexZ)

## Anvil.API.TwoDimArray<T>  [class]
- int Count
- IReadOnlyList<T> Rows
- T this[int rowIndex]
- IEnumerator<T> GetEnumerator()
- T GetRow(int rowIndex)

## Anvil.API.JsonUtility  [class]
- static T? FromJson<T>(string json)
- static string ToJson<T>(T value)

## Anvil.API.NativeUtils  [class]
- static bool CreateFromResRef(ResRefType resRefType, string resRef, Action<CResGFF, CResStruct> deserializeAction)
- static bool DeserializeGff(byte[] serialized, Func<CResGFF, CResStruct, bool> deserializeAction)
- static string ExtractLocString(this CExoLocString locStr, int nID = 0, byte gender = 0)
- static bool IsValidGff(this CResGFF resGff, string expectedFileType, string expectedVersion = DefaultGffVersion)
- static bool IsValidGff(this CResGFF resGff, IEnumerable<string> expectedFileTypes, IEnumerable<string> expectedVersions)
- static byte[]? SerializeGff(string fileType, string version, Func<CResGFF, CResStruct, bool> serializeAction)
- static byte[]? SerializeGff(string fileType, Func<CResGFF, CResStruct, bool> serializeAction)
- static Color ToColor(this Vector vector)
- static CExoLocString ToExoLocString(this string? str, int nId = 0, byte gender = 0)
- static CExoLocString ToExoLocString(this CExoString str, int nId = 0, byte gender = 0)
- static CExoString ToExoString(this string? str)
- static Vector3 ToManagedVector(this Vector vector)
- static Vector ToNativeVector(this Vector3 vector)
- static Vector ToNativeVector(this Color color)
- static CResRef ToResRef(this string? str)
- static Vector3 ToVectorOrientation(this float facing)

## Anvil.API.VirtualMachine  [class]
- EventScriptType CurrentRunningEvent
- uint InstructionLimit
- uint InstructionsExecuted
- bool IsInScriptContext
- int RecursionLevel
- bool ScriptReturnValue
- void Execute(string scriptName, NwObject? target, params (string ParamName, string ParamValue)[] scriptParams)
- void Execute(string scriptName, params (string ParamName, string ParamValue)[] scriptParams)
- void ExecuteInScriptContext(System.Action action, uint objectId = NwObject.Invalid, int scriptEventId = 0)
- T ExecuteInScriptContext<T>(Func<T> action, uint objectId = NwObject.Invalid, int scriptEventId = 0)
- string? GetCurrentScriptName(int depth = 0)

## Anvil.API.CampaignVariableBool  [class]
- override bool Value

## Anvil.API.CampaignVariableEnum<T>  [class]
- CampaignVariableEnum()
- override T Value

## Anvil.API.CampaignVariableFloat  [class]
- override float Value

## Anvil.API.CampaignVariableGuid  [class]
- override Guid Value

## Anvil.API.CampaignVariableInt  [class]
- override int Value

## Anvil.API.CampaignVariableLocation  [class]
- override Location? Value

## Anvil.API.CampaignVariableObject<T>  [class]
- override T Value
- T? GetValue(Location location)
- T? GetValue(NwGameObject owner)

## Anvil.API.CampaignVariableString  [class]
- override string Value

## Anvil.API.CampaignVariableVector  [class]
- override Vector3 Value

## Anvil.API.CampaignVariable  [class]
- string Campaign
- string Name
- NwPlayer? Player
- abstract void Delete()

## Anvil.API.CampaignVariable<T>  [class]
- abstract T Value
- static implicit operator T(CampaignVariable<T> value)
- override void Delete()
- bool Equals(CampaignVariable<T>? other)
- override bool Equals(object? obj)
- override int GetHashCode()
- static bool operator ==(CampaignVariable<T>? left, CampaignVariable<T>? right)
- static bool operator !=(CampaignVariable<T>? left, CampaignVariable<T>? right)

## Anvil.API.LocalVariable<T>  [class]
- override bool HasValue

## Anvil.API.LocalVariableBool  [class]
- override bool Value
- override void Delete()

## Anvil.API.LocalVariableCassowary  [class]
- override Cassowary? Value
- override void Delete()

## Anvil.API.LocalVariableEnum<T>  [class]
- LocalVariableEnum()
- override T Value
- override void Delete()

## Anvil.API.LocalVariableFloat  [class]
- override float Value
- override void Delete()

## Anvil.API.LocalVariableGuid  [class]
- override Guid Value
- override void Delete()

## Anvil.API.LocalVariableInt  [class]
- override int Value
- override void Delete()

## Anvil.API.LocalVariableLocation  [class]
- override Location? Value
- override void Delete()

## Anvil.API.LocalVariableObject<T>  [class]
- override T? Value
- override void Delete()

## Anvil.API.LocalVariableString  [class]
- override string? Value
- override void Delete()

## Anvil.API.LocalVariableStruct<T>  [class]
- override T? Value
- override void Delete()

## Anvil.API.ObjectStorageVariable<T>  [class]

## Anvil.API.ObjectStorageVariableBool  [class]
- sealed override bool HasValue
- sealed override bool Value
- sealed override void Delete()

## Anvil.API.PersistentVariableBool  [class]

## Anvil.API.ObjectStorageVariableEnum<T>  [class]
- sealed override bool HasValue
- sealed override T Value
- sealed override void Delete()

## Anvil.API.PersistentVariableEnum<T>  [class]

## Anvil.API.ObjectStorageVariableFloat  [class]
- sealed override bool HasValue
- sealed override float Value
- sealed override void Delete()

## Anvil.API.PersistentVariableFloat  [class]

## Anvil.API.ObjectStorageVariableGuid  [class]
- sealed override bool HasValue
- sealed override Guid Value
- sealed override void Delete()

## Anvil.API.PersistentVariableGuid  [class]

## Anvil.API.ObjectStorageVariableInt  [class]
- sealed override bool HasValue
- sealed override int Value
- sealed override void Delete()

## Anvil.API.PersistentVariableInt  [class]

## Anvil.API.ObjectStorageVariableString  [class]
- sealed override bool HasValue
- sealed override string? Value
- sealed override void Delete()

## Anvil.API.PersistentVariableString  [class]

## Anvil.API.ObjectStorageVariableStruct<T>  [class]
- sealed override bool HasValue
- sealed override T? Value
- sealed override void Delete()

## Anvil.API.PersistentVariableStruct<T>  [class]

## Anvil.API.ObjectVariable  [class]
- bool HasNothing
- abstract bool HasValue
- string Name
- NwObject Object
- abstract void Delete()

## Anvil.API.ObjectVariable<T>  [class]
- abstract T? Value
- static bool operator ==(ObjectVariable<T> left, ObjectVariable<T> right)
- static implicit operator T?(ObjectVariable<T> value)
- static bool operator !=(ObjectVariable<T> left, ObjectVariable<T> right)
- bool Equals(ObjectVariable<T>? other)
- override bool Equals(object? obj)
- override int GetHashCode()

## Anvil.AnvilCore  [class]
- string? AssemblyName
- string? AssemblyVersion
- string? CoreVersion
- string? NativeVersion
- string? NWNXDotNetVersion
- static T? GetService<T>()
- static void Reload()

## Anvil.IArray<T>  [interface]

## Anvil.Plugins.Plugin  [class]
- AssemblyName Name
- string Path
- PluginInfoAttribute PluginInfo
- string? ResourcePath
- Assembly? Assembly
- IReadOnlyList<Type>? PluginTypes
- bool Loading
- bool IsLoaded

## Anvil.Plugins.PluginInfoAttribute  [class]
- string[] OptionalDependencies
- bool Isolated

## Anvil.Plugins.PluginManager  [class]
- string? GetPluginDirectory(Assembly pluginAssembly)
- bool IsPluginAssembly(Assembly assembly)
- bool IsPluginLoaded(string pluginName)
- Plugin? GetPlugin(string pluginName)
- Plugin? GetPlugin(Assembly assembly)
- Plugin LoadPlugin(string pluginRoot)
- WeakReference UnloadPlugin(Plugin plugin, bool waitForUnload = true)

## Anvil.Services.OverrideNameType  [enum]
- values: Original, Character, Player

## Anvil.Services.PlayerNameOverrideService  [class]
- PlayerNameOverrideService(HookService hookService)
- bool OverwriteDisplayName
- OverrideNameType PlayerListNameType
- bool ShowOverridesToDM
- void ClearPlayerNameOverride(NwPlayer target, bool clearAll = false)
- void ClearPlayerNameOverride(NwPlayer target, NwPlayer observer)
- Dictionary<NwPlayer, PlayerNameOverride> GetOverridesForObserver(NwPlayer observer, bool includeGlobal = false)
- PlayerNameOverride? GetPlayerNameOverride(NwPlayer? target, NwPlayer? observer = null)
- void SetPlayerNameOverride(NwPlayer target, PlayerNameOverride nameOverride)
- void SetPlayerNameOverride(NwPlayer target, PlayerNameOverride nameOverride, NwPlayer observer)

## Anvil.Services.VisibilityMode  [enum]
- values: Default, Visible, Hidden, DMOnly, AlwaysVisible, AlwaysVisibleDMOnly

## Anvil.Services.ChatChannel  [enum]
- values: PlayerTalk, PlayerShout, PlayerWhisper, PlayerTell, ServerMessage, PlayerParty, PlayerDm, DmTalk, DmShout, DmWhisper, DmTell, DmParty, DmDm

## Anvil.Services.ChatService  [class]
- ChatService(HookService hookService)
- void ClearPlayerChatHearingDistance(NwPlayer player, ChatChannel chatChannel)
- void ClearPlayerChatHearingDistance(NwPlayer player)
- float GetChatHearingDistance(ChatChannel chatChannel)
- float GetPlayerChatHearingDistance(NwPlayer player, ChatChannel chatChannel)
- bool SendMessage(ChatChannel chatChannel, string message, NwCreature sender, NwPlayer? target = null)
- bool SendServerMessage(ChatChannel chatChannel, string message, NwPlayer? target = null)
- void SetChatHearingDistance(ChatChannel chatChannel, float distance)
- void SetPlayerChatHearingDistance(NwPlayer player, ChatChannel chatChannel, float distance)

## Anvil.Services.EncodingService  [class]
- Encoding Encoding

## Anvil.Services.FunctionHook<T>  [class]
- T CallOriginal
- void Dispose()

## Anvil.Services.HookOrder  [class]
- const int Default = 0
- const int Earliest = -3000000
- const int Early = -1000000
- const int Final = int.MaxValue
- const int Late = 1000000
- const int Latest = 3000000
- const int SharedHook = int.MinValue
- const int VeryEarly = -2000000
- const int VeryLate = 2000000

## Anvil.Services.HookService  [class]
- FunctionHook<T> RequestHook<T>(T handler, int order = HookOrder.Default) where T : Delegate
- FunctionHook<T> RequestHook<T>(void* handler, int order = HookOrder.Default) where T : Delegate

## Anvil.Services.NativeFunctionAttribute  [class]
- string GccExportName
- string MsvcExportName
- IntPtr Address
- NativeFunctionAttribute(string gccExportName, string msvcExportName)

## Anvil.Services.TargetModeSettings  [class]
- ObjectTypes ValidTargets
- MouseCursor CursorType
- MouseCursor BadCursorType
- TargetingData? TargetingData

## Anvil.Services.TargetingData  [class]
- SpellTargetingShape Shape
- SpellTargetingFlags Flags
- NwSpell? Spell
- NwFeat? Feat
- Vector2 Size
- float Range

## Anvil.Services.DialogService  [class]
- DialogService(HookService hookService)
- uint? CurrentNodeId
- int CurrentNodeIndex
- NodeType CurrentNodeType
- ScriptType CurrentScriptType
- string? GetCurrentNodeText(Language language = Language.English, Gender gender = Gender.Male)
- void SetCurrentNodeText(string text, Language language = Language.English, Gender gender = Gender.Male)

## Anvil.Services.DialogState  [enum]
- values: Invalid, Start, SendEntry, SendReplies, HandleReply

## Anvil.Services.Language  [enum]
- values: English, French, German, Italian, Spanish, Polish, Korean, ChineseTraditional, ChineseSimplified, Japanese

## Anvil.Services.NodeType  [enum]
- values: Invalid, StartingNode, EntryNode, ReplyNode

## Anvil.Services.ScriptType  [enum]
- values: Other, StartingConditional, ActionTaken

## Anvil.Services.EnforceLegalCharacterService  [class]
- EnforceLegalCharacterService(VirtualMachine virtualMachine, HookService hookService)
- event Action<OnELCCustomCheck>? OnCustomCheck
- event Action<OnELCValidationBefore>? OnValidationBefore
- event Action<OnELCValidationFailure>? OnValidationFailure
- event Action<OnELCValidationSuccess>? OnValidationSuccess
- bool EnforceDefaultEventScripts
- bool EnforceEmptyDialog
- void Dispose()

## Anvil.Services.OnELCCustomCheck  [class]
- bool IsFailed
- NwPlayer Player

## Anvil.Services.OnELCValidationBefore  [class]
- NwPlayer Player

## Anvil.Services.OnELCValidationFailure  [class]
- bool IgnoreFailure
- NwPlayer Player
- StrRef StrRef
- ValidationFailureSubType SubType
- ValidationFailureType Type

## Anvil.Services.OnELCItemValidationFailure  [class]
- NwItem Item

## Anvil.Services.OnELCLevelValidationFailure  [class]
- int Level

## Anvil.Services.OnELCSkillValidationFailure  [class]
- NwSkill? Skill

## Anvil.Services.OnELCFeatValidationFailure  [class]
- NwFeat? Feat

## Anvil.Services.OnELCSpellValidationFailure  [class]
- NwSpell? Spell

## Anvil.Services.OnELCValidationSuccess  [class]
- NwPlayer Player

## Anvil.Services.ValidationFailureSubType  [enum]
- values: None, ServerLevelRestriction, LevelHack, ColoredName, UnidentifiedEquippedItem, MinEquipLevel, NonPCCharacter, DMCharacter, NonPlayerRace, NonPlayerClass, ClassLevelRestriction, PrestigeClassRequirements, ClassAlignmentRestriction, StartingAbilityValueMax, AbilityPointBuySystemCalculation, ClassSpellcasterInvalidPrimaryStat, EpicLevelFlag, TooManyHitPoints, UnusableSkill, NotEnoughSkillPoints, InvalidNumRanksInClassSkill, InvalidNumRanksInNonClassSkill, InvalidNumRemainingSkillPoints, InvalidFeat, FeatRequiredSpellLevelNotMet, FeatRequiredBaseAttackBonusNotMet, FeatRequiredAbilityValueNotMet, FeatRequiredSkillNotMet, FeatRequiredFeatNotMet, TooManyFeatsThisLevel, FeatNotAvailableToClass, FeatIsNormalFeatOnly, FeatIsBonusFeatOnly, SpellInvalidSpellGainWizard, SpellInvalidSpellGainBardSorcerer, SpellInvalidSpellGainOtherClasses, InvalidSpell, SpellInvalidSpellLevel, SpellMinimumAbilityBardSorcererUnused, SpellMinimumAbilityWizardUnused, SpellMinimumAbility, SpellRestrictedSpellSchool, SpellAlreadyKnown, SpellWizardExceedsNumSpellsToAdd, IllegalRemovedSpell, RemovedNotKnownSpell, InvalidNumSpells, SpellListComparison, SkillListComparison, FeatListComparison, MiscSavingThrow, NumFeatComparison, InvalidClass, NumMulticlass

## Anvil.Services.ValidationFailureType  [enum]
- values: None, Character, Item, Skill, Feat, Spell, Custom

## Anvil.Services.EventCallbackType  [enum]
- values: Before, After

## Anvil.Services.EventService  [class]
- abstract void ClearObjectSubscriptions(NwObject gameObject)
- abstract void ProcessEvent(IEvent eventData, EventCallbackType eventCallbackType)
- readonly Dictionary<NwObject, Action<T>> FilteredCallbacks = new Dictionary<NwObject, Action<T>>()
- Action<T>? GlobalCallback
- bool HasSubscribers
- override void ClearObjectSubscriptions(NwObject gameObject)
- override void ProcessEvent(IEvent eventData, EventCallbackType eventCallbackType)
- void Subscribe(NwObject obj, Action<T> newHandler, EventCallbackType eventCallbackType)
- void SubscribeAll(Action<T> newHandler, EventCallbackType eventCallbackType)
- void Unsubscribe(NwObject obj, Action<T> handlerToRemove, EventCallbackType eventCallbackType)
- void UnsubscribeAll(Action<T> handlerToRemove, EventCallbackType eventCallbackType)
- EventService(IEnumerable<IEventFactory> eventFactories)
- void ClearObjectSubscriptions(NwObject? nwObject)
- TEvent ProcessEvent<TEvent>(EventCallbackType eventCallbackType, TEvent eventData)
- void Subscribe<TEvent, TFactory>(NwObject? nwObject, Action<TEvent> handler, EventCallbackType eventCallbackType = EventCallbackType.Before)
- void Subscribe<TEvent, TFactory, TRegData>(NwObject? nwObject, TRegData registrationData, Action<TEvent> handler, EventCallbackType eventCallbackType = EventCallbackType.Before)
- void SubscribeAll<TEvent, TFactory>(Action<TEvent> handler, EventCallbackType eventCallbackType = EventCallbackType.Before)
- void SubscribeAll<TEvent, TFactory, TRegData>(TRegData registrationData, Action<TEvent> handler, EventCallbackType eventCallbackType = EventCallbackType.Before)
- void Unsubscribe<TEvent, TFactory>(NwObject? nwObject, Action<TEvent> handler, EventCallbackType eventCallbackType = EventCallbackType.Before)
- void UnsubscribeAll<TEvent, TFactory>(Action<TEvent> handler, EventCallbackType eventCallbackType = EventCallbackType.Before)

## Anvil.Services.CombatLogMessage  [enum]
- values: SimpleAdjective, SimpleDamage, ComplexDamage, ComplexDeath, ComplexAttack, SpecialAttack, SavingThrow, CastSpell, UseSkill, SpellResistance, Feedback, Counterspell, Touchattack, Initiative, DispelMagic, Polymorph, Feedbackstring, Vibrate, Unlockachievement

## Anvil.Services.FeedbackMessage  [enum]
- values: SkillCantUse, SkillCantUseTimer, SkillAnimalEmpathyValidTargets, SkillTauntValidTargets, SkillTauntTargetImmune, SkillPickpocketStoleItem, SkillPickpocketStoleGold, SkillPickpocketAttemptingToSteal, SkillPickpocketAttemptDetected, SkillPickpocketStoleItemTarget, SkillPickpocketStoleGoldTarget, SkillPickpocketTargetBroke, SkillHealTargetNotDiseasedPoisoned, SkillHealValidTargets, SkillStealthInCombat, TargetUnaware, ActionNotPossibleStatus, ActionNotPossiblePvp, ActionCantReachTarget, ActionNoLoot, WeightTooEncumberedToRun, WeightTooEncumberedWalkSlow, WeightTooEncumberedCantPickup, StatsLevelUp, InventoryFull, ContainerFull, TrapTriggered, DamageHealed, ExperienceGained, ExperienceLost, JournalUpdated, BarterCancelled, DetectModeActivated, DetectModeDeactivated, StealthModeActivated, StealthModeDeactivated, ParryModeActivated, ParryModeDeactivated, PowerAttackModeActivated, PowerAttackModeDeactivated, ImprovedPowerAttackModeActivated, ImprovedPowerAttackModeDeactivated, RapidShotModeActivated, RapidShotModeDeactivated, FlurryOfBlowsModeActivated, FlurryOfBlowsModeDeactivated, ExpertiseModeActivated, ExpertiseModeDeactivated, ImprovedExpertiseModeActivated, ImprovedExpertiseModeDeactivated, DefensiveCastModeActivated, DefensiveCastModeDeactivated, ModeCannotUseWeapons, DirtyFightingModeActivated, DirtyFightingModeDeactivated, DefensiveStanceModeActivated, DefensiveStanceModeDeactivated, EquipSkillSpellModifiers, EquipUnidentified, EquipMonkAbilities, EquipInsufficientLevel, EquipProficiencies, EquipWeaponTooLarge, EquipWeaponTooSmall, EquipOneHandedWeapon, EquipTwoHandedWeapon, EquipWeaponSwappedOut, EquipOneChainWeapon, EquipNaturalAcNoStack, EquipArmourAcNoStack, EquipShieldAcNoStack, EquipDeflectionAcNoStack, EquipNoArmorCombat, EquipRangerAbilities, EquipAlignment, EquipClass, EquipRace, UnequipNoArmorCombat, ObjectLocked, ObjectNotLocked, ObjectSpecialKey, ObjectUsedKey, RestExcitedCantRest, RestBeginningRest, RestFinishedRest, RestCancelRest, RestNotAllowedInArea, RestNotAllowedByPossessedFamiliar, RestNotAllowedEnemies, RestCantUnderThisEffect, CastLostTarget, CastCantCast, CastCounterspellTargetLostTarget, CastArcaneSpellFailure, CastCounterspellTargetArcaneSpellFailure, CastEntangleConcentrationFailure, CastCounterspellTargetEntangleConcentrationFailure, CastSpellInterrupted, CastEffectSpellFailure, CastCantCastWhilePolymorphed, CastUseHands, CastUseMouth, CastDefensiveCastConcentrationFailure, CastDefensiveCastConcentrationSuccess, UseItemCantUse, ConversationTooFar, ConversationBusy, ConversationInCombat, CharacterInTransit, CharacterOutTransit, UseItemNotEquipped, DropItemCantDrop, DropItemCantGive, ClientServerSpellMismatch, CombatRunningOutOfAmmo, CombatOutOfAmmo, CombatHenchmanOutOfAmmo, CombatDamageImmunity, CombatSpellImmunity, CombatDamageResistance, CombatDamageResistanceRemaining, CombatDamageReduction, CombatDamageReductionRemaining, CombatSpellLevelAbsorption, CombatSpellLevelAbsorptionRemaining, CombatWeaponNotEffective, CombatEpicDodgeAttackEvaded, CombatMassiveDamage, CombatSavedVsMassiveDamage, CombatSavedVsDevastatingCritical, FeatSapValidTargets, FeatKnockdownValidTargets, FeatImprovedKnockdownValidTargets, FeatCalledShotNoLegs, FeatCalledShotNoArms, FeatSmiteGoodTargetNotGood, FeatSmiteEvilTargetNotEvil, FeatQuiveringPalmHigherLevel, FeatKeenSenseDetect, FeatUseUnarmed, FeatUses, FeatUseWeaponOfChoice, PartyNewLeader, PartyMemberKicked, PartyKickedYou, PartyAlreadyConsidering, PartyAlreadyInvolved, PartySentInvitation, PartyReceivedInvitation, PartyJoined, PartyInvitationIgnored, PartyYouIgnoredInvitation, PartyInvitationRejected, PartyYouRejectedInvitation, PartyInvitationExpired, PartyLeftParty, PartyYouLeft, PartyHenchmanLimit, PartyCannotLeaveTheOneParty, PartyCannotKickFromTheOneParty, PartyYouInvitedNonSingleton, PvpReactionDislikesYou, ItemReceived, ItemLost, ItemEjected, ItemUseUnidentified, ItemGoldGained, ItemGoldLost, LearnScrollNotScroll, LearnScrollCantLearnClass, LearnScrollCantLearnLevel, LearnScrollCantLearnAbility, LearnScrollCantLearnOpposition, LearnScrollCantLearnPossess, LearnScrollCantLearnKnown, LearnScrollCantLearnDivine, LearnScrollSuccess, FloatyTextStrref, FloatyTextString, CannotSellPlotItem, CannotSellContainer, CannotSellItem, NotEnoughGold, TransactionSucceeded, PriceTooHigh, StoreNotEnoughGold, CannotSellStolenItem, CannotSellRestrictedItem, PortalTimedOut, PortalInvalid, ChatTellPlayerNotFound, AlignmentShift, AlignmentPartyShift, AlignmentChange, AlignmentRestrictedByClassLost, AlignmentRestrictedByClassGain, AlignmentRestrictedWarningLoss, AlignmentRestrictedWarningGain, AlignmentEpitomeGained, AlignmentEpitomeLost, ImmunityDisease, ImmunityCriticalHit, ImmunityDeathMagic, ImmunityFear, ImmunityKnockdown, ImmunityParalysis, ImmunityNegativeLevel, ImmunityMindSpells, ImmunityPoison, ImmunitySneakAttack, ImmunitySleep, ImmunityDaze, ImmunityConfusion, ImmunityStun, ImmunityBlindness, ImmunityDeafness, ImmunityCurse, ImmunityCharm, ImmunityDominate, ImmunityEntangle, ImmunitySilence, ImmunitySlow, AssociateSummoned, AssociateUnsummoning, AssociateUnsummoningBecauseRest, AssociateUnsummoningBecauseDied, AssociateDominated, AssociateDominationEnded, AssociatePossessedCannotRecoverTrap, AssociatePossessedCannotBarter, AssociatePossessedCannotEquip, AssociatePossessedCannotRepositoryMove, AssociatePossessedCannotPickUp, AssociatePossessedCannotDrop, AssociatePossessedCannotUnequip, AssociatePossessedCannotRest, AssociatePossessedCannotDialogue, AssociatePossessedCannotGiveItem, AssociatePossessedCannotTakeItem, AssociatePossessedCannotUseContainer, ScriptError, ActionListOverflow, EffectListOverflow, AiUpdateTimeOverflow, ActionListWipeOverflow, EffectListWipeOverflow, SendMessageToPc, SendMessageToPcStrref, GuiOnlyPartyLeaderMayClick, Paused, Unpaused, RestYouMayNotAtThisTime, GuiCharExportRequestSent, GuiCharExportedSuccessfully, GuiErrorCharNotExported, CameraBg, CameraEq, CameraChaseCam, Saving, SaveComplete

## Anvil.Services.FilterMode  [enum]
- values: Blacklist, Whitelist

## Anvil.Services.LogMode  [enum]
- values: Default, Off, Duplicate, Redirect

## Anvil.Services.IInitializable  [interface]

## Anvil.Services.ILateDisposable  [interface]

## Anvil.Services.IUpdateable  [interface]

## Anvil.Services.ObjectStorage  [class]
- bool ContainsFloat(string prefix, string key)
- bool ContainsInt(string prefix, string key)
- bool ContainsString(string prefix, string key)
- float? GetFloat(string prefix, string key)
- int? GetInt(string prefix, string key)
- string? GetString(string prefix, string key)
- bool Remove(string prefix, string key)
- void Set(string prefix, string key, int value, bool persist = false)
- void Set(string prefix, string key, float value, bool persist = false)
- void Set(string prefix, string key, string value, bool persist = false)

## Anvil.Services.ObjectStorageService  [class]
- ObjectStorageService(HookService hookService)
- void DestroyObjectStorage(NwObject gameObject)
- void DestroyObjectStorage(ICGameObject gameObject)
- ObjectStorage GetObjectStorage(NwObject gameObject)
- ObjectStorage GetObjectStorage(ICGameObject gameObject)
- bool TryGetObjectStorage(NwObject gameObject, [NotNullWhen(true)] out ObjectStorage? storage)
- bool TryGetObjectStorage(ICGameObject gameObject, [NotNullWhen(true)] out ObjectStorage? storage)

## Anvil.Services.ObjectStorageValue<T>  [struct]
- bool Persist
- T Value

## Anvil.Services.HomeStorage  [class]
- static string NLogConfig
- static string Paket
- static string PluginData
- static string Plugins
- static string ResourceTemp

## Anvil.Services.ResourceManager  [class]
- const int MaxNameLength = 16
- string CreateResourceDirectory(string path, bool detectChanges = true)
- void DeleteTempResource(string resourceName)
- IEnumerable<string> FindResourcesOfType(ResRefType type, bool moduleOnly = true)
- GffResource? GetGenericFile(string name, ResRefType type)
- string GetNSSContents(string scriptName)
- byte[]? GetResourceData(string name, ResRefType type)
- string? GetResourceText(string name, ResRefType type)
- bool IsValidResource(string name, ResRefType type = ResRefType.UTC)
- void WriteTempResource(string resourceName, byte[] data)
- void WriteTempResource(string resourceName, string text)

## Anvil.Services.ScheduledTask  [class]
- int Compare(ScheduledTask? x, ScheduledTask? y)
- readonly bool Repeating
- readonly TimeSpan Schedule
- int ExecutionCount
- TimeSpan ExecutionTime
- int FailedExecutionCount
- bool IsCancelled
- void Cancel()
- void Dispose()

## Anvil.Services.SchedulerService  [class]
- static readonly TimeSpan NextUpdate = TimeSpan.Zero
- ScheduledTask Schedule(Action action, TimeSpan delay)
- ScheduledTask ScheduleRepeating(Action action, TimeSpan schedule, TimeSpan delay = default)

## Anvil.Services.IScriptDispatcher  [interface]
- int ExecutionOrder

## Anvil.Services.ScriptCallbackHandle  [class]
- readonly string ScriptName
- bool IsValid
- void Dispose()

## Anvil.Services.ScriptHandleFactory  [class]
- int ExecutionOrder
- ScriptCallbackHandle CreateUniqueHandler(Func<CallInfo, ScriptHandleResult> handler)
- bool IsScriptRegistered(string scriptName)
- ScriptCallbackHandle RegisterScriptHandler(string scriptName, Func<CallInfo, ScriptHandleResult> callback)
- bool UnregisterScriptHandler(string scriptName)

## Anvil.Services.ScriptHandleResult  [enum]
- values: NotHandled, Handled, False, True

## Anvil.Services.BindingPriority  [enum]
- values: Highest, VeryHigh, High, AboveNormal, Normal, BelowNormal, Low, VeryLow, Lowest

## Anvil.Services.IServiceManager  [interface]

## Anvil.Services.InjectAttribute  [class]
- InjectAttribute() : this(string.Empty)
- InjectAttribute(string serviceName)
- bool Optional
- string ServiceName

## Anvil.Services.InjectPropertyTypes  [enum]
- values: InstanceOnly, StaticOnly

## Anvil.Services.InjectionService  [class]
- T Inject<T>(T instance)

## Anvil.Services.ServiceBindingAttribute  [class]
- readonly Type BindFrom
- ServiceBindingAttribute(Type bindFrom)

## Anvil.Services.ServiceBindingOptionsAttribute  [class]
- ServiceBindingOptionsAttribute()
- BindingPriority BindingPriority
- bool Lazy
- string[]? PluginDependencies

## Anvil.Services.ITwoDimArray  [interface]

## Anvil.Services.DevastatingCriticalData  [class]
- NwCreature Attacker
- bool Bypass
- int Damage
- NwGameObject Target
- NwItem Weapon

## Anvil.Services.MaxRangedAttackDistanceOverride  [struct]
- float MaxRangedAttackDistance
- float MaxRangedPassiveAttackDistance

## Anvil.Services.WeaponService  [class]
- WeaponService(HookService hookService, EventService eventService)
- event Action<DevastatingCriticalData>? OnDevastatingCriticalHit
- bool EnableSlingGoodAimFeat
- int GreaterWeaponFocusAttackBonus
- int GreaterWeaponSpecializationDamageBonus
- void AddEpicWeaponDevastatingCriticalFeat(NwBaseItem baseItem, NwFeat feat)
- void AddEpicWeaponFocusFeat(NwBaseItem baseItem, NwFeat feat)
- void AddEpicWeaponOverwhelmingCriticalFeat(NwBaseItem baseItem, NwFeat feat)
- void AddEpicWeaponSpecializationFeat(NwBaseItem baseItem, NwFeat feat)
- void AddGreaterWeaponFocusFeat(NwBaseItem baseItem, NwFeat feat)
- void AddGreaterWeaponSpecializationFeat(NwBaseItem baseItem, NwFeat feat)
- void AddWeaponFocusFeat(NwBaseItem baseItem, NwFeat feat)
- void AddWeaponImprovedCriticalFeat(NwBaseItem baseItem, NwFeat feat)
- void AddWeaponOfChoiceFeat(NwBaseItem baseItem, NwFeat feat)
- void AddWeaponSpecializationFeat(NwBaseItem baseItem, NwFeat feat)
- CreatureSize GetWeaponFinesseSize(NwBaseItem baseItem)
- void SetMaxRangedAttackDistanceOverride(NwBaseItem baseItem, float max, float maxPassive, float preferred)
- void SetWeaponFinesseSize(NwBaseItem baseItem, CreatureSize size)
- void SetWeaponIsMonkWeapon(NwBaseItem baseItem)
- void SetWeaponUnarmed(NwBaseItem baseItem)
