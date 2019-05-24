# coding=euc-kr

# Import
import pygame, sys, time
from scripts.mouse import *
from scripts.constants import *
from pygame.locals import *

# ȭ�� �ʱ�ȭ
def initGame():
    global windows, fps_clock

    # �������� ȭ�� ����
    pygame.init()
    windows = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32); 
    pygame.display.set_caption('����Ʈ������� ��������Ʈ - ������')          
    pygame.display.set_icon(pygame.image.load('images/icons/icon.png'))      


    fps_clock = pygame.time.Clock()


    IntroScene()


# ��Ʈ�� ȭ�� �޼ҵ�
def IntroScene():
    # ��Ʈ�� ������ ���� (BG Music, Image)
    pygame.mixer.music.load('sounds/IntroBGM.mp3')
    pygame.mixer.music.play(-1)

    clickSound = pygame.mixer.Sound('sounds/Click.wav')

    # �̹��� ������
    intro_bg = pygame.image.load('images/intro/IntroScene.png')
    start_btn = pygame.image.load('images/intro/IntroStartBtn.png')
    start_btn_clicked = pygame.image.load('images/intro/IntroStartBtn_Clicked.png')
    windows.blit(intro_bg, (0, 0))
    windows.blit(start_btn, (130, 260))
    
    # Flag ����
    intro = True
    music = True
    mouse_clicked = False

    while intro:
        # �̺�Ʈ ����
        # ����� ���ӽ��� ���� �̺�Ʈ�� ����
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
                # ���콺�� ���� ���ڿ� ���� �� ȿ���� �߻� �� ���� Ȯ��
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

        
        # ȭ�� ������Ʈ �ֱ� 30 FPS
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