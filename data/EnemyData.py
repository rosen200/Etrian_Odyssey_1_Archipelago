from enum import IntEnum
from typing import Optional

class EnemyType(IntEnum):
    REGULAR = 1
    FOE = 2
    BOSS = 3

class DropCondition(IntEnum):
    STAB = 0x02
    FIRE = 0x04
    ICE = 0x05
    NOT_BASH = 0x08
    NOT_STAB = 0x09
    NOT_PHYSICAL = 0x0A
    NOT_FIRE = 0x0B
    INSTANT_DEATH = 0x0F
    FULL_BIND = 0x13
    KILL_1_TURNS = 0x41
    KILL_2_TURNS = 0x42
    KILL_3_TURNS = 0x43
    KILL_7_TURNS = 0x47
    NONE = 0xFF

class EnemyData:
    enemy_id: int
    name: str
    level: int
    type: EnemyType
    codex_id: int
    hp: int
    str: int
    vit: int
    tec: int
    cut_resistance: int
    bash_resistance: int
    stab_resistance: int
    fire_resistance: int
    ice_resistance: int
    volt_resistance: int
    item_drop_1: Optional[int]
    item_drop_2: Optional[int]
    item_drop_3: Optional[int]
    drop_condition: Optional[DropCondition]

    def __init__(self, enemy_id, name, level, type, codex_id,
                 hp, str, vit, tec, cut_resistance, bash_resistance,
                 stab_resistance, fire_resistance, ice_resistance, volt_resistance,
                 item_drop_1, item_drop_2, item_drop_3, drop_condition):
        self.enemy_id = enemy_id
        self.name = name
        self.level = level
        self.type = type
        self.codex_id = codex_id
        self.hp = hp
        self.str = str
        self.vit = vit
        self.tec = tec
        self.cut_resistance = cut_resistance
        self.bash_resistance = bash_resistance
        self.stab_resistance = stab_resistance
        self.fire_resistance = fire_resistance
        self.ice_resistance = ice_resistance
        self.volt_resistance = volt_resistance
        self.item_drop_1 = item_drop_1
        self.item_drop_2 = item_drop_2
        self.item_drop_3 = item_drop_3
        self.drop_condition = drop_condition

class EO1Enemies:
    WOLF = 0x01
    DIREWOLF = 0x03
    TREERAT = 0x04
    FLAMERAT = 0x05
    HARE = 0x06
    DARKHARE = 0x07
    ROLLER = 0x08
    ARMOROLL = 0x09
    MOLE = 0x0A
    MAUL = 0x0B
    SLOTH = 0x0C
    ARMOTH = 0x0E
    TREETUSK = 0x0F
    FENDER = 0x10
    GOLDEER = 0x11
    WARBULL = 0x12
    HELLBULL = 0x13
    CUTTER = 0x14
    REDCLAW = 0x15
    DESOULER = 0x16
    SLEEPGEL = 0x17
    VENOMGEL = 0x18
    BURSTGEL = 0x19
    FLAMEGEL = 0x1A
    MUCKDILE = 0x1B
    KINGDILE = 0x1C
    TREEFROG = 0x1D
    HEXFROG = 0x1E
    KINGFROG = 0x1F
    SHELLTOR = 0x20
    SHELLORD = 0x21
    CLAWBUG = 0x22
    CLAWFLY = 0x23
    CLAWLORD = 0x24
    MORIYANA = 0x25
    KINGYANA = 0x26
    WASPIOR = 0x27
    KINGAPIS = 0x28
    MADWORM = 0x29
    MELTWORM = 0x2A
    WOODFLY = 0x2B
    VENOMFLY = 0x2C
    HAZEFLY = 0x2D
    HELLFLY = 0x2E
    SPIDER = 0x2F
    SILKER = 0x30
    SCORPION = 0x31
    METALION = 0x32
    DEATHANT = 0x33
    GUARDANT = 0x34
    LARGEANT = 0x35
    SICKWOOD = 0x36
    ROCKWOOD = 0x37
    FANGLEAF = 0x38
    MANEATER = 0x39
    PETALOID = 0x3A
    EVILOID = 0x3B
    MUSKOID = 0x3C
    FIREBIRD = 0x3D
    SONGBIRD = 0x3E
    GLOWBIRD = 0x3F
    REDBEAK = 0x40
    LUCIFIRD = 0x41
    SWORDER = 0x46
    BLADER = 0x47
    CUTCRAB = 0x48
    IRONCRAB = 0x49
    DINOLICH = 0x4A
    TERALICH = 0x4B
    SOLDIER = 0x4C
    WARRIOR = 0x4D
    MYSTIC = 0x4E
    DRUID = 0x4F
    PIXIE = 0x50
    FAERIE = 0x51
    OGRE = 0x52
    HUNTER = 0x53
    STALKER = 0x54
    MANTIS = 0x55
    MOA = 0x56
    IMMOA = 0x57
    MANDRAKE = 0x58
    HEXROOT = 0x59
    EVILROOT = 0x5A
    WYVERN = 0x64
    CERNUNOS = 0x65
    ROYALANT = 0x66
    COTRANGL = 0x67
    IWAOPELN = 0x68
    ETREANT = 0x69
    WYRM = 0x6A
    DRAKE = 0x6B
    ALRAUNE = 0x6C
    PRIMEVIL = 0x6D
    DRAGON = 0x6E
    MANTICOR = 0x6F
    GOLEM = 0x70
    REN = 0x71
    TLACHTGA = 0x72
    FIREATER = 0x78
    TOXINFLY = 0x79
    OMNIVORE = 0x7B
    STEELWEB = 0x7C
    GOUDARAT = 0x7D
    CUROLLER = 0x7E
    NIGHTOAD = 0x80
    HEXTOAD = 0x81
    SKOLL = 0x82
    FENRIR = 0x97
    STINGMAW = 0x98
    VARAHA = 0x99
    WOODBAT = 0x9A
    VAMPBAT = 0x9B
    CRUELLA = 0x9C
    DIABOLIX = 0x9D
    SPROUT = 0x9E
    BUD = 0x9F
    CLOVER = 0xA0
    MONOCYTE = 0xA1
    RED_CELL = 0xA2
    SABREMAW = 0xA3
    PONDCLAW = 0xA4
    RAGELOPE = 0xA5
    KUYUTHA = 0xA6
    ASSASSIN = 0xA7
    BLOODANT = 0xA8
    SERVANT = 0xA9
    KILLCLAW = 0xAA
    MACABRE = 0xAC
    DRAGOID = 0xAD
    WYRMOID = 0xAE
    DRAKOID = 0xAF

ALL_ENEMIES: list[EnemyData] = [
    EnemyData(EO1Enemies.WOLF, "Wolf", 14, EnemyType.FOE, 0x54, 260, 51, 29, 20, 100, 100, 100, 150, 50, 100, 0xFB0, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.DIREWOLF, "Direwolf", 51, EnemyType.REGULAR, 0x35, 464, 189, 116, 83, 100, 100, 100, 0, 150, 100, 0x101D, 0x101E, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.TREERAT, "Treerat", 2, EnemyType.REGULAR, 0x1, 19, 10, 14, 7, 100, 100, 100, 200, 100, 100, 0xFA1, 0xFA2, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.FLAMERAT, "Flamerat", 39, EnemyType.REGULAR, 0x25, 333, 128, 88, 44, 100, 100, 100, 0, 150, 100, 0xFF6, 0xFF7, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.HARE, "Hare", 7, EnemyType.REGULAR, 0x6, 38, 23, 19, 14, 100, 100, 100, 100, 100, 100, 0xFA1, 0xFA8, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.DARKHARE, "Darkhare", 47, EnemyType.REGULAR, 0x32, 476, 171, 107, 51, 100, 100, 100, 100, 100, 100, 0x1018, 0x1019, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.ROLLER, "Roller", 11, EnemyType.REGULAR, 0x9, 40, 28, 25, 17, 75, 75, 75, 100, 150, 150, 0xFA2, 0xFAD, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.ARMOROLL, "Armoroll", 55, EnemyType.REGULAR, 0x3C, 713, 298, 124, 42, 50, 50, 50, 150, 50, 100, 0x1025, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.MOLE, "Mole", 3, EnemyType.REGULAR, 0x3, 23, 12, 15, 7, 100, 100, 100, 100, 200, 100, 0xFA2, 0xFA3, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.MAUL, "Maul", 47, EnemyType.REGULAR, 0x33, 572, 223, 107, 36, 100, 100, 100, 100, 50, 150, 0x1017, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.SLOTH, "Sloth", 22, EnemyType.REGULAR, 0x11, 212, 84, 44, 20, 100, 100, 100, 50, 200, 100, 0xFC1, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.ARMOTH, "Armoth", 27, EnemyType.FOE, 0x67, 1200, 119, 57, 33, 75, 75, 75, 100, 100, 100, 0xFD9, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.TREETUSK, "Treetusk", 54, EnemyType.FOE, 0x6C, 5500, 339, 122, 58, 75, 75, 75, 100, 100, 100, 0x102A, 0x0, 0x1047, DropCondition.NOT_PHYSICAL),
    EnemyData(EO1Enemies.FENDER, "Fender", 10, EnemyType.REGULAR, 0x7, 55, 36, 23, 12, 100, 100, 100, 100, 100, 200, 0xFA2, 0xFA9, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.GOLDEER, "Goldeer", 35, EnemyType.REGULAR, 0x26, 419, 167, 88, 31, 100, 100, 100, 50, 50, 150, 0xFFA, 0xFFB, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.WARBULL, "Warbull", 16, EnemyType.REGULAR, 0xB, 140, 52, 33, 16, 100, 100, 100, 150, 150, 150, 0xFAD, 0xFAF, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.HELLBULL, "Hellbull", 55, EnemyType.REGULAR, 0x3D, 850, 298, 124, 42, 100, 100, 100, 150, 150, 150, 0x1022, 0x1024, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.CUTTER, "Cutter", 27, EnemyType.FOE, 0x57, 790, 119, 57, 33, 100, 100, 100, 100, 100, 100, 0xFD2, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.REDCLAW, "Redclaw", 36, EnemyType.REGULAR, 0x24, 371, 155, 76, 29, 100, 100, 100, 50, 150, 100, 0xFE4, 0xFE5, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.DESOULER, "Desouler", 50, EnemyType.FOE, 0x5E, 4500, 306, 116, 54, 100, 100, 100, 125, 50, 100, 0x1026, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.SLEEPGEL, "Sleepgel", 18, EnemyType.REGULAR, 0xC, 88, 48, 37, 24, 75, 75, 75, 100, 200, 200, 0xFBD, 0xFBE, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.VENOMGEL, "Venomgel", 18, EnemyType.REGULAR, 0xD, 106, 63, 38, 17, 75, 75, 75, 100, 200, 200, 0xFBD, 0xFBE, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.BURSTGEL, "Burstgel", 47, EnemyType.REGULAR, 0x34, 476, 171, 102, 51, 75, 75, 75, 0, 200, 200, 0x101B, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.FLAMEGEL, "Flamegel", 63, EnemyType.REGULAR, 0x3F, 768, 243, 133, 64, 0, 0, 0, 0, 150, 100, 0x102D, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.MUCKDILE, "Muckdile", 38, EnemyType.FOE, 0x68, 2000, 200, 92, 43, 100, 100, 50, 100, 125, 100, 0xFF5, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.KINGDILE, "Kingdile", 53, EnemyType.FOE, 0x5F, 4500, 333, 120, 57, 100, 100, 50, 100, 125, 100, 0x102B, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.TREEFROG, "Treefrog", 30, EnemyType.REGULAR, 0x1B, 180, 84, 61, 53, 100, 150, 100, 100, 100, 150, 0xFDA, 0xFDB, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.HEXFROG, "Hexfrog", 31, EnemyType.REGULAR, 0x1D, 222, 89, 64, 54, 100, 150, 100, 100, 100, 150, 0xFDA, 0xFDD, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.KINGFROG, "Kingfrog", 52, EnemyType.REGULAR, 0x37, 429, 195, 118, 84, 100, 150, 100, 100, 100, 150, 0x101A, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.SHELLTOR, "Shelltor", 37, EnemyType.FOE, 0x69, 2000, 183, 84, 42, 50, 50, 50, 100, 125, 100, 0xFF4, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.SHELLORD, "Shellord", 69, EnemyType.FOE, 0x61, 7500, 402, 160, 67, 50, 50, 50, 0, 125, 50, 0x1042, 0x0, 0x1043, DropCondition.NOT_BASH),
    EnemyData(EO1Enemies.CLAWBUG, "Clawbug", 4, EnemyType.REGULAR, 0x4, 45, 25, 16, 8, 50, 50, 50, 250, 250, 250, 0xFA4, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.CLAWFLY, "Clawfly", 14, EnemyType.REGULAR, 0xA, 65, 45, 29, 14, 50, 50, 50, 0, 300, 300, 0xFA4, 0xFAE, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.CLAWLORD, "Clawlord", 53, EnemyType.REGULAR, 0x39, 618, 289, 120, 40, 50, 50, 50, 200, 200, 150, 0x101F, 0x1020, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.MORIYANA, "Moriyana", 35, EnemyType.REGULAR, 0x20, 247, 105, 72, 60, 100, 100, 100, 100, 100, 150, 0xFE0, 0xFE1, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.KINGYANA, "Kingyana", 56, EnemyType.REGULAR, 0x3E, 535, 209, 126, 90, 100, 100, 100, 100, 100, 150, 0x1020, 0x1026, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.WASPIOR, "Waspior", 19, EnemyType.REGULAR, 0xE, 88, 52, 39, 25, 100, 100, 100, 100, 100, 150, 0xFB1, 0xFBF, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.KINGAPIS, "Kingapis", 52, EnemyType.REGULAR, 0x38, 594, 216, 118, 56, 100, 100, 100, 100, 100, 150, 0x1027, 0x1028, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.MADWORM, "Madworm", 29, EnemyType.REGULAR, 0x19, 240, 116, 58, 24, 150, 50, 150, 150, 100, 100, 0xFDC, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.MELTWORM, "Meltworm", 34, EnemyType.REGULAR, 0x1F, 329, 145, 70, 28, 150, 50, 150, 150, 100, 100, 0xFDC, 0xFE3, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.WOODFLY, "Woodfly", 2, EnemyType.REGULAR, 0x2, 19, 11, 14, 7, 100, 100, 100, 100, 100, 200, 0xFA5, 0xFA6, 0xFA7, DropCondition.NOT_PHYSICAL),
    EnemyData(EO1Enemies.VENOMFLY, "Venomfly", 6, EnemyType.REGULAR, 0x5, 41, 22, 18, 13, 100, 100, 100, 100, 100, 150, 0xFA5, 0xFA6, 0xFA7, DropCondition.NOT_PHYSICAL),
    EnemyData(EO1Enemies.HAZEFLY, "Hazefly", 64, EnemyType.REGULAR, 0x40, 773, 245, 141, 65, 100, 100, 100, 100, 100, 150, 0x1068, 0x1044, 0x1069, DropCondition.ICE),
    EnemyData(EO1Enemies.HELLFLY, "Hellfly", 65, EnemyType.REGULAR, 0x41, 794, 250, 143, 65, 100, 100, 100, 100, 100, 150, 0x1068, 0x1049, 0x1069, DropCondition.ICE),
    EnemyData(EO1Enemies.SPIDER, "Spider", 20, EnemyType.REGULAR, 0xF, 88, 56, 41, 26, 100, 100, 100, 150, 100, 150, 0xFC0, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.SILKER, "Silker", 53, EnemyType.REGULAR, 0x3A, 429, 200, 120, 86, 100, 100, 100, 150, 100, 150, 0x101C, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.SCORPION, "Scorpion", 25, EnemyType.REGULAR, 0x16, 122, 63, 52, 47, 100, 100, 100, 100, 100, 200, 0xFCA, 0xFBF, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.METALION, "Metalion", 69, EnemyType.REGULAR, 0x48, 1005, 341, 134, 47, 0, 0, 0, 0, 0, 200, 0x106A, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.DEATHANT, "Deathant", 30, EnemyType.REGULAR, 0x1C, 180, 84, 61, 53, 75, 75, 75, 50, 150, 100, 0xFDE, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.GUARDANT, "Guardant", 29, EnemyType.REGULAR, 0x1A, 222, 81, 58, 51, 75, 75, 75, 50, 150, 100, 0xFDF, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.LARGEANT, "Largeant", 66, EnemyType.REGULAR, 0x44, 723, 228, 132, 99, 100, 100, 100, 50, 150, 100, 0x1067, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.SICKWOOD, "Sickwood", 40, EnemyType.FOE, 0x5B, 2000, 195, 89, 44, 100, 100, 100, 125, 100, 100, 0x100A, 0x100B, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.ROCKWOOD, "Rockwood", 68, EnemyType.REGULAR, 0x47, 738, 233, 134, 101, 100, 100, 100, 150, 100, 100, 0x103D, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.FANGLEAF, "Fangleaf", 21, EnemyType.REGULAR, 0x10, 225, 78, 42, 19, 100, 100, 100, 150, 100, 100, 0xFC2, 0xFC3, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.MANEATER, "Maneater", 24, EnemyType.REGULAR, 0x15, 230, 89, 49, 21, 100, 100, 100, 150, 100, 100, 0xFC2, 0xFC4, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.PETALOID, "Petaloid", 22, EnemyType.REGULAR, 0x12, 135, 64, 44, 28, 100, 100, 100, 150, 100, 100, 0xFC5, 0xFC6, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.EVILOID, "Eviloid", 23, EnemyType.REGULAR, 0x13, 142, 66, 46, 29, 100, 100, 100, 150, 100, 100, 0xFC5, 0xFCB, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.MUSKOID, "Muskoid", 51, EnemyType.REGULAR, 0x36, 555, 210, 116, 55, 100, 100, 100, 150, 100, 100, 0x1021, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.FIREBIRD, "Firebird", 23, EnemyType.REGULAR, 0x14, 135, 66, 44, 29, 100, 100, 125, 10, 125, 50, 0xFC7, 0xFC8, 0xFC9, DropCondition.FIRE),
    EnemyData(EO1Enemies.SONGBIRD, "Songbird", 68, EnemyType.FOE, 0x60, 5500, 387, 134, 67, 100, 100, 125, 75, 125, 100, 0x102D, 0x0, 0x1046, DropCondition.NOT_FIRE),
    EnemyData(EO1Enemies.GLOWBIRD, "Glowbird", 26, EnemyType.REGULAR, 0x18, 142, 75, 52, 32, 100, 100, 150, 100, 150, 100, 0xFC7, 0xFCC, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.REDBEAK, "Redbeak", 45, EnemyType.REGULAR, 0x30, 389, 159, 97, 49, 100, 100, 150, 0, 150, 150, 0x1008, 0x1009, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.LUCIFIRD, "Lucifird", 70, EnemyType.REGULAR, 0x49, 858, 268, 130, 68, 50, 50, 150, 75, 75, 75, 0x106A, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.SWORDER, "Sworder", 37, EnemyType.REGULAR, 0x23, 301, 122, 84, 42, 50, 100, 100, 100, 50, 150, 0xFE7, 0xFE8, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.BLADER, "Blader", 65, EnemyType.REGULAR, 0x42, 794, 250, 143, 65, 50, 100, 100, 100, 50, 150, 0x103D, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.CUTCRAB, "Cutcrab", 36, EnemyType.REGULAR, 0x22, 301, 119, 76, 41, 50, 50, 50, 100, 100, 150, 0xFE0, 0xFE9, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.IRONCRAB, "Ironcrab", 70, EnemyType.REGULAR, 0x4A, 1030, 349, 136, 48, 0, 0, 0, 0, 0, 150, 0x0, 0x0, 0x104B, DropCondition.STAB),
    EnemyData(EO1Enemies.DINOLICH, "Dinolich", 55, EnemyType.FOE, 0x6D, 6200, 344, 124, 59, 100, 100, 100, 125, 100, 50, 0x1029, 0x0, 0x104F, DropCondition.NOT_STAB),
    EnemyData(EO1Enemies.TERALICH, "Teralich", 69, EnemyType.FOE, 0x6E, 7500, 405, 134, 67, 75, 75, 75, 125, 100, 50, 0x104C, 0x104D, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.SOLDIER, "Soldier", 39, EnemyType.REGULAR, 0x27, 400, 167, 88, 31, 100, 150, 50, 150, 50, 50, 0x1002, 0x1003, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.WARRIOR, "Warrior", 44, EnemyType.REGULAR, 0x2D, 467, 190, 100, 34, 100, 150, 50, 150, 50, 50, 0x1002, 0x1013, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.MYSTIC, "Mystic", 39, EnemyType.REGULAR, 0x28, 300, 116, 88, 66, 100, 150, 50, 150, 50, 50, 0x1004, 0x1003, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.DRUID, "Druid", 44, EnemyType.REGULAR, 0x2E, 351, 132, 100, 72, 100, 150, 50, 150, 50, 50, 0x1004, 0x1005, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.PIXIE, "Pixie", 43, EnemyType.REGULAR, 0x2B, 333, 126, 96, 71, 100, 100, 100, 0, 0, 0, 0x1006, 0x1007, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.FAERIE, "Faerie", 44, EnemyType.REGULAR, 0x2F, 351, 132, 100, 72, 100, 100, 100, 0, 0, 0, 0x1006, 0x1007, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.OGRE, "Ogre", 46, EnemyType.FOE, 0x6A, 5000, 252, 110, 40, 50, 50, 50, 125, 125, 125, 0x103E, 0x0, 0x103F, DropCondition.KILL_2_TURNS),
    EnemyData(EO1Enemies.HUNTER, "Hunter", 46, EnemyType.FOE, 0x6B, 4600, 239, 104, 65, 100, 100, 100, 50, 50, 50, 0x1040, 0x0, 0x1041, DropCondition.KILL_2_TURNS),
    EnemyData(EO1Enemies.STALKER, "Stalker", 18, EnemyType.FOE, 0x66, 600, 72, 38, 24, 50, 100, 50, 125, 100, 100, 0xFBC, 0x0, 0x105F, DropCondition.KILL_1_TURNS),
    EnemyData(EO1Enemies.MANTIS, "Mantis", 39, EnemyType.REGULAR, 0x29, 400, 167, 88, 31, 50, 100, 50, 150, 100, 100, 0xFFC, 0xFFE, 0xFFD, DropCondition.KILL_1_TURNS),
    EnemyData(EO1Enemies.MOA, "Moa", 25, EnemyType.FOE, 0x55, 900, 90, 52, 31, 100, 100, 100, 100, 100, 100, 0xFD3, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.IMMOA, "Immoa", 42, EnemyType.REGULAR, 0x31, 429, 177, 93, 33, 100, 100, 100, 100, 100, 100, 0xFFF, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.MANDRAKE, "Mandrake", 10, EnemyType.REGULAR, 0x8, 51, 27, 23, 16, 100, 100, 100, 150, 50, 50, 0xFAA, 0xFAB, 0xFAC, DropCondition.FIRE),
    EnemyData(EO1Enemies.HEXROOT, "Hexroot", 43, EnemyType.REGULAR, 0x2C, 369, 140, 96, 47, 100, 100, 100, 150, 50, 50, 0x1000, 0x1001, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.EVILROOT, "Evilroot", 67, EnemyType.REGULAR, 0x46, 811, 255, 132, 66, 100, 100, 100, 150, 50, 50, 0x1045, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.WYVERN, "Wyvern", 40, EnemyType.BOSS, 0x7A, 8000, 260, 107, 88, 75, 75, 75, 50, 75, 0, 0xFD7, 0x0, 0xFD8, DropCondition.KILL_3_TURNS),
    EnemyData(EO1Enemies.CERNUNOS, "Cernunos", 28, EnemyType.BOSS, 0x72, 2750, 170, 69, 68, 100, 100, 100, 50, 100, 150, 0xFD6, 0x0, 0x1060, DropCondition.NONE),
    EnemyData(EO1Enemies.ROYALANT, "Royalant", 32, EnemyType.BOSS, 0x73, 5500, 204, 80, 74, 100, 100, 100, 100, 100, 100, 0xFF1, 0x0, 0x1061, DropCondition.NONE),
    EnemyData(EO1Enemies.COTRANGL, "Cotrangl", 38, EnemyType.BOSS, 0x74, 7000, 250, 104, 86, 100, 100, 100, 125, 0, 75, 0xFF2, 0x0, 0x105C, DropCondition.NOT_FIRE),
    EnemyData(EO1Enemies.IWAOPELN, "Iwaopeln", 46, EnemyType.BOSS, 0x75, 9000, 330, 125, 100, 100, 100, 100, 50, 125, 50, 0x1012, 0x0, 0x1048, DropCondition.NONE),
    EnemyData(EO1Enemies.ETREANT, "Etreant", 56, EnemyType.BOSS, 0x78, 18000, 470, 160, 130, 90, 90, 90, 100, 100, 100, 0x102C, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.WYRM, "Wyrm", 70, EnemyType.BOSS, 0x7D, 35000, 530, 164, 140, 75, 75, 75, 0, 150, 75, 0x1056, 0x0, 0x1055, DropCondition.NONE),
    EnemyData(EO1Enemies.DRAKE, "Drake", 70, EnemyType.BOSS, 0x7E, 35000, 540, 164, 136, 75, 75, 75, 150, 0, 75, 0x1059, 0x0, 0x1062, DropCondition.NONE),
    EnemyData(EO1Enemies.ALRAUNE, "Alraune", 55, EnemyType.BOSS, 0x7C, 16000, 470, 160, 125, 100, 100, 100, 125, 0, 0, 0x105E, 0x0, 0x104A, DropCondition.NOT_FIRE),
    EnemyData(EO1Enemies.PRIMEVIL, "Primevil", 70, EnemyType.BOSS, 0x80, 90000, 585, 170, 160, 150, 150, 150, 150, 150, 150, 0x105A, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.DRAGON, "Dragon", 70, EnemyType.BOSS, 0x7F, 35000, 550, 164, 121, 100, 100, 100, 75, 75, 0, 0x105D, 0x0, 0x1066, DropCondition.NONE),
    EnemyData(EO1Enemies.MANTICOR, "Manticor", 45, EnemyType.BOSS, 0x7B, 8500, 333, 123, 98, 100, 100, 100, 50, 50, 50, 0x1065, 0x0, 0x1058, DropCondition.KILL_7_TURNS),
    EnemyData(EO1Enemies.GOLEM, "Golem", 30, EnemyType.BOSS, 0x79, 7000, 200, 120, 30, 50, 50, 50, 125, 125, 125, 0xFB7, 0x0, 0x1057, DropCondition.INSTANT_DEATH),
    EnemyData(EO1Enemies.REN, "Ren", 47, EnemyType.BOSS, 0x76, 7000, 360, 110, 102, 75, 75, 75, 150, 0, 100, 0x0, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.TLACHTGA, "Tlachtga", 47, EnemyType.BOSS, 0x77, 5000, 210, 105, 141, 125, 125, 125, 50, 50, 50, 0x104E, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.FIREATER, "Fireater", 26, EnemyType.FOE, 0x4B, 864, 113, 54, 32, 100, 100, 150, 10, 150, 50, 0x0, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.TOXINFLY, "Toxinfly", 30, EnemyType.REGULAR, 0x4D, 211, 93, 61, 35, 100, 100, 100, 100, 100, 150, 0x0, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.OMNIVORE, "Omnivore", 32, EnemyType.FOE, 0x4E, 1419, 153, 66, 37, 100, 100, 100, 125, 100, 100, 0x0, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.STEELWEB, "Steelweb", 65, EnemyType.FOE, 0x51, 4367, 375, 143, 65, 100, 100, 100, 125, 100, 150, 0x0, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.GOUDARAT, "Goudarat", 70, EnemyType.FOE, 0x0, 4719, 402, 136, 68, 100, 100, 100, 100, 100, 100, 0x0, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.CUROLLER, "Curoller", 26, EnemyType.REGULAR, 0x71, 142, 75, 54, 32, 100, 100, 100, 100, 125, 125, 0x0, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.NIGHTOAD, "Nightoad", 42, EnemyType.FOE, 0x4F, 1964, 204, 93, 46, 100, 125, 100, 100, 100, 150, 0x0, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.HEXTOAD, "Hextoad", 43, EnemyType.FOE, 0x50, 2030, 210, 96, 47, 100, 125, 100, 100, 100, 150, 0x0, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.SKOLL, "Skoll", 15, EnemyType.FOE, 0x6F, 400, 54, 30, 21, 100, 100, 100, 150, 50, 100, 0xFB0, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.FENRIR, "Fenrir", 18, EnemyType.BOSS, 0x70, 1200, 96, 46, 48, 100, 100, 100, 150, 0, 100, 0xFBA, 0xFBB, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.STINGMAW, "Stingmaw", 25, EnemyType.REGULAR, 0x17, 171, 94, 49, 20, 100, 100, 100, 100, 150, 0, 0xFCE, 0xFCD, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.VARAHA, "Varaha", 54, EnemyType.REGULAR, 0x3B, 555, 226, 122, 58, 100, 100, 100, 100, 100, 100, 0x1022, 0x1023, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.WOODBAT, "Woodbat", 33, EnemyType.REGULAR, 0x1E, 274, 107, 68, 38, 100, 100, 100, 110, 110, 110, 0xFE2, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.VAMPBAT, "Vampbat", 35, EnemyType.REGULAR, 0x21, 301, 116, 72, 40, 100, 100, 100, 150, 100, 100, 0xFE2, 0xFE6, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.CRUELLA, "Cruella", 43, EnemyType.FOE, 0x5C, 2300, 210, 96, 47, 75, 75, 75, 100, 100, 100, 0x100E, 0x100C, 0x1064, DropCondition.FULL_BIND),
    EnemyData(EO1Enemies.DIABOLIX, "Diabolix", 43, EnemyType.FOE, 0x5D, 3200, 210, 96, 47, 100, 100, 100, 100, 100, 100, 0x100E, 0x100D, 0x1063, DropCondition.FULL_BIND),
    EnemyData(EO1Enemies.SPROUT, "Sprout", 1, EnemyType.REGULAR, 0x81, 2000, 20, 20, 20, 300, 300, 300, 300, 300, 300, 0x106E, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.BUD, "Bud", 1, EnemyType.REGULAR, 0x82, 4000, 20, 20, 20, 300, 300, 300, 300, 300, 300, 0x106F, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.CLOVER, "Clover", 1, EnemyType.REGULAR, 0x83, 8000, 20, 20, 20, 300, 300, 300, 300, 300, 300, 0x1070, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.MONOCYTE, "Monocyte", 65, EnemyType.REGULAR, 0x43, 715, 225, 143, 98, 100, 100, 100, 100, 100, 100, 0x1067, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.RED_CELL, "Red Cell", 66, EnemyType.REGULAR, 0x45, 723, 228, 132, 99, 50, 50, 50, 50, 50, 50, 0x102D, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.SABREMAW, "Sabremaw", 40, EnemyType.REGULAR, 0x2A, 333, 130, 89, 44, 100, 100, 100, 150, 0, 100, 0xFF8, 0xFF9, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.PONDCLAW, "Pondclaw", 26, EnemyType.FOE, 0x4C, 660, 113, 54, 32, 50, 50, 50, 150, 200, 200, 0x0, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.RAGELOPE, "Ragelope", 12, EnemyType.FOE, 0x52, 330, 45, 26, 18, 75, 75, 75, 100, 100, 200, 0xFA9, 0xFB9, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.KUYUTHA, "Kuyutha", 13, EnemyType.FOE, 0x53, 350, 48, 27, 19, 100, 100, 150, 100, 100, 100, 0xFAF, 0xFB9, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.ASSASSIN, "Assassin", 26, EnemyType.FOE, 0x56, 950, 121, 54, 32, 90, 90, 90, 100, 100, 150, 0xFD4, 0xFD5, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.BLOODANT, "Bloodant", 29, EnemyType.FOE, 0x58, 800, 134, 58, 34, 75, 75, 75, 50, 125, 100, 0xFDE, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.SERVANT, "Servant", 30, EnemyType.FOE, 0x59, 1300, 140, 61, 35, 75, 75, 75, 50, 125, 100, 0xFDF, 0xFEA, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.KILLCLAW, "Killclaw", 36, EnemyType.FOE, 0x5A, 1900, 179, 76, 41, 50, 50, 50, 125, 125, 125, 0xFF0, 0x0, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.MACABRE, "Macabre", 69, EnemyType.FOE, 0x62, 5000, 393, 134, 67, 50, 50, 100, 75, 75, 75, 0x106A, 0x0, 0x105B, DropCondition.NOT_STAB),
    EnemyData(EO1Enemies.DRAGOID, "Dragoid", 70, EnemyType.FOE, 0x65, 8500, 402, 136, 68, 100, 100, 125, 100, 100, 0, 0x1053, 0x1052, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.WYRMOID, "Wyrmoid", 70, EnemyType.FOE, 0x63, 8500, 402, 136, 68, 100, 100, 100, 0, 125, 100, 0x1053, 0x1050, 0x0, DropCondition.NONE),
    EnemyData(EO1Enemies.DRAKOID, "Drakoid", 70, EnemyType.FOE, 0x64, 8500, 402, 136, 68, 100, 100, 100, 125, 0, 100, 0x1053, 0x1051, 0x0, DropCondition.NONE),
]

ENEMY_BY_ID: dict[int, EnemyData] = {enemy.enemy_id:enemy for enemy in ALL_ENEMIES}
