# coding=euc-kr
# Import
import pygame, sys, time
from mouse import *
from constants import *
from pygame.locals import *

# 화면 초기화
def initGame():
    global windows, fps_clock

    # 실질적인 화면 세팅
    pygame.init()
    windows = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32); 
    pygame.display.set_caption('소프트웨어 공학 팀프로젝트 - 윷놀이')          
    pygame.display.set_icon(pygame.image.load('images/icons/icon.png'))      
    # FPS Object
    fps_clock = pygame.time.Clock()

    # Scene 호출
    num_of_player, num_of_mal = IntroScene()
    GameScene(num_of_player, num_of_mal)

def IntroScene():
    # 인트로 페이지 설정 (BG Music, Image)
    pygame.mixer.music.load('sounds/IntroBGM.mp3')
    pygame.mixer.music.play(-1)

    clickSound = pygame.mixer.Sound('sounds/Click.wav')

    # 이미지 렌더링
    intro_bg = pygame.image.load('images/intro/IntroScene.png')
    start_btn = pygame.image.load('images/intro/IntroStartBtn.png')
    start_btn_clicked = pygame.image.load('images/intro/IntroStartBtn_Clicked.png')
    set_dialog = pygame.image.load('images/intro/SettingDlg.png')
    set_cursor = pygame.image.load('images/intro/SetCursor.png')
    windows.blit(intro_bg, (0, 0))
    windows.blit(start_btn, (130, 260))
    
    # Flag 변수
    intro = True
    music = True
    dlg = False
    mouse_clicked = False

    # Setting 변수
    num_of_player = 2
    num_of_mal = 4

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
                if not dlg:
                    # 마우스가 시작 글자에 닿을 시 글자 확대
                    if 115 < mouse_x and mouse_x < 205 and 250 < mouse_y and mouse_y < 285:                      
                        windows.blit(intro_bg, (0, 0))
                        windows.blit(start_btn_clicked, (128, 260))
                    else:
                        windows.blit(intro_bg, (0, 0))
                        windows.blit(start_btn, (130, 260))
            if event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = getMousePos(event)
                # 마우스가 시작 글자에 닿을 시 효과음 발생 및 글자 확대
                if 115 < mouse_x and mouse_x < 205 and 250 < mouse_y and mouse_y < 285 and not dlg:
                    clickSound.play()                    
                    windows.blit(set_dialog, (220, 100))
                    windows.blit(set_cursor, (430, 202))
                    windows.blit(set_cursor, (535, 263))
                
                    dlg = True
                    num_of_player = 2
                    num_of_mal = 4
                
                # 세팅 창이 열려있을 때 마우스 처리
                else:
                    # 플레이어 체크
                    if 418 < mouse_x and mouse_x < 458 and 208 < mouse_y and mouse_y < 248:
                        mouse_clicked = True
                        num_of_player = 2
                    elif 470 < mouse_x and mouse_x < 510 and 208 < mouse_y and mouse_y < 248:
                        mouse_clicked = True
                        num_of_player = 3
                    elif 520 < mouse_x and mouse_x < 560 and 208 < mouse_y and mouse_y < 248:
                        mouse_clicked = True
                        num_of_player = 4
                    # 말 체크
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
                    # X 버튼
                    elif 628 < mouse_x and mouse_x < 645 and 124 < mouse_y and mouse_y < 140:
                        clickSound.play()
                        windows.blit(intro_bg, (0, 0))
                        windows.blit(start_btn, (130, 260))
                        dlg = False
                    # 시작 버튼
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

        # 화면 업데이트 주기 30 FPS
        pygame.display.update()
        fps_clock.tick(30)

    return num_of_player, num_of_mal

def GameScene(num_of_player, num_of_mal):
    # 게임 페이지 설정 (BG Music, Image)
    pygame.mixer.music.load('sounds/GameBGM.mp3')
    time.sleep(1)
    pygame.mixer.music.play(-1)

    # 플래그 변수
    game = True
    game_bg = pygame.image.load('images/game/GameScene.png')

    while game:
        windows.blit(game_bg, (0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

# 게임 실행
initGame()