def distance(pt1, pt2):
  return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

def find_closest(pt, coords):
  closest_coord = None
  closest_coord_dist = 100000000
  for coord in coords:
    dist = distance(pt, coord)
    if dist < closest_coord_dist:
      closest_coord = coord
      closest_coord_dist = dist
      continue
    if dist == closest_coord_dist:
      closest_coord = None
  return closest_coord

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

  grid = [[0] * size[0] for i in range(size[1])]

  coord_area = {}
  infinite_coords = set()

  for y, line in enumerate(grid):
    for x, _ in enumerate(line):
      closest = find_closest((x,y), coords)
      if closest is not None:
        if closest in coord_area:
          coord_area[closest] = coord_area[closest] + 1
        else:
          coord_area[closest] = 1
        if x == 0 or y == 0 or x == size[0] - 1 or y == size[1] - 1:
          infinite_coords.add(closest)

  print("There are {} input coords, and {} are infinite".format(len(coords), len(infinite_coords)))

  max_size = 0
  for key, value in coord_area.items():
    if key not in infinite_coords:
      if value > max_size:
        max_size = value
    
  print("The largest area is: {}".format(max_size))

if __name__ == '__main__':
  main()