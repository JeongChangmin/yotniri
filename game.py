import pygame, sys, time
import controller
from mouse import *
from player import Player
from constants import *
from pygame.locals import *

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
		print('dd')
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
						pygame.mixer.music.set_volume(0.0)
						music = False
					else:
						pygame.mixer.music.play(-1)
						pygame.mixer.music.set_volume(1.0)
						music = True

			# 마우스 클릭 이벤트
			if event.type == MOUSEBUTTONUP:
				if on_title:
					mouse_x, mouse_y = get_mouse_pos(event)
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
	# 게임 페이지 설정
	pygame.font.init()
	fontObj = pygame.font.Font('fonts/malgun.ttf', 18)

	pygame.mixer.music.load('sounds/bgm_game.mp3')
	pygame.mixer.music.play(-1)
	sound_click = pygame.mixer.Sound('sounds/click.wav')

	# 게임 관리 객체
	game_manager = controller.GameManager(set_manager)

	# 게임 이미지 렌더링
	bg_game = pygame.image.load('images/game/bg_game.png')
	sprite_throw = pygame.image.load('images/game/sprite_throw.png')
	windows.blit(bg_game, (0, 0))
	windows.blit(sprite_throw, (514, 503))

	# Flag 변수
	flag_game = True			# 이벤트 반복 플래그
	on_music = True				# BGM On / Off
	
	while flag_game:
		# 플레이어 렌더링
		for p in game_manager.get_player():
			if p.player_id == 1:
				textSurface = fontObj.render('박 문 일', True, WHITE)
				textRect = textSurface.get_rect()
				textRect.center = (96, 29)
				windows.blit(textSurface, textRect)
				for h in p.horse:
					if h.horse_id <= 3:  
						windows.blit(h.sprite_img, (15 + (h.horse_id - 1) * 60, 165))
					else:
						windows.blit(h.sprite_img, (15 + (h.horse_id - 4) * 60, 225))
			elif p.player_id == 2:
				textSurface = fontObj.render('박 민 수', True, WHITE)
				textRect = textSurface.get_rect()
				textRect.center = (798, 29)
				windows.blit(textSurface, textRect)
				for h in p.horse:
					if h.horse_id <= 3:
						windows.blit(h.sprite_img, (712 + (h.horse_id - 1) * 60, 165))
					else:
						windows.blit(h.sprite_img, (712 + (h.horse_id - 4) * 60, 225))
			elif p.player_id == 3:
				textSurface = fontObj.render('전 지 훈', True, WHITE)
				textRect = textSurface.get_rect()
				textRect.center = (96, 310)
				windows.blit(textSurface, textRect)
				for h in p.horse:
					if h.horse_id <= 3:
						windows.blit(h.sprite_img, (15 + (h.horse_id - 1) * 60, 444))
					else:
						windows.blit(h.sprite_img, (15 + (h.horse_id - 4) * 60, 504))
			elif p.player_id == 4:
				textSurface = fontObj.render('정 창 민', True, WHITE)
				textRect = textSurface.get_rect()
				textRect.center = (798, 310)
				windows.blit(textSurface, textRect)
				for h in p.horse:
					if h.horse_id <= 3:
						windows.blit(h.sprite_img, (712 + (h.horse_id - 1) * 60, 444))
					else:
						windows.blit(h.sprite_img, (712 + (h.horse_id - 4) * 60, 504))

		for event in pygame.event.get():
			# 종료 이벤트
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			# 키보드 이벤트
			if event.type == KEYUP:
				# BGM On / Off
				if event.key == ord('p'):
					if music:
						pygame.mixer.music.stop()
						music = False
					else:
						pygame.mixer.music.play(-1)
						music = True
				# 메인 화면으로 이동
				if event.key == K_ESCAPE:
					flag_game = False
                

		# 화면 갱신 주기 30 fps
		pygame.display.update()
		fps.tick(30)

# 게임 실행
init_game()
