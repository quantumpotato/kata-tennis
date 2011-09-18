require File.join(File.dirname(__FILE__),'../tennis')
require File.join(File.dirname(__FILE__),'../game')
require File.join(File.dirname(__FILE__),'../player')

describe 'Tennis' do
  before :each do
    @game = Game.new
    @player = Player.new
  end
  
  it "should have a score" do
    @player.should_not be_nil
  end
  
  it "should have a limited range of scores" do
    POSSIBLE_SCORES.should eql([0, 15, 30, 40])
  end
  
  it "should have a game" do
    @game.should_not be_nil
  end
  
  it "should have players" do
    @game.players.should_not be_nil
  end
  
   it "game should have a game with two players" do
     @game.players.size.should eql(2)
   end
   
   it "should allow players to score points and change score from 0 to 15" do
     @game.score_point(0)
     @game.players[0].score.should eql(15)
   end
   
   it "should allow a player to win if they score at 40" do
     4.times do
       @game.score_point(0)
     end
     
     @game.winner.should eql(@game.players[0])  
   end
   
   it "should not win if players are tied at 40" do
     3.times do
       @game.score_point(0)
       @game.score_point(1)
     end
     
     @game.score_point(0)
       
     @game.winner.should be_nil
   end
   
   it "should give a player the advantage for scoring when tied at 40" do
     3.times do
       @game.score_point(0)
       @game.score_point(1)
     end
     
     @game.score_point(0)
     
     @game.players[0].advantage.should be_true
   end
   
   it "should allow the player to win if the player scores with the advantage" do
     3.times do
       @game.score_point(0)
       @game.score_point(1)
     end
     
     2.times do
       @game.score_point(0)
     end
     
     @game.winner.should eql(@game.players[0])
   end
   
   it "should reset the advantage when the disadvantaged player scores at 40" do
     4.times do
       @game.score_point(0)
       @game.score_point(1)
     end
     
     @game.players[0].advantage.should be_false
     @game.players[1].advantage.should be_false
    end     
    
    it "should play through a game" do
      4.times do
        @game.score_point(0)
        @game.score_point(1)
      end
      
      2.times do
        @game.score_point(0)
      end
      
      @game.winner.should eql(@game.players[0])
    end
end