import tennis

class TestTennis:
	def setup_method(self, method):
		self.tennis = tennis.Tennis()
		
	def test_scores(self):
		assert self.tennis.scores == [0, 15, 30, 40]
		
		
	def test_game_has_two_players(self):
		assert len(self.tennis.players) == 2

	def test_players_start_with_0_points(self):
		assert self.tennis.players[0] == 0
		assert self.tennis.players[1] == 0
		
	def test_player_can_score_from_0_to_15_points(self):
		self.tennis.score_point(0)
		assert self.tennis.current_score(0) == 15
		
	def test_player_can_win_after_scoring_4_times(self):
		self.tennis.score_point(0)
		self.tennis.score_point(0)
		self.tennis.score_point(0)
		self.tennis.score_point(0)						
			
		assert self.tennis.winner == 0
	
	def test_player_cannot_win_when_tied_at_40(self):
		self.tennis.score_point(0)
		self.tennis.score_point(0)
		self.tennis.score_point(0)
		self.tennis.score_point(1)
		self.tennis.score_point(1)
		self.tennis.score_point(1)
		self.tennis.score_point(0)
		
		assert self.tennis.winner == -1
		
	def test_player_can_gain_advantage_when_scoring_at_tied_40(self):
		self.tennis.score_point(0)
		self.tennis.score_point(0)
		self.tennis.score_point(0)
		self.tennis.score_point(1)
		self.tennis.score_point(1)
		self.tennis.score_point(1)
		self.tennis.score_point(0)
		
		assert self.tennis.advantage == 0
		
	def test_player_can_lose_advantage_when_opponent_scores(self):
		self.tennis.score_point(0)
		self.tennis.score_point(0)
		self.tennis.score_point(0)
		self.tennis.score_point(1)
		self.tennis.score_point(1)
		self.tennis.score_point(1)
		self.tennis.score_point(0)
		self.tennis.score_point(1)
		
		assert self.tennis.advantage == -1
		
	def test_player_can_win_with_advantage(self):
		self.tennis.score_point(0)
		self.tennis.score_point(0)
		self.tennis.score_point(0)
		self.tennis.score_point(1)
		self.tennis.score_point(1)
		self.tennis.score_point(1)
		self.tennis.score_point(0)
		self.tennis.score_point(0)
		
		assert self.tennis.winner == 0
		
	def test_example_game(self):
		self.tennis.score_point(0)
		self.tennis.score_point(0)
		self.tennis.score_point(0)
		self.tennis.score_point(1)
		self.tennis.score_point(1)
		self.tennis.score_point(1)
		self.tennis.score_point(0)
		self.tennis.score_point(1)
		self.tennis.score_point(0)
		assert self.tennis.winner == -1
		self.tennis.score_point(0)
		assert self.tennis.winner == 0