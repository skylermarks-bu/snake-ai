import pygame 
import ai

pygame.init()

screen = pygame.display.set_mode([500, 500])
running = True

agentpos = (100, 100)	#The position of the worm is a vector in R2, or a touple
applepos = (400, 400)	#with two values


dims = 30		# Set the width and height of the squares 

def run_game():	# This function will run a single round of the game
	energy = 10
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False
	
		agent_rect = pygame.Rect(agentpos[0]-dims/2, agentpos[1]-dims/2, dims, dims) # Rectangle for the agent
		apple_rect = pygame.Rect(applepos[0]-dims/2, applepos[1]-dims/2, dims, dims) # Rectangle for the apple

		if agent_rect.colliderect(apple_rect):
			return True
		if energy <= 0:
			return False
		
	
		screen.fill((255, 255, 255))	# Fill the background with white
	
		pygame.draw.rect(screen, (0, 255, 0),	# Draw a square where the worm is
			agent_rect)
		pygame.draw.rect(screen, (255, 0, 0),	# Draw a square where the apple is
			apple_rect)
	
		pygame.display.flip()	# I don't know why we need this but if you remove 
								# it the screen goes black
	
run_game()
	
# Done! Time to quit.

pygame.quit()
