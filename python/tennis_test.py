import tennis

class TestTennis:
	def setup_method(self, method):
		self.tennis = tennis.Tennis()
		
	def test_scores(self):
		assert self.tennis.scores == [0, 15, 30, 40]
		
		
	def test_game_has_two_players(self):
		assert len(self.tennis.players) == 2
