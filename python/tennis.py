import player

class Tennis:

	scores = [0, 15, 30, 40]
	
	def __init__(self):
		self.players = [0,0]
		
	def score_point(self, scorer):
		self.players[scorer] += 1
				
	def score(self, index):
		return Tennis.scores[self.players[index]]