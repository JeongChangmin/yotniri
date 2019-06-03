import pygame, sys, time
import controller

from sprite import *
from mouse import *
from player import Player
from constants import *
from pygame.locals import *

import random

# 초기 화면을 구성하는 메소드
def init_game():
	global windows, fps, set_manager

	# Window Initialize...
	pygame.init()
	windows = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32);
	pygame.display.set_caption('소프트웨어 공학 팀 프로젝트 - 윷놀이')
	pygame.display.set_icon(pygame.image.load('images/icons/icon.png'))

	# 화면 갱신 시간 tick 설정
	fps = pygame.time.Clock()

	# 컨트롤러 관련 객체
	set_manager = controller.SettingManager()

	# Scene 호출
	while True:
		player, horse = intro_scene()
		set_manager.set_settings(player, horse)
		game_scene()


# 인트로 화면을 구성하는 메소드
def intro_scene():
	# 인트로 페이지 설정
	pygame.mixer.music.load('sounds/1.mp3')
	sound_click = pygame.mixer.Sound('sounds/click.wav')

	# 인트로 이미지 렌더링
	bg_intro = pygame.image.load('images/intro/bg_intro.png')
	sprite_title = pygame.image.load('images/intro/sprite_title.png')
	sprite_with = pygame.image.load('images/intro/sprite_title_with.png')
	sprite_touches = []
	for i in range(0, 21):
		sprite_touches.append(pygame.image.load('images/intro/sprite_touch_' + str(i) + '.png'))
	sprite_dialog = pygame.image.load('images/intro/dlg_settings.png')
	sprite_selector = pygame.image.load('images/intro/sprite_selector.png')

	windows.blit(bg_intro, (0, 0))

	# Flag 변수
	flag_intro = True			# 이벤트 반복 플래그
	on_title = False			# 타이틀 애니메이션 플래그
	title_y = -120				# 타이틀 애니메이션 Y-좌표
	flag_alpha = True			# 터치 버튼 알파 플래그
	touch_temp = 0				# 터치 버튼 알파 유지
	touch_alpha = 0				# 터치 버튼 알파값
	on_music = True				# BGM On / Off
	flag_dlg = False			# 다이얼로그 플래그
	click_mouse = False			# 마우스 클릭 체크

	# 반환할 설정 변수 (기본 플레이어 2, 말 4)
	num_of_player = 2
	num_of_horse = 4

	while flag_intro:
		# 인트로 렌더링
		if not flag_dlg:
			windows.blit(bg_intro, (0, 0))
		if on_title and not flag_dlg:
			windows.blit(sprite_with, (523, 100))
			windows.blit(sprite_title, (177, title_y))

		# 인트로 페이지 타이틀 애니메이션
		if not on_title:
			title_y += 15

			if title_y >= 105:
				# 타이틀 로딩 완료 시 음악 재생
				on_title = True
				windows.blit(sprite_with, (523, 100))
				pygame.mixer.music.play(-1)

			windows.blit(sprite_title, (177, title_y))

		# 터치 스프라이트 애니메이션
		if on_title and not flag_dlg:
			if flag_alpha:
				touch_temp += 1
				if touch_alpha < 20:
					touch_alpha += 1
				else:
					if touch_temp < 31:
						touch_temp += 1
					else:
						touch_temp = 0
						touch_alpha -= 2
						flag_alpha = False
			else:
				touch_temp += 1
				if touch_alpha > 0:
					touch_alpha -= 1
				else:
					if touch_temp < 31:
						touch_temp += 1
					else:
						touch_temp = 0
						touch_alpha += 2
						flag_alpha = True

			windows.blit(sprite_touches[touch_alpha], POS_INTRO_TOUCH)

		# 이벤트 설정
		for event in pygame.event.get():
			# 키보드 이벤트
			if event.type == KEYUP:
				# BGM On / Off
				if event.key == ord('p') and on_title:
					if on_music:
						pygame.mixer.music.stop()
						on_music = False
					else:
						pygame.mixer.music.play(-1)
						on_music = True

			# 마우스 클릭 이벤트
			if event.type == MOUSEBUTTONUP:
				mouse_x, mouse_y = get_mouse_pos(event)
				if on_title:
					# 화면 클릭 시 세팅 다이얼로그 오픈
					if 0 <= mouse_x and mouse_x <= 900 and 0 <= mouse_y and mouse_y <= 570 and not flag_dlg:
						sound_click.play()
						windows.blit(bg_intro, (0, 0))
						windows.blit(sprite_with, (523, 100))
						windows.blit(sprite_title, (177, title_y))
						windows.blit(sprite_dialog, (220, 100))
						windows.blit(sprite_selector, (430, 202))
						windows.blit(sprite_selector, (535, 263))

						touch_temp = 0
						touch_alpha = 0

						flag_dlg = True
						num_of_player = 2
						num_of_horse = 4
						continue
					# 다이얼로그가 열려있을 때 처리
				if flag_dlg:
					# 플레이어 체크
					if 418 < mouse_x and mouse_x < 458 and 208 < mouse_y and mouse_y < 248:
						num_of_player = 2
						click_mouse = True
					elif 470 < mouse_x and mouse_x < 510 and 208 < mouse_y and mouse_y < 248:
						num_of_player = 3
						click_mouse = True
					elif 520 < mouse_x and mouse_x < 560 and 208 < mouse_y and mouse_y < 248:
						num_of_player = 4
						click_mouse = True
					# 말 체크
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
					# X 버튼
					elif 628 < mouse_x and mouse_x < 645 and 124 < mouse_y and mouse_y < 140:
						flag_dlg = False
					# 시작 버튼
					elif 495 < mouse_x and mouse_x < 650 and 344 < mouse_y and mouse_y < 404:
						sound_click.play()
						time.sleep(0.5)

						# 게임 화면 이미지 미리 렌더링
						bg_game = pygame.image.load('images/game/bg_game.png')
						windows.blit(bg_game, (0, 0))
						flag_intro = False

					if click_mouse:
						windows.blit(sprite_dialog, (220, 100))
						if num_of_player == 2:
						    windows.blit(sprite_selector, (430, 202))
						elif num_of_player == 3:
						    windows.blit(sprite_selector, (482, 202))
						elif num_of_player == 4:
						    windows.blit(sprite_selector, (535, 202))
						if num_of_horse == 2:
						    windows.blit(sprite_selector, (430, 263))
						elif num_of_horse == 3:
						    windows.blit(sprite_selector, (482, 263))
						elif num_of_horse == 4:
						    windows.blit(sprite_selector, (535, 263))
						elif num_of_horse == 5:
						    windows.blit(sprite_selector, (586, 263))
						sound_click.play()
						click_mouse = False

			# 종료 이벤트
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		# 화면 갱신 주기 30 fps
		pygame.display.update()
		fps.tick(30)

	return num_of_player, num_of_horse

# 게임 화면을 구성하는 메소드
def game_scene():
	# Game Manager Ref
	game_manager = controller.GameManager(set_manager)

	# Flag Variables
	flag_game = True			# main loop
	flag_music = True			# bgm on, off
	flag_throw_pushed = False	# throw yut

	# etc Variables
	rand_yut = 0
	rand_yut_cnt = 0

	# Font
	pygame.font.init()
	font_obj = pygame.font.Font('fonts/malgunbd.ttf', 18)

	# Sound
	pygame.mixer.music.load('sounds/bgm_game.mp3')
	pygame.mixer.music.play(-1)

	sound_click = pygame.mixer.Sound('sounds/click.wav')
	sound_yut_do = []
	sound_yut_gae = []
	sound_yut_girl = []
	sound_yut_yut = []
	sound_yut_mo = []
	sound_yut_back = []
	sound_yut_nak = []
	for i in range(1, 5):
		sound_yut_do.append(pygame.mixer.Sound('sounds/yut_do' + str(i) + '.wav'))
		sound_yut_gae.append(pygame.mixer.Sound('sounds/yut_gae' + str(i) + '.wav'))
		sound_yut_girl.append(pygame.mixer.Sound('sounds/yut_girl' + str(i) + '.wav'))
		sound_yut_yut.append(pygame.mixer.Sound('sounds/yut_yut' + str(i) + '.wav'))
		sound_yut_mo.append(pygame.mixer.Sound('sounds/yut_mo' + str(i) + '.wav'))
		sound_yut_back.append(pygame.mixer.Sound('sounds/yut_back' + str(i) + '.wav'))
		sound_yut_nak.append(pygame.mixer.Sound('sounds/yut_nak' + str(i) + '.wav'))

	# Image Render
	bg_game = pygame.image.load('images/game/bg_game.png')
	windows.blit(bg_game, (0, 0))
	## Sprite Standing ##
	player_1p_standing = 0
	player_2p_standing = 0
	player_3p_standing = 0
	player_4p_standing = 0
	player_standing = []
	## Sprite Player ##
	player_1p_horse = []
	player_2p_horse = []
	player_3p_horse = []
	player_4p_horse = []
	for p in game_manager.get_player():
		if p.player_id == 1:
			if player_1p_standing == 0:
				player_1p_standing = SpritePlayerStanding(1, (55, 65))
				player_standing.append(player_1p_standing)
				font_surface = font_obj.render('박 문 일', True, NAME_COLOR)
				windows.blit(font_surface, (66, 18))
			for h in p.horse:
				if h.horse_id <= 3:
					player_1p_horse.append(SpritePlayerHorse(1, (15 + (h.horse_id - 1) * 60, 158)))
				else:
					player_1p_horse.append(SpritePlayerHorse(1, (15 + (h.horse_id - 4) * 60, 216)))
		elif p.player_id == 2:
			if player_2p_standing == 0:
				player_2p_standing = SpritePlayerStanding(2, (755, 72))
				player_standing.append(player_2p_standing)
				font_surface = font_obj.render('박 민 수', True, NAME_COLOR)
				windows.blit(font_surface, (765, 18))
			for h in p.horse:
				if h.horse_id <= 3:
					player_2p_horse.append(SpritePlayerHorse(2, (715 + (h.horse_id - 1) * 60, 163)))
				else:
					player_2p_horse.append(SpritePlayerHorse(2, (715 + (h.horse_id - 4) * 60, 221)))
		elif p.player_id == 3:
			if player_3p_standing == 0:
				player_3p_standing = SpritePlayerStanding(3, (55, 349))
				player_standing.append(player_3p_standing)
				font_surface = font_obj.render('전 지 훈', True, NAME_COLOR)
				windows.blit(font_surface, (66, 297))
			for h in p.horse:
				if h.horse_id <= 3:
					player_3p_horse.append(SpritePlayerHorse(3, (15 + (h.horse_id - 1) * 60, 431)))
				else:
					player_3p_horse.append(SpritePlayerHorse(3, (15 + (h.horse_id - 4) * 60, 489)))
		elif p.player_id == 4:
			if player_4p_standing == 0:
				player_4p_standing = SpritePlayerStanding(4, (755, 343))
				player_standing.append(player_4p_standing)
				font_surface = font_obj.render('정 창 민', True, NAME_COLOR)
				windows.blit(font_surface, (765, 297))
			for h in p.horse:
				if h.horse_id <= 3:
					player_4p_horse.append(SpritePlayerHorse(4, (715 + (h.horse_id - 1) * 60, 436)))
				else:
					player_4p_horse.append(SpritePlayerHorse(4, (715 + (h.horse_id - 4) * 60, 494)))
	player_standing_group = pygame.sprite.RenderPlain(*player_standing)
	player_1p_horse_group = pygame.sprite.RenderPlain(*player_1p_horse)
	player_2p_horse_group = pygame.sprite.RenderPlain(*player_2p_horse)
	player_3p_horse_group = pygame.sprite.RenderPlain(*player_3p_horse)
	player_4p_horse_group = pygame.sprite.RenderPlain(*player_4p_horse)
	## Sprite Yut ##
	sprite_throw = SpriteThrowYut((514, 503))
	sprite_throw_group = pygame.sprite.RenderPlain(sprite_throw)
	sprite_yut = SpriteYut((240, 70))
	sprite_yut_group = pygame.sprite.RenderPlain(sprite_yut)

	while flag_game:
		# event driven
		for event in pygame.event.get():
			## Quit ##
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			## Key up ##
			if event.type == KEYUP:
				# BGM On, Off
				if event.key == ord('p'):
					if flag_music:
						pygame.mixer.music.stop()
						flag_music = False
					else:
						pygame.mixer.music.play(-1)
						flag_music = True
				# Goto Main
				if event.key == K_ESCAPE:
					flag_game = False
			## Mouse Motion ##
			if event.type == MOUSEMOTION:
				mouse_x, mouse_y = get_mouse_pos(event)

				# Throw Yut
				if 514 <= mouse_x and mouse_x <= 688 and 503 <= mouse_y and mouse_y <= 562:
					sprite_throw.update(1)
				else:
					sprite_throw.update(0)
			## Mouse Button Down ##
			if event.type == MOUSEBUTTONDOWN:
				mouse_x, mouse_y = get_mouse_pos(event)

				# Throw Yut
				if 514 <= mouse_x and mouse_x <= 688 and 503 <= mouse_y and mouse_y <= 562:
					sprite_throw.update(2)
			## Mouse Button Up ##
			if event.type == MOUSEBUTTONUP:
				mouse_x, mouse_y = get_mouse_pos(event)

				# Throw Yut
				if 514 <= mouse_x and mouse_x <= 688 and 503 <= mouse_y and mouse_y <= 562 and not flag_throw_pushed:
					sprite_throw.update(0)
					flag_throw_pushed = True
					rand_yut = random.randint(-1, 5)
					rand_yut_cnt = 0

		# update
		## sprite throw yut ##
		if flag_throw_pushed:
			sprite_yut_group.update(rand_yut)
			sprite_yut_group.clear(windows, bg_game)
			sprite_yut_group.draw(windows)

			rand_yut_cnt += 1

			if rand_yut_cnt == 15:
				if rand_yut == -1:
					sound_yut_back[random.randint(0, 3)].play()
				elif rand_yut == 0:
					sound_yut_nak[random.randint(0, 3)].play()
				elif rand_yut == 1:
					sound_yut_do[random.randint(0, 3)].play()
				elif rand_yut == 2:
					sound_yut_gae[random.randint(0, 3)].play()
				elif rand_yut == 3:
					sound_yut_girl[random.randint(0, 3)].play()
				elif rand_yut == 4:
					sound_yut_yut[random.randint(0, 3)].play()
				elif rand_yut == 5:
					sound_yut_mo[random.randint(0, 3)].play()
				time.sleep(1.0)
			else:
				time.sleep(0.1)

			if rand_yut_cnt == 21:
				flag_throw_pushed = False
				rand_yut_cnt = 0
				sprite_yut_group.clear(windows, bg_game)
		## sprite player ##
		player_standing_group.update()
		player_1p_horse_group.update()
		player_2p_horse_group.update()
		player_3p_horse_group.update()
		player_4p_horse_group.update()
		player_standing_group.clear(windows, bg_game)
		player_1p_horse_group.clear(windows, bg_game)
		player_2p_horse_group.clear(windows, bg_game)
		player_3p_horse_group.clear(windows, bg_game)
		player_4p_horse_group.clear(windows, bg_game)
		player_standing_group.draw(windows)
		player_1p_horse_group.draw(windows)
		player_2p_horse_group.draw(windows)
		player_3p_horse_group.draw(windows)
		player_4p_horse_group.draw(windows)
		## sprite throw yut ##
		sprite_throw_group.clear(windows, bg_game)
		sprite_throw_group.draw(windows)

		# all screen flip
		pygame.display.flip()
		fps.tick(FPS)

# 게임 실행
init_game()
