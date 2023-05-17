import numpy as np
print("AI imported")

def action(me, target):
	dif  = me - target
	out = (float(abs(dif[0]) > abs(dif[1]))*sign(dif[0]), float(abs(dif[0]) <= abs(dif[1]))*sign(dif[1]))
	"""
			The above is some dark magic. Python casts booleans to one and zero,
			so I've set  the first component of out to one if the first
			component is larger and the second to one if the second component is
			larger. I then multiply each component of out by the sign of the
			component of dif. This means that if 
	"""
	print(out)
	return out

def sign(x):
	if x == 0:
		return x
	return x/abs(x)
