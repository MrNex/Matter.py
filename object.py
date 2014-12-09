import pygame.draw
import spritesheet
class Object:

	def __init__(self, xPos, yPos, xDim, yDim):
		self.position = [xPos, yPos]
		#self.x_position = xPos
		#self.y_position = yPos
		#self.prev_position = [self.x_position, self.y_position]
		#self.prev_position = [self.position[0], self.position[1]]
		self.prev_position = [self.position[0], self.position[1]]
		self.dimension = [xDim, yDim]
		self.color = (150, 150, 150, 100)
	
	def update(self):
		#self.prev_position = (self.x_position, self.y_position)
		for i in range(0, 2):
			self.prev_position[i] = self.position[i]
		

	##Checks if two objects are colliding
	def is_colliding(self, object):
		#If the object is yourself, return false
		if(self == object): return false

		#Check for intersection on X axis
		if(	
			self.position[0] < object.position[0] + object.dimension[0] and 
			self.position[0] + self.dimension[0] > object.position[0]
		):
			#Check for intersection on Y axis
			if(
				self.position[1] < object.position[1] + object.dimension[1] and 
				self.position[1] + self.dimension[1] > object.position[1]
			):
				#If intersections on both axis: return true
				return True
		#Else, return false
		return False

	#Returns a vector indicating the direction and magnitude of the side of the object
	#which the particle is colliding 
	def get_colliding_side(self, object):
		_collision_side = [0, 0]
		_distances = [ 
			#difference in left side of particle from right side of object
			abs(self.position[0] - (object.position[0] + object.dimension[0])),
			#Difference in right side of particle from left side of object
			abs((self.position[0] + self.dimension[0]) - object.position[0]),
			#difference in top side of particle from bottom side of object
			abs(self.position[1] - (object.position[1] + object.dimension[1])),
			#difference in bottom side of particle from top side of object
			abs((self.position[1] + self.dimension[1]) - object.position[1])]

		_smallest_index = 0
		#Determine the smallest difference
		for _index in range(0, 4):
			if(_distances[_index] < _distances[_smallest_index]): _smallest_index = _index
		
		#If the colliding side was the:
		if(_smallest_index == 0):		#Right side
			_collision_side[1] = object.dimension[1]
		elif(_smallest_index == 1):		#Left side
			_collision_side[1] = -object.dimension[1]
		elif(_smallest_index == 2):		#bottom side
			_collision_side[0] = -object.dimension[0]
		else:					#Top side
			_collision_side[0] = object.dimension[0]
		
		return _collision_side


	##Draws this object
	def draw(self, _screen, _camera_x_translation):
		self.clear_shape(_screen, _camera_x_translation)
		self.draw_shape(_screen, _camera_x_translation)

	def draw_shape(self, _screen, _camera_x_translation):
		pygame.draw.rect(
				_screen, 
				self.color, 
				((self.position[0] - _camera_x_translation, self.position[1]), self.dimension)
				)

	def clear_shape(self, _screen, _camera_x_translation):
		pygame.draw.rect(
				_screen, 
				(0, 0, 0), 
				((self.prev_position[0] - _camera_x_translation + 3, self.prev_position[1]), self.dimension)
				)
