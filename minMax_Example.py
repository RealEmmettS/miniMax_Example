import math

#this program assumes a game has been made already. This is simply a basic AI to go along with the currently existing game

class MinMax():

  #gamestate is an object of a class/struct with property playerTurn and property move
  #playerTurn -> who's turn isinstance
  #move -> what move will be played

  def __init__(self, player = 1, gamestate): #initial method
    m = math
    self.reward = -m.inf
    self.player = player
    self.gamestate = gamestate
    self.children = {}
    self.construct() #constructs children until construct method terminates

  def add(self, move, newGameState):
    self.children[move] = MinMax(move, newGameState)
  
  def construct(self): #construct miniMax tree
    if(gamestate.terminal()):
      self.reward = self.gameState.reward()
    else:
      maxCurrReward = 0
      for move in gamestate.getMoves():
        self.add(move, copy.deepcopy(gameState.makeMove(move))) #runs until loop terminates
        maxCurrReward = max(reward, self.children[move].reward)
      self.reward = - maxCurrReward
