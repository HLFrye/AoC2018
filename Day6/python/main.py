def distance(pt1, pt2):
  return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])


def main():
  coords = []
  size = 0,0
  with open("../input.txt") as input:
    for line in input.readlines():
      parts = line.split(',')
      input_coord = int(parts[0]), int(parts[1])
      if input_coord[0] > size[0]:
        size = input_coord[0], size[1]
      if input_coord[1] > size[1]:
        size = size[0], input_coord[1]

      coords.append((int(parts[0]), int(parts[1])))

  safe_spaces = 0

  for x in range(0, size[0]):
    for y in range(0, size[1]):
      total_dist = 0
      for coord in coords:
        total_dist = total_dist + distance((x, y), coord)
      if total_dist < 10000:
        safe_spaces = safe_spaces + 1

  print("The safe area is: {}".format(safe_spaces))

if __name__ == '__main__':
  main()