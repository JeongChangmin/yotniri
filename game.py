# coding=euc-kr
# Import
import pygame, sys, time
from mouse import *
from constants import *
from pygame.locals import *

# ȭ�� �ʱ�ȭ
def initGame():
    global windows, fps_clock

    # �������� ȭ�� ����
    pygame.init()
    windows = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32); 
    pygame.display.set_caption('����Ʈ���� ���� ��������Ʈ - ������')          
    pygame.display.set_icon(pygame.image.load('images/icons/icon.png'))      
    # FPS Object
    fps_clock = pygame.time.Clock()

    # Scene ȣ��
    num_of_player, num_of_mal = IntroScene()
    GameScene(num_of_player, num_of_mal)

def IntroScene():
    # ��Ʈ�� ������ ���� (BG Music, Image)
    pygame.mixer.music.load('sounds/IntroBGM.mp3')
    pygame.mixer.music.play(-1)

    clickSound = pygame.mixer.Sound('sounds/Click.wav')

    # �̹��� ������
    intro_bg = pygame.image.load('images/intro/IntroScene.png')
    start_btn = pygame.image.load('images/intro/IntroStartBtn.png')
    start_btn_clicked = pygame.image.load('images/intro/IntroStartBtn_Clicked.png')
    set_dialog = pygame.image.load('images/intro/SettingDlg.png')
    set_cursor = pygame.image.load('images/intro/SetCursor.png')
    windows.blit(intro_bg, (0, 0))
    windows.blit(start_btn, (130, 260))
    
    # Flag ����
    intro = True
    music = True
    dlg = False
    mouse_clicked = False

    # Setting ����
    num_of_player = 2
    num_of_mal = 4

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
                if not dlg:
                    # ���콺�� ���� ���ڿ� ���� �� ���� Ȯ��
                    if 115 < mouse_x and mouse_x < 205 and 250 < mouse_y and mouse_y < 285:                      
                        windows.blit(intro_bg, (0, 0))
                        windows.blit(start_btn_clicked, (128, 260))
                    else:
                        windows.blit(intro_bg, (0, 0))
                        windows.blit(start_btn, (130, 260))
            if event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = getMousePos(event)
                # ���콺�� ���� ���ڿ� ���� �� ȿ���� �߻� �� ���� Ȯ��
                if 115 < mouse_x and mouse_x < 205 and 250 < mouse_y and mouse_y < 285 and not dlg:
                    clickSound.play()                    
                    windows.blit(set_dialog, (220, 100))
                    windows.blit(set_cursor, (430, 202))
                    windows.blit(set_cursor, (535, 263))
                
                    dlg = True
                    num_of_player = 2
                    num_of_mal = 4
                
                # ���� â�� �������� �� ���콺 ó��
                else:
                    # �÷��̾� üũ
                    if 418 < mouse_x and mouse_x < 458 and 208 < mouse_y and mouse_y < 248:
                        mouse_clicked = True
                        num_of_player = 2
                    elif 470 < mouse_x and mouse_x < 510 and 208 < mouse_y and mouse_y < 248:
                        mouse_clicked = True
                        num_of_player = 3
                    elif 520 < mouse_x and mouse_x < 560 and 208 < mouse_y and mouse_y < 248:
                        mouse_clicked = True
                        num_of_player = 4
                    # �� üũ
                    elif 418 < mouse_x and mouse_x < 458 and 269 < mouse_y and mouse_y < 308:
                        mouse_clicked = True
                        num_of_mal = 2
                    elif 470 < mouse_x and mouse_x < 510 and 269 < mouse_y and mouse_y < 308:
                        mouse_clicked = True
                        num_of_mal = 3
                    elif 520 < mouse_x and mouse_x < 560 and 269 < mouse_y and mouse_y < 308:
                        mouse_clicked = True
                        num_of_mal = 4
                    elif 572 < mouse_x and mouse_x < 612 and 269 < mouse_y and mouse_y < 308:
                        mouse_clicked = True
                        num_of_mal = 5
                    # X ��ư
                    elif 628 < mouse_x and mouse_x < 645 and 124 < mouse_y and mouse_y < 140:
                        clickSound.play()
                        windows.blit(intro_bg, (0, 0))
                        windows.blit(start_btn, (130, 260))
                        dlg = False
                    # ���� ��ư
                    elif 495 < mouse_x and mouse_x < 650 and 344 < mouse_y and mouse_y < 404:
                        clickSound.play()
                        intro = False
                
                    if mouse_clicked and dlg:
                        windows.blit(set_dialog, (220, 100))
                        if num_of_player == 2:
                            windows.blit(set_cursor, (430, 202))
                        elif num_of_player == 3:
                            windows.blit(set_cursor, (482, 202))
                        elif num_of_player == 4:
                            windows.blit(set_cursor, (535, 202))
                        if num_of_mal == 2:
                            windows.blit(set_cursor, (430, 263))
                        elif num_of_mal == 3:
                            windows.blit(set_cursor, (482, 263))
                        elif num_of_mal == 4:
                            windows.blit(set_cursor, (535, 263))
                        elif num_of_mal == 5:
                            windows.blit(set_cursor, (586, 263))
                        clickSound.play()
                        mouse_clicked = False

        # ȭ�� ������Ʈ �ֱ� 30 FPS
        pygame.display.update()
        fps_clock.tick(30)

    return num_of_player, num_of_mal

def GameScene(num_of_player, num_of_mal):
    # ���� ������ ���� (BG Music, Image)
    pygame.mixer.music.load('sounds/GameBGM.mp3')
    time.sleep(1)
    pygame.mixer.music.play(-1)

    # �÷��� ����
    game = True
    game_bg = pygame.image.load('images/game/GameScene.png')

    while game:
        windows.blit(game_bg, (0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

# ���� ����
initGame()