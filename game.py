# coding=euc-kr

# Import
import pygame, sys, time
from scripts.mouse import *
from scripts.constants import *
from pygame.locals import *

# 화면 초기화
def initGame():
    global windows, fps_clock

    # 실질적인 화면 세팅
    pygame.init()
    windows = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32); 
    pygame.display.set_caption('소프트웨어공학 팀프로젝트 - 윷놀이')          
    pygame.display.set_icon(pygame.image.load('images/icons/icon.png'))      


    fps_clock = pygame.time.Clock()


    IntroScene()


# 인트로 화면 메소드
def IntroScene():
    # 인트로 페이지 설정 (BG Music, Image)
    pygame.mixer.music.load('sounds/IntroBGM.mp3')
    pygame.mixer.music.play(-1)

    clickSound = pygame.mixer.Sound('sounds/Click.wav')

    # 이미지 렌더링
    intro_bg = pygame.image.load('images/intro/IntroScene.png')
    start_btn = pygame.image.load('images/intro/IntroStartBtn.png')
    start_btn_clicked = pygame.image.load('images/intro/IntroStartBtn_Clicked.png')
    windows.blit(intro_bg, (0, 0))
    windows.blit(start_btn, (130, 260))
    
    # Flag 변수
    intro = True
    music = True
    mouse_clicked = False

    while intro:
        # 이벤트 설정
        # 종료와 게임시작 관련 이벤트만 지정
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                # BGM On, Off
                if event.key == ord('p'):
                    print('p');
                    if music:
                        pygame.mixer.music.stop()
                        music = False
                    else:
                        pygame.mixer.music.play(-1)
                        music = True
            if event.type == MOUSEMOTION:
                mouse_x, mouse_y = getMousePos(event)
                # 마우스가 시작 글자에 닿을 시 효과음 발생 및 글자 확대
                if 115 < mouse_x and mouse_x < 205 and 250 < mouse_y and mouse_y < 285:
                    if not mouse_clicked:
                        clickSound.play()
                        windows.blit(intro_bg, (0, 0))
                        windows.blit(start_btn_clicked, (128, 260))
                        mouse_clicked = True
                else:
                    windows.blit(intro_bg, (0, 0))
                    windows.blit(start_btn, (130, 260))
                    mouse_clicked = False

        
        # 화면 업데이트 주기 30 FPS
        pygame.display.update()
        fps_clock.tick(30)

# Scenes
def GameScene():
    global background, windows, fps_clock, bgm

    game = True
    pygame.mixer.music.play()

    windows.blit(background, (0,0))

    while game:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        
        pygame.display.update()
        fps_clock.tick(30)
    pass



initGame()