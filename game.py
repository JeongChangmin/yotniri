import pygame
from pygame.locals import *

windows = pygame.display.set_mode((400, 300), 0, 32);
pygame.display.set_caption('Term Project - Yut')

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			quit()