import pygame, sys
from settings import WIDTH, HEIGHT, NAV_HEIGHT, PAUSED
from world import World

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT + NAV_HEIGHT))
pygame.display.set_caption("PacMan")

class Main:
	def __init__(self, screen):
		self.screen = screen
		self.FPS = pygame.time.Clock()

	def main(self):
		world = World(self.screen)
		while True:
			self.screen.fill("black")
			events = []

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				events.append(event)
				world.handle_event(event)

			if not PAUSED:
				world.update(events)
				pygame.display.update()
			if PAUSED:
				# Display paused message; maybe a pause menu in the future
				# Maybe in the future we turn on or off auto-play?
				# Maybe in the future we can switch pathfinding?
				None
			self.FPS.tick(30)


if __name__ == "__main__":
    from options import show_algorithm_info
    show_algorithm_info()
    play = Main(screen)
    play.main()