import pygame
from pygame.locals import *

class Horse:
	def __init__(self, player_id, horse_id, img):
		self.player_id = player_id
		self.horse_id = horse_id
		self.sprite_img = pygame.image.load(img)
