from builtins import *


# -------------------------------------------------------------------------------
# Main Entry
# -------------------------------------------------------------------------------

def run():
	"""Main loop that spawns drones to harvest hay in parallel columns.
	
	Each drone handles one column, continuously harvesting and tilling.
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
	
	Waits for all drones to spawn before starting (sync barrier).
	Each iteration moves north through the entire column, harvesting
	and tilling soil as needed.
	"""
	# Sync barrier: wait until all drones are spawned
	while num_drones() < max_drones():
		get_pos_x()  # no-op to pass time
	
	while True:
		for _ in range(get_world_size()):
			if can_harvest():
				harvest()
			if get_ground_type() == Grounds.Soil:
				till()
			move(North)


run()
