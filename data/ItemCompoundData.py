from dataclasses import dataclass
from typing import TYPE_CHECKING

from .InventoryItemData import *
from .MaterialData import *

# TODO this is not super clean but i am not touching inventory items now.
class EO1ItemID:
    #JADE_ORE = 0x103C
    MEDICA = 0x10B7
    MEDICA_II = 0x10B8
    MEDICA_III = 0x10B9
    MEDICA_IV = 0x10BA
    MEDICA_V = 0x10BB
    AMRITA = 0x10BC
    AMRITA_II = 0x10BD
    HAMAO = 0x10BE
    HAMAOPRIME = 0x10BF
    SOMA = 0x10C0
    SOMAPRIME = 0x10C1
    NECTAR = 0x10C2
    NECTAR_II = 0x10C3
    NECTAR_III = 0x10C4
    THERIACA_A = 0x10C7
    THERIACA_B = 0x10C8
    AXCELA = 0x10CD
    AXCELA_II = 0x10CE
    AXCELA_III = 0x10CF
    BRAVANT = 0x10D1
    BRAVANT_II = 0x10D2
    STONARD = 0x10D3
    STONARD_II = 0x10D4
    FIRE_MIST = 0x10D7
    ICE_MIST = 0x10D8
    VOLT_MIST = 0x10D9
    ALL_MIST = 0x10DA
    BLAZE_OIL = 0x10DB
    FREEZE_OIL = 0x10DC
    SHOCK_OIL = 0x10DD
    WARD_CHIME = 0x10DF
    GOLD_CHIME = 0x10E0
    #DUMMY = 0x10EB
    MAGNET = 0x10EC
    #MAP_EVENT = 0x10ED
    #HOLY_WATER = 0x10EE
    #WATER = 0x10EF
    #BOTTLE = 0x10F0
    #JUNK_BOX = 0x10F1
    #JUNK_BOX = 0x10F2
    #LOCKET = 0x10F3
    #PLANT_SEED = 0x10F4
    #GOLD_STONE = 0x10F5
    #GOLD_STONE = 0x10F6
    #MOON_STONE = 0x10F7
    #GOUDA = 0x10F8
    #ODD_POWDER = 0x10F9
    #LUCKY_COIN = 0x10FA
    #RUST_SWORD = 0x10FB
    #BROKEN_AXE = 0x10FC
    #OLD_WAND = 0x10FD
    #PANACEA = 0x10FE
    #RARE_BLOOM = 0x10FF
    #GOLD_SEED = 0x1100
    #VOX_STONE = 0x1101
    #CLEAR_KEY = 0x1102
    #VIOLET_KEY = 0x1103
    #DRAGON_EGG = 0x1104
    #CARD_KEY = 0x1105
    #HOLY_GRAIL = 0x1106
    #COPPER_TOP = 0x1107
    #SHINY_DISC = 0x1108
    #SOFT_GLASS = 0x1109
    #TOKEN = 0x110A
    #CLAM_TOOL = 0x110B
    #MAGIC_DOWN = 0x110C
    #MAGIC_DOWN = 0x110D
    #MAGIC_DOWN = 0x110E
    #DIAMOND = 0x110F
    #BLACK_GEM = 0x1110
    #SHINY_GEM = 0x1111
    #OLD_SCROLL = 0x1112
    #HEX_BELL = 0x1113
    #MAP = 0x1114
    #RADHA_NOTE = 0x1115
    #WARP_WIRE = 0x1116
    #TOUGH_FANG = 0x1117
    #TOUGH_WING = 0x1119
    #FROZEN_ARM = 0x113D
    #ANKH_A = 0x113E
    #ANKH_B = 0x113F
    #ANKH_C = 0x1140
    #ANKH_D = 0x1141
    #ANKH_E = 0x1142
    #ANKH_MOTOR = 0x1143
    #BANDANNA = 0x1144
    #PEARL = 0x1145
    #RARE_MEAT = 0x1146
    KNIFE = 0x0001
    SCRAMASAX = 0x0002
    DAGGER = 0x0003
    SHORTSWORD = 0x0004
    BOAR_SPEAR = 0x0005
    BROADSWORD = 0x0006
    RAPIER = 0x0007
    VIKING = 0x0008
    SHAMSHIR = 0x0009
    CLAYMORE = 0x000A
    EXECUTOR = 0x000B
    KATZBALGER = 0x000C
    STEELSWORD = 0x000D
    EPEE = 0x000E
    LAST_ESTOC = 0x000F
    PATTISA = 0x0010
    FLAMBERGE = 0x0011
    DUERGAR = 0x0015
    SHINRYUU = 0x0017
    BONE_AXE = 0x001E
    HAND_AXE = 0x001F
    CELTIS = 0x0020
    BROADAXE = 0x0021
    BATTLE_AXE = 0x0022
    BILIOMG = 0x0023
    TABAR = 0x0024
    GREAT_AXE = 0x0025
    BARDICHE = 0x0026
    HALBERD = 0x0027
    WAND = 0x0028
    BREAKER = 0x0029
    LABYRIS = 0x002A
    FRANCISCA = 0x002B
    BHUJ = 0x002C
    FASCES_AXE = 0x002D
    FLAME_AXE = 0x0030
    METEOR_AXE = 0x0031
    HATCHET = 0x0032
    STAFF = 0x0036
    BONE_STAFF = 0x0037
    BONE_MACE = 0x0038
    DOWN_STAFF = 0x0039
    BONE_FLAIL = 0x003A
    GEM_STAFF = 0x003B
    WAR_MACE = 0x003C
    LUCK_STAFF = 0x003D
    GODENDAG = 0x003E
    MYSTIC_ROD = 0x003F
    WARHAMMER = 0x0040
    ARCANA_ROD = 0x0041
    SAGE_WAND = 0x0042
    WAKIZASHI = 0x0049
    UCHIGATANA = 0x004A
    OHDACHI = 0x004B
    KOGARASU = 0x004C
    SHIDA = 0x004D
    ZANMATOU = 0x004E
    KUZUNOSADA = 0x004F
    HACHI = 0x0050
    HISAMEMARU = 0x0051
    MASAMUNE = 0x0052
    WOOD_BOW = 0x0058
    ENAMEL_BOW = 0x0059
    SHORT_BOW = 0x005A
    BEAST_BOW = 0x005B
    HARD_SLING = 0x005C
    LONG_BOW = 0x005D
    HINDI = 0x005E
    SELF_BOW = 0x005F
    HUNTER_BOW = 0x0060
    FIN_BOW = 0x0061
    VINE_BOW = 0x0062
    HEAVEN_BOW = 0x0063
    SHIDGEDOU = 0x0064
    WAR_BOW = 0x0065
    ARBALEST = 0x0066
    FAILNAUGHT = 0x0067
    ZAMIEL_BOW = 0x0069
    ARC_DRAWER = 0x006A
    LIGHT_WHIP = 0x0070
    FANG_WHIP = 0x0071
    BULLWHIP = 0x0072
    VINE_WHIP = 0x0073
    NAIL_WHIP = 0x0074
    EDGE_WHIP = 0x0075
    TOXIC_WHIP = 0x0076
    GUM_WHIP = 0x0077
    WIND_WHIP = 0x0078
    SHRED_WHIP = 0x0079
    STING_WHIP = 0x007A
    BLADE_WHIP = 0x007B
    NINE_TAILS = 0x007C
    KNOUT = 0x007D
    DEAD_WHIP = 0x007E
    TORMENTOR = 0x007F
    DOMINATOR = 0x0081
    VOLT_WHIP = 0x0083
    THORN_WHIP = 0x0084
    TWEED = 0x03E9
    JERKIN = 0x03EA
    LEAF_COAT = 0x03EB
    HIDE_VEST = 0x03EC
    HIDE_ARMOR = 0x03ED
    PLATE = 0x03EE
    DOUBLET = 0x03EF
    BUFFCOAT = 0x03F0
    BRIAULT = 0x03F1
    CHAIN_MAIL = 0x03F2
    PETAL_COAT = 0x03F3
    LEAF_TUNIC = 0x03F4
    IRON_PLATE = 0x03F5
    RING_MAIL = 0x03F6
    OAK_JACKET = 0x03F7
    WING_COAT = 0x03F8
    HAUBERK = 0x03F9
    STUD_VEST = 0x03FB
    FANCY_COAT = 0x03FC
    COTARDIE = 0x03FD
    FULL_ARMOR = 0x03FE
    PLATE_MAIL = 0x03FF
    N7_DOUBLET = 0x0400
    SURCOAT = 0x0401
    TIGER_COAT = 0x0403
    FAIRY_ROBE = 0x0404
    DARK_TUNIC = 0x0405
    BRIGANDINE = 0x0406
    EBON_PLATE = 0x0407
    LYCORIS = 0x0408
    WYVERNMAIL = 0x0409
    JAZERAINT = 0x040A
    DEMON_COAT = 0x040B
    RUNE_TWEED = 0x040C
    RUNE_TUNIC = 0x040D
    BLOOD_MAIL = 0x040E
    COMPOSITE = 0x040F
    AZURE_COAT = 0x0410
    BLOOD_COAT = 0x0411
    DINO_PLATE = 0x0412
    DEMON_MAIL = 0x0413
    SYLPHEED = 0x0414
    HOLY_ARMOR = 0x0415
    GHOST_VEST = 0x0416
    MOBIUS_ALB = 0x0417
    ANGEL_ROBE = 0x0418
    FAIRY_MAIL = 0x0419
    RUBY_MAIL = 0x041A
    HEX_MANTLE = 0x041B
    MOSS_COAT = 0x041C
    FLAME_COAT = 0x041D
    FROST_COAT = 0x041E
    VOLT_COAT = 0x041F
    HAIRPIN = 0x07D1
    HIDE_HAT = 0x07D2
    PLUMED_HAT = 0x07D3
    CHAIN_HELM = 0x07D4
    GUM_HELM = 0x07D5
    SCALE_HELM = 0x07D6
    SCALE_CAP = 0x07D7
    SANDY_PIN = 0x07D8
    TIGER_CAP = 0x07D9
    CIRCLET = 0x07DA
    BLOOD_HELM = 0x07DB
    ANGEL_HELM = 0x07DC
    KNIT_GLOVE = 0x07E2
    HIDE_GLOVE = 0x07E3
    DOWN_GLOVE = 0x07E4
    IRON_GLOVE = 0x07E5
    BEAR_GLOVE = 0x07E6
    GUM_GLOVE = 0x07E7
    FANG_GLOVE = 0x07E8
    SAND_GLOVE = 0x07E9
    TIGER_HAND = 0x07EA
    RUNE_GLOVE = 0x07EB
    BLOOD_GAGE = 0x07EC
    BRAVE_GAGE = 0x07ED
    EBON_GLOVE = 0x07EE
    ATHANOR = 0x07EF
    RUBY_GAGE = 0x07F0
    TOXIC_GAGE = 0x07F1
    TARGE = 0x07F6
    HIDE_ASPIS = 0x07F7
    ASPIS = 0x07F8
    OVAL_ASPIS = 0x07F9
    HEAT_ASPIS = 0x07FA
    GUM_ASPIS = 0x07FB
    BODY_ASPIS = 0x07FC
    EBON_ASPIS = 0x07FD
    MOON_ASPIS = 0x07FE
    KING_ASPIS = 0x07FF
    HALO_ASPIS = 0x0800
    HOLY_ASPIS = 0x0801
    PAIN_ASPIS = 0x0802
    LEAF_BOOT = 0x0808
    HIDE_BOOT = 0x0809
    PLUME_BOOT = 0x080A
    CHAIN_BOOT = 0x080B
    MOCCASINS = 0x080C
    SCALE_BOOT = 0x080D
    FAIRY_BOOT = 0x080E
    TIGER_BOOT = 0x080F
    FLAME_BOOT = 0x0810
    FUR_BOOT = 0x0811
    DYED_BOOT = 0x0812
    SPEED_BOOT = 0x0813
    HIDE_BELT = 0x0BB9
    HIDE_RING = 0x0BBA
    RED_CHARM = 0x0BBB
    PETAL_RING = 0x0BBC
    CUT_CHARM = 0x0BBD
    GEM_RING = 0x0BBE
    LEAF_CAPE = 0x0BBF
    FIRE_RING = 0x0BC0
    STAR_CHARM = 0x0BC1
    TUSK_CHARM = 0x0BC2
    OLD_CHOKER = 0x0BC3
    HIDE_CAPE = 0x0BC4
    AMBER_RING = 0x0BC5
    SEA_CHARM = 0x0BC6
    BLUE_RING = 0x0BC7
    RED_CAPE = 0x0BC8
    EVIL_CHARM = 0x0BC9
    ROSE_RING = 0x0BCA
    ROYAL_RING = 0x0BCB
    GOLD_CAPE = 0x0BCC
    ANGEL_RING = 0x0BCD
    WARD_GEM = 0x0BCE
    JEWEL_EYE = 0x0BCF
    RUBY = 0x0BD0
    SAPPHIRE = 0x0BD1
    TOPAZ = 0x0BD2
    TOURMALINE = 0x0BD3
    ADAMAS = 0x0BD4
    HEX_DOLL = 0x0BD5
    OCARINA = 0x0BD6
    LUTE = 0x0BD7
    FLUTE = 0x0BD8
    KITHARA = 0x0BD9
    AULOS = 0x0BDA
    ANGEL_HARP = 0x0BDB
    SYRINX = 0x0BDC
    TOWN_MEDAL = 0x0BDD
    TOWN_CROWN = 0x0BDE
    MOSS_RING = 0x0BDF
    MOSS_BAND = 0x0BE0

@dataclass
class EO1ItemCompound:
    item_id: int
    material_1_id: int
    material_2_id: int
    material_3_id: int
    material_1_count: int
    material_2_count: int
    material_3_count: int


ITEM_COMPOUND_TABLE: list[EO1ItemCompound] = [
    EO1ItemCompound(EO1ItemID.DAGGER, EO1MaterialID.SMALL_FANG, 0, 0, 3, 0, 0),
    EO1ItemCompound(EO1ItemID.SHORTSWORD, EO1MaterialID.HARDWOOD, EO1MaterialID.HARD_SHELL, 0, 1, 1, 0),
    EO1ItemCompound(EO1ItemID.BOAR_SPEAR, EO1MaterialID.LARGE_FANG, EO1MaterialID.THORN, 0, 1, 5, 0),
    EO1ItemCompound(EO1ItemID.BROADSWORD, EO1MaterialID.STEEL_LUMP, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.RAPIER, EO1MaterialID.IRON_SHELL, EO1MaterialID.LIGHT_WOOD, 0, 1, 10, 0),
    EO1ItemCompound(EO1ItemID.VIKING, EO1MaterialID.SHARP_HORN, EO1MaterialID.TIGER_FANG, 0, 1, 1, 0),
    EO1ItemCompound(EO1ItemID.SHAMSHIR, EO1MaterialID.ELASTIC, EO1MaterialID.STEEL_BONE, 0, 5, 5, 0),
    EO1ItemCompound(EO1ItemID.CLAYMORE, EO1MaterialID.CARAPACE, EO1MaterialID.SHRED_NAIL, 0, 1, 1, 0),
    EO1ItemCompound(EO1ItemID.EXECUTOR, EO1MaterialID.DEATH_CLAW, EO1MaterialID.RED_HIDE, 0, 1, 1, 0),
    EO1ItemCompound(EO1ItemID.KATZBALGER, EO1MaterialID.HEATED_FUR, EO1MaterialID.SHINY_HORN, 0, 5, 1, 0),
    EO1ItemCompound(EO1ItemID.STEELSWORD, EO1MaterialID.STEEL_CHIP, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.EPEE, EO1MaterialID.WHITE_FANG, EO1MaterialID.STEEL_CLAW, 0, 5, 1, 0),
    EO1ItemCompound(EO1ItemID.LAST_ESTOC, EO1MaterialID.SPACE_NAIL, EO1MaterialID.REX_THROAT, 0, 1, 2, 0),
    EO1ItemCompound(EO1ItemID.PATTISA, EO1MaterialID.SPACE_CLAW, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.FLAMBERGE, EO1MaterialID.SPACE_NAIL, 0, 0, 5, 0, 0),
    EO1ItemCompound(EO1ItemID.DUERGAR, EO1MaterialID.SWORD_RIB, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.SHINRYUU, EO1MaterialID.FIRE_SCALE, EO1MaterialID.ICE_SCALE, EO1MaterialID.VOLT_SCALE, 1, 1, 1),
    EO1ItemCompound(EO1ItemID.BONE_AXE, EO1MaterialID.BEAST_BONE, 0, 0, 5, 0, 0),
    EO1ItemCompound(EO1ItemID.HAND_AXE, EO1MaterialID.HARDWOOD, EO1MaterialID.HARD_SHELL, 0, 5, 5, 0),
    EO1ItemCompound(EO1ItemID.CELTIS, EO1MaterialID.HUGE_FANG, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.BROADAXE, EO1MaterialID.STEEL_LUMP, 0, 0, 5, 0, 0),
    EO1ItemCompound(EO1ItemID.BATTLE_AXE, EO1MaterialID.IRON_SHELL, EO1MaterialID.STEEL_LUMP, 0, 1, 5, 0),
    EO1ItemCompound(EO1ItemID.BILIOMG, EO1MaterialID.BIRD_LIMB, EO1MaterialID.IRON_SHELL, 0, 1, 5, 0),
    EO1ItemCompound(EO1ItemID.TABAR, EO1MaterialID.BONE_SHARD, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.GREAT_AXE, EO1MaterialID.CARAPACE, 0, 0, 5, 0, 0),
    EO1ItemCompound(EO1ItemID.BARDICHE, EO1MaterialID.RED_BLADE, EO1MaterialID.BLOOD_FANG, 0, 1, 5, 0),
    EO1ItemCompound(EO1ItemID.HALBERD, EO1MaterialID.NYX_SCYTHE, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.BREAKER, EO1MaterialID.HARD_SHARD, EO1MaterialID.BROKEN_EYE, 0, 5, 3, 0),
    EO1ItemCompound(EO1ItemID.LABYRIS, EO1MaterialID.SAND_TWIG, EO1MaterialID.STEEL_CLAW, 0, 10, 1, 0),
    EO1ItemCompound(EO1ItemID.FRANCISCA, EO1MaterialID.SPACE_NAIL, 0, 0, 5, 0, 0),
    EO1ItemCompound(EO1ItemID.BHUJ, EO1MaterialID.GOLD_HORN, EO1MaterialID.GOLD_TUSK, 0, 1, 1, 0),
    EO1ItemCompound(EO1ItemID.FASCES_AXE, EO1MaterialID.DEATH_STEM, EO1MaterialID.SPACE_HUSK, EO1MaterialID.SPACE_CLAW, 10, 5, 1),
    EO1ItemCompound(EO1ItemID.FLAME_AXE, EO1MaterialID.FIRE_FANG, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.METEOR_AXE, EO1MaterialID.STATUE_ARM, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.BONE_STAFF, EO1MaterialID.BEAST_BONE, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.BONE_MACE, EO1MaterialID.BEAST_BONE, EO1MaterialID.LARGE_FANG, 0, 15, 1, 0),
    EO1ItemCompound(EO1ItemID.DOWN_STAFF, EO1MaterialID.FEATHER, EO1MaterialID.LIGHT_WOOD, 0, 1, 5, 0),
    EO1ItemCompound(EO1ItemID.BONE_FLAIL, EO1MaterialID.TAILBONE, EO1MaterialID.BIRD_TALON, 0, 5, 1, 0),
    EO1ItemCompound(EO1ItemID.GEM_STAFF, EO1MaterialID.GLASS_EYE, 0, 0, 2, 0, 0),
    EO1ItemCompound(EO1ItemID.WAR_MACE, EO1MaterialID.CARAPACE, 0, 0, 10, 0, 0),
    EO1ItemCompound(EO1ItemID.LUCK_STAFF, EO1MaterialID.PURE_ROOT, 0, 0, 3, 0, 0),
    EO1ItemCompound(EO1ItemID.GODENDAG, EO1MaterialID.RED_BEAK, EO1MaterialID.STEEL_CHIP, 0, 5, 5, 0),
    EO1ItemCompound(EO1ItemID.MYSTIC_ROD, EO1MaterialID.GEM_CORE, 0, 0, 2, 0, 0),
    EO1ItemCompound(EO1ItemID.WARHAMMER, EO1MaterialID.SPACE_HUSK, EO1MaterialID.TINY_TOOTH, 0, 10, 10, 0),
    EO1ItemCompound(EO1ItemID.ARCANA_ROD, EO1MaterialID.ROYAL_MANE, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.SAGE_WAND, EO1MaterialID.BEAST_EYE, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.WAKIZASHI, EO1MaterialID.HARDWOOD, EO1MaterialID.METAL_HORN, 0, 5, 1, 0),
    EO1ItemCompound(EO1ItemID.UCHIGATANA, EO1MaterialID.IRON_SHELL, 0, 0, 3, 0, 0),
    EO1ItemCompound(EO1ItemID.OHDACHI, EO1MaterialID.SHRED_NAIL, EO1MaterialID.BUG_NEST, 0, 3, 5, 0),
    EO1ItemCompound(EO1ItemID.KOGARASU, EO1MaterialID.SHINY_HORN, 0, 0, 5, 0, 0),
    EO1ItemCompound(EO1ItemID.SHIDA, EO1MaterialID.STEEL_CHIP, 0, 0, 5, 0, 0),
    EO1ItemCompound(EO1ItemID.ZANMATOU, EO1MaterialID.SPACE_CLAW, 0, 0, 5, 0, 0),
    EO1ItemCompound(EO1ItemID.KUZUNOSADA, EO1MaterialID.GOLD_HORN, 0, 0, 5, 0, 0),
    EO1ItemCompound(EO1ItemID.HACHI, EO1MaterialID.ANTS_JAW, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.HISAMEMARU, EO1MaterialID.FROST_BONE, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.MASAMUNE, EO1MaterialID.DEMON_CORE, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.ENAMEL_BOW, EO1MaterialID.HORN, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.SHORT_BOW, EO1MaterialID.HORN, EO1MaterialID.GUM_HIDE, 0, 2, 5, 0),
    EO1ItemCompound(EO1ItemID.BEAST_BOW, EO1MaterialID.LARGE_FANG, EO1MaterialID.GUM_HIDE, 0, 1, 10, 0),
    EO1ItemCompound(EO1ItemID.HARD_SLING, EO1MaterialID.LIGHT_WOOD, EO1MaterialID.STICKY_GOO, 0, 5, 3, 0),
    EO1ItemCompound(EO1ItemID.LONG_BOW, EO1MaterialID.GUM_VINE, EO1MaterialID.TAILBONE, 0, 5, 1, 0),
    EO1ItemCompound(EO1ItemID.HINDI, EO1MaterialID.TAILBONE, EO1MaterialID.SHARP_HORN, 0, 4, 1, 0),
    EO1ItemCompound(EO1ItemID.SELF_BOW, EO1MaterialID.ELASTIC, 0, 0, 5, 0, 0),
    EO1ItemCompound(EO1ItemID.HUNTER_BOW, EO1MaterialID.BAT_WING, EO1MaterialID.BONE_SHARD, 0, 5, 5, 0),
    EO1ItemCompound(EO1ItemID.FIN_BOW, EO1MaterialID.HUGE_FIN, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.VINE_BOW, EO1MaterialID.TENDON, EO1MaterialID.DRIED_VINE, 0, 1, 1, 0),
    EO1ItemCompound(EO1ItemID.HEAVEN_BOW, EO1MaterialID.DRIED_VINE, EO1MaterialID.SAND_TWIG, 0, 1, 5, 0),
    EO1ItemCompound(EO1ItemID.SHIDGEDOU, EO1MaterialID.THROB_VINE, EO1MaterialID.DRIED_VINE, 0, 4, 5, 0),
    EO1ItemCompound(EO1ItemID.WAR_BOW, EO1MaterialID.REX_THROAT, 0, 0, 5, 0, 0),
    EO1ItemCompound(EO1ItemID.ARBALEST, EO1MaterialID.GOLD_HORN, EO1MaterialID.DEATH_STEM, 0, 1, 5, 0),
    EO1ItemCompound(EO1ItemID.FAILNAUGHT, EO1MaterialID.SPACE_CLAW, EO1MaterialID.ROYAL_HIDE, 0, 1, 1, 0),
    EO1ItemCompound(EO1ItemID.ZAMIEL_BOW, EO1MaterialID.EBON_PLUME, 0, 0, 10, 0, 0),
    EO1ItemCompound(EO1ItemID.ARC_DRAWER, EO1MaterialID.ICE_SPINE, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.FANG_WHIP, EO1MaterialID.SMALL_FANG, EO1MaterialID.SOFT_HIDE, 0, 5, 5, 0),
    EO1ItemCompound(EO1ItemID.BULLWHIP, EO1MaterialID.VINE, EO1MaterialID.GUM_HIDE, 0, 5, 5, 0),
    EO1ItemCompound(EO1ItemID.VINE_WHIP, EO1MaterialID.VINE, EO1MaterialID.THORN, 0, 10, 10, 0),
    EO1ItemCompound(EO1ItemID.NAIL_WHIP, EO1MaterialID.BENT_CLAW, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.EDGE_WHIP, EO1MaterialID.GUM_VINE, EO1MaterialID.BENT_CLAW, 0, 1, 1, 0),
    EO1ItemCompound(EO1ItemID.TOXIC_WHIP, EO1MaterialID.STINGER, EO1MaterialID.TOXIC_BARB, 0, 10, 1, 0),
    EO1ItemCompound(EO1ItemID.GUM_WHIP, EO1MaterialID.GUM_THROAT, 0, 0, 5, 0, 0),
    EO1ItemCompound(EO1ItemID.WIND_WHIP, EO1MaterialID.CRAB_LEG, EO1MaterialID.SHRED_NAIL, 0, 1, 5, 0),
    EO1ItemCompound(EO1ItemID.SHRED_WHIP, EO1MaterialID.DEATH_CLAW, EO1MaterialID.CRAB_LEG, 0, 1, 5, 0),
    EO1ItemCompound(EO1ItemID.STING_WHIP, EO1MaterialID.WHITE_FANG, EO1MaterialID.HEATED_FUR, 0, 1, 5, 0),
    EO1ItemCompound(EO1ItemID.BLADE_WHIP, EO1MaterialID.STEEL_CHIP, EO1MaterialID.TENDON, 0, 1, 5, 0),
    EO1ItemCompound(EO1ItemID.NINE_TAILS, EO1MaterialID.RED_STRING, EO1MaterialID.RED_THREAD, 0, 3, 3, 0),
    EO1ItemCompound(EO1ItemID.KNOUT, EO1MaterialID.REX_THROAT, EO1MaterialID.RED_BLOOD, 0, 3, 3, 0),
    EO1ItemCompound(EO1ItemID.DEAD_WHIP, EO1MaterialID.DEATH_STEM, EO1MaterialID.GOLD_TUSK, 0, 5, 1, 0),
    EO1ItemCompound(EO1ItemID.TORMENTOR, EO1MaterialID.ROYAL_HIDE, EO1MaterialID.ANGEL_WING, 0, 1, 10, 0),
    EO1ItemCompound(EO1ItemID.DOMINATOR, EO1MaterialID.ROSE_WHIP, EO1MaterialID.WINE_WHIP, 0, 1, 1, 0),
    EO1ItemCompound(EO1ItemID.VOLT_WHIP, EO1MaterialID.BARBEL, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.THORN_WHIP, EO1MaterialID.ROYAL_VINE, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.TWEED, 0, 0, 0, 7, 0, 0),
    EO1ItemCompound(EO1ItemID.JERKIN, EO1MaterialID.SOFT_HIDE, 0, 0, 7, 0, 0),
    EO1ItemCompound(EO1ItemID.LEAF_COAT, EO1MaterialID.VINE, EO1MaterialID.TINY_PETAL, 0, 5, 1, 0),
    EO1ItemCompound(EO1ItemID.HIDE_VEST, EO1MaterialID.GUM_HIDE, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.HIDE_ARMOR, EO1MaterialID.STIFF_HIDE, 0, 0, 5, 0, 0),
    EO1ItemCompound(EO1ItemID.PLATE, EO1MaterialID.METAL_HORN, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.DOUBLET, EO1MaterialID.HARE_TAIL, 0, 0, 3, 0, 0),
    EO1ItemCompound(EO1ItemID.BUFFCOAT, EO1MaterialID.HARE_TAIL, EO1MaterialID.GUM_HIDE, EO1MaterialID.VINE, 1, 1, 1),
    EO1ItemCompound(EO1ItemID.BRIAULT, EO1MaterialID.WHITE_HIDE, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.CHAIN_MAIL, EO1MaterialID.STEEL_LUMP, EO1MaterialID.STINGER, 0, 5, 3, 0),
    EO1ItemCompound(EO1ItemID.PETAL_COAT, EO1MaterialID.DYE_PETAL, EO1MaterialID.STICKY_WEB, 0, 3, 1, 0),
    EO1ItemCompound(EO1ItemID.LEAF_TUNIC, EO1MaterialID.THICK_LEAF, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.IRON_PLATE, EO1MaterialID.IRON_SHELL, EO1MaterialID.STINGER, 0, 3, 3, 0),
    EO1ItemCompound(EO1ItemID.RING_MAIL, EO1MaterialID.IRON_SHELL, EO1MaterialID.BIRD_TALON, 0, 5, 1, 0),
    EO1ItemCompound(EO1ItemID.OAK_JACKET, EO1MaterialID.SCENT_WOOD, EO1MaterialID.FEATHER, 0, 3, 3, 0),
    EO1ItemCompound(EO1ItemID.WING_COAT, EO1MaterialID.FEATHER, 0, 0, 10, 0, 0),
    EO1ItemCompound(EO1ItemID.HAUBERK, EO1MaterialID.THIN_SHELL, EO1MaterialID.STEEL_LUMP, 0, 1, 12, 0),
    EO1ItemCompound(EO1ItemID.STUD_VEST, EO1MaterialID.ELASTIC, 0, 0, 3, 0, 0),
    EO1ItemCompound(EO1ItemID.FANCY_COAT, EO1MaterialID.GUM_THROAT, EO1MaterialID.GLASS_EYE, 0, 3, 1, 0),
    EO1ItemCompound(EO1ItemID.COTARDIE, EO1MaterialID.ELASTIC, EO1MaterialID.BAT_WING, 0, 7, 3, 0),
    EO1ItemCompound(EO1ItemID.FULL_ARMOR, EO1MaterialID.CARAPACE, EO1MaterialID.RED_HIDE, 0, 3, 1, 0),
    EO1ItemCompound(EO1ItemID.PLATE_MAIL, EO1MaterialID.CARAPACE, EO1MaterialID.FISH_SCALE, 0, 7, 3, 0),
    EO1ItemCompound(EO1ItemID.N7_DOUBLET, EO1MaterialID.SHINY_GOO, EO1MaterialID.BAT_WING, 0, 1, 7, 0),
    EO1ItemCompound(EO1ItemID.SURCOAT, EO1MaterialID.RED_HIDE, 0, 0, 2, 0, 0),
    EO1ItemCompound(EO1ItemID.TIGER_COAT, EO1MaterialID.WHITE_SKIN, 0, 0, 3, 0, 0),
    EO1ItemCompound(EO1ItemID.FAIRY_ROBE, EO1MaterialID.FAIRY_WING, 0, 0, 3, 0, 0),
    EO1ItemCompound(EO1ItemID.DARK_TUNIC, EO1MaterialID.SAND_CLOTH, EO1MaterialID.INK_STICK, 0, 3, 3, 0),
    EO1ItemCompound(EO1ItemID.BRIGANDINE, EO1MaterialID.STEEL_CHIP, EO1MaterialID.RED_PLUME, 0, 3, 3, 0),
    EO1ItemCompound(EO1ItemID.EBON_PLATE, EO1MaterialID.STEEL_CHIP, EO1MaterialID.INK_STICK, 0, 4, 7, 0),
    EO1ItemCompound(EO1ItemID.LYCORIS, EO1MaterialID.RED_PLUME, EO1MaterialID.INK_STICK, 0, 4, 5, 0),
    EO1ItemCompound(EO1ItemID.WYVERNMAIL, EO1MaterialID.TOUGH_WING, EO1MaterialID.RED_BEAK, EO1MaterialID.STEEL_CHIP, 1, 1, 5),
    EO1ItemCompound(EO1ItemID.JAZERAINT, EO1MaterialID.WHITE_SKIN, EO1MaterialID.RED_STRING, EO1MaterialID.RED_THREAD, 7, 1, 1),
    EO1ItemCompound(EO1ItemID.DEMON_COAT, EO1MaterialID.DEMON_FUR, 0, 0, 3, 0, 0),
    EO1ItemCompound(EO1ItemID.RUNE_TWEED, EO1MaterialID.RED_FUR, EO1MaterialID.RED_BLOOD, 0, 3, 1, 0),
    EO1ItemCompound(EO1ItemID.RUNE_TUNIC, EO1MaterialID.RED_FUR, EO1MaterialID.GUM_THREAD, 0, 2, 5, 0),
    EO1ItemCompound(EO1ItemID.BLOOD_MAIL, EO1MaterialID.SPACE_HUSK, 0, 0, 2, 0, 0),
    EO1ItemCompound(EO1ItemID.COMPOSITE, EO1MaterialID.SPACE_HUSK, 0, 0, 5, 0, 0),
    EO1ItemCompound(EO1ItemID.AZURE_COAT, EO1MaterialID.GOLD_FUR, EO1MaterialID.BLUE_BLOOD, 0, 5, 10, 0),
    EO1ItemCompound(EO1ItemID.BLOOD_COAT, EO1MaterialID.GOLD_FUR, EO1MaterialID.RED_BLOOD, 0, 5, 10, 0),
    EO1ItemCompound(EO1ItemID.DINO_PLATE, EO1MaterialID.STERNUM, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.DEMON_MAIL, EO1MaterialID.EVIL_SHELL, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.SYLPHEED, EO1MaterialID.EVIL_PLUME, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.HOLY_ARMOR, EO1MaterialID.N1000_SHELL, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.GHOST_VEST, EO1MaterialID.GEM_SCALE, 0, 0, 10, 0, 0),
    EO1ItemCompound(EO1ItemID.MOBIUS_ALB, EO1MaterialID.GEM_PLUME, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.ANGEL_ROBE, EO1MaterialID.GOLD_PLUME, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.FAIRY_MAIL, EO1MaterialID.VELVET, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.RUBY_MAIL, EO1MaterialID.RUBY_SKULL, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.HEX_MANTLE, EO1MaterialID.HEX_CHAIN, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.MOSS_COAT, EO1MaterialID.SHROUD, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.FLAME_COAT, EO1MaterialID.FLAME_SKIN, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.FROST_COAT, EO1MaterialID.FROST_SKIN, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.VOLT_COAT, EO1MaterialID.VOLT_SKIN, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.HIDE_HAT, EO1MaterialID.SOFT_HIDE, EO1MaterialID.GUM_HIDE, 0, 3, 1, 0),
    EO1ItemCompound(EO1ItemID.PLUMED_HAT, EO1MaterialID.FEATHER, 0, 0, 5, 0, 0),
    EO1ItemCompound(EO1ItemID.CHAIN_HELM, EO1MaterialID.STEEL_LUMP, EO1MaterialID.STINGER, 0, 3, 1, 0),
    EO1ItemCompound(EO1ItemID.GUM_HELM, EO1MaterialID.ELASTIC, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.SCALE_HELM, EO1MaterialID.FISH_SCALE, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.SCALE_CAP, EO1MaterialID.FISH_SCALE, 0, 0, 12, 0, 0),
    EO1ItemCompound(EO1ItemID.SANDY_PIN, EO1MaterialID.SAND_TWIG, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.TIGER_CAP, EO1MaterialID.WHITE_SKIN, 0, 0, 3, 0, 0),
    EO1ItemCompound(EO1ItemID.CIRCLET, EO1MaterialID.GOLD_SHELL, EO1MaterialID.GEM_CORE, 0, 1, 1, 0),
    EO1ItemCompound(EO1ItemID.BLOOD_HELM, EO1MaterialID.SPACE_HUSK, EO1MaterialID.RED_BLOOD, 0, 3, 3, 0),
    EO1ItemCompound(EO1ItemID.ANGEL_HELM, EO1MaterialID.HELL_WING, 0, 0, 10, 0, 0),
    EO1ItemCompound(EO1ItemID.HIDE_GLOVE, EO1MaterialID.SOFT_HIDE, EO1MaterialID.GUM_HIDE, 0, 7, 3, 0),
    EO1ItemCompound(EO1ItemID.DOWN_GLOVE, EO1MaterialID.FEATHER, EO1MaterialID.BIRD_TALON, 0, 7, 3, 0),
    EO1ItemCompound(EO1ItemID.IRON_GLOVE, EO1MaterialID.STEEL_LUMP, EO1MaterialID.TIGER_FUR, 0, 3, 2, 0),
    EO1ItemCompound(EO1ItemID.BEAR_GLOVE, EO1MaterialID.BEAR_FUR, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.GUM_GLOVE, EO1MaterialID.ELASTIC, EO1MaterialID.FISH_FIN, 0, 7, 1, 0),
    EO1ItemCompound(EO1ItemID.FANG_GLOVE, EO1MaterialID.FISH_SCALE, EO1MaterialID.BLOOD_FANG, 0, 3, 3, 0),
    EO1ItemCompound(EO1ItemID.SAND_GLOVE, EO1MaterialID.SAND_CLOTH, 0, 0, 7, 0, 0),
    EO1ItemCompound(EO1ItemID.TIGER_HAND, EO1MaterialID.WHITE_SKIN, EO1MaterialID.DRIED_VINE, 0, 3, 1, 0),
    EO1ItemCompound(EO1ItemID.RUNE_GLOVE, EO1MaterialID.RED_FUR, EO1MaterialID.GEM_CORE, 0, 2, 1, 0),
    EO1ItemCompound(EO1ItemID.BLOOD_GAGE, EO1MaterialID.SPACE_HUSK, EO1MaterialID.RED_BLOOD, EO1MaterialID.SPACE_CLAW, 2, 1, 4),
    EO1ItemCompound(EO1ItemID.BRAVE_GAGE, EO1MaterialID.EVIL_SCALE, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.EBON_GLOVE, EO1MaterialID.BLACK_ROOT, 0, 0, 3, 0, 0),
    EO1ItemCompound(EO1ItemID.ATHANOR, EO1MaterialID.HEX_MARROW, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.RUBY_GAGE, EO1MaterialID.RUBY_BONE, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.TOXIC_GAGE, EO1MaterialID.TOXIC_HAND, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.HIDE_ASPIS, EO1MaterialID.SOFT_HIDE, 0, 0, 10, 0, 0),
    EO1ItemCompound(EO1ItemID.ASPIS, EO1MaterialID.HARD_SHELL, EO1MaterialID.HARDWOOD, 0, 5, 10, 0),
    EO1ItemCompound(EO1ItemID.OVAL_ASPIS, EO1MaterialID.STEEL_LUMP, EO1MaterialID.STINGER, 0, 3, 9, 0),
    EO1ItemCompound(EO1ItemID.HEAT_ASPIS, EO1MaterialID.IRON_SHELL, EO1MaterialID.LIGHT_WOOD, 0, 3, 1, 0),
    EO1ItemCompound(EO1ItemID.GUM_ASPIS, EO1MaterialID.ELASTIC, EO1MaterialID.BUG_NEST, 0, 3, 1, 0),
    EO1ItemCompound(EO1ItemID.BODY_ASPIS, EO1MaterialID.RED_BLADE, EO1MaterialID.BUG_NEST, EO1MaterialID.CARAPACE, 1, 3, 9),
    EO1ItemCompound(EO1ItemID.EBON_ASPIS, EO1MaterialID.HARD_SHARD, EO1MaterialID.INK_STICK, EO1MaterialID.STEEL_CHIP, 3, 3, 3),
    EO1ItemCompound(EO1ItemID.MOON_ASPIS, EO1MaterialID.SILVER_EYE, 0, 0, 3, 0, 0),
    EO1ItemCompound(EO1ItemID.KING_ASPIS, EO1MaterialID.GOLD_SHELL, EO1MaterialID.SPACE_HUSK, 0, 10, 7, 0),
    EO1ItemCompound(EO1ItemID.HALO_ASPIS, EO1MaterialID.ANGEL_WING, EO1MaterialID.SPACE_CLAW, 0, 8, 5, 0),
    EO1ItemCompound(EO1ItemID.HOLY_ASPIS, EO1MaterialID.OLD_SHELL, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.PAIN_ASPIS, EO1MaterialID.N1000_SHELL, EO1MaterialID.N100_SHELL, 0, 5, 5, 0),
    EO1ItemCompound(EO1ItemID.HIDE_BOOT, EO1MaterialID.SOFT_HIDE, EO1MaterialID.GUM_HIDE, 0, 9, 5, 0),
    EO1ItemCompound(EO1ItemID.PLUME_BOOT, EO1MaterialID.FEATHER, 0, 0, 12, 0, 0),
    EO1ItemCompound(EO1ItemID.CHAIN_BOOT, EO1MaterialID.STEEL_LUMP, EO1MaterialID.TIGER_FUR, 0, 3, 5, 0),
    EO1ItemCompound(EO1ItemID.MOCCASINS, EO1MaterialID.RED_HIDE, 0, 0, 3, 0, 0),
    EO1ItemCompound(EO1ItemID.SCALE_BOOT, EO1MaterialID.FISH_SCALE, EO1MaterialID.FISH_FIN, 0, 7, 1, 0),
    EO1ItemCompound(EO1ItemID.FAIRY_BOOT, EO1MaterialID.SAND_CLOTH, EO1MaterialID.FAIRY_WING, 0, 3, 5, 0),
    EO1ItemCompound(EO1ItemID.TIGER_BOOT, EO1MaterialID.WHITE_SKIN, 0, 0, 7, 0, 0),
    EO1ItemCompound(EO1ItemID.FLAME_BOOT, EO1MaterialID.FIRE_TAIL, EO1MaterialID.STEEL_CHIP, 0, 3, 7, 0),
    EO1ItemCompound(EO1ItemID.FUR_BOOT, EO1MaterialID.GOLD_FUR, EO1MaterialID.GUM_THREAD, 0, 2, 4, 0),
    EO1ItemCompound(EO1ItemID.DYED_BOOT, EO1MaterialID.GOLD_SHELL, EO1MaterialID.RED_BLOOD, EO1MaterialID.RED_FUR, 1, 4, 1),
    EO1ItemCompound(EO1ItemID.SPEED_BOOT, EO1MaterialID.EVIL_CREST, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.HIDE_RING, EO1MaterialID.SOFT_HIDE, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.RED_CHARM, EO1MaterialID.RED_FRUIT, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.PETAL_RING, EO1MaterialID.TINY_PETAL, 0, 0, 10, 0, 0),
    EO1ItemCompound(EO1ItemID.CUT_CHARM, EO1MaterialID.SCYTHE, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.GEM_RING, EO1MaterialID.PYROXENE, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.LEAF_CAPE, EO1MaterialID.THICK_LEAF, 0, 0, 5, 0, 0),
    EO1ItemCompound(EO1ItemID.FIRE_RING, EO1MaterialID.CARMINITE, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.STAR_CHARM, EO1MaterialID.STARSEED, 0, 0, 3, 0, 0),
    EO1ItemCompound(EO1ItemID.TUSK_CHARM, EO1MaterialID.GREAT_TUSK, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.OLD_CHOKER, EO1MaterialID.FOSSIL, 0, 0, 3, 0, 0),
    EO1ItemCompound(EO1ItemID.HIDE_CAPE, EO1MaterialID.GATOR_SKIN, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.AMBER_RING, EO1MaterialID.N100_SHELL, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.SEA_CHARM, EO1MaterialID.STAB_SHELL, EO1MaterialID.SEA_BRANCH, EO1MaterialID.ROCK_CORAL, 1, 1, 1),
    EO1ItemCompound(EO1ItemID.BLUE_RING, EO1MaterialID.CORUNDUM, 0, 0, 2, 0, 0),
    EO1ItemCompound(EO1ItemID.RED_CAPE, EO1MaterialID.RED_PLUME, 0, 0, 5, 0, 0),
    EO1ItemCompound(EO1ItemID.EVIL_CHARM, EO1MaterialID.MUSK, EO1MaterialID.NYX_SCYTHE, 0, 5, 3, 0),
    EO1ItemCompound(EO1ItemID.ROSE_RING, EO1MaterialID.OLEANDER, EO1MaterialID.SAND_TWIG, 0, 1, 2, 0),
    EO1ItemCompound(EO1ItemID.ROYAL_RING, EO1MaterialID.CULLINAN, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.GOLD_CAPE, EO1MaterialID.GOLD_FUR, EO1MaterialID.GUM_THREAD, 0, 3, 5, 0),
    EO1ItemCompound(EO1ItemID.ANGEL_RING, EO1MaterialID.SHINY_VINE, EO1MaterialID.ANGEL_WING, 0, 1, 3, 0),
    EO1ItemCompound(EO1ItemID.WARD_GEM, EO1MaterialID.CURSE_TUSK, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.JEWEL_EYE, EO1MaterialID.GEM_CORE, EO1MaterialID.SHINY_VINE, 0, 2, 1, 0),
    EO1ItemCompound(EO1ItemID.RUBY, EO1MaterialID.RED_ORE, 0, 0, 30, 0, 0),
    EO1ItemCompound(EO1ItemID.SAPPHIRE, EO1MaterialID.AZURE_ORE, 0, 0, 30, 0, 0),
    EO1ItemCompound(EO1ItemID.TOPAZ, EO1MaterialID.YELLOW_ORE, 0, 0, 30, 0, 0),
    EO1ItemCompound(EO1ItemID.TOURMALINE, EO1MaterialID.TRI_COLOR, 0, 0, 10, 0, 0),
    EO1ItemCompound(EO1ItemID.ADAMAS, EO1MaterialID.CULLINAN, 0, 0, 50, 0, 0),
    EO1ItemCompound(EO1ItemID.HEX_DOLL, EO1MaterialID.HEADROOT, EO1MaterialID.ARMROOT, EO1MaterialID.LEGROOT, 1, 1, 1),
    EO1ItemCompound(EO1ItemID.OCARINA, EO1MaterialID.HORN, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.LUTE, EO1MaterialID.LIGHT_WOOD, EO1MaterialID.GUM_VINE, 0, 5, 5, 0),
    EO1ItemCompound(EO1ItemID.FLUTE, EO1MaterialID.BONE_SHARD, EO1MaterialID.STEEL_BONE, 0, 5, 5, 0),
    EO1ItemCompound(EO1ItemID.KITHARA, EO1MaterialID.DRIED_VINE, EO1MaterialID.SAND_TWIG, 0, 10, 3, 0),
    EO1ItemCompound(EO1ItemID.AULOS, EO1MaterialID.SPACE_HUSK, EO1MaterialID.GOLD_TUSK, 0, 1, 2, 0),
    EO1ItemCompound(EO1ItemID.ANGEL_HARP, EO1MaterialID.SHINY_SEED, EO1MaterialID.SHINY_VINE, 0, 3, 5, 0),
    EO1ItemCompound(EO1ItemID.SYRINX, EO1MaterialID.HOLED_LIMB, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.MOSS_RING, EO1MaterialID.M_LEAF, 0, 0, 5, 0, 0),
    EO1ItemCompound(EO1ItemID.MOSS_BAND, EO1MaterialID.L_LEAF, 0, 0, 3, 0, 0),
    EO1ItemCompound(EO1ItemID.MEDICA_II, EO1MaterialID.TINY_PETAL, 0, 0, 10, 0, 0),
    EO1ItemCompound(EO1ItemID.MEDICA_III, EO1MaterialID.CRABAPPLE, EO1MaterialID.MINT_LEAF, 0, 5, 1, 0),
    EO1ItemCompound(EO1ItemID.MEDICA_IV, EO1MaterialID.ROCK_CORAL, 0, 0, 10, 0, 0),
    EO1ItemCompound(EO1ItemID.MEDICA_V, EO1MaterialID.LIFE_HONEY, EO1MaterialID.SHINY_SEED, 0, 3, 1, 0),
    EO1ItemCompound(EO1ItemID.AMRITA_II, EO1MaterialID.STRAWBERRY, EO1MaterialID.ANT_HONEY, 0, 1, 1, 0),
    EO1ItemCompound(EO1ItemID.HAMAO, EO1MaterialID.MINT_LEAF, EO1MaterialID.AMBER_LUMP, 0, 2, 10, 0),
    EO1ItemCompound(EO1ItemID.HAMAOPRIME, EO1MaterialID.SAP_WINE, EO1MaterialID.SHINY_SEED, EO1MaterialID.VOLT_CORE, 3, 1, 1),
    EO1ItemCompound(EO1ItemID.SOMA, EO1MaterialID.DRY_PEACH, EO1MaterialID.FAIRY_SAP, 0, 1, 3, 0),
    EO1ItemCompound(EO1ItemID.SOMAPRIME, EO1MaterialID.ODD_FRUIT, EO1MaterialID.AMBROSIA, EO1MaterialID.VOLT_CORE, 5, 1, 1),
    EO1ItemCompound(EO1ItemID.NECTAR, EO1MaterialID.AMBER_LUMP, 0, 0, 5, 0, 0),
    EO1ItemCompound(EO1ItemID.NECTAR_II, EO1MaterialID.SAP_WINE, EO1MaterialID.DRY_PEACH, 0, 1, 3, 0),
    EO1ItemCompound(EO1ItemID.NECTAR_III, EO1MaterialID.ODD_FRUIT, EO1MaterialID.AMBROSIA, EO1MaterialID.VOLT_CORE, 5, 1, 1),
    EO1ItemCompound(EO1ItemID.THERIACA_A, EO1MaterialID.BUG_WING, 0, 0, 5, 0, 0),
    EO1ItemCompound(EO1ItemID.THERIACA_B, EO1MaterialID.AMBER_LUMP, EO1MaterialID.STARSEED, 0, 3, 1, 0),
    EO1ItemCompound(EO1ItemID.AXCELA_II, EO1MaterialID.STRAWBERRY, 0, 0, 2, 0, 0),
    EO1ItemCompound(EO1ItemID.AXCELA_III, EO1MaterialID.SHINY_SEED, 0, 0, 2, 0, 0),
    EO1ItemCompound(EO1ItemID.BRAVANT, EO1MaterialID.AMBER_LUMP, EO1MaterialID.MUGWORT, 0, 1, 1, 0),
    EO1ItemCompound(EO1ItemID.BRAVANT_II, EO1MaterialID.ANT_HONEY, 0, 0, 3, 0, 0),
    EO1ItemCompound(EO1ItemID.STONARD, EO1MaterialID.MINT_LEAF, EO1MaterialID.THICK_LEAF, 0, 3, 3, 0),
    EO1ItemCompound(EO1ItemID.STONARD_II, EO1MaterialID.CORDYCEPS, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.FIRE_MIST, EO1MaterialID.NARCISSUS, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.ICE_MIST, EO1MaterialID.NARCISSUS, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.VOLT_MIST, EO1MaterialID.NARCISSUS, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.ALL_MIST, EO1MaterialID.MOSCHINO, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.BLAZE_OIL, EO1MaterialID.CROSS_SEED, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.FREEZE_OIL, EO1MaterialID.CROSS_SEED, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.SHOCK_OIL, EO1MaterialID.CROSS_SEED, 0, 0, 1, 0, 0),
    EO1ItemCompound(EO1ItemID.GOLD_CHIME, EO1MaterialID.GLASS_EYE, EO1MaterialID.CARAPACE, 0, 1, 1, 0),
    EO1ItemCompound(EO1ItemID.MAGNET, EO1MaterialID.SCRAP_IRON, 0, 0, 3, 0, 0),
    #EO1ItemCompound(EO1ItemID.WARP_WIRE, EO1MaterialID.<!0000>, 0, 0, 1, 0, 0),
]