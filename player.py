import pygame.mouse, math
from object import Object
from particlesystem import ParticleSystem
class Player(Object):
	swap_point_limit = 5
	

	def __init__(self, xPos, yPos, state):
		Object.__init__(self, xPos, yPos, 60, 60)
		self.state = state
		self.color = (255, 0, 0)
		self.state_swap_points = [0, 0, 0]
		_dx, _dy = self.dimension
		self.particle_sys = ParticleSystem(xPos, yPos, _dx, _dy)

	def update(self):
		Object.update(self)
		mouseChange = pygame.mouse.get_rel()
		x, y = mouseChange
		x = pow(x, 2)
		y = pow(y, 2)
		mag = math.sqrt(x + y)
		self.update_state(mag)

		#move player
		self.x_position += 3
		
		#Update particle system's position
		self.particle_sys.x_position = self.x_position
		self.particle_sys.y_position = self.y_position

		#Update particle system
		self.particle_sys.update(self.state)
	
	#Determines whether the player is colliding with an object.
	#Calls resolve_collisions(_object) from particlesystem.py causing
	#particle's determined as colliding, to have their collisions be resolved.
	#Returns true if any particle, or the player's bounding box, is colliding with the object
	#Returns false if the object is yourself, 
	#if the object has an allowed_state attribute which matches player's state attribute
	#Or is no collision is detected.
	def is_colliding(self, _object):
		#If the object is yourself, return false- you can't collide with yourself
		if(_object == self): return False
		#If the object has an allowed state which matches your state- return false
		if(hasattr(_object, 'allowed_state')):
			if(self.state == _object.allowed_state): return False

		#If the oject is not yourself or an obstacle with a matching state
		_collided = False
		#Test all particles to see if they are colliding
		_collided = self.particle_sys.resolve_collisions(_object)
		#If no particles are colliding check if the player's collision box is colliding
		if(not _collided):
			_collided = Object.is_colliding(self, _object)
		return _collided
		
		
	def push_left(self, _trans):
		Object.push_left(self, _trans)
		self.particle_sys.push_left(_trans)

	def update_state(self, mag):
		if(mag == 0):
			self.state_swap_points[0] += 1
			if(self.state_swap_points[0] >= self.swap_point_limit):
				self.state = 'solid'
				self.color = (255, 0, 0)
				self.state_swap_points[0] = 0
				self.state_swap_points[1] = 0
				self.state_swap_points[2] = 0
		elif(mag < 50):
			self.state_swap_points[1] += 1
			if(self.state_swap_points[1] >= self.swap_point_limit):
				self.state = 'liquid'
				self.color = (0, 0, 255)
				self.state_swap_points[0] = 0
				self.state_swap_points[1] = 0
				self.state_swap_points[2] = 0
		else:
			self.state_swap_points[2] += 1
			if(self.state_swap_points[2] >= self.swap_point_limit):
				self.state = 'gas'
				self.color = (255, 255, 255)
				self.state_swap_points[0] = 0
				self.state_swap_points[1] = 0
				self.state_swap_points[2] = 0

	def draw(self, _screen, _camera_x_translation):
		#Object.draw(self, _screen)
		self.particle_sys.draw(_screen, _camera_x_translation)
