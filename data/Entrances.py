from enum import IntEnum
from typing import Optional
from dataclasses import dataclass
from abc import ABC, abstractmethod

class EntranceType(IntEnum):
    Entrance = 0
    StairsDown = 1
    StairsUp = 2
    Elevator = 3
    Pitfall = 4
    StratumTransition = 5
    VioletCrystalDoor = 6
    ClearCrystalDoor = 7
    CardKeyDoor = 8
    EventLockedShortcut = 9
    MandatoryFight = 10


class EO1Entrance(ABC):
    destination: str
    name_prefix: Optional[str]

    def __init__(self, destination: str, name_prefix: Optional[str] = ""):
        self.destination = destination
        self.name_prefix = name_prefix

    #@property
    #def is_stratum_transition(self) -> bool:
    #    return False

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    def full_name(self) -> str:
        return f"{self.name_prefix} {self.name}" if self.name_prefix else self.name

    @property
    @abstractmethod
    def entrance_type(self) -> EntranceType:
        pass

class Entrance(EO1Entrance):
    name = "To"
    entrance_type = EntranceType.Entrance

class StairsUp(EO1Entrance):
    name = "Stairs Up"
    entrance_type = EntranceType.StairsUp

class StairsDown(EO1Entrance):
    name = "Stairs Down"
    entrance_type = EntranceType.StairsDown

class Elevator(EO1Entrance):
    name = "Elevator"
    entrance_type = EntranceType.Elevator

class Pitfall(EO1Entrance):
    name = "Pitfall"
    entrance_type = EntranceType.Pitfall

class StratumTransition(StairsDown):
    entrance_type = EntranceType.StratumTransition
    #@override
    #def is_stratum_transition(self) -> bool:
    #    return True
    #pass

class VioletCrystalDoor(EO1Entrance):
    name = "Violet Crystal Door"
    entrance_type = EntranceType.VioletCrystalDoor

class ClearCrystalDoor(EO1Entrance):
    name = "Clear Crystal Door"
    entrance_type = EntranceType.ClearCrystalDoor

class CardKeyDoor(EO1Entrance):
    name = "Card Key Door"
    entrance_type = EntranceType.CardKeyDoor

class EventLockedShortcut(EO1Entrance):
    name = "Event Locked Shortcut"
    entrance_type = EntranceType.EventLockedShortcut
    event_name: str
    stratum_required: int

    def __init__(self, destination: str, event_name: str, stratum_required: int, name_prefix: Optional[str] = ""):
        super().__init__(destination, name_prefix)
        self.event_name = event_name
        self.stratum_required = stratum_required

class MandatoryFight(EO1Entrance):
    name = "Fight" # todo
    entrance_type = EntranceType.MandatoryFight
    enemies: list[int]

    def __init__(self, destination: str, enemies: list[int], name_prefix: Optional[str] = ""):
        super().__init__(destination, name_prefix)
        self.enemies = enemies



# unused
class EO1Entrances:
    LABYRINTH_ENTRANCE = "Labyrinth Entrance"
    B1F_CLEAR_CRYSTAL_DOOR = "B1F Clear Crystal Door"
    B1F_VIOLET_CRYSTAL_DOOR = "B1F Violet Crystal Door"
    B1F_SECRET_SHORTCUT = "B1F Secret Shortcut"
    B1F_STAIRS = "B1F Stairs"
    B2F_CLEAR_CRYSTAL_DOOR = "B2F Clear Crystal Door"
    B2F_STAIRS = "B2F Stairs"
    B3F_STAIRS = "B3F Stairs"
    B4F_STAIRS = "B4F Stairs"
    B5F_CLEAR_CRYSTAL_DOOR = "B5F Clear Crystal Door"
    B5F_STAIRS = "B5F Stairs"
    B5F_SECRET_UPWARD_STAIRS = "B5F Secret Upward Stairs"
    B4F_SECRET_UPWARD_STAIRS = "B4F Secret Upward Stairs"
    B6F_CLEAR_CRYSTAL_DOOR = "B6F Clear Crystal Door"
    B6F_STAIRS = "B6F Stairs"
    B7F_STAIRS = "B7F Stairs"
    B8F_STAIRS_CENTER = "B8F Stairs Center"
    B8F_STAIRS_WEST = "B8F Stairs West"
    B8F_VIOLET_CRYSTAL_DOOR = "B8F Violet Crystal Door"
    B9F_UPWARD_STAIRS = "B9F Upward Stairs"
    B9F_STAIRS = "B9F Stairs"
    B9F_CLEAR_CRYSTAL_DOOR = "B9F Clear Crystal Door"
    B10F_STAIRS = "B10F Stairs"
    B10F_VIOLET_CRYSTAL_DOOR = "B10F Violet Crystal Door"
    B11F_VIOLET_CRYSTAL_DOOR = "B11F Violet Crystal Door"
    B11F_SECRET_UPWARD_STAIRS = "B11F Secret Upward Stairs"
    B10F_SECRET_UPWARD_STAIRS = "B10F Secret Upward Stairs"
    B9F_SECRET_UPWARD_STAIRS = "B9F Secret Upward Stairs"
    B8F_SECRET_UPWARD_STAIRS = "B8F Secret Upward Stairs"
    B11F_STAIRS = "B11F Stairs"
    B12F_STAIRS = "B12F Stairs"
    B13F_STAIRS = "B13F Stairs"
    B14F_UPWARD_STAIRS = "B14F Upward Stairs"
    B14F_STAIRS = "B14F Stairs"
    B15F_STAIRS = "B15F Stairs"
    B16F_SECRET_UPWARD_STAIRS = "B16F Secret Upward Stairs"
    B16F_SECRET_STAIRS = "B16F Secret Stairs"
    B16F_SECRET_SHORTCUT_WEST = "B16F Secret Shortcut West"
    B16F_SECRET_SHORTCUT_EAST = "B16F Secret Shortcut East"
    B16F_STAIRS = "B16F Stairs"
    B17F_STAIRS = "B17F Stairs"
    B18F_STAIRS = "B18F Stairs"
    B19F_STAIRS = "B19F Stairs"
    B20F_VIOLET_CRYSTAL_DOOR = "B20F Violet Crystal Door"
    B20F_STAIRS = "B20F Stairs"
    B21F_BRIDGE = "B21F Bridge"
    B21F_STAIRS_NORTH_WEST = "B21F Stairs North West"
    B21F_STAIRS_SOUTH_WEST = "B21F Stairs South West"
    B21F_STAIRS_NORTH_EAST = "B21F Stairs North East"
    B21F_ELEVATOR_NORTH_WEST = "B21F Elevator North West"
    B21F_ELEVATOR_SOUTH_WEST = "B21F Elevator South West"
    B21F_ELEVATOR_NORTH_EAST = "B21F Elevator North East"
    B21F_ELEVATOR_SOUTH_EAST = "B21F Elevator South East"
    B22F_SOUTH_EAST_UPWARD_STAIRS = "B22F South East Upward Stairs"
    B22F_NORTH_EAST_STAIRS = "B22F North East Stairs"
    B22F_NORTH_WEST_STAIRS = "B22F North West Stairs"
    #B22F_NORTH_EAST_UPWARD_STAIRS = "B22F North East Upward Stairs"
    #B22F_SOUTH_WEST_STAIRS = "B22F South West Stairs"
    #B22F_EAST_ELEVATOR = "B22F East Elevator"
    B23F_SOUTH_EAST_UPWARD_STAIRS = "B23F South East Upward Stairs"
    B23F_SOUTH_WEST_UPWARD_STAIRS = "B23F South West Upward Stairs"
    #B23F_WEST_ELEVATOR = "B23F West Elevator"
    B23F_NORTH_EAST_STAIRS = "B23F North East Stairs"
    B23F_NORTH_WEST_STAIRS = "B23F North West Stairs"
    B23F_NORTH_WEST_UPWARD_STAIRS = "B23F North West Upward Stairs"

    B24F_SOUTH_WEST_UPWARD_STAIRS = "B24F South West Upward Stairs"
    # B24F West Elevator is never an exit.
    B24F_SOUTH_EAST_UPWARD_STAIRS = "B24F East Upward Stairs"
    # B24F NORTH WEST UPWARD STAIRS is never an exit.
    # B24F East Elevator can be an exit if Ren and Tlatchtga skip is implemented (elevator as a check+location)
    # B24F North East Upward Stairs may be an exit under some cases?
    B25F_STAIRS = "B25F Stairs"
    B26F_STAIRS = "B26F Stairs"
    B27F_STAIRS = "B27F Stairs"
    B27F_PITFALL = "B27F Pitfall"
    B28F_UPSIDE_STAIRS = "B28F Upside Stairs"
    B28F_STAIRS = "B28F Stairs"
    B29F_STAIRS = "B29F Stairs"

