import numpy as np

def estimate(n=1000):
	random = np.random.rand(2*n).reshape(n, 2)

	inCircle = []

	for r in random:
		if r[0]**2 + r[1]**2 <= 1:
			inCircle.append(r)

	pi = float(len(inCircle)) / float(n) * 4
	
	print "Estimated Pi is: " + str(pi)