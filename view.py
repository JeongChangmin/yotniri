import controller

import pygame
import sys
import time

import copy

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
		# 스프라이트 임포팅
		import sprite

		# 이미지 < 배경 / 스프라이트 >
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

							num_of_player, num_of_horse = controller.default_value

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
							controller.num_of_player = num_of_player
							controller.num_of_horse = num_of_horse

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
		# 스프라이트 임포팅
		import sprite

		# 폰트
		pygame.font.init()
		font_obj = pygame.font.Font('fonts/malgunbd.ttf', 18)
	
		# 배경 이미지
		sprite_bg = pygame.image.load('images/game/bg_game.png')
		self.window.blit(sprite_bg, POS_ORIGIN)
	
		# 말을 전부 처리
		sprite_horse = []
		sprite_mover = []
	
		# 폰트 처리 / 스탠딩 처리
		n = controller.num_of_player
		h = controller.num_of_horse
		for i in range(0, n):
			font_surface = font_obj.render(controller.player[i].player_name, True, NAME_COLOR)
			sprite_standing = pygame.image.load('images/game/sprite_' + str(i+1) + 'p_standing.png')
	
			sprite_temp = []
			sprite_temp_2 = []
			sprite_temp_3 = []

			if i == 0:
				for n in range(0, h):
					if n < 3:
						sprite_temp.append(sprite.Horse(i + 1, n + 1, (POS_1P_HORSE_X + (n * 58), POS_1P_HORSE_Y_1)))
						sprite_temp_2.append(sprite.Horse(i + 1, n + 1, (-100,-100)))
					else:
						sprite_temp.append(sprite.Horse(i + 1, n + 1, (POS_1P_HORSE_X + ((n - 3) * 58), POS_1P_HORSE_Y_2)))
						sprite_temp_2.append(sprite.Horse(i + 1, n + 1, (-100,-100)))
				sprite_horse.append(sprite_temp)
				sprite_mover.append(sprite_temp_2)
				self.window.blit(font_surface, (66, 18))
				self.window.blit(sprite_standing, POS_1P_STANDING)
			elif i == 1:
				sprite_temp = []
				for n in range(0, h):
					if n < 3:
						sprite_temp.append(sprite.Horse(i + 1, n + 1, (POS_2P_HORSE_X + (n * 58), POS_2P_HORSE_Y_1)))
						sprite_temp_2.append(sprite.Horse(i + 1, n + 1, (-100,-100)))
					else:
						sprite_temp.append(sprite.Horse(i + 1, n + 1, (POS_2P_HORSE_X + ((n - 3) * 58), POS_2P_HORSE_Y_2)))
						sprite_temp_2.append(sprite.Horse(i + 1, n + 1, (-100,-100)))
				sprite_horse.append(sprite_temp)
				sprite_mover.append(sprite_temp_2)
				self.window.blit(font_surface, (765, 18))
				self.window.blit(sprite_standing, POS_2P_STANDING)
			elif i == 2:
				sprite_temp = []
				for n in range(0, h):
					if n < 3:
						sprite_temp.append(sprite.Horse(i + 1, n + 1, (POS_3P_HORSE_X + (n * 58), POS_3P_HORSE_Y_1)))
						sprite_temp_2.append(sprite.Horse(i + 1, n + 1, (-100,-100)))
					else:
						sprite_temp.append(sprite.Horse(i + 1, n + 1, (POS_3P_HORSE_X + ((n - 3) * 58), POS_3P_HORSE_Y_2)))
						sprite_temp_2.append(sprite.Horse(i + 1, n + 1, (-100,-100)))
				sprite_horse.append(sprite_temp)
				sprite_mover.append(sprite_temp_2)
				self.window.blit(font_surface, (66, 297))
				self.window.blit(sprite_standing, POS_3P_STANDING)
			elif i == 3:
				sprite_temp = []
				for n in range(0, h):
					if n < 3:
						sprite_temp.append(sprite.Horse(i + 1, n + 1, (POS_4P_HORSE_X + (n * 58), POS_4P_HORSE_Y_1)))
						sprite_temp_2.append(sprite.Horse(i + 1, n + 1, (-100,-100)))
					else:
						sprite_temp.append(sprite.Horse(i + 1, n + 1, (POS_4P_HORSE_X + ((n - 3) * 58), POS_4P_HORSE_Y_2)))
						sprite_temp_2.append(sprite.Horse(i + 1, n + 1, (-100,-100)))
				sprite_horse.append(sprite_temp)
				sprite_mover.append(sprite_temp_2)
				self.window.blit(font_surface, (765, 297))
				self.window.blit(sprite_standing, POS_4P_STANDING)
	
		# 스프라이트
		sprite_throw = sprite.ThrowYut(POS_GAME_THROW_YUT)
		sprite_yut = sprite.Yut(POS_GAME_YUT)
		sprite_gameover = sprite.GameOver(POS_GAMEOVER)

		sprite_yut_result = [
			pygame.image.load('images/game/sprite_yut_result_0.png'),
			pygame.image.load('images/game/sprite_yut_result_1.png'),
			pygame.image.load('images/game/sprite_yut_result_2.png'),
			pygame.image.load('images/game/sprite_yut_result_3.png'),
			pygame.image.load('images/game/sprite_yut_result_4.png'),
			pygame.image.load('images/game/sprite_yut_result_5.png')
		]
		sprite_stack = [
			sprite.GroupStack('images/game/sprite_group_2.png', (-30, -30)),
			sprite.GroupStack('images/game/sprite_group_3.png', (-30, -30)),
			sprite.GroupStack('images/game/sprite_group_4.png', (-30, -30)),
			sprite.GroupStack('images/game/sprite_group_5.png', (-30, -30))
		]


		# 이미지 렌더링
		sprite_throw_g = pygame.sprite.RenderPlain(sprite_throw)
		sprite_yut_g = pygame.sprite.RenderPlain(sprite_yut)
		sprite_stack_g = pygame.sprite.RenderPlain(*sprite_stack)
		sprite_gameover_g = pygame.sprite.RenderPlain(sprite_gameover)
	
		sprite_horse_render = []
		for sprite in sprite_horse:
			sprite_horse_render.append(pygame.sprite.RenderPlain(*sprite))
		sprite_mover_render = []
		for sprite in sprite_mover:
			sprite_mover_render.append(pygame.sprite.RenderPlain(*sprite))

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
		is_gameover = False				# 게임오버 플래그
		rand_yut = 0					# 윷 던지기 결과
		throw_push = False				# 윷 던지기 플래그
		yut_animate_cnt = 0				# 윷 던지기 카운트 (스프라이트)
	
		movable = False					# 말을 이동해야할 차례
		on_selector = False				# 셀렉터 표시
		select_horse = False			# 말 선택 했는지 체크
		select_result = False			# 이동할 값 선택 했는지 체크
		flag_key = False				# 키보드 조작으로 윷 던지기
	
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

					# 윷 임의 조작
					if not throw_push and not on_selector:
						# a 뒷도부터...
						if event.key == ord('a'):
							rand_yut = 0
							flag_key = True
						elif event.key == ord('s'):
							rand_yut = 1
							flag_key = True
						elif event.key == ord('d'):
							rand_yut = 2
							flag_key = True
						elif event.key == ord('f'):
							rand_yut = 3
							flag_key = True
						elif event.key == ord('g'):
							rand_yut = 4
							flag_key = True
						elif event.key == ord('h'):
							rand_yut = 5
							flag_key = True

						if flag_key:
							throw_push = True
							yut_animate_cnt = 0

				# 마우스 이벤트 (모션)
				if event.type == MOUSEMOTION and not is_gameover:
					mouse_x, mouse_y = self.get_mouse_pos(event)
	
					# 윷 던지기
					if 514 <= mouse_x and mouse_x <= 688 and 503 <= mouse_y and mouse_y <= 562 and not throw_push and not on_selector:
						sprite_throw.update(1)
					else:
						sprite_throw.update(0)
	
				# 마우스 이벤트 (클릭 다운)
				if event.type == MOUSEBUTTONDOWN and not is_gameover:
					mouse_x, mouse_y = self.get_mouse_pos(event)
	
					# 윷 던지기
					if 514 <= mouse_x and mouse_x <= 688 and 503 <= mouse_y and mouse_y <= 562 and not throw_push and not on_selector:
						sprite_throw.update(2)
	
				# 마우스 이벤트 (클릭 업)
				if event.type == MOUSEBUTTONUP:
					mouse_x, mouse_y = self.get_mouse_pos(event)
					
					# 게임 오버 시 메인화면으로 이동
					if is_gameover:
						if 0 <= mouse_x and mouse_x <= WINDOW_WIDTH and 0 <= mouse_y and mouse_y <= WINDOW_HEIGHT:
							event_loop = False
					else:
						# 윷 던지기
						if 514 <= mouse_x and mouse_x <= 688 and 503 <= mouse_y and mouse_y <= 562 and not throw_push and not on_selector:
							sprite_throw.update(0)
	
							throw_push = True
							yut_animate_cnt = 0
							rand_yut = controller.throw_random_yut()


						# 셀렉터가 배치되어 있을 시 (말 선택)
						print(mouse_x, mouse_y)
						
						######
						# 1P
						######
						if controller.turn == 1 and on_selector:
							push = False

							if 15 <= mouse_x and mouse_x <= 63 and 167 <= mouse_y and mouse_y <= 213 and controller.num_of_horse >= 1:
								if not controller.player[controller.turn-1].horse[0].goal:
									ret = controller.game.move(controller, controller.player[0], controller.player[0].horse[0])

									if 'fail' in ret:
										push = True
										on_selector = False
									else:
										if 'goal' in ret:
											if 'group' in ret:
												if controller.player[0].horse[0].goal:
													pass
												else:
													for group in controller.player[0].group:
														if controller.player[0].horse[0].horse_id in group:
															for h in group:
																sprite_horse[0][h-1].switch('goal')
																sprite_mover[0][h-1].ret_wait()
																controller.player[0].goal += 1
																controller.player[0].horse[h-1].goal = True
															sound_goal[random.randint(0,4)].play()
											else:
												if controller.player[0].horse[0].goal:
													pass
												else:
													sprite_horse[0][0].switch('goal')
													sprite_mover[0][0].ret_wait()
													controller.player[0].goal += 1
													controller.player[0].horse[0].goal = True
													sound_goal[random.randint(0,4)].play()
											push = True
										elif 'catch' in ret:
											# 말을 잡았으니 위치 갱신
											sprite_mover[ret[0]-1][ret[1]-1].update((-100,-100))

											# 자기자신 렌더링 (그룹 체크)
											for group in controller.player[0].group:
												if controller.player[0].horse[0].horse_id in group:
													for h in group:
														sprite_mover[0][h-1].update(POS_SPRITE_HORSE[controller.player[0].horse[h-1].position[1]][controller.player[0].horse[h-1].position[0]])
											#sprite_mover[0][0].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[0].position[1]][controller.player[controller.turn-1].horse[0].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										elif 'groupcatch' in ret:
											# 말을 잡았으니 위치 갱신
											for h_index in ret[3]:
												sprite_mover[ret[0]-1][h_index-1].update((-100,-100))
											# 자기자신 렌더링 (그룹 체크)
											for group in controller.player[0].group:
												if controller.player[0].horse[0].horse_id in group:
													for h in group:
														sprite_mover[0][h-1].update(POS_SPRITE_HORSE[controller.player[0].horse[h-1].position[1]][controller.player[0].horse[h-1].position[0]])
											#sprite_mover[0][0].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[0].position[1]][controller.player[controller.turn-1].horse[0].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										else:
											if 'group' in ret:
												for group in controller.player[0].group:
													if controller.player[0].horse[0].horse_id in group:
														for h in group:
															sprite_mover[0][h-1].update(POS_SPRITE_HORSE[controller.player[0].horse[h-1].position[1]][controller.player[0].horse[h-1].position[0]])
											else:
												sprite_mover[0][0].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[0].position[1]][controller.player[controller.turn-1].horse[0].position[0]])
											push = True

										on_selector = False

							elif 75 <= mouse_x and mouse_x <= 123 and 167 <= mouse_y and mouse_y <= 213 and controller.num_of_horse >= 2:
								if not controller.player[controller.turn-1].horse[1].goal:
									ret = controller.game.move(controller, controller.player[0], controller.player[0].horse[1])

									if 'fail' in ret:
										push = True
										on_selector = False
									else:
										if 'goal' in ret:
											if 'group' in ret:
												if controller.player[0].horse[1].goal:
													pass
												else:
													for group in controller.player[0].group:
														if controller.player[0].horse[1].horse_id in group:
															for h in group:
																sprite_horse[0][h-1].switch('goal')
																sprite_mover[0][h-1].ret_wait()
																controller.player[0].goal += 1
																controller.player[0].horse[h-1].goal = True
															sound_goal[random.randint(0,4)].play()
											else:
												if controller.player[0].horse[1].goal:
													pass
												else:
													sprite_horse[0][1].switch('goal')
													sprite_mover[0][1].ret_wait()
													controller.player[0].goal += 1
													controller.player[0].horse[0].goal = True
													sound_goal[random.randint(0,4)].play()
											push = True
										elif 'catch' in ret:
											# 말을 잡았으니 위치 갱신
											sprite_mover[ret[0]-1][ret[1]-1].update((-100,-100))
											
											# 자기자신 렌더링 (그룹 체크)
											for group in controller.player[0].group:
													if controller.player[0].horse[1].horse_id in group:
														for h in group:
															sprite_mover[0][h-1].update(POS_SPRITE_HORSE[controller.player[0].horse[h-1].position[1]][controller.player[0].horse[h-1].position[0]])
											#sprite_mover[0][1].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[1].position[1]][controller.player[controller.turn-1].horse[1].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										elif 'groupcatch' in ret:
											# 말을 잡았으니 위치 갱신
											for h_index in ret[3]:
												sprite_mover[ret[0]-1][h_index-1].update((-100,-100))
											# 자기자신 렌더링 (그룹 체크)
											for group in controller.player[0].group:
													if controller.player[0].horse[1].horse_id in group:
														for h in group:
															sprite_mover[0][h-1].update(POS_SPRITE_HORSE[controller.player[0].horse[h-1].position[1]][controller.player[0].horse[h-1].position[0]])
											# sprite_mover[0][1].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[1].position[1]][controller.player[controller.turn-1].horse[1].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										else:
											if 'group' in ret:
												for group in controller.player[0].group:
													if controller.player[0].horse[1].horse_id in group:
														for h in group:
															sprite_mover[0][h-1].update(POS_SPRITE_HORSE[controller.player[0].horse[h-1].position[1]][controller.player[0].horse[h-1].position[0]])
											else:
												sprite_mover[0][1].update(POS_SPRITE_HORSE[controller.player[0].horse[1].position[1]][controller.player[0].horse[1].position[0]])
											push = True

										on_selector = False
			
							elif 133 <= mouse_x and mouse_x <= 181 and 167 <= mouse_y and mouse_y <= 213 and controller.num_of_horse >= 3:
								if not controller.player[controller.turn-1].horse[2].goal:
									ret = controller.game.move(controller, controller.player[0], controller.player[0].horse[2])
									
									if 'fail' in ret:
										push = True
										on_selector = False
									else:
										if 'goal' in ret:
											if 'group' in ret:
												if controller.player[0].horse[2].goal:
													pass
												else:
													for group in controller.player[0].group:
														if controller.player[0].horse[2].horse_id in group:
															for h in group:
																sprite_horse[0][h-1].switch('goal')
																sprite_mover[0][h-1].ret_wait()
																controller.player[0].goal += 1
																controller.player[0].horse[h-1].goal = True
															sound_goal[random.randint(0,4)].play()
											else:
												if controller.player[0].horse[2].goal:
													pass
												else:
													sprite_horse[0][2].switch('goal')
													sprite_mover[0][2].ret_wait()
													controller.player[0].goal += 1
													controller.player[0].horse[2].goal = True
													sound_goal[random.randint(0,4)].play()
											push = True
										elif 'catch' in ret:
											# 말을 잡았으니 위치 갱신
											sprite_mover[ret[0]-1][ret[1]-1].update((-100,-100))
											sprite_mover[0][2].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[2].position[1]][controller.player[controller.turn-1].horse[2].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										elif 'groupcatch' in ret:
											# 말을 잡았으니 위치 갱신
											for h_index in ret[3]:
												sprite_mover[ret[0]-1][h_index-1].update((-100,-100))
											sprite_mover[0][2].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[2].position[1]][controller.player[controller.turn-1].horse[2].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										else:
											if 'group' in ret:
												for group in controller.player[0].group:
													if controller.player[0].horse[2].horse_id in group:
														for h in group:
															sprite_mover[0][h-1].update(POS_SPRITE_HORSE[controller.player[0].horse[h-1].position[1]][controller.player[0].horse[h-1].position[0]])
											else:
												sprite_mover[0][2].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[2].position[1]][controller.player[controller.turn-1].horse[2].position[0]])
											push = True

										on_selector = False

							elif 15 <= mouse_x and mouse_x <= 64 and 226 <= mouse_y and mouse_y <= 270 and controller.num_of_horse >= 4:
								if not controller.player[controller.turn-1].horse[3].goal:
									ret = controller.game.move(controller, controller.player[0], controller.player[0].horse[3])
									
									if 'fail' in ret:
										push = True
										on_selector = False
									else:
										if 'goal' in ret:
											if 'group' in ret:
												if controller.player[0].horse[3].goal:
													pass
												else:
													for group in controller.player[0].group:
														if controller.player[0].horse[3].horse_id in group:
															for h in group:
																sprite_horse[0][h-1].switch('goal')
																sprite_mover[0][h-1].ret_wait()
																controller.player[0].goal += 1
																controller.player[0].horse[h-1].goal = True
															sound_goal[random.randint(0,4)].play()
											else:
												if controller.player[0].horse[3].goal:
													pass
												else:
													sprite_horse[0][3].switch('goal')
													sprite_mover[0][3].ret_wait()
													controller.player[0].goal += 1
													controller.player[0].horse[3].goal = True
													sound_goal[random.randint(0,4)].play()
											push = True
										elif 'catch' in ret:
											# 말을 잡았으니 위치 갱신
											sprite_mover[ret[0]-1][ret[1]-1].update((-100,-100))
											sprite_mover[0][3].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[3].position[1]][controller.player[controller.turn-1].horse[3].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										elif 'groupcatch' in ret:
											# 말을 잡았으니 위치 갱신
											for h_index in ret[3]:
												sprite_mover[ret[0]-1][h_index-1].update((-100,-100))
											sprite_mover[0][3].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[3].position[1]][controller.player[controller.turn-1].horse[3].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										else:
											if 'group' in ret:
												for group in controller.player[0].group:
													if controller.player[0].horse[3].horse_id in group:
														for h in group:
															sprite_mover[0][h-1].update(POS_SPRITE_HORSE[controller.player[0].horse[h-1].position[1]][controller.player[0].horse[h-1].position[0]])
											else:
												sprite_mover[0][3].update(POS_SPRITE_HORSE[controller.player[0].horse[3].position[1]][controller.player[0].horse[3].position[0]])
											push = True

										on_selector = False

							elif 75 <= mouse_x and mouse_x <= 124 and 226 <= mouse_y and mouse_y <= 270 and controller.num_of_horse >= 5:
								if not controller.player[controller.turn-1].horse[4].goal:
									ret = controller.game.move(controller, controller.player[0], controller.player[0].horse[4])
									
									if 'fail' in ret:
										push = True
										on_selector = False
									else:
										if 'goal' in ret:
											if 'group' in ret:
												if controller.player[0].horse[4].goal:
													pass
												else:
													for group in controller.player[0].group:
														if controller.player[0].horse[4].horse_id in group:
															for h in group:
																sprite_horse[0][h-1].switch('goal')
																sprite_mover[0][h-1].ret_wait()
																controller.player[0].goal += 1
																controller.player[0].horse[h-1].goal = True
															sound_goal[random.randint(0,4)].play()
											else:
												if controller.player[0].horse[4].goal:
													pass
												else:
													sprite_horse[0][4].switch('goal')
													sprite_mover[0][4].ret_wait()
													controller.player[0].goal += 1
													controller.player[0].horse[4].goal = True
													sound_goal[random.randint(0,4)].play()
											push = True
										elif 'catch' in ret:
											# 말을 잡았으니 위치 갱신
											sprite_mover[ret[0]-1][ret[1]-1].update((-100,-100))
											sprite_mover[0][4].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[4].position[1]][controller.player[controller.turn-1].horse[4].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										elif 'groupcatch' in ret:
											# 말을 잡았으니 위치 갱신
											for h_index in ret[3]:
												sprite_mover[ret[0]-1][h_index-1].update((-100,-100))
											sprite_mover[0][4].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[4].position[1]][controller.player[controller.turn-1].horse[4].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										else:
											if 'group' in ret:
												for group in controller.player[0].group:
													if controller.player[0].horse[4].horse_id in group:
														for h in group:
															sprite_mover[0][h-1].update(POS_SPRITE_HORSE[controller.player[0].horse[h-1].position[1]][controller.player[0].horse[h-1].position[0]])
											else:
												sprite_mover[0][4].update(POS_SPRITE_HORSE[controller.player[0].horse[4].position[1]][controller.player[0].horse[4].position[0]])
											push = True

										on_selector = False

							if push and not controller.player[0].throwable:
								controller.next_turn()

						######
						# 2P
						######
						if controller.turn == 2 and on_selector:
							push = False

							if 713 <= mouse_x and mouse_x <= 761 and 167 <= mouse_y and mouse_y <= 213 and controller.num_of_horse >= 1:
								if not controller.player[controller.turn-1].horse[0].goal:
									ret = controller.game.move(controller, controller.player[1], controller.player[1].horse[0])

									if 'fail' in ret:
										push = True
										on_selector = False
									else:
										if 'goal' in ret:
											if 'group' in ret:
												if controller.player[1].horse[0].goal:
													pass
												else:
													for group in controller.player[1].group:
														if controller.player[1].horse[0].horse_id in group:
															for h in group:
																sprite_horse[1][h-1].switch('goal')
																sprite_mover[1][h-1].ret_wait()
																controller.player[1].goal += 1
																controller.player[1].horse[h-1].goal = True
															sound_goal[random.randint(0,4)].play()
											else:
												if controller.player[1].horse[0].goal:
													pass
												else:
													sprite_horse[1][0].switch('goal')
													sprite_mover[1][0].ret_wait()
													controller.player[1].goal += 1
													controller.player[1].horse[0].goal = True
													sound_goal[random.randint(0,4)].play()
											push = True
										elif 'catch' in ret:
											# 말을 잡았으니 위치 갱신
											sprite_mover[ret[0]-1][ret[1]-1].update((-100,-100))
											sprite_mover[1][0].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[0].position[1]][controller.player[controller.turn-1].horse[0].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										elif 'groupcatch' in ret:
											# 말을 잡았으니 위치 갱신
											for h_index in ret[3]:
												sprite_mover[ret[0]-1][h_index-1].update((-100,-100))
											sprite_mover[1][0].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[0].position[1]][controller.player[controller.turn-1].horse[0].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										else:
											if 'group' in ret:
												for group in controller.player[1].group:
													if controller.player[1].horse[0].horse_id in group:
														for h in group:
															sprite_mover[1][h-1].update(POS_SPRITE_HORSE[controller.player[1].horse[h-1].position[1]][controller.player[1].horse[h-1].position[0]])
											else:
												sprite_mover[1][0].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[0].position[1]][controller.player[controller.turn-1].horse[0].position[0]])
											push = True

										on_selector = False
									
							elif 774 <= mouse_x and mouse_x <= 821 and 167 <= mouse_y and mouse_y <= 213 and controller.num_of_horse >= 2:
								if not controller.player[controller.turn-1].horse[1].goal:
									ret = controller.game.move(controller, controller.player[1], controller.player[1].horse[1])
									if 'fail' in ret:
										push = True
										on_selector = False
									else:
										if 'goal' in ret:
											if 'group' in ret:
												if controller.player[1].horse[1].goal:
													pass
												else:
													for group in controller.player[1].group:
														if controller.player[1].horse[1].horse_id in group:
															for h in group:
																sprite_horse[1][h-1].switch('goal')
																sprite_mover[1][h-1].ret_wait()
																controller.player[1].goal += 1
																controller.player[1].horse[h-1].goal = True
															sound_goal[random.randint(0,4)].play()
											else:
												if controller.player[1].horse[1].goal:
													pass
												else:
													sprite_horse[1][1].switch('goal')
													sprite_mover[1][1].ret_wait()
													controller.player[1].goal += 1
													controller.player[1].horse[1].goal = True
													sound_goal[random.randint(0,4)].play()
											push = True
										elif 'catch' in ret:
											# 말을 잡았으니 위치 갱신
											sprite_mover[ret[0]-1][ret[1]-1].update((-100,-100))
											sprite_mover[1][1].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[1].position[1]][controller.player[controller.turn-1].horse[1].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										elif 'groupcatch' in ret:
											# 말을 잡았으니 위치 갱신
											for h_index in ret[3]:
												sprite_mover[ret[0]-1][h_index-1].update((-100,-100))
											sprite_mover[1][1].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[1].position[1]][controller.player[controller.turn-1].horse[1].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										else:
											if 'group' in ret:
												for group in controller.player[1].group:
													if controller.player[1].horse[1].horse_id in group:
														for h in group:
															sprite_mover[1][h-1].update(POS_SPRITE_HORSE[controller.player[1].horse[h-1].position[1]][controller.player[1].horse[h-1].position[0]])
											else:
												sprite_mover[1][1].update(POS_SPRITE_HORSE[controller.player[1].horse[1].position[1]][controller.player[1].horse[1].position[0]])
											push = True


										on_selector = False
									
							elif 832 <= mouse_x and mouse_x <= 879 and 167 <= mouse_y and mouse_y <= 213 and controller.num_of_horse >= 3:
								if not controller.player[controller.turn-1].horse[2].goal:
									ret = controller.game.move(controller, controller.player[1], controller.player[1].horse[2])
									if 'fail' in ret:
										push = True
										on_selector = False
									else:
										if 'goal' in ret:
											if 'group' in ret:
												if controller.player[1].horse[2].goal:
													pass
												else:
													for group in controller.player[1].group:
														if controller.player[1].horse[2].horse_id in group:
															for h in group:
																sprite_horse[1][h-1].switch('goal')
																sprite_mover[1][h-1].ret_wait()
																controller.player[1].goal += 1
																controller.player[1].horse[h-1].goal = True
															sound_goal[random.randint(0,4)].play()
											else:
												if controller.player[1].horse[2].goal:
													pass
												else:
													sprite_horse[1][2].switch('goal')
													sprite_mover[1][2].ret_wait()
													controller.player[1].goal += 1
													controller.player[1].horse[2].goal = True
													sound_goal[random.randint(0,4)].play()
											push = True
										elif 'catch' in ret:
											# 말을 잡았으니 위치 갱신
											sprite_mover[ret[0]-1][ret[1]-1].update((-100,-100))
											sprite_mover[1][2].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[2].position[1]][controller.player[controller.turn-1].horse[2].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										elif 'groupcatch' in ret:
											# 말을 잡았으니 위치 갱신
											for h_index in ret[3]:
												sprite_mover[ret[0]-1][h_index-1].update((-100,-100))
											sprite_mover[1][2].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[2].position[1]][controller.player[controller.turn-1].horse[2].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										else:
											if 'group' in ret:
												for group in controller.player[1].group:
													if controller.player[1].horse[2].horse_id in group:
														for h in group:
															sprite_mover[1][h-1].update(POS_SPRITE_HORSE[controller.player[1].horse[h-1].position[1]][controller.player[1].horse[h-1].position[0]])
											else:
												sprite_mover[1][2].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[2].position[1]][controller.player[controller.turn-1].horse[2].position[0]])
											push = True

										on_selector = False

							elif 711 <= mouse_x and mouse_x <= 762 and 226 <= mouse_y and mouse_y <= 270 and controller.num_of_horse >= 4:
								if not controller.player[controller.turn-1].horse[3].goal:
									ret = controller.game.move(controller, controller.player[1], controller.player[1].horse[3])
									if 'fail' in ret:
										push = True
										on_selector = False
									else:
										if 'goal' in ret:
											if 'group' in ret:
												if controller.player[1].horse[3].goal:
													pass
												else:
													for group in controller.player[1].group:
														if controller.player[1].horse[3].horse_id in group:
															for h in group:
																sprite_horse[1][h-1].switch('goal')
																sprite_mover[1][h-1].ret_wait()
																controller.player[1].goal += 1
																controller.player[1].horse[h-1].goal = True
															sound_goal[random.randint(0,4)].play()
											else:
												if controller.player[1].horse[3].goal:
													pass
												else:
													sprite_horse[1][3].switch('goal')
													sprite_mover[1][3].ret_wait()
													controller.player[1].goal += 1
													controller.player[1].horse[3].goal = True
													sound_goal[random.randint(0,4)].play()
											push = True
										elif 'catch' in ret:
											# 말을 잡았으니 위치 갱신
											sprite_mover[ret[0]-1][ret[1]-1].update((-100,-100))
											sprite_mover[1][3].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[3].position[1]][controller.player[controller.turn-1].horse[3].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										elif 'groupcatch' in ret:
											# 말을 잡았으니 위치 갱신
											for h_index in ret[3]:
												sprite_mover[ret[0]-1][h_index-1].update((-100,-100))
											sprite_mover[1][3].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[3].position[1]][controller.player[controller.turn-1].horse[3].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										else:
											if 'group' in ret:
												for group in controller.player[1].group:
													if controller.player[1].horse[3].horse_id in group:
														for h in group:
															sprite_mover[1][h-1].update(POS_SPRITE_HORSE[controller.player[1].horse[h-1].position[1]][controller.player[1].horse[h-1].position[0]])
											else:
												sprite_mover[1][3].update(POS_SPRITE_HORSE[controller.player[1].horse[3].position[1]][controller.player[1].horse[3].position[0]])
											push = True

										on_selector = False

							elif 773 <= mouse_x and mouse_x <= 821 and 226 <= mouse_y and mouse_y <= 270 and controller.num_of_horse >= 5:
								if not controller.player[controller.turn-1].horse[4].goal:
									ret = controller.game.move(controller, controller.player[1], controller.player[1].horse[4])
									if 'fail' in ret:
										push = True
										on_selector = False
									else:
										if 'goal' in ret:
											if 'group' in ret:
												if controller.player[1].horse[4].goal:
													pass
												else:
													for group in controller.player[1].group:
														if controller.player[1].horse[4].horse_id in group:
															for h in group:
																sprite_horse[1][h-1].switch('goal')
																sprite_mover[1][h-1].ret_wait()
																controller.player[1].goal += 1
																controller.player[1].horse[h-1].goal = True
															sound_goal[random.randint(0,4)].play()
											else:
												if controller.player[1].horse[4].goal:
													pass
												else:
													sprite_horse[1][4].switch('goal')
													sprite_mover[1][4].ret_wait()
													controller.player[1].goal += 1
													controller.player[1].horse[4].goal = True
													sound_goal[random.randint(0,4)].play()
											push = True
										elif 'catch' in ret:
											# 말을 잡았으니 위치 갱신
											sprite_mover[ret[0]-1][ret[1]-1].update((-100,-100))
											sprite_mover[1][4].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[4].position[1]][controller.player[controller.turn-1].horse[4].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										elif 'groupcatch' in ret:
											# 말을 잡았으니 위치 갱신
											for h_index in ret[3]:
												sprite_mover[ret[0]-1][h_index-1].update((-100,-100))
											sprite_mover[1][4].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[4].position[1]][controller.player[controller.turn-1].horse[4].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										else:
											if 'group' in ret:
												for group in controller.player[1].group:
													if controller.player[1].horse[4].horse_id in group:
														for h in group:
															sprite_mover[1][h-1].update(POS_SPRITE_HORSE[controller.player[1].horse[h-1].position[1]][controller.player[1].horse[h-1].position[0]])
											else:
												sprite_mover[1][4].update(POS_SPRITE_HORSE[controller.player[1].horse[4].position[1]][controller.player[1].horse[4].position[0]])
											push = True

										on_selector = False

							if push and not controller.player[1].throwable:
								controller.next_turn()
					
						######
						# 3P
						######
						if controller.turn == 3 and on_selector:
							push = False

							if 15 <= mouse_x and mouse_x <= 63 and 444 <= mouse_y and mouse_y <= 491 and controller.num_of_horse >= 1:
								if not controller.player[controller.turn-1].horse[0].goal:
									ret = controller.game.move(controller, controller.player[2], controller.player[2].horse[0])
									if 'fail' in ret:
										push = True
										on_selector = False
									else:
										if 'goal' in ret:
											if 'group' in ret:
												if controller.player[2].horse[0].goal:
													pass
												else:
													for group in controller.player[2].group:
														if controller.player[2].horse[0].horse_id in group:
															for h in group:
																sprite_horse[3][h-1].switch('goal')
																sprite_mover[2][h-1].ret_wait()
																controller.player[2].goal += 1
																controller.player[2].horse[h-1].goal = True
															sound_goal[random.randint(0,4)].play()
											else:
												if controller.player[2].horse[0].goal:
													pass
												else:
													sprite_horse[2][0].switch('goal')
													sprite_mover[2][0].ret_wait()
													controller.player[2].goal += 1
													controller.player[2].horse[0].goal = True
													sound_goal[random.randint(0,4)].play()
											push = True
										elif 'catch' in ret:
											# 말을 잡았으니 위치 갱신
											sprite_mover[ret[0]-1][ret[1]-1].update((-100,-100))
											sprite_mover[2][0].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[0].position[1]][controller.player[controller.turn-1].horse[0].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										elif 'groupcatch' in ret:
											# 말을 잡았으니 위치 갱신
											for h_index in ret[3]:
												sprite_mover[ret[0]-1][h_index-1].update((-100,-100))
											sprite_mover[2][0].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[0].position[1]][controller.player[controller.turn-1].horse[0].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										else:
											if 'group' in ret:
												for group in controller.player[2].group:
													if controller.player[2].horse[0].horse_id in group:
														for h in group:
															sprite_mover[2][h-1].update(POS_SPRITE_HORSE[controller.player[2].horse[h-1].position[1]][controller.player[2].horse[h-1].position[0]])
											else:
												sprite_mover[2][0].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[0].position[1]][controller.player[controller.turn-1].horse[0].position[0]])
											push = True

										on_selector = False
									
							elif 73 <= mouse_x and mouse_x <= 122 and 444 <= mouse_y and mouse_y <= 491 and controller.num_of_horse >= 2:
								if not controller.player[controller.turn-1].horse[1].goal:
									ret = controller.game.move(controller, controller.player[2], controller.player[2].horse[1])
									if 'fail' in ret:
										push = True
										on_selector = False
									else:
										if 'goal' in ret:
											if 'group' in ret:
												if controller.player[2].horse[1].goal:
													pass
												else:
													for group in controller.player[2].group:
														if controller.player[2].horse[1].horse_id in group:
															for h in group:
																sprite_horse[2][h-1].switch('goal')
																sprite_mover[2][h-1].ret_wait()
																controller.player[2].goal += 1
																controller.player[2].horse[h-1].goal = True
															sound_goal[random.randint(0,4)].play()
											else:
												if controller.player[2].horse[1].goal:
													pass
												else:
													sprite_horse[2][1].switch('goal')
													sprite_mover[2][1].ret_wait()
													controller.player[2].goal += 1
													controller.player[2].horse[1].goal = True
													sound_goal[random.randint(0,4)].play()
											push = True
										elif 'catch' in ret:
											# 말을 잡았으니 위치 갱신
											sprite_mover[ret[0]-1][ret[1]-1].update((-100,-100))
											sprite_mover[2][1].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[1].position[1]][controller.player[controller.turn-1].horse[1].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										elif 'groupcatch' in ret:
											# 말을 잡았으니 위치 갱신
											for h_index in ret[3]:
												sprite_mover[ret[0]-1][h_index-1].update((-100,-100))
											sprite_mover[2][1].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[1].position[1]][controller.player[controller.turn-1].horse[1].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										else:
											if 'group' in ret:
												for group in controller.player[2].group:
													if controller.player[2].horse[1].horse_id in group:
														for h in group:
															sprite_mover[2][h-1].update(POS_SPRITE_HORSE[controller.player[2].horse[h-1].position[1]][controller.player[2].horse[h-1].position[0]])
											else:
												sprite_mover[2][1].update(POS_SPRITE_HORSE[controller.player[2].horse[1].position[1]][controller.player[2].horse[1].position[0]])
											push = True


										on_selector = False
									
							elif 133 <= mouse_x and mouse_x <= 445 and 444 <= mouse_y and mouse_y <= 491 and controller.num_of_horse >= 3:
								if not controller.player[controller.turn-1].horse[2].goal:
									ret = controller.game.move(controller, controller.player[2], controller.player[2].horse[2])
									if 'fail' in ret:
										push = True
										on_selector = False
									else:
										if 'goal' in ret:
											if 'group' in ret:
												if controller.player[2].horse[2].goal:
													pass
												else:
													for group in controller.player[2].group:
														if controller.player[2].horse[2].horse_id in group:
															for h in group:
																sprite_horse[2][h-1].switch('goal')
																sprite_mover[2][h-1].ret_wait()
																controller.player[2].goal += 1
																controller.player[2].horse[h-1].goal = True
															sound_goal[random.randint(0,4)].play()
											else:
												if controller.player[2].horse[2].goal:
													pass
												else:
													sprite_horse[2][2].switch('goal')
													sprite_mover[2][2].ret_wait()
													controller.player[2].goal += 1
													controller.player[2].horse[2].goal = True
													sound_goal[random.randint(0,4)].play()
											push = True
										elif 'catch' in ret:
											# 말을 잡았으니 위치 갱신
											sprite_mover[ret[0]-1][ret[1]-1].update((-100,-100))
											sprite_mover[2][2].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[2].position[1]][controller.player[controller.turn-1].horse[2].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										elif 'groupcatch' in ret:
											# 말을 잡았으니 위치 갱신
											for h_index in ret[3]:
												sprite_mover[ret[0]-1][h_index-1].update((-100,-100))
											sprite_mover[2][2].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[2].position[1]][controller.player[controller.turn-1].horse[2].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										else:
											if 'group' in ret:
												for group in controller.player[2].group:
													if controller.player[2].horse[2].horse_id in group:
														for h in group:
															sprite_mover[2][h-1].update(POS_SPRITE_HORSE[controller.player[2].horse[h-1].position[1]][controller.player[2].horse[h-1].position[0]])
											else:
												sprite_mover[2][2].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[2].position[1]][controller.player[controller.turn-1].horse[2].position[0]])
											push = True

										on_selector = False

							elif 14 <= mouse_x and mouse_x <= 63 and 504 <= mouse_y and mouse_y <= 550 and controller.num_of_horse >= 4:
								if not controller.player[controller.turn-1].horse[3].goal:
									ret = controller.game.move(controller, controller.player[2], controller.player[2].horse[3])
									if 'fail' in ret:
										push = True
										on_selector = False
									else:
										if 'goal' in ret:
											if 'group' in ret:
												if controller.player[2].horse[3].goal:
													pass
												else:
													for group in controller.player[2].group:
														if controller.player[2].horse[3].horse_id in group:
															for h in group:
																sprite_horse[2][h-1].switch('goal')
																sprite_mover[2][h-1].ret_wait()
																controller.player[2].goal += 1
																controller.player[2].horse[h-1].goal = True
															sound_goal[random.randint(0,4)].play()
											else:
												if controller.player[2].horse[3].goal:
													pass
												else:
													sprite_horse[2][3].switch('goal')
													sprite_mover[2][3].ret_wait()
													controller.player[2].goal += 1
													controller.player[2].horse[3].goal = True
													sound_goal[random.randint(0,4)].play()
											push = True
										elif 'catch' in ret:
											# 말을 잡았으니 위치 갱신
											sprite_mover[ret[0]-1][ret[1]-1].update((-100,-100))
											sprite_mover[2][3].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[3].position[1]][controller.player[controller.turn-1].horse[3].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										elif 'groupcatch' in ret:
											# 말을 잡았으니 위치 갱신
											for h_index in ret[3]:
												sprite_mover[ret[0]-1][h_index-1].update((-100,-100))
											sprite_mover[2][3].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[3].position[1]][controller.player[controller.turn-1].horse[3].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										else:
											if 'group' in ret:
												for group in controller.player[2].group:
													if controller.player[2].horse[3].horse_id in group:
														for h in group:
															sprite_mover[2][h-1].update(POS_SPRITE_HORSE[controller.player[2].horse[h-1].position[1]][controller.player[2].horse[h-1].position[0]])
											else:
												sprite_mover[2][3].update(POS_SPRITE_HORSE[controller.player[2].horse[3].position[1]][controller.player[2].horse[3].position[0]])
											push = True

										on_selector = False

							elif 74 <= mouse_x and mouse_x <= 122 and 504 <= mouse_y and mouse_y <= 551 and controller.num_of_horse >= 5:
								if not controller.player[controller.turn-1].horse[4].goal:
									ret = controller.game.move(controller, controller.player[2], controller.player[2].horse[4])
									if 'fail' in ret:
										push = True
										on_selector = False
									else:
										if 'goal' in ret:
											if 'group' in ret:
												if controller.player[2].horse[4].goal:
													pass
												else:
													for group in controller.player[2].group:
														if controller.player[2].horse[4].horse_id in group:
															for h in group:
																sprite_horse[2][h-1].switch('goal')
																sprite_mover[2][h-1].ret_wait()
																controller.player[2].goal += 1
																controller.player[2].horse[h-1].goal = True
															sound_goal[random.randint(0,4)].play()
											else:
												if controller.player[2].horse[4].goal:
													pass
												else:
													sprite_horse[2][4].switch('goal')
													sprite_mover[2][4].ret_wait()
													controller.player[2].goal += 1
													controller.player[2].horse[4].goal = True
													sound_goal[random.randint(0,4)].play()
											push = True
										elif 'catch' in ret:
											# 말을 잡았으니 위치 갱신
											sprite_mover[ret[0]-1][ret[1]-1].update((-100,-100))
											sprite_mover[2][4].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[4].position[1]][controller.player[controller.turn-1].horse[4].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										elif 'groupcatch' in ret:
											# 말을 잡았으니 위치 갱신
											for h_index in ret[3]:
												sprite_mover[ret[0]-1][h_index-1].update((-100,-100))
											sprite_mover[2][4].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[4].position[1]][controller.player[controller.turn-1].horse[4].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										else:
											if 'group' in ret:
												for group in controller.player[2].group:
													if controller.player[2].horse[4].horse_id in group:
														for h in group:
															sprite_mover[2][h-1].update(POS_SPRITE_HORSE[controller.player[2].horse[h-1].position[1]][controller.player[2].horse[h-1].position[0]])
											else:
												sprite_mover[2][4].update(POS_SPRITE_HORSE[controller.player[2].horse[4].position[1]][controller.player[2].horse[4].position[0]])
											push = True

										on_selector = False

							if push and not controller.player[2].throwable:
								controller.next_turn()

						######
						# 4P
						######
						if controller.turn == 4 and on_selector:
							push = False

							if 714 <= mouse_x and mouse_x <= 762 and 444 <= mouse_y and mouse_y <= 491 and controller.num_of_horse >= 1:
								if not controller.player[controller.turn-1].horse[0].goal:
									ret = controller.game.move(controller, controller.player[3], controller.player[3].horse[0])
									if 'fail' in ret:
										push = True
										on_selector = False
									else:
										if 'goal' in ret:
											if 'group' in ret:
												if controller.player[3].horse[0].goal:
													pass
												else:
													for group in controller.player[3].group:
														if controller.player[3].horse[0].horse_id in group:
															for h in group:
																sprite_horse[2][h-1].switch('goal')
																sprite_mover[3][h-1].ret_wait()
																controller.player[3].goal += 1
																controller.player[3].horse[h-1].goal = True
															sound_goal[random.randint(0,4)].play()
											else:
												if controller.player[3].horse[0].goal:
													pass
												else:
													sprite_horse[3][0].switch('goal')
													sprite_mover[3][0].ret_wait()
													controller.player[3].goal += 1
													controller.player[3].horse[0].goal = True
													sound_goal[random.randint(0,4)].play()
											push = True
										elif 'catch' in ret:
											# 말을 잡았으니 위치 갱신
											sprite_mover[ret[0]-1][ret[1]-1].update((-100,-100))
											sprite_mover[3][0].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[0].position[1]][controller.player[controller.turn-1].horse[0].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										elif 'groupcatch' in ret:
											# 말을 잡았으니 위치 갱신
											for h_index in ret[3]:
												sprite_mover[ret[0]-1][h_index-1].update((-100,-100))
											sprite_mover[3][0].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[0].position[1]][controller.player[controller.turn-1].horse[0].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										else:
											if 'group' in ret:
												for group in controller.player[3].group:
													if controller.player[3].horse[0].horse_id in group:
														for h in group:
															sprite_mover[3][h-1].update(POS_SPRITE_HORSE[controller.player[3].horse[h-1].position[1]][controller.player[3].horse[h-1].position[0]])
											else:
												sprite_mover[3][0].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[0].position[1]][controller.player[controller.turn-1].horse[0].position[0]])
											push = True

										on_selector = False
									
							elif 773 <= mouse_x and mouse_x <= 820 and 444 <= mouse_y and mouse_y <= 491 and controller.num_of_horse >= 2:
								if not controller.player[controller.turn-1].horse[1].goal:
									ret = controller.game.move(controller, controller.player[3], controller.player[3].horse[1])
									if 'fail' in ret:
										push = True
										on_selector = False
									else:
										if 'goal' in ret:
											if 'group' in ret:
												if controller.player[3].horse[1].goal:
													pass
												else:
													for group in controller.player[3].group:
														if controller.player[3].horse[1].horse_id in group:
															for h in group:
																sprite_horse[3][h-1].switch('goal')
																sprite_mover[3][h-1].ret_wait()
																controller.player[3].goal += 1
																controller.player[3].horse[h-1].goal = True
															sound_goal[random.randint(0,4)].play()
											else:
												if controller.player[3].horse[1].goal:
													pass
												else:
													sprite_horse[3][1].switch('goal')
													sprite_mover[3][1].ret_wait()
													controller.player[3].goal += 1
													controller.player[3].horse[1].goal = True
													sound_goal[random.randint(0,4)].play()
											push = True
										elif 'catch' in ret:
											# 말을 잡았으니 위치 갱신
											sprite_mover[ret[0]-1][ret[1]-1].update((-100,-100))
											sprite_mover[3][1].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[1].position[1]][controller.player[controller.turn-1].horse[1].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										elif 'groupcatch' in ret:
											# 말을 잡았으니 위치 갱신
											for h_index in ret[3]:
												sprite_mover[ret[0]-1][h_index-1].update((-100,-100))
											sprite_mover[3][1].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[1].position[1]][controller.player[controller.turn-1].horse[1].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										else:
											if 'group' in ret:
												for group in controller.player[3].group:
													if controller.player[3].horse[1].horse_id in group:
														for h in group:
															sprite_mover[3][h-1].update(POS_SPRITE_HORSE[controller.player[3].horse[h-1].position[1]][controller.player[3].horse[h-1].position[0]])
											else:
												sprite_mover[3][1].update(POS_SPRITE_HORSE[controller.player[3].horse[1].position[1]][controller.player[3].horse[1].position[0]])
											push = True


										on_selector = False
									
							elif 832 <= mouse_x and mouse_x <= 879 and 444 <= mouse_y and mouse_y <= 491 and controller.num_of_horse >= 3:
								if not controller.player[controller.turn-1].horse[2].goal:
									ret = controller.game.move(controller, controller.player[3], controller.player[3].horse[2])
									if 'fail' in ret:
										push = True
										on_selector = False
									else:
										if 'goal' in ret:
											if 'group' in ret:
												if controller.player[3].horse[2].goal:
													pass
												else:
													for group in controller.player[3].group:
														if controller.player[3].horse[2].horse_id in group:
															for h in group:
																sprite_horse[3][h-1].switch('goal')
																sprite_mover[3][h-1].ret_wait()
																controller.player[3].goal += 1
																controller.player[3].horse[h-1].goal = True
															sound_goal[random.randint(0,4)].play()
											else:
												if controller.player[3].horse[2].goal:
													pass
												else:
													sprite_horse[3][2].switch('goal')
													sprite_mover[3][2].ret_wait()
													controller.player[3].goal += 1
													controller.player[3].horse[2].goal = True
													sound_goal[random.randint(0,4)].play()
											push = True
										elif 'catch' in ret:
											# 말을 잡았으니 위치 갱신
											sprite_mover[ret[0]-1][ret[1]-1].update((-100,-100))
											sprite_mover[3][2].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[2].position[1]][controller.player[controller.turn-1].horse[2].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										elif 'groupcatch' in ret:
											# 말을 잡았으니 위치 갱신
											for h_index in ret[3]:
												sprite_mover[ret[0]-1][h_index-1].update((-100,-100))
											sprite_mover[3][2].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[2].position[1]][controller.player[controller.turn-1].horse[2].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										else:
											if 'group' in ret:
												for group in controller.player[3].group:
													if controller.player[3].horse[2].horse_id in group:
														for h in group:
															sprite_mover[3][h-1].update(POS_SPRITE_HORSE[controller.player[3].horse[h-1].position[1]][controller.player[3].horse[h-1].position[0]])
											else:
												sprite_mover[3][2].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[2].position[1]][controller.player[controller.turn-1].horse[2].position[0]])
											push = True

										on_selector = False

							elif 714 <= mouse_x and mouse_x <= 762 and 504 <= mouse_y and mouse_y <= 550 and controller.num_of_horse >= 4:
								if not controller.player[controller.turn-1].horse[3].goal:
									ret = controller.game.move(controller, controller.player[3], controller.player[3].horse[3])
									if 'fail' in ret:
										push = True
										on_selector = False
									else:
										if 'goal' in ret:
											if 'group' in ret:
												if controller.player[3].horse[3].goal:
													pass
												else:
													for group in controller.player[3].group:
														if controller.player[3].horse[3].horse_id in group:
															for h in group:
																sprite_horse[3][h-1].switch('goal')
																sprite_mover[3][h-1].ret_wait()
																controller.player[3].goal += 1
																controller.player[3].horse[h-1].goal = True
															sound_goal[random.randint(0,4)].play()
											else:
												if controller.player[3].horse[3].goal:
													pass
												else:
													sprite_horse[3][3].switch('goal')
													sprite_mover[3][3].ret_wait()
													controller.player[3].goal += 1
													controller.player[3].horse[3].goal = True
													sound_goal[random.randint(0,4)].play()
											push = True
										elif 'catch' in ret:
											# 말을 잡았으니 위치 갱신
											sprite_mover[ret[0]-1][ret[1]-1].update((-100,-100))
											sprite_mover[3][3].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[3].position[1]][controller.player[controller.turn-1].horse[3].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										elif 'groupcatch' in ret:
											# 말을 잡았으니 위치 갱신
											for h_index in ret[3]:
												sprite_mover[ret[0]-1][h_index-1].update((-100,-100))
											sprite_mover[3][3].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[3].position[1]][controller.player[controller.turn-1].horse[3].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										else:
											if 'group' in ret:
												for group in controller.player[3].group:
													if controller.player[3].horse[3].horse_id in group:
														for h in group:
															sprite_mover[3][h-1].update(POS_SPRITE_HORSE[controller.player[3].horse[h-1].position[1]][controller.player[3].horse[h-1].position[0]])
											else:
												sprite_mover[3][3].update(POS_SPRITE_HORSE[controller.player[3].horse[3].position[1]][controller.player[3].horse[3].position[0]])
											push = True

										on_selector = False

							elif 771 <= mouse_x and mouse_x <= 821 and 504 <= mouse_y and mouse_y <= 551 and controller.num_of_horse >= 5:
								if not controller.player[controller.turn-1].horse[4].goal:
									ret = controller.game.move(controller, controller.player[3], controller.player[3].horse[4])
									if 'fail' in ret:
										push = True
										on_selector = False
									else:
										if 'goal' in ret:
											if 'group' in ret:
												if controller.player[3].horse[4].goal:
													pass
												else:
													for group in controller.player[3].group:
														if controller.player[3].horse[4].horse_id in group:
															for h in group:
																sprite_horse[3][h-1].switch('goal')
																sprite_mover[3][h-1].ret_wait()
																controller.player[3].goal += 1
																controller.player[3].horse[h-1].goal = True
															sound_goal[random.randint(0,4)].play()
											else:
												if controller.player[3].horse[4].goal:
													pass
												else:
													sprite_horse[3][4].switch('goal')
													sprite_mover[3][4].ret_wait()
													controller.player[3].goal += 1
													controller.player[3].horse[4].goal = True
													sound_goal[random.randint(0,4)].play()
											push = True
										elif 'catch' in ret:
											# 말을 잡았으니 위치 갱신
											sprite_mover[ret[0]-1][ret[1]-1].update((-100,-100))
											sprite_mover[3][4].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[4].position[1]][controller.player[controller.turn-1].horse[4].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										elif 'groupcatch' in ret:
											# 말을 잡았으니 위치 갱신
											for h_index in ret[3]:
												sprite_mover[ret[0]-1][h_index-1].update((-100,-100))
											sprite_mover[3][4].update(POS_SPRITE_HORSE[controller.player[controller.turn-1].horse[4].position[1]][controller.player[controller.turn-1].horse[4].position[0]])
											sound_catch[random.randint(0,2)].play()
											push = False
										else:
											if 'group' in ret:
												for group in controller.player[3].group:
													if controller.player[3].horse[4].horse_id in group:
														for h in group:
															sprite_mover[3][h-1].update(POS_SPRITE_HORSE[controller.player[3].horse[h-1].position[1]][controller.player[3].horse[h-1].position[0]])
											else:
												sprite_mover[3][4].update(POS_SPRITE_HORSE[controller.player[3].horse[4].position[1]][controller.player[3].horse[4].position[0]])
											push = True

										on_selector = False

							if push and not controller.player[3].throwable:
								controller.next_turn()

						
			# 게임 오버 (한 명이라도 말을 전부 골인시켰을 경우)
			for player in range(0, controller.num_of_player):

				if controller.player[player].goal == (controller.num_of_horse) and not is_gameover:
					sprite_gameover.set_winner(player)
					pygame.mixer.music.stop()
					sound_win.play()
					sprite_gameover_g.draw(self.window)
					is_gameover = True

			# 윷 던지기 애니메이션
			if throw_push:
				sprite_yut_g.update(rand_yut)
				sprite_yut_g.clear(self.window, sprite_bg)
				sprite_yut_g.draw(self.window)
				
				yut_animate_cnt += 1
	
				if yut_animate_cnt == 15:
					sound_yut[rand_yut][random.randint(0, 3)].play()
	
					# 플레이어 윷 스택 추가
					controller.player[controller.turn-1].set_yut(rand_yut)
	
					time.sleep(0.6)
				else:
					time.sleep(0.05)
	
				if yut_animate_cnt == 21:
					throw_push = False
					flag_key = False
					yut_animate_cnt = 0
					sprite_yut_g.clear(self.window, sprite_bg)
	
					# 플레이어 윷 렌더링
					# 배경 이미지 다시 그림
					self.window.blit(sprite_bg, POS_ORIGIN)
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
	
					self.window.blit(sprite_yut_result[rand_yut], (219, 511))
	
					# 말을 옮기기 위해 셀렉터 설정
					on_selector = True

					# 윷 / 모의 경우 더 던질 수 있도록 처리
					if rand_yut != 4 and rand_yut != 5:
						controller.player[controller.turn-1].throwable = False
					else:
						controller.player[controller.turn-1].throwable = True

			# 말 업데이트
			for render in sprite_horse_render:
				render.clear(self.window, sprite_bg)
				render.draw(self.window)
			for render in sprite_mover_render:
				render.clear(self.window, sprite_bg)
				render.draw(self.window)

			# 이미지 업데이트
			sprite_throw_g.clear(self.window, sprite_bg)
			sprite_throw_g.draw(self.window)
			sprite_stack_g.clear(self.window, sprite_bg)
			sprite_stack_g.draw(self.window)

			# 화면 업데이트
			pygame.display.update()
			self.fps.tick(FPS)

	# Get Mouse Pos
	def get_mouse_pos(self, event):
		return event.pos
