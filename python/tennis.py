class Tennis:

	scores = [0, 15, 30, 40]
	
	def __init__(self):
		self.players = [0,0]
		self.winner = -1
		self.advantage = -1
		
	def score_point(self, scorer):
		self.players[scorer] += 1
		opponent = abs(scorer - 1)
		if self.players[scorer] > 3:
			self.players[scorer] = 3
			if self.players[opponent] < 3:
				self.winner = scorer
			else:
				self.winner = -1
				if self.advantage == opponent:
					self.advantage = -1
				elif self.advantage == scorer:
					self.winner = scorer
				else:
					self.advantage = scorer
				
	def current_score(self, index):
		return Tennis.scores[self.players[index]]