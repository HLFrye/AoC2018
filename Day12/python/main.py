from functools import reduce

padding = 2

def convert_input(x):
  return 1 if x == "#" else 0

def convert_output(x):
  return '#' if x == 1 else '.'

class GameState:
  def __init__(self, initial_state, state_start):
    self.min = state_start
    self.max = len(initial_state) + state_start
    self.data = initial_state

  def get_min(self):
    return self.min - padding

  def get_range(self):
    return range(self.get_min(), self.max + padding)

  def get(self, pos):
    if pos < self.min or pos >= self.max:
      return 0
    return self.data[pos - self.min]

  def get_pos_value(self, pos):
    return reduce(lambda x, y: (x << 1) | y, map(self.get, range(pos - 2, pos + 3)))

  def print(self):
    state_graph = ''.join([convert_output(self.get(x)) for x in range(-15, 120)])
    print("[{}]".format(state_graph))

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
  initial_state = initial_state.strip()
  initial_state = map(convert_input, initial_state)
  return list(initial_state)

def update(state, rules):
  curr = 0
  updated = [0] * (len(state.data) + 4)
  pt = 0
  for point in state.data:
    curr = (curr << 1 | point) & 31 
    updated[pt] = rules.rules[curr]
    pt = pt + 1

  for i in range(0,4):
    updated[pt+i] = rules.rules[(curr << (1 + i)) & 31]

  start_at = state.get_min()
  new_state = [rules.rules[state.get_pos_value(x)] for x in state.get_range()]
  return GameState(updated, start_at)

def plant_indexes(state):
  return filter(lambda x: state.get(x) == 1, state.get_range())

def main():
  with open("../input.txt") as input:
    initial_state = GameState(read_initial_state(input.readline()), 0)
    input.readline()
    rules = Rules(input.readlines())

  state = initial_state
  for iteration in range(0, 20):
    state = update(state, rules)

  result = sum(plant_indexes(state))

  print("Result: {}".format(result))    


if __name__ == "__main__":
  main()