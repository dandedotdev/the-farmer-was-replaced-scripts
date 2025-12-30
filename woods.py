from builtins import *


# -------------------------------------------------------------------------------
# Main Entry
# -------------------------------------------------------------------------------

def run():
	"""Main loop that spawns drones to harvest wood in parallel columns.
	
	Each drone handles one column, continuously watering and planting trees/bushes.
	Main drone waits until all drones are spawned before starting work.
	"""
	while num_drones() < max_drones():
		if spawn_drone(harvest_column):
			move(East)
	harvest_column()


# -------------------------------------------------------------------------------
# Core Functions
# -------------------------------------------------------------------------------

def harvest_column():
	"""Continuously harvest a single column in an infinite loop.
	
	Plants trees on checkerboard pattern (diagonal cells) and bushes elsewhere.
	Ensures water level is sufficient before each harvest.
	"""
	# Wait for all drones to spawn before starting
	while num_drones() < max_drones():
		pass
	
	while True:
		for _ in range(get_world_size()):
			# Ensure sufficient water level
			while get_water() < 0.76:
				use_item(Items.Water)
			
			# Harvest if ready
			harvested = can_harvest()
			if harvested:
				harvest()
			
			# Ensure soil for planting
			if get_ground_type() != Grounds.Soil:
				till()
			
			# Checkerboard pattern: trees on diagonal cells after harvest, bush otherwise
			if harvested and (get_pos_x() + get_pos_y()) % 2 == 0:
				plant(Entities.Tree)
				# if num_items(Items.Fertilizer) > 4000:
				# 	use_item(Items.Fertilizer)
			else:
				plant(Entities.Bush)
			
			move(North)


run()

