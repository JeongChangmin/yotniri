class Player:
	def __init__(self, player_id, player_name, num_of_horse):
		self.player_id = player_id
		self.player_name = player_name

		self.horse = []
		for i in range(1, num_of_horse + 1):
			self.horse.append(Horse(player_id, i))

		self.yut = 0 					# 뒷도 ~ 모
		self.wait = num_of_horse		# 대기열에 있는 말 개수
		self.goal = 0					# 골인한 말 개수
		self.throwable = False			# 더 던질 수 있는지
		self.group = [
				[], [], [], [], []
			]

	def get_yut(self):
		return self.yut

	def set_yut(self, data):
		self.yut = data


# 말 클래스
class Horse:
	def __init__(self, player_id, horse_id):
		self.player_id = player_id
		self.horse_id = horse_id

		self.position = (6, 7)	# 출발 좌표
		self.start = False		# 출발 했는지 여부 (마지막 6,6 위치에서 다시 출발하는 것 방지)
		self.goal = False		# 골인 했는지 여부


# 윷판 클래스
class Board:
	def __init__(self):
		self.board = [
				[ XY(), XY(), XY(),    0, XY(), XY(), XY() ],
				[ XY(), XY(),    0,    0,    0, XY(), XY() ],
				[ XY(),    0, XY(),    0, XY(),    0, XY() ],
				[    0,    0,    0, XY(),    0,    0,    0 ],
				[ XY(),    0, XY(),    0, XY(),    0, XY() ],
				[ XY(), XY(),    0,    0,    0, XY(), XY() ],
				[ XY(), XY(), XY(),    0, XY(), XY(), XY() ]
			]

class XY:
	def __init__(self):
		self.exist = False

		self.player_id = 0
		self.horse_id = 0

	# 위치 정보 갱신
	def arrive_info(self, horse):
		self.exist = True

		self.player_id = horse.player_id
		self.horse_id = horse.horse_id

	def leave_info(self):
		self.exist = False

		self.player_id = 0
		self.horse_id = 0