from builtins import *


# -------------------------------------------------------------------------------
# Core Functions
# -------------------------------------------------------------------------------

def generate_maze():
	"""Generate a maze by planting a bush and applying weird substance.
	
	The amount of substance scales exponentially with maze unlock level.
	"""
	plant(Entities.Bush)
	substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

def maze():
	"""Drone function that continuously checks for treasure and generates new mazes.
	
	When 25 drones are active, checks for treasure to harvest,
	then generates a new maze to explore.
	"""
	while True:
		if num_drones() == 25:
			if get_entity_type() == Entities.Treasure:
				harvest()
			generate_maze()


# -------------------------------------------------------------------------------
# Main Entry
# -------------------------------------------------------------------------------

clear()
set_world_size(5)
visited = set()

# Spawn drones at unique positions until reaching maximum capacity
while num_drones() < 26:
	current = (get_pos_x(), get_pos_y())
	if current not in visited:
		visited.add(current)
		spawn_drone(maze)
		move(North)
	else:
		move(East)