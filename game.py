# Import
import pygame
from pygame.locals import *

# Contants
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 700

BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED   = (255,  0,  0)
GREEN = (0  ,255,  0)
BLUE  = (0  ,  0,255)

FPS = 30

# Window Setting
pygame.init()

windows = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32);
pygame.display.set_caption('Term Project - Yut')
fps_clock = pygame.time.Clock()


# Scenes
def IntroScene():
	intro = True

	while intro:
		windows.fill(BLACK)

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				quit()
			if event.type == KEYUP:
				if event.key == ord('a'):
					intro = False

		pygame.display.update()
		fps_clock.tick(30)

def SettingScene():
	setting = True

	while setting:
		windows.fill(GREEN)

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				quit()
			if event.type == KEYUP:
				if event.key == ord('s'):
					setting = False

		pygame.display.update()
		fps_clock.tick(30)

def GameScene():
	game = True

	while game:
		windows.fill(RED)

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				quit()
			if event.type == KEYUP:
				if event.key == ord('d'):
					game = False

		pygame.display.update()
		fps_clock.tick(30)


while True:
	IntroScene()
	SettingScene()
	GameScene()