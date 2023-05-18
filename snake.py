import pygame	# Our graphics library
import numpy as np	# To deal with vectors
import ai	# Import the script ai.py
import time	# For time.sleep

pygame.init()	# Start the graphics library

screen = pygame.display.set_mode([500, 500])	# Generate a 500x500 window

dims = 30		# Set the width and height of the squares 

def run_game():	# This function will run a single round of the game
	energy = 11	# Initialize energy to 11
	count = 0	# Dummy variable for use later
	agentpos = np.array((400, 100))	#The position of the worm is a vector in R2, or a touple
	applepos = np.array((400, 400))	#with two values
	action = ai.action(agentpos, applepos)	# 
	while True:
		time.sleep(0.01)	# We want to move at a reasonable pace. This is 
							# actually a very bad way to do this, as the
							# program will still speed up and slow down as the
							# processing speed changes. I'll use pygame's
							# internal clock to set a more consistent FPS later
							# when it becomes a problem due to intensive
							# computation. For now it's fine though.

		if agentpos[0] > 500:	# Wrap on a torus
			agentpos[0] = 0		# This is quite crude at the moment; eventually
		if agentpos[1] > 500:	# I'll write some code to make the rectangle 
			agentpos[1] = 0		# go off one side of the screen and come back on
								# the other smoothly instead of just jumping.
		if agentpos[0] < 0:	
			agentpos[0] = 500		
		if agentpos[1] < 0:	
			agentpos[1] = 500		

		for event in pygame.event.get():	# If we tell the window to close,
			if event.type == pygame.QUIT:	# close the window
				return False
	
		if count < dims:	# Here we're ensuring that it only changes direction
			energy -= 1/dims	# every time it moves it's own length. So it
			agentpos = agentpos - action	# will move for dims (30) pixels,
			count += 1	# and then it will choose the next direction.
		else:
			action = ai.action(agentpos, applepos)	# Choose next direction
			count = 0	# Reset the count
		agent_rect = pygame.Rect(agentpos[0]-dims/2, agentpos[1]-dims/2, dims, dims) # Rectangle for the agent
		apple_rect = pygame.Rect(applepos[0]-dims/2, applepos[1]-dims/2, dims, dims) # Rectangle for the apple
		energy_bar = pygame.Rect(10, 10, energy * 10, 10)	# Rectangle for
															# energy bar
		if agent_rect.colliderect(apple_rect):	# Win condition
			energy += 15	# Add to energy
			return True		# We won!
		if energy <= 0:		# Lose condition
			return False	# We lost
		
		screen.fill((255, 255, 255))	# Fill the background with white
	
		pygame.draw.rect(screen, (0, 255, 0),	# Draw a square where the worm is
			agent_rect)
		pygame.draw.rect(screen, (0, 255, 0),	# Draw a square where the worm is
			energy_bar)
		pygame.draw.rect(screen, (255, 0, 0),	# Draw a square where the apple is
			apple_rect)
	
		pygame.display.flip()	# I don't know why we need this but if you remove 
								# it the screen goes black
	
run_game()
# Done! Time to quit.

pygame.quit()

