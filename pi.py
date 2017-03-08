import numpy as np

class Pi(object):
	"""
	Estimates Pi using Monte Carlo Method
	Takes an integer points: number of random points as input
	"""
	def __init__(self, points=1000):
		self.points = points

	def estimate(self):
		random = np.random.rand(2*self.points).reshape(self.points, 2)
		inCircle = []
		for r in random:
			if r[0]**2 + r[1]**2 <= 1:
				inCircle.append(r)
		return float(len(inCircle)) / float(self.points) * 4
	
	def __str__(self):
		pi = self.estimate()
		return "Estimated Pi is: " + str(pi)