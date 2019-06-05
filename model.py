# 모델 클래스
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
