import re
import sys

class Light:
  def __init__(self, defstring):
    m = re.match(r"position=<\s*(?P<x>-?\d+),\s*(?P<y>-?\d+)> velocity=<\s*(?P<dx>-?\d+),\s*(?P<dy>-?\d+)>", defstring)
    self.x = int(m.group('x'))
    self.y = int(m.group('y'))
    self.dx = int(m.group('dx'))
    self.dy = int(m.group('dy'))

  def move_next(self):
    self.x = self.x + self.dx
    self.y = self.y + self.dy

def get_bounds(lights):
  min_x = sys.maxsize
  min_y = sys.maxsize
  max_x = 0
  max_y = 0
  for light in lights:
    if light.x < min_x:
      min_x = light.x
    if light.y < min_y:
      min_y = light.y
    if light.x > max_x:
      max_x = light.x
    if light.y > max_y:
      max_y = light.y
  return min_x, min_y, max_x, max_y

def expand_bounds(amount, bounds):
  min_x, min_y, max_x, max_y = bounds
  return min_x - amount, min_y - amount, max_x + amount, max_y + amount

def render(lights):
  min_x, min_y, max_x, max_y = expand_bounds(3, get_bounds(lights))
  grid = [[0] * (max_x - min_x) for i in range(max_y - min_y)]
  for light in lights:
    view_y = light.y - min_y
    view_x = light.x - min_x
    grid[view_y][view_x] = 1

  return grid

def main():
  with open("../sample.txt") as input:
    lights = [Light(x) for x in input.readlines()]

  for s in range(0, 3):
    for light in lights:
      light.move_next()

  grid = render(lights)
  for row in grid:
    print(row)


if __name__ == "__main__":
  main()