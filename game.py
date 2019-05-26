import pygame, sys, time
from mouse import *
from constants import *
from pygame.locals import *

# 초기 화면을 구성하는 메소드
# 내부에서 Intro, Game Scene 호출
def initGame():
    global windows, fpsClock

    # Window Initialize...
    pygame.init()
    windows = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32); 
    pygame.display.set_caption('소프트웨어 공학 팀프로젝트 - 윷놀이')          
    pygame.display.set_icon(pygame.image.load('images/icons/icon.png'))      
    
    # FPS를 관리하기 위한 변수
    fpsClock = pygame.time.Clock()

    # Scene 호출
    while True:
        numOfPlayer, numOfHorse = IntroScene()
        GameScene(numOfPlayer, numOfHorse)
                   

# 시작 화면을 구성하는 메소드
def IntroScene():
    # 인트로 페이지 설정
    pygame.mixer.music.load('sounds/bgm_intro.mp3')
    pygame.mixer.music.play(-1)

    soundClick = pygame.mixer.Sound('sounds/click.wav')

    # 시작 화면 이미지 렌더링
    spriteIntroBg = pygame.image.load('images/intro/bg_intro.png')
    spriteStartBtn = pygame.image.load('images/intro/sprite_button_start.png')
    spriteStartBtnOn = pygame.image.load('images/intro/sprite_button_start_on.png')
    spriteSetDialog = pygame.image.load('images/intro/dlg_settings.png')
    spriteSelectCursor = pygame.image.load('images/intro/sprite_selection.png')
    windows.blit(spriteIntroBg, (0, 0))
    windows.blit(spriteStartBtn, (130, 260))
    
    # Flag 변수
    intro = True                # 이벤트 루프 탈출
    music = True                # BGM On / Off 
    dlg = False                 # 다이얼로그 
    mouseClicked = False        # 마우스 클릭 체크

    # 반환할 설정 변수 (기본 플레이어 2, 말 4)
    numOfPlayer = 2
    numOfHorse = 4

    while intro:
        # 이벤트 설정
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
            # 마우스 모션 이벤트
            if event.type == MOUSEMOTION:
                mouseXPos, mouseYPos = getMousePos(event)
                if not dlg:
                    # 마우스가 시작 글자에 닿을 시 글자 확대
                    if 115 < mouseXPos and mouseXPos < 205 and 250 < mouseYPos and mouseYPos < 285:                      
                        windows.blit(spriteIntroBg, (0, 0))
                        windows.blit(spriteStartBtnOn, (128, 260))
                    else:
                        windows.blit(spriteIntroBg, (0, 0))
                        windows.blit(spriteStartBtn, (130, 260))
            # 마우스 클릭 이벤트
            if event.type == MOUSEBUTTONUP:
                mouseXPos, mouseYPos = getMousePos(event)
                # 시작 클릭 시 세팅 다이얼로그를 열면서 효과음 발생
                if 115 < mouseXPos and mouseXPos < 205 and 250 < mouseYPos and mouseYPos < 285 and not dlg:
                    soundClick.play()                    
                    windows.blit(spriteSetDialog, (220, 100))
                    windows.blit(spriteSelectCursor, (430, 202))
                    windows.blit(spriteSelectCursor, (535, 263))
                
                    dlg = True
                    numOfPlayer = 2
                    numOfHorse = 4
                # 세팅 다이얼로그가 열려있을 때 마우스 처리
                else:
                    # 플레이어 체크
                    if 418 < mouseXPos and mouseXPos < 458 and 208 < mouseYPos and mouseYPos < 248:
                        mouseClicked = True
                        numOfPlayer = 2
                    elif 470 < mouseXPos and mouseXPos < 510 and 208 < mouseYPos and mouseYPos < 248:
                        mouseClicked = True
                        numOfPlayer = 3
                    elif 520 < mouseXPos and mouseXPos < 560 and 208 < mouseYPos and mouseYPos < 248:
                        mouseClicked = True
                        numOfPlayer = 4
                    # 말 체크
                    elif 418 < mouseXPos and mouseXPos < 458 and 269 < mouseYPos and mouseYPos < 308:
                        mouseClicked = True
                        numOfHorse = 2
                    elif 470 < mouseXPos and mouseXPos < 510 and 269 < mouseYPos and mouseYPos < 308:
                        mouseClicked = True
                        numOfHorse = 3
                    elif 520 < mouseXPos and mouseXPos < 560 and 269 < mouseYPos and mouseYPos < 308:
                        mouseClicked = True
                        numOfHorse = 4
                    elif 572 < mouseXPos and mouseXPos < 612 and 269 < mouseYPos and mouseYPos < 308:
                        mouseClicked = True
                        numOfHorse = 5
                    # X 버튼
                    elif 628 < mouseXPos and mouseXPos < 645 and 124 < mouseYPos and mouseYPos < 140:
                        soundClick.play()
                        windows.blit(spriteIntroBg, (0, 0))
                        windows.blit(spriteStartBtn, (130, 260))
                        dlg = False
                    # 시작 버튼
                    elif 495 < mouseXPos and mouseXPos < 650 and 344 < mouseYPos and mouseYPos < 404:
                        soundClick.play()                        
                        time.sleep(0.5)

                        # 게임 화면 이미지 미리 렌더링
                        spriteGameBg = pygame.image.load('images/game/bg_game.png')
                        windows.blit(spriteGameBg, (0, 0))
                        intro = False
                
                    if mouseClicked and dlg:
                        windows.blit(spriteSetDialog, (220, 100))
                        if numOfPlayer == 2:
                            windows.blit(spriteSelectCursor, (430, 202))
                        elif numOfPlayer == 3:
                            windows.blit(spriteSelectCursor, (482, 202))
                        elif numOfPlayer == 4:
                            windows.blit(spriteSelectCursor, (535, 202))
                        if numOfHorse == 2:
                            windows.blit(spriteSelectCursor, (430, 263))
                        elif numOfHorse == 3:
                            windows.blit(spriteSelectCursor, (482, 263))
                        elif numOfHorse == 4:
                            windows.blit(spriteSelectCursor, (535, 263))
                        elif numOfHorse == 5:
                            windows.blit(spriteSelectCursor, (586, 263))
                        soundClick.play()
                        mouseClicked = False

        # 화면 업데이트 주기 30 FPS
        pygame.display.update()
        fpsClock.tick(30)

    return numOfPlayer, numOfHorse

# 게임 화면을 구성하는 메소드
def GameScene(numOfPlayer, numOfHorse):
    # 게임 페이지 설정
    pygame.mixer.music.load('sounds/bgm_game.mp3')
    pygame.mixer.music.play(-1)

    soundClick = pygame.mixer.Sound('sounds/click.wav')

    # 게임 화면 이미지 렌더링
    spriteGameBg = pygame.image.load('images/game/bg_game.png')
    windows.blit(spriteGameBg, (0, 0))
    
    # Flag 변수
    game = True                 # 이벤트 루프 탈출
    music = True                # BGM On / Off 

    while game:
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
                # goto Main
                if event.key == K_ESCAPE:
                    game = False
                

        # 화면 업데이트 주기 30 FPS
        pygame.display.update()
        fpsClock.tick(30)

# 게임 실행
initGame()