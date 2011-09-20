class Tennis:

	scores = [0, 15, 30, 40]
	
	def __init__(self):
		self.players = [0,0]
		self.winner = -1
		self.advantage = -1
		
	def handle_advantage_for_scorer(self, scorer):
		opponent = abs(scorer -1)
		self.winner = -1
		if self.advantage == opponent:
			self.advantage = -1
		elif self.advantage == scorer:
			self.winner = scorer
		else:
			self.advantage = scorer

	def player_score_ready_to_win(self, player):
		return self.players[player] > 3
	
	def player_score_under_win_threshold(self, player):
		return self.players[player] < 3
		
	def handle_player_ready_to_win(self, player):
		opponent = abs(player - 1)
		if self.player_score_ready_to_win(player):
			self.players[player] = 3
			if self.player_score_under_win_threshold(opponent):
				self.winner = player
			else:
				self.handle_advantage_for_scorer(player)
		
	def score_point(self, scorer):
		self.players[scorer] += 1
		self.handle_player_ready_to_win(scorer)
				
	def current_score(self, index):
		return Tennis.scores[self.players[index]]