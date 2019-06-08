import model
import view
import game
import random

class Controller:
	def __init__(self):
		self.view = view.View()
		self.game = game.Game(model.Board())

		# 게임 기본 세팅
		self.num_of_player = 2
		self.num_of_horse = 4
		self.default_value = (2, 4)

		self.player = []	# 플레이어 정보
		self.turn = 1		# 현재 턴

	# 게임 실행
	def run_game(self):
		while True:
			self.view.show_intro(self)
			self.game_setting()
			self.view.show_game(self)
			self.game_reset()

	# 플레이어 세팅
	def game_setting(self):
		for i in range(1, self.num_of_player + 1):
			if i == 1:
				player_name = '박 문 일'
			elif i == 2:
				player_name = '박 민 수'
			elif i == 3:
				player_name = '전 지 훈'
			elif i == 4:
				player_name = '정 창 민'
			self.player.append(model.Player(i, player_name, self.num_of_horse))

	# 게임 리셋
	def game_reset(self):
		self.player.clear()
		self.turn = 1

	# 윷 던지기 랜덤 값
	def throw_random_yut(self):
		return random.randint(3,3)#random.randint(0, 5)

	# 게임 턴을 넘김
	def next_turn(self):
		if self.turn >= self.num_of_player:
			self.turn = 1
		else:
			self.turn += 1
		return self.turn

if __name__ == "__main__":
	Controller().run_game()
