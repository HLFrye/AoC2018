import re
import sys
from PIL import Image
import numpy as np
import pytesseract

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

  if min_x < 0 and min_y < 0:
    return None
  # size = (max_y - min_y) * (max_x - min_x)
  # print("({}): {}, {} to {}, {}".format(size, min_x, min_y, max_x, max_y))
  grid = np.zeros(shape=(max_y - min_y, max_x - min_x), dtype=np.int16)
  for light in lights:
    view_y = light.y - min_y
    view_x = light.x - min_x
    grid[view_y][view_x] = 255
  return grid

def main():
  with open("../input.txt") as input:
    lights = [Light(x) for x in input.readlines()]

  for attempt in range(0, 20000):
    # print("Processing attempt {}".format(attempt))
    for light in lights:
      light.move_next()  
    grid = render(lights)
    if grid is None:
      continue
    im = Image.fromarray(grid)
    im = im.convert('RGB')
    im.save("./attempt-{}.bmp".format(attempt), "BMP")
    msg = pytesseract.image_to_string(im, config='-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 -psm 6', lang='eng')
    if msg != "":
      break

  print(msg)

if __name__ == "__main__":
  main()