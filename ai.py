import numpy as np
print("AI imported")

def action(me, target):
	dif  = torusvecmin(me, target, 500)
	out = (float(abs(dif[0]) > abs(dif[1]))*sign(dif[0]), float(abs(dif[0]) <= abs(dif[1]))*sign(dif[1]))
	"""
			The above is some dark magic. Python casts booleans to one and zero,
			so I've set  the first component of out to one if the first
			component is larger and the second to one if the second component is
			larger. I then multiply each component of out by the sign of the
			component of dif. This means that if one or both of the components
			are going backwards, the component will continue to point in the
			same direction after we've messed with it. This leaves a unit vector
			in either the positive or negative of the basis vectors, which is
			what we need to move in one of the four directions as the snake. 
	"""
	return out

def sign(x):
	if x == 0:
		return x
	return x/abs(x)

def torusvecmin(a, b, loop):
	lengths  = []
	vectors  = []
	print(a)
	print(b)
	for i in [-500, 0, 500]:
		for j in (-500, 0, 500):
			vec = np.array((i, j))
			vector = a-b-vec
			vectors.append(vector)
			lengths.append(abs(np.linalg.norm(vector)))
	print(vectors)
	ret = (vectors[lengths.index(min(lengths))])
	return ret


