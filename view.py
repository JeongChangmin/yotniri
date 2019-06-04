import controller

import pygame
import sys
import time

import sprite

from const import *
from pygame.locals import *

import random

class View:
	# Initialize...
	def __init__(self):
		# View 초기 설정
		pygame.init()
		self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32);
		pygame.display.set_caption('소프트웨어 공학 팀 프로젝트 - 윷놀이')
		pygame.display.set_icon(pygame.image.load('images/icons/icon.png'))

		# 동기화 관련 변수
		self.fps = pygame.time.Clock()

	# Show Intro
	def show_intro(self, controller):
		# 이미지 (배경 / 스프라이트)
		sprite_bg = pygame.image.load('images/intro/bg_intro.png')
		sprite_title = sprite.IntroTitle('images/intro/sprite_title.png', POS_INTRO_TITLE)
		sprite_title_w = sprite.IntroTitle('images/intro/sprite_title_with.png', POS_INTRO_TITLE_W)
		sprite_touch = sprite.IntroTouch('images/intro/sprite_touch_', POS_INTRO_TOUCH)
		sprite_dlg = sprite.IntroTitle('images/intro/dlg_settings.png', POS_INTRO_DLG)
		sprite_selector = pygame.image.load('images/intro/sprite_selector.png')
		self.window.blit(sprite_bg, POS_ORIGIN)

		# 이미지 렌더링
		sprite_title_g = pygame.sprite.RenderPlain(sprite_title)
		sprite_title_w_g = pygame.sprite.RenderPlain(sprite_title_w)
		sprite_touch_g = pygame.sprite.RenderPlain(sprite_touch)
		sprite_dlg_g = pygame.sprite.RenderPlain(sprite_dlg)

		# 사운드 (배경 / 효과음)
		pygame.mixer.music.load('sounds/1.mp3')
		sound_click = pygame.mixer.Sound('sounds/click.wav')

		# 플래그
		event_loop = True				# 이벤트 반복
		on_title = False				# 타이틀 애니메이션 플래그
		title_x = POS_INTRO_TITLE[0]	# 타이틀 이미지 X-좌표
		title_y = POS_INTRO_TITLE[1]	# 타이틀 이미지 Y-좌표
		on_dlg = False					# 다이얼로그 플래그
		click_mouse = False				# 마우스 클릭 플래그

		num_of_player = 0				# 다이얼로그 세팅 값 (플레이어)
		num_of_horse = 0				# 다이얼로그 세팅 값 (말)

		# 이벤트 처리
		while event_loop:
			# 타이틀 로딩 애니메이션
			if not on_title:
				title_y += 15
				sprite_title_g.update((title_x, title_y))
				sprite_title_g.clear(self.window, sprite_bg)
				sprite_title_g.draw(self.window)
				if title_y >= 105:
					on_title = True
					sprite_title_w_g.draw(self.window)
					pygame.mixer.music.play(-1)

			# 터치 애니메이션
			if on_title:
				sprite_touch_g.update(on_dlg)
				sprite_touch_g.clear(self.window, sprite_bg)
				sprite_touch_g.draw(self.window)

			for event in pygame.event.get():
				# 종료 이벤트
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

				# 마우스 이벤트
				if event.type == MOUSEBUTTONUP:
					mouse_x, mouse_y = self.get_mouse_pos(event)

					# 다이얼로그
					if on_title:
						if 0 <= mouse_x and mouse_x <= WINDOW_WIDTH and 0 <= mouse_y and mouse_y <= WINDOW_HEIGHT and not on_dlg:
							sound_click.play()
							
							sprite_dlg_g.draw(self.window)
							self.window.blit(sprite_selector, (430, 202))
							self.window.blit(sprite_selector, (535, 263))

							num_of_player, num_of_horse = controller.action('get_setting_default')
							
							on_dlg = True
							continue
					if on_dlg:
						# 플레이어 클릭
						if 418 < mouse_x and mouse_x < 458 and 208 < mouse_y and mouse_y < 248:
							num_of_player = 2
							click_mouse = True
						elif 470 < mouse_x and mouse_x < 510 and 208 < mouse_y and mouse_y < 248:
							num_of_player = 3
							click_mouse = True
						elif 520 < mouse_x and mouse_x < 560 and 208 < mouse_y and mouse_y < 248:
							num_of_player = 4
							click_mouse = True

						# 말 클릭
						elif 418 < mouse_x and mouse_x < 458 and 269 < mouse_y and mouse_y < 308:
							num_of_horse = 2
							click_mouse = True
						elif 470 < mouse_x and mouse_x < 510 and 269 < mouse_y and mouse_y < 308:
							num_of_horse = 3
							click_mouse = True
						elif 520 < mouse_x and mouse_x < 560 and 269 < mouse_y and mouse_y < 308:
							num_of_horse = 4
							click_mouse = True
						elif 572 < mouse_x and mouse_x < 612 and 269 < mouse_y and mouse_y < 308:
							num_of_horse = 5
							click_mouse = True

						# X 버튼 클릭
						elif 628 < mouse_x and mouse_x < 645 and 124 < mouse_y and mouse_y < 140:
							sprite_dlg_g.clear(self.window, sprite_bg)
							sprite_title_g.draw(self.window)
							sprite_title_w_g.draw(self.window)
							on_dlg = False

						# 게임 시작 클릭
						elif 495 < mouse_x and mouse_x < 650 and 344 < mouse_y and mouse_y < 404:
							sound_click.play()
							time.sleep(0.5)

							# 설정 저장
							controller.action('set_setting', { 'num_of_player' : num_of_player, 'num_of_horse' : num_of_horse})
							
							sprite_bg = pygame.image.load('images/game/bg_game.png')
							event_loop = False

						if click_mouse:
							sprite_dlg_g.draw(self.window)
							if num_of_player == 2:
							    self.window.blit(sprite_selector, (430, 202))
							elif num_of_player == 3:
							    self.window.blit(sprite_selector, (482, 202))
							elif num_of_player == 4:
							    self.window.blit(sprite_selector, (535, 202))
							if num_of_horse == 2:
							    self.window.blit(sprite_selector, (430, 263))
							elif num_of_horse == 3:
							    self.window.blit(sprite_selector, (482, 263))
							elif num_of_horse == 4:
							    self.window.blit(sprite_selector, (535, 263))
							elif num_of_horse == 5:
							    self.window.blit(sprite_selector, (586, 263))
							sound_click.play()
							click_mouse = False

			# 화면 업데이트
			pygame.display.update()
			self.fps.tick(FPS)


	# Show Game
	def show_game(self, controller):
		# 폰트
		pygame.font.init()
		font_obj = pygame.font.Font('fonts/malgunbd.ttf', 18)

		# 배경 이미지
		sprite_bg = pygame.image.load('images/game/bg_game.png')
		self.window.blit(sprite_bg, POS_ORIGIN)

		# 폰트 처리 / 스탠딩 처리
		for i in range(0, len(controller.player)):
			font_surface = font_obj.render(controller.player[i].player_name, True, NAME_COLOR)
			sprite_standing = pygame.image.load('images/game/sprite_' + str(i+1) + 'p_standing.png')

			if i == 0:
				self.window.blit(font_surface, (66, 18))
				self.window.blit(sprite_standing, POS_1P_STANDING)
			elif i == 1:
				self.window.blit(font_surface, (765, 18))
				self.window.blit(sprite_standing, POS_2P_STANDING)
			elif i == 2:
				self.window.blit(font_surface, (66, 297))
				self.window.blit(sprite_standing, POS_3P_STANDING)
			elif i == 3:
				self.window.blit(font_surface, (765, 297))
				self.window.blit(sprite_standing, POS_4P_STANDING)

		# 스프라이트
		sprite_throw = sprite.ThrowYut(POS_GAME_THROW_YUT)
		sprite_yut = sprite.Yut(POS_GAME_YUT)

		# 이미지 렌더링
		sprite_throw_g = pygame.sprite.RenderPlain(sprite_throw)
		sprite_yut_g = pygame.sprite.RenderPlain(sprite_yut)

		# 사운드 (배경 / 효과음)
		pygame.mixer.Sound('sounds/start.wav').play()
		pygame.mixer.music.load('sounds/bgm_game.mp3')
		pygame.mixer.music.play(-1)
		sound_click = pygame.mixer.Sound('sounds/click.wav')
		sound_yut = []
		sound_yut_do = []
		sound_yut_gae = []
		sound_yut_girl = []
		sound_yut_yut = []
		sound_yut_mo = []
		sound_yut_back = []
		for i in range(1, 5):
			sound_yut_do.append(pygame.mixer.Sound('sounds/yut_do' + str(i) + '.wav'))
			sound_yut_gae.append(pygame.mixer.Sound('sounds/yut_gae' + str(i) + '.wav'))
			sound_yut_girl.append(pygame.mixer.Sound('sounds/yut_girl' + str(i) + '.wav'))
			sound_yut_yut.append(pygame.mixer.Sound('sounds/yut_yut' + str(i) + '.wav'))
			sound_yut_mo.append(pygame.mixer.Sound('sounds/yut_mo' + str(i) + '.wav'))
			sound_yut_back.append(pygame.mixer.Sound('sounds/yut_back' + str(i) + '.wav'))
		sound_yut.append(sound_yut_back)
		sound_yut.append(sound_yut_do)
		sound_yut.append(sound_yut_gae)
		sound_yut.append(sound_yut_girl)
		sound_yut.append(sound_yut_yut)
		sound_yut.append(sound_yut_mo)
		sound_catch = []
		for i in range(1, 4):
			sound_catch.append(pygame.mixer.Sound('sounds/catch' + str(i) + '.wav'))
		sound_goal = []
		for i in range(1, 6):
			sound_goal.append(pygame.mixer.Sound('sounds/goal' + str(i) + '.wav'))
		sound_win = pygame.mixer.Sound('sounds/Win_Y.wav')
			
		# 플래그
		event_loop = True				# 이벤트 반복
		rand_yut = 0					# 윷 던지기 결과
		throw_push = False				# 윷 던지기 플래그
		rand_yut_cnt = 0				# 윷 던지기 카운트 (스프라이트)
		

		# 이벤트 처리
		while event_loop:
			for event in pygame.event.get():
				# 종료 이벤트
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

				# 키보드 이벤트
				if event.type == KEYUP:
					if event.key == K_ESCAPE:
						event_loop = False

				# 마우스 이벤트 (모션)
				if event.type == MOUSEMOTION:
					mouse_x, mouse_y = self.get_mouse_pos(event)

					# 윷 던지기
					if 514 <= mouse_x and mouse_x <= 688 and 503 <= mouse_y and mouse_y <= 562 and not throw_push:
						sprite_throw.update(1)
					else:
						sprite_throw.update(0)

				# 마우스 이벤트 (클릭 다운)
				if event.type == MOUSEBUTTONDOWN:
					mouse_x, mouse_y = self.get_mouse_pos(event)

					# 윷 던지기
					if 514 <= mouse_x and mouse_x <= 688 and 503 <= mouse_y and mouse_y <= 562 and not throw_push:
						sprite_throw.update(2)

				# 마우스 이벤트 (클릭 업)
				if event.type == MOUSEBUTTONUP:
					mouse_x, mouse_y = self.get_mouse_pos(event)

					# 윷 던지기
					if 514 <= mouse_x and mouse_x <= 688 and 503 <= mouse_y and mouse_y <= 562 and not throw_push:
						sprite_throw.update(0)

						throw_push = True
						rand_yut_cnt = 0
						rand_yut = controller.random_yut()

			
			# 윷 던지기 애니메이션
			if throw_push:
				sprite_yut_g.update(rand_yut)
				sprite_yut_g.clear(self.window, sprite_bg)
				sprite_yut_g.draw(self.window)

				rand_yut_cnt += 1

				if rand_yut_cnt == 15:
					sound_yut[rand_yut][random.randint(0, 3)].play()
					time.sleep(1.0)
				else:
					time.sleep(0.1)

				if rand_yut_cnt == 21:
					throw_push = False
					rand_yut_cnt = 0
					sprite_yut_g.clear(self.window, sprite_bg)
			

			# 이미지 업데이트
			sprite_throw_g.clear(self.window, sprite_bg)
			sprite_throw_g.draw(self.window)

			# 화면 업데이트
			pygame.display.update()
			self.fps.tick(FPS)

	# Get Mouse Pos
	def get_mouse_pos(self, event):
		return event.pos