import numpy as np

def estimate(n=1000):
	"""
	Estimates Pi using Monte Carlo Metho
	Takes an integer n: number of random points as input
	Outputs an estimaton of pi
	"""
	random = np.random.rand(2*n).reshape(n, 2)

	inCircle = []

	for r in random:
		if r[0]**2 + r[1]**2 <= 1:
			inCircle.append(r)

	return float(len(inCircle)) / float(n) * 4
	