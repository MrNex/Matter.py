import pygame.draw
from player import Player, Object

class Obstacle(Object):
	allowedState = None

	def __init__(self, xPos, yPos, xDim, yDim, state):
		Object.__init__(self, xPos, yPos, xDim, yDim)
		self.allowedState = state
		
		if(self.allowedState == 'solid'): self.color = (255, 0, 0)
		elif(self.allowedState == 'liquid'): self.color = (0, 0, 255)
		elif(self.allowedState == 'gas'): self.color = (255, 255, 255)

	def update(self):
		x, y = self.position
		x -= 2
		self.position = (x, y)

	def is_colliding(self, player):
		if(player.state == self.allowedState): return False
		return Object.is_colliding(self, player)
