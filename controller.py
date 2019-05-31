from player import Player
from horse import Horse

# 게임 설정 관리 클래스
class SettingManager:
	def __init__(self):
		self.num_of_player = 4
		self.num_of_horse = 2
		
	def get_settings():
		return self.get_num_of_player, self.get_num_of_horse

	def set_settings(self, player, horse):
		self.num_of_player = player
		self.num_of_horse = horse

	def get_num_of_player(self):
		return self.num_of_player

	def get_num_of_horse(self):
		return self.num_of_horse


# 게임을 전반적으로 관리하는 클래스
class GameManager:
	# manager = SettingManager
	def __init__(self, manager):
		self.player = []
		
		for i in range(0, manager.get_num_of_player()):
			self.player.append(Player(i+1, manager.get_num_of_horse()))

	def get_player(self):
		return self.player