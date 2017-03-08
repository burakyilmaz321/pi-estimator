import numpy as np

x_range = np.arange(-1., 1., 0.01)
y_range = np.arange(-1., 1., 0.01)

inCircle = []
points = []
circle = []
random = []

for x in x_range:
	for y in y_range:
		points.append((round(x, 2), round(y, 2)))

for p in points:
	if p[0]**2 + p[1]**2 <= 1:
		circle.append(p)

for i in range(10000):
	random.append((round(np.random.random(), 2), round(np.random.random(), 2)))

for c in random:
	if c in circle:
		inCircle.append(c)

pi = float(len(inCircle)) / 10000. * 4

print "Estimated Pi is: " + str(pi)