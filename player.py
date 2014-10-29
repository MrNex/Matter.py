import pygame.mouse, math
from object import Object
class Player(Object):
	state = 'solid'
	swapPointLimit = 5
	stateSwapPoints = [0, 0, 0]

	def __init__(self, xPos, yPos, state):
		Object.__init__(self, xPos, yPos, 200, 200)
		self.state = state
		self.color = (255, 0, 0)

	def update(self):
		mouseChange = pygame.mouse.get_rel()
		x, y = mouseChange
		x = pow(x, 2)
		y = pow(y, 2)
		mag = math.sqrt(x + y)
		self.update_state(mag)

	def update_state(self, mag):
		if(mag == 0):
			self.stateSwapPoints[0] += 1
			if(self.stateSwapPoints[0] >= self.swapPointLimit):
				self.state = 'solid'
				self.color = (255, 0, 0)
				self.stateSwapPoints[0] = 0
				self.stateSwapPoints[1] = 0
				self.stateSwapPoints[2] = 0
		elif(mag < 50):
			self.stateSwapPoints[1] += 1
			if(self.stateSwapPoints[1] >= self.swapPointLimit):
				self.state = 'liquid'
				self.color = (0, 0, 255)
				self.stateSwapPoints[0] = 0
				self.stateSwapPoints[1] = 0
				self.stateSwapPoints[2] = 0
		else:
			self.stateSwapPoints[2] += 1
			if(self.stateSwapPoints[2] >= self.swapPointLimit):
				self.state = 'gas'
				self.color = (255, 255, 255)
				self.stateSwapPoints[0] = 0
				self.stateSwapPoints[1] = 0
				self.stateSwapPoints[2] = 0
	
	def push_left(self):
		_x, _y = self.position
		_x -= 2
		self.position = (_x, _y)
