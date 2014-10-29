import pygame.draw
class Object:
	position = None
	prev_position = None
	dimension = None
	color = None

	def __init__(self, xPos, yPos, xDim, yDim):
		self.position = (xPos, yPos)
		self.prev_position = self.position
		self.dimension = (xDim, yDim)

	##Checks if two objects are colliding
	def is_colliding(self, object):
		if(self == object): return false
		objX, objY = object.position
		objDX, objDY = object.dimension
		x, y = self.position
		dX, dY = self.dimension
		if(x < objX + objDX and x + dX > objX):
			if(y < objY + objDY and y + dY > objY):
				return True
		return False

	##Checks if this object is to the right of the left side of the screen
	#Only returns false if the object fell off the LEFT side of the screen!
	def is_on_screen(self):
		_x, _y = self.position
		_dx, _dy = self.dimension
		if(_x + _dx <= 0): return False
		return True

	##Draws this object
	def draw(self, screen):
		if(not self.prev_position == self.position):
			pygame.draw.rect(screen, (0, 0, 0), (self.prev_position, self.dimension))
			self.prev_position = self.position
		pygame.draw.rect(screen, self.color, (self.position, self.dimension))
