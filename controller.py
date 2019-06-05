import model
import view
import random

class Controller:
	def __init__(self):
		self.model = model.Model()
		self.view = view.View()

		self.player = []
		self.turn = 1

	# 게임 실행
	def run_game(self):
		while True:
			self.view.show_intro(self)
			self.game_setting()
			self.view.show_game(self)
			self.game_reset()

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

	# 게임 리셋
	def game_reset(self):
		self.player.clear()
		self.turn = 1

	# 윷 던지기 랜덤 값
	def random_yut(self):
		val = random.randint(0, 100)
		yut = 0

		# 확률 조정
		if 0 <= val and val < 5:
			yut = 0
		elif 5 <= val and val < 20:
			yut = 1
		elif 20 <= val and val < 55:
			yut = 4#2
		elif 55 <= val and val < 80:
			yut = 3
		elif 80 <= val and val < 90:
			yut = 4
		else:
			yut = 5

		return yut

	# 게임 턴을 알림
	def next_turn(self):
		if self.turn >= self.model.setting.get_setting()['num_of_player']:
			self.turn = 1
		else:
			self.turn += 1
		print(self.turn)
		return self.turn

	# Action ( ↔ Model)
	def action(self, action, data = 0):
		# 게임 설정값
		if action == 'set_setting':
			self.model.setting.set_setting(data)
		elif action == 'get_setting':
			return self.model.setting.get_setting()
		elif action == 'get_setting_default':
			return self.model.setting.get_default()
		elif action == 'set_yut':
			self.player[self.turn - 1].set_yut(data)
		elif action == 'get_yut':
			return self.player[self.turn - 1].get_yut()
		elif action == 'clear_yut':
			self.player[self.turn - 1].clear_yut()


if __name__ == "__main__":
	Controller().run_game()
