from dataclasses import dataclass
from ...data.EnemyData import EO1Enemies

from .SimplifiedValuesCriteria import *

@dataclass
class SimplifiedEnemyValues:
    enemy_id: int
    defeat_criteria: SVCriteria
    survive_criteria: SVCriteria = field(default_factory=TrueSVCriteria)

SIMPLIFIED_ENEMY_VALUES_TABLE: list[SimplifiedEnemyValues] = [
    # Stratum 1
    SimplifiedEnemyValues(EO1Enemies.TREERAT, TrueSVCriteria()),
    SimplifiedEnemyValues(EO1Enemies.WOODFLY, TrueSVCriteria()),
    SimplifiedEnemyValues(EO1Enemies.MOLE, ClassSVCriteria(front_class_count=1)),
    SimplifiedEnemyValues(EO1Enemies.CLAWBUG,
                          OrSVCriteria([
                              CanUseDmgSkillSVCriteria(skill_power=SkillPower.WEAK),
                              CanUseDmgSkillSVCriteria(damage_type=EO1Element.ELEMENTAL)
                          ])),

    SimplifiedEnemyValues(EO1Enemies.VENOMFLY,
                          OrSVCriteria([
                              CanUseDmgSkillSVCriteria(skill_power=SkillPower.MEDIUM),
                              CanUseDmgSkillSVCriteria(damage_type=EO1Element.THUNDER),
                              HasAntiStatusSVCriteria()
                          ])),
    SimplifiedEnemyValues(EO1Enemies.HARE, TrueSVCriteria()),
    SimplifiedEnemyValues(EO1Enemies.FENDER, ClassSVCriteria(front_class_count=1, back_class_count=1), ClassSVCriteria(front_class_count=1)),
    SimplifiedEnemyValues(EO1Enemies.MANDRAKE, ClassSVCriteria(front_class_count=1, back_class_count=1), ClassSVCriteria(front_class_count=1)),
    SimplifiedEnemyValues(EO1Enemies.ROLLER, ClassSVCriteria(front_class_count=1, back_class_count=1), ClassSVCriteria(front_class_count=1)),
    SimplifiedEnemyValues(EO1Enemies.CLAWFLY, ClassSVCriteria(front_class_count=2, back_class_count=1), ClassSVCriteria(front_class_count=1)),
    SimplifiedEnemyValues(EO1Enemies.WARBULL, ClassSVCriteria(front_class_count=2, back_class_count=1), ClassSVCriteria(front_class_count=1)),

    SimplifiedEnemyValues(EO1Enemies.RAGELOPE, ClassSVCriteria(front_class_count=2, back_class_count=1)),
    SimplifiedEnemyValues(EO1Enemies.KUYUTHA, ClassSVCriteria(front_class_count=2, back_class_count=1)),
    SimplifiedEnemyValues(EO1Enemies.STALKER, ClassSVCriteria(front_class_count=2, back_class_count=1)),
    SimplifiedEnemyValues(EO1Enemies.WOLF, ClassSVCriteria(front_class_count=2, back_class_count=1)),

    SimplifiedEnemyValues(EO1Enemies.SKOLL, ClassSVCriteria(front_class_count=2, back_class_count=1)),
    SimplifiedEnemyValues(EO1Enemies.FENRIR,
                          AndSVCriteria([
                              ClassSVCriteria(front_class_count=2, back_class_count=2, total_class_count=5,
                                              criteria=CanUseActiveSkill(
                                                  damage_type_resistances=[EO1Element.ICE],
                                                  skill_viability_level=SkillViabilityLevel.NORMAL)
                                              ),
                              #CanInflictAilment(EO1Ailment.HEAD_BIND),
                          ])),

    ## Stratum 2
    #    SimplifiedEnemyValues(EO1Enemies.SLEEPGEL),
    #    SimplifiedEnemyValues(EO1Enemies.VENOMGEL),
    #    SimplifiedEnemyValues(EO1Enemies.WASPIOR),
    #    SimplifiedEnemyValues(EO1Enemies.SPIDER),
    #    SimplifiedEnemyValues(EO1Enemies.FANGLEAF),
    #    SimplifiedEnemyValues(EO1Enemies.SLOTH),
    #    SimplifiedEnemyValues(EO1Enemies.PETALOID),
    #    SimplifiedEnemyValues(EO1Enemies.EVILOID),
    #    SimplifiedEnemyValues(EO1Enemies.FIREBIRD),
    #    SimplifiedEnemyValues(EO1Enemies.MANEATER),
    #    SimplifiedEnemyValues(EO1Enemies.SCORPION),
    #    SimplifiedEnemyValues(EO1Enemies.STINGMAW),
    #    SimplifiedEnemyValues(EO1Enemies.GLOWBIRD),
    #    SimplifiedEnemyValues(EO1Enemies.SPROUT, TrueSVCriteria()),
    #
    #    SimplifiedEnemyValues(EO1Enemies.MOA),
    #    SimplifiedEnemyValues(EO1Enemies.CUTTER),
    #    SimplifiedEnemyValues(EO1Enemies.ASSASSIN),
    #    SimplifiedEnemyValues(EO1Enemies.ARMOTH),
    #    SimplifiedEnemyValues(EO1Enemies.PONDCLAW),
    #
    #    SimplifiedEnemyValues(EO1Enemies.CUROLLER),
    #    SimplifiedEnemyValues(EO1Enemies.CERNUNOS),
    #
    #    # Stratum 3
    #    SimplifiedEnemyValues(EO1Enemies.MADWORM),
    #    SimplifiedEnemyValues(EO1Enemies.GUARDANT),
    #    SimplifiedEnemyValues(EO1Enemies.TREEFROG),
    #    SimplifiedEnemyValues(EO1Enemies.DEATHANT),
    #    SimplifiedEnemyValues(EO1Enemies.HEXFROG),
    #    SimplifiedEnemyValues(EO1Enemies.WOODBAT),
    #    SimplifiedEnemyValues(EO1Enemies.MELTWORM),
    #    SimplifiedEnemyValues(EO1Enemies.MORIYANA),
    #    SimplifiedEnemyValues(EO1Enemies.VAMPBAT),
    #    SimplifiedEnemyValues(EO1Enemies.CUTCRAB),
    #    SimplifiedEnemyValues(EO1Enemies.SWORDER),
    #    SimplifiedEnemyValues(EO1Enemies.REDCLAW),
    #
    #    SimplifiedEnemyValues(EO1Enemies.BLOODANT),
    #    SimplifiedEnemyValues(EO1Enemies.SERVANT),
    #    SimplifiedEnemyValues(EO1Enemies.KILLCLAW),
    #    SimplifiedEnemyValues(EO1Enemies.MUCKDILE),
    #    SimplifiedEnemyValues(EO1Enemies.SHELLTOR),
    #
    #    SimplifiedEnemyValues(EO1Enemies.ROYALANT),
    #    SimplifiedEnemyValues(EO1Enemies.COTRANGL),
    #
    #    # Stratum 4
    #    SimplifiedEnemyValues(EO1Enemies.FLAMERAT),
    #    SimplifiedEnemyValues(EO1Enemies.GOLDEER),
    #    SimplifiedEnemyValues(EO1Enemies.MANTIS),
    #    SimplifiedEnemyValues(EO1Enemies.SABREMAW),
    #    SimplifiedEnemyValues(EO1Enemies.SOLDIER),
    #    SimplifiedEnemyValues(EO1Enemies.MYSTIC),
    #    SimplifiedEnemyValues(EO1Enemies.IMMOA),
    #    SimplifiedEnemyValues(EO1Enemies.HEXROOT),
    #    SimplifiedEnemyValues(EO1Enemies.WARRIOR),
    #    SimplifiedEnemyValues(EO1Enemies.DRUID),
    #    SimplifiedEnemyValues(EO1Enemies.FAERIE),
    #    SimplifiedEnemyValues(EO1Enemies.REDBEAK),
    #    SimplifiedEnemyValues(EO1Enemies.PIXIE),
    #
    #    SimplifiedEnemyValues(EO1Enemies.SICKWOOD),
    #    SimplifiedEnemyValues(EO1Enemies.CRUELLA),
    #    SimplifiedEnemyValues(EO1Enemies.DIABOLIX),
    #    SimplifiedEnemyValues(EO1Enemies.OGRE),
    #    SimplifiedEnemyValues(EO1Enemies.HUNTER),
    #    SimplifiedEnemyValues(EO1Enemies.BUD, TrueSVCriteria()),
    #
    #    SimplifiedEnemyValues(EO1Enemies.IWAOPELN),
    #
    #    # Stratum 5
    #    SimplifiedEnemyValues(EO1Enemies.DARKHARE),
    #    SimplifiedEnemyValues(EO1Enemies.MAUL),
    #    SimplifiedEnemyValues(EO1Enemies.BURSTGEL),
    #    SimplifiedEnemyValues(EO1Enemies.DIREWOLF),
    #    SimplifiedEnemyValues(EO1Enemies.MUSKOID),
    #    SimplifiedEnemyValues(EO1Enemies.KINGFROG),
    #    SimplifiedEnemyValues(EO1Enemies.KINGAPIS),
    #    SimplifiedEnemyValues(EO1Enemies.CLAWLORD),
    #    SimplifiedEnemyValues(EO1Enemies.SILKER),
    #    SimplifiedEnemyValues(EO1Enemies.VARAHA),
    #    SimplifiedEnemyValues(EO1Enemies.ARMOROLL),
    #    SimplifiedEnemyValues(EO1Enemies.HELLBULL),
    #    SimplifiedEnemyValues(EO1Enemies.KINGYANA),
    #
    #    SimplifiedEnemyValues(EO1Enemies.DESOULER),
    #    SimplifiedEnemyValues(EO1Enemies.KINGDILE),
    #    SimplifiedEnemyValues(EO1Enemies.TREETUSK),
    #    SimplifiedEnemyValues(EO1Enemies.DINOLICH),
    #
    #    SimplifiedEnemyValues(EO1Enemies.REN),
    #    SimplifiedEnemyValues(EO1Enemies.TLACHTGA),
    #    SimplifiedEnemyValues(EO1Enemies.ETREANT),
    #
    #    # Stratum 6
    #    SimplifiedEnemyValues(EO1Enemies.FLAMEGEL),
    #    SimplifiedEnemyValues(EO1Enemies.HAZEFLY),
    #    SimplifiedEnemyValues(EO1Enemies.HELLFLY),
    #    SimplifiedEnemyValues(EO1Enemies.BLADER),
    #    SimplifiedEnemyValues(EO1Enemies.MONOCYTE),
    #    SimplifiedEnemyValues(EO1Enemies.LARGEANT),
    #    SimplifiedEnemyValues(EO1Enemies.RED_CELL),
    #    SimplifiedEnemyValues(EO1Enemies.EVILROOT),
    #    SimplifiedEnemyValues(EO1Enemies.ROCKWOOD),
    #    SimplifiedEnemyValues(EO1Enemies.METALION),
    #    SimplifiedEnemyValues(EO1Enemies.LUCIFIRD),
    #    SimplifiedEnemyValues(EO1Enemies.IRONCRAB),
    #    SimplifiedEnemyValues(EO1Enemies.CLOVER, TrueSVCriteria()),
    #
    #    SimplifiedEnemyValues(EO1Enemies.SONGBIRD),
    #    SimplifiedEnemyValues(EO1Enemies.SHELLORD),
    #    SimplifiedEnemyValues(EO1Enemies.MACABRE),
    #    SimplifiedEnemyValues(EO1Enemies.TERALICH),
    #
    #    SimplifiedEnemyValues(EO1Enemies.DRAGOID),
    #    SimplifiedEnemyValues(EO1Enemies.WYRMOID),
    #    SimplifiedEnemyValues(EO1Enemies.DRAKOID),
    #    SimplifiedEnemyValues(EO1Enemies.PRIMEVIL),
    #
    #    # Superbosses
    #    SimplifiedEnemyValues(EO1Enemies.WYVERN),
    #    SimplifiedEnemyValues(EO1Enemies.GOLEM),
    #    SimplifiedEnemyValues(EO1Enemies.ALRAUNE),
    #    SimplifiedEnemyValues(EO1Enemies.MANTICOR),
    #    SimplifiedEnemyValues(EO1Enemies.WYRM),
    #    SimplifiedEnemyValues(EO1Enemies.DRAKE),
    #    SimplifiedEnemyValues(EO1Enemies.DRAGON),
    #
    #    # Quest enemies
    #    SimplifiedEnemyValues(EO1Enemies.FIREATER),
    #    SimplifiedEnemyValues(EO1Enemies.TOXINFLY),
    #    SimplifiedEnemyValues(EO1Enemies.OMNIVORE),
    #    SimplifiedEnemyValues(EO1Enemies.STEELWEB),
    #    SimplifiedEnemyValues(EO1Enemies.GOUDARAT),
    #    SimplifiedEnemyValues(EO1Enemies.NIGHTOAD),
    #    SimplifiedEnemyValues(EO1Enemies.HEXTOAD),
]

SIMPLIFIED_ENEMY_VALUES_BY_ID: dict[int, SimplifiedEnemyValues] = {enemy_data.enemy_id:enemy_data for enemy_data in SIMPLIFIED_ENEMY_VALUES_TABLE}