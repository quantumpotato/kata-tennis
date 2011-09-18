require File.join(File.dirname(__FILE__),'/player')

class Game
  attr_accessor :players
  attr_reader :winner
  
  def initialize
    @players = [Player.new, Player.new]
    @winner = nil
  end
  
  def score_point(player_index)
    player = @players[player_index]
    player.score_point
    
    if player.scored_winning_point
      other_player_index = (player_index - 1).abs
      opponent = @players[other_player_index]
      
      if opponent.current_score_index < 3 || player.advantage
        @winner = player
      else 
        player.scored_winning_point = false
        if !opponent.advantage
          player.advantage = true
        else
          opponent.advantage = false
        end
      end
      
    end
  end

  
end