from object import Object

class Boundary(Object):
	def __init__(self, xPos, yPos, xDim, yDim):
		Object.__init__(self, xPos, yPos, xDim, yDim)
		self.color = (255, 255, 255)

	def update(self):
		Object.update(self)
		#Move boundary at same speed as camera
		self.position[0] += 3
		
