import pygame
import time
from pygame.locals import *

class SpritePlayerHorse(pygame.sprite.Sprite):
	def __init__(self, image, rect):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(image)

		self.image_goal = pygame.image.load('images/game/sprite_1p_catch.png')
		self.image_norm = pygame.image.load(image)
		self.rect = rect

	def update(self, i):
		x, y = self.rect



		if i == 1:
			self.image = self.image_goal

		if i == 2:
			self.image = self.image_norm


class SpriteThrowYut(pygame.sprite.Sprite):
	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)

		self.image_norm = pygame.image.load('images/game/sprite_throw.png')
		self.image_over = pygame.image.load('images/game/sprite_throw_mouseover.png')
		self.image_press = pygame.image.load('images/game/sprite_throw_pressed.png')

		self.image = self.image_norm
		self.rect = pos

	def update(self, value):
		if value == 0:
			self.image = self.image_norm
		elif value == 1:
			self.image = self.image_over
		elif value == 2:
			self.image = self.image_press


class SpriteYut(pygame.sprite.Sprite):
	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)

		self.image_nak = []
		for i in range(0, 21):
			self.image_nak.append(pygame.image.load('images/game/yut/0/startPlanetYutGame.yut.0.' + str(i) + '.png'))
		
		self.index = 0
		self.image = self.image_nak[self.index]
		self.rect = pos

	def update(self):
		self.index += 1
		if self.index >= len(self.image_nak):
			self.index = 0
			return
		self.image = self.image_nak[self.index]
		
			