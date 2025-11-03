import pygame
import math

from settings import CHAR_SIZE, PLAYER_SPEED, BOARD_RATIO, MAP
from animation import import_sprite
from algorithms import bfs, dfs, ucs, astar

class Pac(pygame.sprite.Sprite):
	def __init__(self, row, col):
		super().__init__()

		self.abs_x = (row * CHAR_SIZE)
		self.abs_y = (col * CHAR_SIZE)

		# pac animation
		self._import_character_assets()
		self.frame_index = 0
		self.animation_speed = 0.5
		self.image = self.animations["idle"][self.frame_index]
		self.rect = self.image.get_rect(topleft = (self.abs_x, self.abs_y))
		self.mask = pygame.mask.from_surface(self.image)

		self.pac_speed = PLAYER_SPEED
		self.immune_time = 0
		self.immune = False

		self.directions = {'left': (-PLAYER_SPEED, 0), 'right': (PLAYER_SPEED, 0), 'up': (0, -PLAYER_SPEED), 'down': (0, PLAYER_SPEED)}
		self.keys = {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'up': pygame.K_UP, 'down': pygame.K_DOWN}
		self.direction = (0, 0)
	
		# pac status
		self.status = "idle"
		self.life = 3
		self.pac_score = 0

		# AI
		self.ai_enabled = True
		self.algorithm = "bfs"  # bfs, dfs, ucs, astar
		self.current_path = []  # list of grid cells to follow
		self.target = None
		self.walls_set = set()
		self.width, self.height = BOARD_RATIO

	# gets all the image needed for animating specific player action
	def _import_character_assets(self):
		character_path = "assets/pac/"
		self.animations = {
			"up": [],
			"down": [],
			"left": [],
			"right": [],
			"idle": [],
			"power_up": []
		}
		for animation in self.animations.keys():
			full_path = character_path + animation
			self.animations[animation] = import_sprite(full_path)

	def grid_pos(self):
		return (self.rect.x // CHAR_SIZE, self.rect.y // CHAR_SIZE)

	def at_cell_center(self):
		return (self.rect.x % CHAR_SIZE == 0) and (self.rect.y % CHAR_SIZE == 0)

	def set_algo(self, name):
		name = name.lower()
		if name in ("bfs","dfs","ucs","astar"):
			self.algorithm = name
			self.current_path = []  # force replan

	def set_ai(self, enabled: bool):
		self.ai_enabled = enabled
		self.current_path = []

	def update_walls(self, walls_rects):
		# cache grid walls as set of blocked (x,y)
		self.walls_set = set((r.x // CHAR_SIZE, r.y // CHAR_SIZE) for r in walls_rects)

	def choose_target(self, berry_positions):
		# pick nearest berry by Manhattan distance from current position
		if not berry_positions:
			return None
		px, py = self.grid_pos()
		best = min(berry_positions, key=lambda b: abs(b[0]-px)+abs(b[1]-py))
		return best

	def plan_path(self, start, goal):
		if goal is None:
			return []
		algo = self.algorithm
		w, h = self.width, self.height
		walls = self.walls_set
		if algo == "bfs":
			return bfs(start, goal, w, h, walls)
		elif algo == "dfs":
			return dfs(start, goal, w, h, walls)
		elif algo == "ucs":
			return ucs(start, goal, w, h, walls)
		else:
			return astar(start, goal, w, h, walls)

	def follow_path(self):
		# Follow current_path cell by cell; when arriving at next cell center, pop it.
		if not self.current_path:
			self.direction = (0,0)
			return
		# current_path includes start cell; ensure we target next waypoint beyond current cell
		if len(self.current_path) >= 2:
			next_cell = self.current_path[1]
		else:
			next_cell = self.current_path[0]
		cx, cy = self.grid_pos()
		nx, ny = next_cell
		# determine direction
		if self.at_cell_center():
			dx = nx - cx
			dy = ny - cy
			if dx < 0: 
				self.direction = self.directions['left']; self.status = "left"
			elif dx > 0: 
				self.direction = self.directions['right']; self.status = "right"
			elif dy < 0: 
				self.direction = self.directions['up']; self.status = "up"
			elif dy > 0: 
				self.direction = self.directions['down']; self.status = "down"

		# move forward if not colliding (world still enforces walls)
		self.rect.move_ip(self.direction)

		# if we reached next cell, trim it from path
		if self.at_cell_center() and self.grid_pos() == next_cell:
			# drop all leading cells equal to our current grid cell
			while self.current_path and self.current_path[0] == next_cell:
				self.current_path.pop(0)

	def _is_collide(self, x, y):
		tmp_rect = self.rect.move(x, y)
		if tmp_rect.collidelist(self.walls_collide_list) == -1:
			return False
		return True

	def move_to_start_pos(self):
		self.rect.x = self.abs_x
		self.rect.y = self.abs_y

	# update with sprite/sheets
	def animate(self, pressed_key, walls_collide_list):
		animation = self.animations[self.status]

		# loop over frame index
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0
		image = animation[int(self.frame_index)]
		self.image = pygame.transform.scale(image, (CHAR_SIZE, CHAR_SIZE))

		self.walls_collide_list = walls_collide_list

		if not self.ai_enabled:
			for key, key_value in self.keys.items():
				if pressed_key[key_value] and not self._is_collide(*self.directions[key]):
					self.direction = self.directions[key]
					self.status = key if not self.immune else "power_up"
					break
			
			if not self._is_collide(*self.direction):
				self.rect.move_ip(self.direction)
				self.status = self.status if not self.immune else "power_up"
			if self._is_collide(*self.direction):
				self.status = "idle" if not self.immune else "power_up"
		else:
			# AI control path-following
			self.status = self.status if not self.immune else "power_up"
			self.follow_path()

	def update(self):
		# Timer based from FPS count
		self.immune = True if self.immune_time > 0 else False
		self.immune_time -= 1 if self.immune_time > 0 else 0

		self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
