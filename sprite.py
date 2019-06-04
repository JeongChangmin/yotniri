import pygame
import time
from pygame.locals import *

## 인트로 스프라이트 ##
class IntroTitle(pygame.sprite.Sprite):
	def __init__(self, src, pos):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(src)
		self.rect = pos

	def update(self, pos):
		self.rect = pos

class IntroTouch(pygame.sprite.Sprite):
	def __init__(self, src, pos):
		pygame.sprite.Sprite.__init__(self)

		self.index = 0
		self.flag = True
		self.images = []
		for i in range(0, 21):
			self.images.append(pygame.image.load(src + str(i) + '.png'))
		self.image = self.images[0]
		self.rect = pos

	def update(self, on_dlg):
		if not on_dlg:
			if self.index >= (len(self.images)-1):
				self.flag = False
			if self.index == 0:
				self.flag = True

			if self.flag:
				self.index += 1
			else:
				self.index -= 1
		else:
			self.index = 20
		self.image = self.images[self.index]


## 인게임 스프라이트 ##
class ThrowYut(pygame.sprite.Sprite):
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

class Horse(pygame.sprite.Sprite):
	def __init__(self, player_id, pos):
		pygame.sprite.Sprite.__init__(self)

		self.image_norm = pygame.image.load('images/game/sprite_' + str(player_id) + 'p_normal.png')
		self.image_goal = pygame.image.load('images/game/sprite_' + str(player_id) + 'p_goal.png')
		self.image_move = pygame.image.load('images/game/sprite_' + str(player_id) + 'p_move.png')
		self.image_catch = pygame.image.load('images/game/sprite_' + str(player_id) + 'p_catch.png')

		self.image = self.image_norm
		self.rect = pos

	def update(self):
		pass

class Yut(pygame.sprite.Sprite):
	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)

		self.num_of_img = 21
		self.image_do = []
		self.image_gae = []
		self.image_girl = []
		self.image_yut = []
		self.image_mo = []
		self.image_back = []

		for i in range(0, self.num_of_img):
			self.image_do.append(pygame.image.load('images/game/yut/1/startPlanetYutGame.yut.1.' + str(i) + '.png'))
			self.image_gae.append(pygame.image.load('images/game/yut/2/startPlanetYutGame.yut.2.' + str(i) + '.png'))
			self.image_girl.append(pygame.image.load('images/game/yut/3/startPlanetYutGame.yut.3.' + str(i) + '.png'))
			self.image_yut.append(pygame.image.load('images/game/yut/4/startPlanetYutGame.yut.4.' + str(i) + '.png'))
			self.image_mo.append(pygame.image.load('images/game/yut/5/startPlanetYutGame.yut.5.' + str(i) + '.png'))
			self.image_back.append(pygame.image.load('images/game/yut/0/startPlanetYutGame.yut.-1.' + str(i) + '.png'))

		self.index = 0
		self.image = self.image_do[self.index]
		self.rect = pos

	def update(self, value):
		self.index += 1
		if self.index >= len(self.image_do):
			self.index = 0

		if value == 0:
			self.image = self.image_back[self.index]
		elif value == 1:
			self.image = self.image_do[self.index]
		elif value == 2:
			self.image = self.image_gae[self.index]
		elif value == 3:
			self.image = self.image_girl[self.index]
		elif value == 4:
			self.image = self.image_yut[self.index]
		elif value == 5:
			self.image = self.image_mo[self.index]
