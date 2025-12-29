from builtins import *


# -------------------------------------------------------------------------------
# Main Entry
# -------------------------------------------------------------------------------

def run():
	"""Main loop that continuously generates and solves mazes.
	
	Uses recursive fork search: drones spawn child drones at forks,
	each using opposite hand rule. Max 2 forks per drone lineage.
	"""
	while True:
		generate()
		
		# Spawn initial left-hand drone if starting position has 2+ directions
		if count_open_directions() >= 2:
			spawn_drone(make_navigator(2, True))
		
		# Main drone uses right-hand rule with 2 fork opportunities
		make_navigator(2, False)()
		make_navigator(2, False)()


# -------------------------------------------------------------------------------
# Core Functions
# -------------------------------------------------------------------------------

def generate():
	"""Generate a maze by planting a bush and applying weird substance.
	
	The amount of substance scales exponentially with maze unlock level.
	"""
	plant(Entities.Bush)
	substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

def make_navigator(forks_remaining, use_left=False, first_move=None):
	"""Factory function that creates a navigator with fork capability.
	
	Args:
		forks_remaining: Number of times this drone can fork at intersections.
		use_left: If True, use left-hand rule; otherwise use right-hand rule.
		first_move: If set, move this direction first to diverge from parent.
	
	Returns:
		A zero-argument function that navigates the maze and forks when possible.
	"""
	def nav():
		# Take diverging step if specified
		if first_move != None:
			move(first_move)
		
		if use_left:
			directions = (North, West, South, East)  # counter-clockwise
		else:
			directions = (North, East, South, West)  # clockwise
		
		facing = 0
		forks_left = forks_remaining
		treasure_pos = measure()
		
		while get_entity_type() != Entities.Treasure:
			if get_entity_type() != Entities.Hedge:
				return False
			
			# Shortcut: if adjacent to treasure, try direct move
			if treasure_pos != None:
				tx, ty = treasure_pos
				dx = tx - get_pos_x()
				dy = ty - get_pos_y()
				if abs(dx) + abs(dy) == 1:
					# Determine direction to treasure
					if dx == 1:
						target_dir = East
					elif dx == -1:
						target_dir = West
					elif dy == 1:
						target_dir = North
					else:
						target_dir = South
					if move(target_dir):
						break  # Successfully reached treasure
			
			# Fork at intersections if we have forks remaining
			if forks_left > 0:
				open_dirs = find_open_directions()
				if len(open_dirs) >= 2:
					# Find direction main drone will NOT take (give to child)
					my_choice = get_wall_follower_choice(directions, facing, open_dirs)
					alt_dir = None
					for d in open_dirs:
						if d != my_choice:
							alt_dir = d
							break
					if alt_dir != None:
						spawn_drone(make_navigator(forks_left - 1, not use_left, alt_dir))
						forks_left -= 1
			
			# Wall follower: try right/left -> front -> left/right -> back
			for turn in (1, 0, 3, 2):
				new_facing = (facing + turn) % 4
				if move(directions[new_facing]):
					facing = new_facing
					break
		
		harvest()
		return True
	
	return nav


# -------------------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------------------

def count_open_directions():
	"""Count how many directions are passable from current position.
	
	Returns:
		Number of open directions (0-4).
	"""
	return len(find_open_directions())

def find_open_directions():
	"""Return list of passable directions from current position."""
	result = []
	for d in (North, East, South, West):
		if move(d):
			move(opposite(d))
			result.append(d)
	return result

def get_wall_follower_choice(directions, facing, open_dirs):
	"""Determine which direction wall follower will choose.
	
	Args:
		directions: Direction tuple based on hand rule.
		facing: Current facing index (0-3).
		open_dirs: List of open directions.
	
	Returns:
		The direction wall follower will move to.
	"""
	for turn in (1, 0, 3, 2):
		new_facing = (facing + turn) % 4
		d = directions[new_facing]
		if d in open_dirs:
			return d
	return None

def opposite(direction):
	"""Return the opposite direction."""
	opposites = {North: South, South: North, East: West, West: East}
	return opposites[direction]
