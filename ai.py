import numpy as np
import pickle
import pygame
print("AI imported")

screenx = 1000	# Screen X dimension
screeny = 1000	# Screen Y dimension
def action(me, target):
	dif  = torusvecmin(me, target, 500) # Call the function we define below
	out = oneoffour(dif)
	return out

def sign(x):		
	""" Function that returns the sign of the input, or 0 when the input
	vanishes"""
	if x == 0:		
		return x	# We can't divide by 0, so return zero if the input is 0
	return x/abs(x)	# Return x/|X|

def torusvecmin(a, b, loop):
	lengths  = []	# Initialize empty list of lengths
	vectors  = []	# Initialize empty list of vectors
	for i in [-screenx, 0, screenx]:		# Loop through the possible offsets for the
		for j in (-screeny, 0, screeny):	# surface of the torus
			vec = np.array((i, j))	# Create a vector of the offsets
			vector = a-b-vec	# Find the difference between the first and
								# second vectors after applying the offset 
			vectors.append(vector)	# Append this to the list of vectors
			lengths.append(abs(np.linalg.norm(vector))) # Append the norm of
														# this vector to the 
														# list of lengths
	return (vectors[lengths.index(min(lengths))])	# Return the shortest vector


def oneoffour(dif):
	""" This is some dark magic. Python casts booleans to one and zero,
			so I've set  the first component of out to one if the first
			component is larger and the second to one if the second component is
			larger. I then multiply each component of out by the sign of the
			component of dif. This means that if one or both of the components
			are going backwards, the component will continue to point in the
			same direction after we've messed with it. This leaves a unit vector
			in either the positive or negative of the basis vectors, which is
			what we need to move in one of the four directions as the snake. 
	"""
	return (float(abs(dif[0]) > abs(dif[1]))*sign(dif[0]), float(abs(dif[0]) <= abs(dif[1]))*sign(dif[1]))

