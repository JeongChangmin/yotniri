from horse import Horse

class Player:
	def __init__(self, player_id, numOfHorse):
		self.player_id = player_id
		self.horse = []
		self.numOfHorse = numOfHorse
		for i in range(0, numOfHorse):
			self.horse.append(Horse(self.player_id, i+1))
		
		

	
