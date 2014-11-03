import pygame.draw
class Object:

	def __init__(self, xPos, yPos, xDim, yDim):
		self.x_position = xPos
		self.y_position = yPos
		self.prev_position = (self.x_position, self.y_position)
		self.dimension = (xDim, yDim)

	##Checks if two objects are colliding
	def is_colliding(self, object):
		if(self == object): return false
		objDX, objDY = object.dimension
		dX, dY = self.dimension
		if(self.x_position < object.x_position + objDX and self.x_position + dX > object.x_position):
			if(self.y_position < object.y_position + objDY and self.y_position + dY > object.y_position):
				return True
		return False

	##Checks if this object is to the right of the left side of the screen
	#Only returns false if the object fell off the LEFT side of the screen!
	def is_on_screen(self):
		_dx, _dy = self.dimension
		if(self.x_position + _dx <= 0): return False
		return True

	##Draws this object
	def draw(self, _screen):
		if(not self.prev_position == (self.x_position, self.y_position)):
			self.clear_shape(_screen)
		self.draw_shape(_screen)
		

	def draw_shape(self, _screen):
		pygame.draw.rect(_screen, self.color, ((self.x_position, self.y_position), self.dimension))

	def clear_shape(self, _screen):
		pygame.draw.rect(_screen, (0, 0, 0), (self.prev_position, self.dimension))
		self.prev_position = (self.x_position, self.y_position)

	def push_left(self, _trans):
		self.x_position -= _trans
