from particle import Particle
class ParticleSystem:

	def __init__(self, _x_pos, _y_pos, _width, _height):
		self.x_position = _x_pos
		self.y_position = _y_pos
		self.width = _width
		self.height = _height
		Particle.particle_radius = self.width / 6
		
		#Particle.update_constants()

		self.particles = []
		for x in range(0, 9):
			self.particles.append(Particle(
				self.x_position, 
				self.y_position,
				x))
		Particle.particles_in_system = self.particles

	

	def update(self, _state):
		for particle in self.particles:
			particle.update(_state, (self.x_position, self.y_position), self.width / 2)

	def push_left(self, _trans):
		self.x_position -= trans
		for particle in self.particles:
			particle.push_left(_trans)

	def calculate_containment_force(self, _particle, _contantment_range_factor):
		#Create contentment force
		_containment_force = [0, 0]
		
		#Get center of system
		_sys_center = [self.x_position + self.width / 2, self.y_position + self.height / 2]

		#Calculate particle's distance from the center of the system
		_dist =  math.sqrt( (_sys_center[0] - _particle.x_position)**2 + (_sys_center[1] - _particle.y_position)**2 )
		#calculate the containment range
		_containment_range = (self.width / 2) * _containment_range_factor

		#If thedistance is greater than the containment range we must have a non zero containment force
		if(_dist > _containment_range):
			_containment_force += [_sys_center[0] - _particle.x_position, _sys_center[1] - _particle.y_position]
		return _containment_force


	def draw(self, _screen):
		for particle in self.particles:
			particle.draw(_screen)

	

		

