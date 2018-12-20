from functools import reduce

def convert_input(value):
  return 1 if value == '#' else 0

class GameState:
  def __init__(self, pots_set):
    self.active_pots = pots_set

  def plant_in(self, pos):
    return 1 if pos in self.active_pots else 0

  def value_at(self, pos):
    value = 0
    for x in range(pos - 2, pos + 3):
      value = (value << 1) | self.plant_in(x)
    return value

  def update(self, rules):
    check_set = set()
    for pos in self.active_pots:
      for possible_pos in range(pos - 2, pos + 3):
        check_set.add(possible_pos)

    new_set = set()
    for pos in check_set:
      if rules.rules[self.value_at(pos)] == 1:
        new_set.add(pos)
    self.active_pots = new_set

  def get_code(self):
    return sum(self.active_pots)

class Rules:
  def __init__(self, lines):
    self.rules = [0] * 32
    for line in lines:
      pattern = line[0:5]
      result = line[9:10]
      idx = reduce(lambda x, y: (x << 1) | y, map(convert_input, pattern))
      self.rules[idx] = convert_input(result)

  def print(self):
    for k,v in enumerate(self.rules):
      print("Rule {} = {}".format(k,v))

def read_initial_state(input):
  initial_state = input[15:]
  active_pots = set()
  for idx, char in enumerate(initial_state.strip()):
    if char == '#':
      active_pots.add(idx)
  return active_pots

def main():
  with open("../input.txt") as input:
    state = GameState(read_initial_state(input.readline()))
    input.readline()
    rules = Rules(input.readlines())

  for iteration in range(0, 100000):
    state.update(rules)

  remaining = 50000000000 - 100000
  result = sum(map(lambda x: x + remaining, state.active_pots))

  # for iteration in range(0, 50000000000):
  #   if iteration % 100000 == 0:
  #     print("Processing iteration {}, count = {}".format(iteration, len(state.active_pots)))
  #   state.update(rules)

  print("Result: {}".format(result))    

if __name__ == "__main__":
  main()