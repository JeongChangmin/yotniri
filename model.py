
#모델 클래스
class Model:
	def __init__(self):
		self.setting = Setting()

# 게임 세팅 클래스
class Setting:
	def __init__(self):
		self.num_of_player = 2
		self.num_of_horse = 4

		self.default = (2, 4)

	def get_default(self):
		return self.default

	def set_setting(self, data):
		self.num_of_player = data['num_of_player']
		self.num_of_horse = data['num_of_horse']

	def get_setting(self):
		return { 'num_of_player' : self.num_of_player, 'num_of_horse' : self.num_of_horse }

# 플레이어 클래스
class Player:
	def __init__(self, player_id, player_name, num_of_horse):
		self.player_id = player_id
		self.player_name = player_name

		self.horse = []
		for i in range(1, num_of_horse + 1):
			self.horse.append(Horse(player_id, i))

		self.yut = {} 					# 뒷도 ~ 모
		self.num_of_wait = num_of_horse	# 대기열에 있는 말 개수

	def get_yut(self):
		return self.yut

	def set_yut(self, data):
		if data == 0:
			if 'back' in self.yut.keys():
				self.yut['back'] = self.yut['back'] + 1
			else:
				self.yut['back'] = 1
		elif data == 1:
			if 'do' in self.yut.keys():
				self.yut['do'] = self.yut['do'] + 1
			else:
				self.yut['do'] = 1
		elif data == 2:
			if 'gae' in self.yut.keys():
				self.yut['gae'] = self.yut['gae'] + 1
			else:
				self.yut['gae'] = 1
		elif data == 3:
			if 'girl' in self.yut.keys():
				self.yut['girl'] = self.yut['girl'] + 1
			else:
				self.yut['girl'] = 1
		elif data == 4:
			if 'yut' in self.yut.keys():
				self.yut['yut'] = self.yut['yut'] + 1
			else:
				self.yut['yut'] = 1
		elif data == 5:
			if 'mo' in self.yut.keys():
				self.yut['mo'] = self.yut['mo'] + 1
			else:
				self.yut['mo'] = 1

	def clear_yut(self):
		self.yut.clear()

# 말 클래스


class Horse:
    def __init__(self, player_id, horse_id):
        self.player_id = player_id
        self.horse_id = horse_id
        self.posX = 6
        self.posY = -1






# 윷놀이 이동 위치 이벤트

import random

# 윷 이벤트 결과
def yutObject(player_id, yutExecute=True): # 윷 던지고 난 결과     # 플레이어id, 말번호,  윷을 던지는 신호를 줄 경우

    dic = {'도': 1, '개': 2, '걸': 3, '윷': 4, '모': 5, '빽도': -1}

    n = random.sample(['도', '개', '걸', '윷', '모', '빽도'], 1)

    a = n[0]
    print(a)

    return player_id, dic[a], n[0]



# main
# 지도 맵
N = 6
map = [[0 for col in range(N + 2)] for row in range(N + 2)]



# 입력값 : 플레이어 id, 해당 플레이어의 몇번째의 말, 말 전 위치 x값, 말 전 위치 y값, 현재 말 위치 x값, 현재 말 위치 y값

# 윷 이동 후 위치값 반환 이벤트
def yut_move(id, num, bx, by, x, y, z):
    player_id = id
    numOfHorse = num

    # 이미 돌아왔던 흔적 -> 백도 때문에 넣음
    before_x = bx
    before_y = by

    horse = Horse(id, num)

    horse.posX = x
    horse.posY = y


    if(z == -1): # 빽도일 경우
        if((horse.posX, horse.posY) == (6,-1)):
            return
        elif((horse.posX, horse.posY) == (6,1)):
            horse.posX = 6
            horse.posY = 0
            return player_id, numOfHorse, before_x, before_y, horse.posX, horse.posY
        else:
            horse.posX =  before_x[1]
            horse.posY =  before_y[1]
            before_x[1] = before_x[2]
            before_y[1] = before_y[2]
            return player_id, numOfHorse, before_x, before_y, horse.posX, horse.posY



    # 만약 시작점이 (6,-1)이라면
    if((horse.posX, horse.posY) == (6,-1)):
        horse.posX = 6
        horse.posY = 0
        yut_result = z
        while(yut_result):
            horse.posY += 1
            before_x[yut_result] = horse.posX
            before_y[yut_result] = horse.posY
            if ((horse.posX, horse.posY) == (6, 3)):  # (3,0) 예외처리하기
                horse.posY += 1
            yut_result -= 1
        return player_id, numOfHorse, before_x, before_y, horse.posX, horse.posY
    elif((horse.posX, horse.posY) == (6,0)): # 현재 위치가 (6,0)이라면
        print("도착")
        return player_id, numOfHorse
    else:
        horse.posX = x
        horse.posY = y
        yut_result = z

# 현재 위치가 (6,6)일경우
    if((horse.posX, horse.posY) == (6,6)):
        while(yut_result): #결과 칸수 -> 한칸씩 어떻게 변화를 하는지 알려줌
                before_x[yut_result] = horse.posX
                before_y[yut_result] = horse.posY
                if(horse.posX == 0 and horse.posY == 0):
                    horse.posX += 1
                else:
                    horse.posX -= 1
                    horse.posY -= 1
                yut_result -= 1
        return player_id, numOfHorse, before_x, before_y, horse.posX, horse.posY

# 현재 위치가 (0, 6)일 경우
    #if(horse.posX, horse.posY == (0,6)):
    if((horse.posX, horse.posY) == (0, 6)):
        while(yut_result): #-- & 현재위치가 아닐경우
                if(horse.posX > 6 and horse.posY> 0):
                    print("도착2!!")
                    break
                else:
                    before_x[yut_result] = horse.posX
                    before_y[yut_result] = horse.posY
                    horse.posX+=1
                    horse.posY-=1
                yut_result -= 1
        return player_id, numOfHorse, before_x, before_y, horse.posX, horse.posY


# 현재 위치가 (3, 3)일 경우
    if((horse.posX, horse.posY) == (3,3)):
        while(yut_result):# -- & 현재위치가 아닐경우):
                if(horse.posX >= 6 and horse.posY <= 0):
                    print("도착3!!")
                    break
                else:
                    before_x[yut_result] = horse.posX
                    before_y[yut_result] = horse.posY
                    horse.posX+=1
                    horse.posY-=1
                yut_result -= 1
        return player_id, numOfHorse,  before_x, before_y, horse.posX, horse.posY

# 안에
# 현재 위치가 대각선이라면...(3, 3) (6,6), (0,6)을 제외한
# (1, 1), (2, 2), (4, 4), (5, 5), (1, 5), (2, 4), (4, 2), (5, 1)
    if(((horse.posX, horse.posY) == (1, 1)) or ((horse.posX, horse.posY) == (2, 2)) or ((horse.posX, horse.posY) == (4, 4)) or ((horse.posX, horse.posY) == (5, 5)) or ((horse.posX, horse.posY) == (1, 5)) or ((horse.posX, horse.posY) == (2, 4)) or ((horse.posX, horse.posY) == (4, 2)) or ((horse.posX, horse.posY) == (5, 1))):
        while(yut_result):# -- & 현재위치가 아닐경우):
            if((horse.posX, horse.posY) == (0, 0)):
                before_x[yut_result] = horse.posX
                before_y[yut_result] = horse.posY
                horse.posX += 1
            elif(((horse.posX, horse.posY) == (1, 5)) or ((horse.posX, horse.posY) == (2, 4)) or ((horse.posX, horse.posY) == (4, 2)) or ((horse.posX, horse.posY) == (5, 1))):# y=-2x꼴
                if((horse.posX, horse.posY) == (2, 4) and (yut_result > 1)):
                    if(yut_result == 2):
                        while(yut_result):
                            before_x[yut_result] = horse.posX
                            before_y[yut_result] = horse.posY
                            horse.posX = horse.posX + 1
                            horse.posY = horse.posY - 1
                            yut_result-=1
                        #horse.posX += 2
                        #horse.posY -= 2
                        break
                    elif(yut_result == 3):
                        while (yut_result):
                            before_x[yut_result] = horse.posX
                            before_y[yut_result] = horse.posY
                            horse.posX = horse.posX + 1
                            horse.posY = horse.posY - 1
                            yut_result -= 1
                        #horse.posX += 3
                        #horse.posY -= 3
                        break
                    elif(yut_result == 4):
                        while (yut_result):
                            before_x[yut_result] = horse.posX
                            before_y[yut_result] = horse.posY
                            horse.posX = horse.posX + 1
                            horse.posY = horse.posY - 1
                            yut_result -= 1
                        #horse.posX += 4
                        #horse.posY -= 4
                        break
                    elif(yut_result == 5):
                        print("도착!!")
                        break
                before_x[yut_result] = horse.posX
                before_y[yut_result] = horse.posY
                horse.posX+=1
                horse.posY-=1
            elif(horse.posX == horse.posY):  # y=2x꼴
                before_x[yut_result] = horse.posX
                before_y[yut_result] = horse.posY
                horse.posX -= 1
                horse.posY -= 1
            else:
                before_x[yut_result] = horse.posX
                before_y[yut_result] = horse.posY
                horse.posX += 1
                if ((horse.posX, horse.posY) == (3, 0)): # (3,0) 예외처리하기
                    horse.posX += 1
            if(horse.posX > 6 and horse.posY <= 0):
                print("도착4!!")
                break
            yut_result -= 1
        return player_id, numOfHorse, before_x, before_y , horse.posX, horse.posY

# 현재위치가 대각선, (6,6), (0,6), (3,3)이 아니라면
    while(yut_result):
        if(horse.posX == 6 and ((horse.posY < 6) and (horse.posY > 0))):  # 현재 위치가 어디에 있는지
            before_x[yut_result] = horse.posX
            before_y[yut_result] = horse.posY
            horse.posY+=1
            if ((horse.posX, horse.posY) == (6, 3)):  # (3,0) 예외처리하기
                horse.posY += 1
        elif(((horse.posX > 0) and (horse.posX <= 6)) and horse.posY == 6):
            before_x[yut_result] = horse.posX
            before_y[yut_result] = horse.posY
            horse.posX-=1
            if ((horse.posX, horse.posY) == (3, 6)):  # (3,0) 예외처리하기
                horse.posX -= 1
        elif((horse.posX, horse.posY) == (0, 0)):
            before_x[yut_result] = horse.posX
            before_y[yut_result] = horse.posY
            horse.posX += 1
        elif(horse.posX == 0 and ((horse.posY <= 6) and (horse.posY > 0))):
            before_x[yut_result] = horse.posX
            before_y[yut_result] = horse.posY
            horse.posY-=1
            if ((horse.posX, horse.posY) == (0, 3)):  # (3,0) 예외처리하기
                horse.posY -= 1
        elif(horse.posX <= 6 and horse.posY == 0):
            before_x[yut_result] = horse.posX
            before_y[yut_result] = horse.posY
            horse.posX+=1
            if ((horse.posX, horse.posY) == (3, 0)):  # (3,0) 예외처리하기
                horse.posX += 1
        if(horse.posX > 6 and horse.posY == 0):
            print("도착5!!")
            break
        yut_result -= 1
    return player_id, numOfHorse, before_x, before_y, horse.posX, horse.posY

# 반환값 : 플레이어 id, 해당 플레이어의 몇번째의 말, 말 전 위치 x값, 말 전 위치 y값, 현재 말 위치 x값, 현재 말 위치 y값



# 윷 던지는 이벤트
def yut_event(player_id):


    # 윷 이벤트 결과값 변수의 초기
    num = [0, 0, 0, 0, 0, 0]
    horse_id = [1, 2, 3, 4, 5]

    i = 1

    # 윷 던지고 나온 결과값
    num[i] = yutObject(player_id, True)[1]
    while(num[i] == 4 or num[i] == 5): # 윷 또는 모가 오면 또 던짐
        i+=1
        num[i] = yutObject(player_id, True)[1]  # 윷 결과값을 여기에 모으기
    #print(num)
    #print("몇번", i)
    # 해당 num값을 view에 보여줌!!! 윷인지 도인지 등등

    # 말 id전달 -> 현재 맵위에 있는 말, 보유한 말 중에서 마지막 말
    # if( 만약 맴 위에 있는 말이 있다면 or 보유한 말 중에서 마지막 값):
    # 아무말도 없고 백도이면 그 다음 플레이어로 옮기기
    # horse_id_num -> 만약 그 말들이 3개라면 -> a=3
    horse_id_num = [0,1]
    a = 1
    # -> 맵위에 있지 않는 말에서 백도가 나오면 그 다음 플레이어 값 전달하고 여기서 종료
    while(a):
        # 윷의 결과값에 맞게 좌표 이동시키기
        result = yut_move_event(player_id, horse_id_num[a], i, num)
        a-=1

    return result






def yut_move_event(player_id, horse_id, i, num):

    horse = Horse(player_id, horse_id) # 해당 말 위치값도 전달하기


    yut_move_result = [0,0,0,0,0]

    before_x = [0, 0, 0, 0, 0, 0]
    before_y = [0, 0, 0, 0, 0, 0]


    print(horse.posX, horse.posY)
    k = i
    j = 1

    while (i):

        if(j>1):
            before_x = yut_move_result[j-1][2]
            before_y = yut_move_result[j-1][3]
            horse.posX = yut_move_result[j-1][4]
            horse.posY = yut_move_result[j-1][5]
        yut_move_result[j] = yut_move(player_id, horse_id, before_x, before_y, horse.posX, horse.posY, num[j])  # 위치이동
        #if( 만약 말을 잡으면)
    # # 자기함수 다시 불러옴 yut_event
        i-=1
        j+=1
#    print("이동한 위치", yut_move_result[j-1][4], yut_move_result[j-1][5])

    horse_move_posX = yut_move_result[j-1][4]
    horse_move_posY = yut_move_result[j-1][5]
    player_id+=1

    return horse_move_posX, horse_move_posY



# controller에서
#import model


# view에서 첫번째 플레이어 순서가 옴
# view에서 '윷 던지기'를 누름 -> 1
#print(model.yut_event(1))

# 어떻게 실행?
#print(yut_event(1))
# 처음 위치 : (6,-1) -> 아직 맵 위에 말 놓이기 전!!!!
# 결과값은 이동한 후의 위치 x,y좌표 반환!!!

#  처음 뺵도일때만  오류!!!