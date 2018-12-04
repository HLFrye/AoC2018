import re

def translate(line):
  m = re.match(r'#(?P<id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<width>\d+)x(?P<height>\d+)', line)
  return {
    'id': int(m.group('id')),
    'x': int(m.group('x')),
    'y': int(m.group('y')),
    'width': int(m.group('width')),
    'height': int(m.group('height'))
  }

def input_items(filename):
  with open(filename) as input:
    for line in input.readlines():
      yield translate(line.strip())

def render(grid, item):
  for y in range(item['y'], item['y'] + item['height']):
    for x in range(item['x'], item['x'] + item['width']):
      if grid[y][x] == 0:
        grid[y][x] = item['id']
      else:
        grid[y][x] = -1

def is_overlap(space):
  return space == -1

def main():
  items = []
  max_x = 0
  max_y = 0
  for item in input_items("../input.txt"):
    items.append(item)
    max_x = max(max_x, item['x'] + item['width'])
    max_y = max(max_y, item['y'] + item['height'])

  grid = [[0] * max_x for i in range(max_y)]
  for item in items:
    render(grid, item)

  overlap_count = 0
  for line in grid:
    for space in line:
      if is_overlap(space):
        overlap_count = overlap_count + 1

  print("Overlap is {}".format(overlap_count))

if __name__ == '__main__':
  main()