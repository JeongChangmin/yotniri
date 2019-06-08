
class Game:
	def __init__(self, map_info):
		self.info = map_info	# 위치 정보

	# 말이 어느 위치로 이동할 수 있는지 반환
	def move(self, controller, player, horse):
		x, y = horse.position
		ret = []
		
		# 현재 있는 곳의 좌표가 내가 머물고 있는 좌표라면?
		# 정리하고 새롭게 떠날 준비를 한다
		if x <= 6 and y <= 6 and self.info.board[y][x].player_id == horse.player_id:
			self.info.board[y][x].leave_info()
		

		# 뒷도 - 위치 처리
		if 0 == player.yut:
			# 아직 대기열이라면
			if y == 7:
				pass
			else:
				# 우하단
				if x == 6 and y == 6 and horse.start:
					x -= 1
					y -= 1
				# 좌측
				if x == 0:
					if y == 0:
						x += 1
					elif y == 6:
						x += 1
						y -= 1
					else:
						y -= 1
						if y == 3:
							y -= 1
				# 우측
				elif x == 6:
					if y == 0:
						y += 1
					else:
						y += 1
						if y == 3:
							y += 1
				# 상단
				elif y == 0:
					x += 1
					
					if x == 3:
						x += 1
				# 하단
				elif y == 6:
					x -= 1
	
					if x == 3:
						x -= 1
				# 좌 대각선
				elif x == y:
					if x == 3 and y == 3:
						x += 1
						y -= 1
					else:
						x -= 1
						y -= 1
				# 우 대각선
				else:
					x += 1
					y -= 1
	
			

		# 도 - 위치 처리
		elif 1 == player.yut:
			# 아직 대기열이라면
			if y == 7:
				y -= 2
				horse.start == True
				player.wait -= 1
			else:
				# 우하단
				if x == 6 and y == 6 and horse.start:
					x += 1
	
				# 좌측
				elif x == 0:
					if y == 0:
						x += 1
						y += 1
					elif y == 6:
						x += 1
					else:
						y += 1
						if y == 3:
							y += 1
				# 우측
				elif x == 6:
					if y == 0:
						x -= 1
						y += 1
					else:
						y -= 1
						if y == 3:
							y -= 1
				# 상단
				elif y == 0:
					if x == 0:
						x += 1
						y += 1
					else:
						x -= 1
						if x == 3:
							x -= 1
				# 하단
				elif y == 6:
					x += 1
					if x == 3:
						x += 1
				# 좌 대각선
				elif x == y:
					x += 1
					y += 1
				# 우 대각선
				else:
					if x == y:
						x += 1
						y += 1
					else:
						x -= 1
						y += 1
	
		# 개 - 위치 처리
		elif 2 == player.yut:
			# 아직 대기열이라면
			if y == 7:
				y -= 3
				horse.start == True
				player.wait -= 1
			else:
				# 우하단
				if x == 6 and y == 6 and horse.start:
					x += 2
	
				# 좌측
				if x == 0:
					if y == 0:
						x += 2
						y += 2
					elif y == 2:
						y += 1
	
					elif y == 6:
						x += 2
					elif y == 5:
						x += 1
						y += 1
					else:
						y += 2
						if y == 3:
							y += 1
				# 우측
				elif x == 6:
					if y == 4:
						y -= 1
	
					if y == 0:
						x -= 2
						y += 2
					elif y == 1:
						x -= 1
						y -= 1
					else:
						y -= 2
						if y == 3:
							y -= 1
				# 상단
				elif y == 0:
					if x == 4:
						x -= 1
	
					if x == 0:
						x += 2
						y += 2
					elif x == 1:
						x -= 1
						y += 1
					else:
						x -= 2
						if x == 3:
							x -= 1
				# 하단
				elif y == 6:
					if x == 2:
						x += 1
	
					x += 2
					if x == 3:
						x += 1
				# 좌 대각선
				elif x == y:
					x += 2
					y += 2
				# 우 대각선
				else:
					if x == y:
						x += 2
						y += 2
					else:
						x -= 2
						y += 2
	
		# 걸 - 위치 처리
		if 3 == player.yut:
			print('현재 플레이어 : ', player.player_id)
			print('현재 플레이어 좌표 : ', horse.position)
			# 아직 대기열이라면
			if y == 7:
				y -= 5
				horse.start = True
				player.wait -= 1
			else:
				# 우하단
				if x == 6 and y == 6 and horse.start:
					x += 3
	
				# 좌측
				if x == 0:
					if y == 6:
						x += 4
					elif y == 5:
						x += 2
						y += 1
					elif y == 4:
						x += 1
						y += 2
					elif y == 2:
						y += 4
					elif y == 1:
						y += 4
					elif y == 0:
						x += 3
						y += 3
				# 우측
				elif x == 6:
					if y == 6:
						y -= 4
					elif y == 5:
						y -= 4
					elif y == 4:
						y -= 4
					elif y == 2:
						y -= 2
						x -= 1
					elif y == 1:
						y -= 1
						x -= 2
					elif y == 0:
						x -= 3
						y += 3
				# 상단
				elif y == 0:
					if x == 0:
						x += 3
						y += 3
					elif x == 1:
						x -= 1
						y += 2
					elif x == 2:
						x -= 2
						y += 1
					elif x == 4:
						x -= 4
					elif x == 5:
						x -= 4
				# 하단
				elif y == 6:
					if x == 0:
						x += 4
					if x == 1:
						x += 4
					elif x == 2:
						x += 4
					elif x == 4:
						x += 3
					elif x == 5:
						x += 3
				# 좌 대각선
				elif x == y:
					x += 3
					y += 3
				# 우 대각선
				else:
					if x == y:
						x += 3
						y += 3
					else:
						x -= 3
						y += 3
	
		# 윷 - 위치 처리
		if 4 == player.yut:
			# 아직 대기열이라면
			if y == 7:
				y -= 6
				horse.start = True
				player.wait -= 1
			else:
				# 우하단
				if x == 6 and y == 6 and horse.start:
					x += 4
	
				# 좌측
				if x == 0:
					if y == 6:
						x += 5
					elif y == 5:
						x += 4
						y += 1
					elif y == 4:
						x += 2
						y += 2
					elif y == 2:
						x += 1
						y += 4
					elif y == 1:
						y += 5
					elif y == 0:
						x += 4
						y += 4
				# 우측
				elif x == 6:
					if y == 6:
						y -= 5
					elif y == 5:
						y -= 5
					elif y == 4:
						y -= 4
						x -= 1
					elif y == 2:
						y -= 2
						x -= 2
					elif y == 1:
						y -= 1
						x -= 4
					elif y == 0:
						x -= 4
						y += 4
				# 상단
				elif y == 0:
					if x == 0:
						x += 4
						y += 4
					elif x == 1:
						x -= 1
						y += 4
					elif x == 2:
						x -= 2
						y += 2
					elif x == 4:
						x -= 4
						y += 1
					elif x == 5:
						x -= 5
				# 하단
				elif y == 6:
					x += 5
				# 좌 대각선
				elif x == y:
					x += 4
					y += 4
				# 우 대각선
				else:
					if x == y:
							x += 4
							y += 4
					else:
						if x == 2 and y == 4:
							x = 2
							y = 6
						elif x == 1 and y == 5:
							x = 4
							y = 6
						else:
							x -= 4
							y += 4
	
		# 모 - 위치 처리
		if 5 == player.yut:
			# 아직 대기열이라면
			if y == 7:
				y -= 7
				horse.start = True
				player.wait -= 1
			else:
				# 우하단
				if x == 6 and y == 6 and horse.start:
					x += 5
	
				# 좌측
				if x == 0:
					if y == 6:
						x += 6
					elif y == 5:
						x += 5
						y += 1
					elif y == 4:
						x += 4
						y += 2
					elif y == 2:
						x += 2
						y += 4
					elif y == 1:
						y += 5
						x += 1
					elif y == 0:
						x += 5
						y += 5
				# 우측
				elif x == 6:
					if y == 6:
						y -= 6
					elif y == 5:
						y -= 5
	
						x -= 1
					elif y == 4:
						y -= 4
						x -= 2
					elif y == 2:
						y -= 2
						x -= 4
					elif y == 1:
						y -= 1
						x -= 5
					elif y == 0:
						x -= 5
						y += 5
				# 상단
				elif y == 0:
					if x == 0:
						x += 5
						y += 5
					elif x == 1:
						x -= 1
						y += 5
					elif x == 2:
						x -= 2
						y += 4
					elif x == 4:
						x -= 4
						y += 2
					elif x == 5:
						x -= 5
						y += 1
				# 하단
				elif y == 6:
					x += 6
				# 좌 대각선
				elif x == y:
					x += 4
					y += 4
				# 우 대각선
				else:
					if x == 4 and y == 2:
						x = 1
						y = 6
					elif x == 2 and y == 4:
						x = 4
						y = 6
					elif x == 1 and y == 5:
						x = 5
						y = 6
					else:
						x -= 6
						y += 6


		# 캐치
		if x <= 6 and y <= 6 and self.info.board[y][x].player_id != horse.player_id and self.info.board[y][x].player_id != 0:
			print('설마 같은 말 잡나')
			# 캐치한 플레이어 정보 획득
			other_player_id = self.info.board[y][x].player_id
			other_horse_id = self.info.board[y][x].horse_id

			ret.append(other_player_id)
			ret.append(other_horse_id)

			flag = True

			# 그룹이 있다면 그룹부터 정리
			for group in controller.player[other_player_id-1].group:
				if other_horse_id in group:
					ret.append('groupcatch')
					temp_h = []
					for h_id in group:
						controller.player[other_player_id-1].wait += 1
						controller.player[other_player_id-1].horse[h_id-1].position = (6,7)
						controller.player[other_player_id-1].horse[h_id-1].start = False

						temp_h.append(h_id)
					flag = False
					ret.append(temp_h)
					group[:] = []

			# 그룹이 아니라면?
			if controller.player[other_player_id-1].horse[other_horse_id-1].position != (6,7) and flag:
				ret.append('catch')
				controller.player[other_player_id-1].wait += 1
				controller.player[other_player_id-1].horse[other_horse_id-1].position = (6,7)
				controller.player[other_player_id-1].horse[other_horse_id-1].start = False


			print('잡힌 말 주인 : {0}, 잡힌 말 아이디 : {1}'.format(other_player_id, other_horse_id))
			print(ret)

		# 그룹 함께 이동
		for group in player.group:
			if horse.horse_id in group:
				for i in range(0, len(group)):
					player.horse[group[i]-1].position = (x,y)
					print('그룹 함께 이동 좌표 : ', (x,y))
				ret.append('group')

		# 그룹화
		if x <= 6 and y <= 6 and self.info.board[y][x].player_id == horse.player_id:
			print('그룹화 됨')
			# 그룹이 비어있는지 체크하고 병합
			for group in player.group:
				# 그룹이 있다면 아이디 체크 후 병합
				if group:
					# 
					if self.info.board[y][x].horse_id in group:
						group.append(horse.horse_id)
						break
				# 그룹이 비어있으면 둘다 넣음
				else:
					group.append(self.info.board[y][x].horse_id)
					group.append(horse.horse_id)
					break 

		
			

		
		# 골인 관련
		if x > 6 or y > 6:
			ret.append('goal')
		else:
			# 좌표 등록
			self.info.board[y][x].arrive_info(horse)
			horse.position = (x,y)
			print('XY-신규좌표등록(p,h): {0},{1}'.format(self.info.board[y][x].player_id, self.info.board[y][x].horse_id))

			if horse.start == False:
				horse.start = True





		print('---------------------------')
		return ret





















		## 캐치
		#temp = False
		#if x <= 6 and y <= 6 and self.info.board[y][x].player_id != horse.player_id and self.info.board[y][x].player_id != 0:
		#	ret.append('catch')
		#
		#	other_player = 0
		#	other_horse = 0
		#
		#	# 그룹 체크해서 그룹 전부 제거
		#	temp_g = []
		#	temp = False
		#	for group in controller.player[self.info.board[y][x].player_id-1].group:
		#		if self.info.board[y][x].horse_id in group:
		#			other_player = self.info.board[y][x].player_id-1
		#			for index in group:
		#				controller.player[other_player].wait += 1
		#				controller.player[other_player].horse[index].postion = (6,7)
		#				controller.player[other_player].horse[index].start = False
		#				temp_g.append(index)
		#			temp = True
		#
		#	if not temp:
		#		other_player = self.info.board[y][x].player_id
		#		other_horse = self.info.board[y][x].horse_id
		#		controller.player[other_player-1].wait += 1
		#		controller.player[other_player-1].horse[other_horse-1].position = (6,7)
		#		controller.player[other_player-1].horse[other_horse-1].start = False
		#
		#	#print('[XY{0},{1}] 지울 데이터 - player: {2}'.format(y,x,self.info.board[y][x].player_id))
		#
		#	controller.player[other_player-1].wait += 1
		#	controller.player[other_player-1].horse[other_horse-1].position = (6,7)
		#
		#	# 잡아서 위치 모든 것 리셋
		#	ret.append(other_player)
		#	ret.append(other_horse)




		#	ret_group = []
		#	ret.append('catch')
		#	ret.append(self.info.board[y][x].player_id)
		#
		#	for group in controller.player[self.info.board[y][x].player_id-1].group:
		#		# 그룹이 있다면 전부 제거
		#		t = []
		#		if group:
		#			if controller.player[self.info.board[y][x].player_id-1].horse[controller.player[self.info.board[y][x].horse_id-1]] in group:
		#				for h_id in group:
		#					controller.player[self.info.board[y][x].player_id-1].wait += 1
		#					controller.player[self.info.board[y][x].player_id-1].horse[h_id-1].positon = (6,7)
		#					controller.player[self.info.board[y][x].player_id-1].horse[h_id-1].start = False
		#					t.append(h_id)
		#				group[:] = []
		#				
		#				temp = True
		#				ret_group.append(t)
		#				ret.append(ret_group)
		#				ret.append('group')
		#				break
		#			
		#	if not temp:
		#		controller.player[self.info.board[y][x].player_id-1].wait += 1
		#		controller.player[self.info.board[y][x].player_id-1].horse[self.info.board[y][x].horse_id-1].positon = (6,7)
		#		controller.player[self.info.board[y][x].player_id-1].horse[self.info.board[y][x].horse_id-1].start = False
		#		print('잡힌말 : ', self.info.board[y][x].player_id-1, self.info.board[y][x].horse_id-1)
		#		print('포지션 : ', controller.player[self.info.board[y][x].player_id-1].horse[self.info.board[y][x].horse_id-1].positon)
		#		ret.append(self.info.board[y][x].horse_id-1)
		#
		#	print(ret)

		

		