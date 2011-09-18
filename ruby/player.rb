POSSIBLE_SCORES = [0, 15, 30, 40]

class Player
  attr_accessor :current_score_index
  attr_accessor :scored_winning_point
  attr_accessor :advantage
  
  def initialize
    @current_score_index = 0
    @scored_winning_point = false
    @advantage = false
  end
  
  def score
    POSSIBLE_SCORES[@current_score_index]
  end
  
  def score_point 
    @current_score_index += 1
    if current_score_index > POSSIBLE_SCORES.size - 1
      if current_score_index == 4
        @scored_winning_point = true
      end
      @current_score_index = POSSIBLE_SCORES.size - 1 
    end
  end
end