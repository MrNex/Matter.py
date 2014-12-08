import pygame.mouse, math
from movableobject import MovableObject
from particlesystem import ParticleSystem
class Player(MovableObject):
	swap_point_limit = 5
	

	def __init__(self, xPos, yPos, state):
		MovableObject.__init__(self, xPos, yPos, 60, 60)
		self.state = state
		self.color = (255, 0, 0, 100)
		self.state_swap_points = [0, 0, 0]
		_dx, _dy = self.dimension
		self.particle_sys = ParticleSystem(xPos, yPos, _dx, _dy)
		self.velocity[0] = 3
		self.float_point = 350
		self.float_range = 10

	def update(self):
		MovableObject.update(self)
		
		#Determine the state of the player
		mouseChange = pygame.mouse.get_rel()
		x, y = mouseChange
		x = pow(x, 2)
		y = pow(y, 2)
		mag = math.sqrt(x + y)
		self.update_state(mag)

		#Set the player's velocity to move right
		self.velocity[0] = 3
		self.velocity[1] += self.get_buoyant_force()

		#move player
		for i in range(0, 2):
			self.position[i] += self.velocity[i]

		#Update particle system's position
		#self.particle_sys.x_position = self.x_position
		self.particle_sys.x_position = self.position[0]
		#self.particle_sys.y_position = self.y_position
		self.particle_sys.y_position = self.position[1]

		#Update particle system
		self.particle_sys.update(self.state)
	
	#Determines whether the player is colliding with an object.
	#Calls resolve_collisions(_object) from particlesystem.py causing
	#particle's determined as colliding, to have their collisions be resolved.
	#Returns true if any particle, or the player's bounding box, AND the object are colliding
	#Returns false if the object is yourself, Or no mutual collision is detected.
	def is_colliding(self, _object):
		#If the object is yourself, return false- you can't collide with yourself
		if(_object == self): return False

		#If the oject is not yourself or an obstacle with a matching state
		_collided = False
		#Check all particles to see if they are colliding and resolve colisions if appropriate
		self.particle_sys.resolve_collisions(_object)
		#check if the player's collision box is colliding objects
		_collided = _object.is_colliding(self)
		return _collided

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


	def get_buoyant_force(self):
		if(self.state == 'solid') : return 0.0
		#if(self.state == 'liquid') : return -0.1
		if(self.state == 'gas') : return -0.2
		if(self.position[1]-self.float_point < self.float_range): return 0.0
		if(self.position[1]-self.float_point > -self.float_point): return -0.2
		if(self.position[1] < self.float_point and self.velocity[1] < 0.0): return -0.11 * abs(self.position[1] - self.float_point)
		if(self.position[1] > self.float_point and self.velocity[1] > 0.0): return -0.09 * abs(self.position[1] - self.float_point)


	def draw(self, _screen, _camera_x_translation):
		MovableObject.draw(self, _screen, _camera_x_translation)
		self.particle_sys.draw(_screen, _camera_x_translation)

	def resolve_collision(self, _colliding_surface):
		if(_colliding_surface[0] == 0):
			self.position[0] -= 4	#if collision is on X axis move left by camera speed + 1
		else:
			MovableObject.resolve_collision(self, _colliding_surface)
			
		
