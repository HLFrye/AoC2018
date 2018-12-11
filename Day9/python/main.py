import re

class GameDefinition:
  def __init__(self, defstring):
    # 477 players; last marble is worth 70851 points
    m = re.match(r"(?P<numPlayers>\d+) players; last marble is worth (?P<last>\d+) points", defstring)
    self.players = [0] * int(m.group('numPlayers'))
    self.last_marble = int(m.group('last'))
    self.marbles = [0]
    self.current_marble = 0
    self.next_marble = 1

  def place_next_marble(self):
    if self.next_marble % 23 != 0:      
      next_marble = (self.current_marble + 1) % len(self.marbles)
      pos = next_marble + 1
      self.marbles.insert(pos, self.next_marble)
      self.next_marble = self.next_marble + 1
      self.current_marble = pos
      return 0
    else:
      score = self.next_marble
      remove_marble_pos = self.current_marble - 7
      if remove_marble_pos < 0:
        remove_marble_pos = remove_marble_pos + len(self.marbles)
      remove_marble_pos = remove_marble_pos % len(self.marbles)
      score = score + self.marbles.pop(remove_marble_pos)
      self.current_marble = remove_marble_pos
      self.next_marble = self.next_marble + 1
      return score

  def run_game(self):
    curr_player = 0
    while self.next_marble <= self.last_marble:
      player_score = self.place_next_marble()
      self.players[curr_player] = self.players[curr_player] + player_score
      curr_player = (curr_player + 1) % len(self.players)

  def high_score(self):
    max_score = 0
    for player in self.players:
      if player > max_score:
        max_score = player
    return max_score

def main():
  with open("../input.txt") as input:
    game = GameDefinition(input.readline())

  game.run_game()
  print("The high score is {}".format(game.high_score()))

if __name__ == '__main__':
  main()