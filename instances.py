"""Stub implementations for The Farmer Was Replaced game API.

This module provides placeholder definitions to enable IDE autocompletion
and type checking during development outside the game environment.
"""

from enum import Enum, auto


class Entities(Enum):
	Bush = auto()
	Treasure = auto()
	Hedge = auto()


class Items(Enum):
	Weird_Substance = auto()
	Fertilizer = auto()


class Unlocks(Enum):
	Mazes = auto()


# Direction constants
North = "North"
South = "South"
East = "East"
West = "West"

