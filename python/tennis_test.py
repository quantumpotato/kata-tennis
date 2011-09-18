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
		assert self.tennis.score(0) == 15