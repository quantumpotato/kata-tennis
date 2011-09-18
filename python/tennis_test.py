import tennis

class TestTennis:
	def setup_method(self, method):
		self.scores = [0, 15, 30, 40]
		
	def test_scores(self):
		assert self.scores == [0, 15, 30, 40]