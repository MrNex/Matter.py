import pygame.draw
from player import Player, Object

class Obstacle(Object):
	movement_speed = 3


	def __init__(self, xPos, yPos, xDim, yDim, state):
		Object.__init__(self, xPos, yPos, xDim, yDim)
		self.allowedState = state
		
		if(self.allowedState == 'solid'): self.color = (255, 0, 0)
		elif(self.allowedState == 'liquid'): self.color = (0, 0, 255)
		elif(self.allowedState == 'gas'): self.color = (255, 255, 255)

	def update(self):
		self.x_position -= Obstacle.movement_speed

	def is_colliding(self, player):
		if(player.state == self.allowedState): return False
		return Object.is_colliding(self, player)
