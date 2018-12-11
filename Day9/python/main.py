import re

class Marble:
  def __init__(self, value):
    self.value = value
    self.next = self
    self.prev = self

  def add_before(self, newprev):
    newprev.prev = self.prev
    newprev.next = self

    self.prev.next = newprev
    self.prev = newprev
  
  def remove(self):
    self.prev.next = self.next
    self.next.prev = self.prev

class GameDefinition:
  def __init__(self, defstring):
    # 477 players; last marble is worth 70851 points
    m = re.match(r"(?P<numPlayers>\d+) players; last marble is worth (?P<last>\d+) points", defstring)
    self.players = [0] * int(m.group('numPlayers'))
    self.last_marble = 100 * int(m.group('last'))
    self.current_marble = Marble(0)
    self.next_marble_value = 1

  def place_next_marble(self):
    if self.next_marble_value % 23 != 0:      
      new_marble = Marble(self.next_marble_value)
      self.current_marble.next.next.add_before(new_marble)
      self.next_marble_value = self.next_marble_value + 1
      self.current_marble = new_marble
      return 0
    else:
      score = self.next_marble_value
      for x in range(0, 7):
        self.current_marble = self.current_marble.prev

      score = score + self.current_marble.value
      self.current_marble.remove()
      self.current_marble = self.current_marble.next
      self.next_marble_value = self.next_marble_value + 1
      return score

  def run_game(self):
    curr_player = 0
    while self.next_marble_value <= self.last_marble:
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