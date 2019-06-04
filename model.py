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


# 말 클래스
class Horse:
	def __init__(self, player_id, horse_id):
		self.player_id = player_id
		self.horse_id = horse_id
