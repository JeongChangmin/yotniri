import model
import view
import random

class Controller:
	def __init__(self):
		self.model = model.Model()
		self.view = view.View()

		self.player = []

	# 게임 실행
	def run_game(self):
		while True:
			self.view.show_intro(self)
			self.game_setting()
			self.view.show_game(self)
	
	# 플레이어 세팅
	def game_setting(self):
		num_data = self.model.setting.get_setting()

		for i in range(1, num_data['num_of_player'] + 1):
			if i == 1:
				player_name = '박 문 일'
			elif i == 2:
				player_name = '박 민 수'
			elif i == 3:
				player_name = '전 지 훈'
			elif i == 4:
				player_name = '정 창 민'
			self.player.append(model.Player(i, player_name, num_data['num_of_horse']))

	# 윷 던지기 랜덤 값
	def random_yut(self):
		return random.randint(0, 5)

	# Action ( ↔ Model)
	def action(self, action, data = 0):
		# 게임 설정값
		if action == 'set_setting':
			self.model.setting.set_setting(data)
		elif action == 'get_setting':
			return self.model.setting.get_setting()
		elif action == 'get_setting_default':
			return self.model.setting.get_default()
		
	








# 게임을 전반적으로 관리하는 클래스
class GameManager:
	# manager = SettingManager
	def __init__(self, manager):
		self.player = []
		
		for i in range(0, manager.get_num_of_player()):
			self.player.append(Player(i+1, manager.get_num_of_horse()))

	def get_player(self):
		return self.player



if __name__ == "__main__":
	Controller().run_game()