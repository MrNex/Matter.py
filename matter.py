import pygame.display, pygame.time, pygame.event, math, sys
from itertools import ifilter
from random import randint
from player import Player
from obstacle import Obstacle


class MatterGame:

	def __init__(self):
		#self.screen = pygame.display.set_mode((1024, 768))
		self.screen = pygame.display.get_surface()
		self.clock = pygame.time.Clock()
		self.spawn_rate = 300
		self.spawn_timer = 0
		self.player = Player(400, 400, 'solid')
		self.obstacles = []
		self.running = 1
		self.add_random_obstacle()
		self.paused = False

	#Adds a random obstacle to self.obstacles
	def add_random_obstacle(self):
		_rnd_state_index = randint(0, 3)
		_rnd_state = None
		if(_rnd_state_index == 0): _rnd_state = 'solid'
		elif(_rnd_state_index == 1): _rnd_state = 'liquid'
		else: _rnd_state = 'gas'
		_obstacle = Obstacle(self.screen.get_width(), 400, 200, 200, _rnd_state)
		self.obstacles.append(_obstacle)


	#Runs the game
	def run(self):
		while self.running:			#Start the game loop
			self.clock.tick(30)		#Allow game to run at a maximum of 30 loops per second
			
			#Input management
			#Keyboard
			for event in pygame.event.get():
				if hasattr(event, 'key'):
					if event.key == pygame.K_ESCAPE: self.running = 0


		        #Update game logic
			#Spawn obstacles
			self.spawn_timer += 1
			if(self.spawn_timer >= self.spawn_rate):
				self.spawn_timer = 0
				self.add_random_obstacle()
	
	

			#Update objects
			#update player
			self.player.update()
			#Update Loop for obstacles
			for _obstacle in self.obstacles:
				_obstacle.update()
				if(_obstacle.is_colliding(self.player)):		#Player collision detected 
					self.player.push_left(Obstacle.movement_speed)	#Push player towards left of screen
					if(not self.player.is_on_screen()):		#If player is no longer on screen
						print('Game Over')			#Game over
						self.running = 0			#Exit loop
	

			#Screen bounds check
			self.obstacles[:] = ifilter(lambda e: e.is_on_screen(), self.obstacles)


		        #Draw Code
			#screen.fill((0, 0, 0))					#Clear screen
			self.player.draw(self.screen)
			for _obstacle in self.obstacles:
				_obstacle.draw(self.screen)
			pygame.display.update()					#Update display

	def read_file(self, file_path):
		pass

	def write_file(self, file_path):
		pass
	


#Program starts here if this file is ran from command line
def main():
	pygame.init()
	pygame.display.set_mode((0, 0), pygame.RESIZABLE)
	game = MatterGame()
	game.run()
	print("closing")

#In case of name mangling
if __name__ == '__main__':
	main()
