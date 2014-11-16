import math
from object import Object
class MovableObject(Object):
	def __init__(self, _xPos, _yPos, _width, _height):
		Object.__init__(self, _xPos, _yPos, _width, _height)
		self.velocity = [0, 0]

	def update(self):
		Object.update(self)

	def resolve_collision(self, _colliding_surface):
		_resolution_velocity = [0, 0]
		#Determine the axis of collision, and zero velocity on axis
		if(_colliding_surface[0] == 0):		#If surface is vertical, collision on X axis
			_resolution_velocity[0] = -2 * self.velocity[0]
			if(abs(self.velocity[0]) > 1):
				self.velocity[0] *= -0.2
			else:
				self.velocity[0] *= -1 
		elif(_colliding_surface[1] == 0):	#If the surface is horizontal, collision on Y axis
			_resolution_velocity[1] = -2 * self.velocity[1]
			if(abs(self.velocity[1]) > 1):
				self.velocity[1] *= -0.2
			else:
				self.velocity[1] *= -1
		#Revert position on collision axis by adding -velocity[axis]
		for i in range(0, 2):
			self.position[i] += int(math.floor(_resolution_velocity[i]))


