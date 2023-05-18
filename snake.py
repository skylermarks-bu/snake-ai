import pygame 
import numpy as np
import ai
import time

pygame.init()

screen = pygame.display.set_mode([500, 500])
running = True



dims = 30		# Set the width and height of the squares 


def run_game():	# This function will run a single round of the game
	global dims
	energy = 11
	count = 0
	agentpos = np.array((400, 100))	#The position of the worm is a vector in R2, or a touple
	applepos = np.array((400, 400))	#with two values
	action = ai.action(agentpos, applepos) 
	while True:
		time.sleep(0.01)

		if agentpos[0] > 500:	# Wrap on a torus
			agentpos[0] = 0		# This is quite crude at the moment; eventually
		if agentpos[1] > 500:	# I'll write some code to make the rectangle 
			agentpos[1] = 0		# go off one side of the screen and come back on
								# the other smoothly instead of just jumping.
		if agentpos[0] < 0:	
			agentpos[0] = 500		
		if agentpos[1] < 0:	
			agentpos[1] = 500		

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False
	
		if count < dims:
			energy -= 1/dims
			agentpos = agentpos - action
			count += 1
		else:
			action = ai.action(agentpos, applepos) 
			dir = np.array((float(action[0] < action[1]), float(action[1] >= action[0])))
			count = 0
		agent_rect = pygame.Rect(agentpos[0]-dims/2, agentpos[1]-dims/2, dims, dims) # Rectangle for the agent
		apple_rect = pygame.Rect(applepos[0]-dims/2, applepos[1]-dims/2, dims, dims) # Rectangle for the apple
		energy_bar = pygame.Rect(10, 10, energy * 10, 10)
		

		if agent_rect.colliderect(apple_rect):
			energy += 15
			return True
		if energy <= 0:
			return False
		
	
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

