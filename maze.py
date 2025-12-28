from instances import Entities, Items, Unlocks, North, South, East, West
from utils import (
	plant,
	harvest,
	move,
	get_world_size,
	get_entity_type,
	num_unlocked,
	use_item,
)

def run():
	"""Main loop that continuously generates and solves mazes."""
	while True:
		generate()
		navigate()

def generate():
	"""Generate a maze by planting a bush and applying weird substance.
	
	The amount of substance scales exponentially with maze unlock level.
	"""
	plant(Entities.Bush)
	substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

def navigate(action = harvest):
	"""Navigate the maze using the right-hand wall follower algorithm.
	
	Args:
		action: Callback to execute when treasure is found. Defaults to harvest.
	
	Returns:
		True if treasure was found, False if not in a valid maze.
	"""
	# wall follower: guaranteed to find treasure in a perfect maze
	directions = (North, East, South, West)  # clockwise
	facing = 0  # start facing north
	
	while get_entity_type() != Entities.Treasure:
		if get_entity_type() != Entities.Hedge:
			return False
		
		# try order: right -> front -> left -> back
		for turn in (1, 0, 3, 2):
			new_facing = (facing + turn) % 4
			if move(directions[new_facing]):
				facing = new_facing
				break
	
	action()
	return True