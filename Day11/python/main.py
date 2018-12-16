def get_hundreds(num):
  total_hundreds = num / 100
  return int(total_hundreds % 10)

def populate_grid(input):
  def calc_fuel_level(x, y):
    rack_id = x + 10
    power_level = rack_id * y
    power_level = power_level + input
    power_level = power_level * rack_id
    power_level = get_hundreds(power_level)
    return power_level - 5

  grid = [[0] * 300 for i in range(300)]
  for x in range(0, 300):
    for y in range(0, 300):
      grid[y][x] = calc_fuel_level(x, y)

  return grid

def get_subgrid_total(grid, x, y, size):
  total = 0
  for dx in range(0, size):
    for dy in range(0, size):
      total = total + grid[y+dy][x+dx] 
  return total

def calculate(input, size):
  grid = populate_grid(input)

  max_fuel_level = 0
  max_point = None
  for x in range(0, 300 - size):
    for y in range(0, 300 - size):
      level = get_subgrid_total(grid, x, y, size)
      if level > max_fuel_level:
        max_fuel_level = level
        max_point = x,y

  return max_point, max_fuel_level

def print_power_level(input, x, y):
  grid = populate_grid(input)
  return grid[y][x]

def main():
  with open("../input.txt") as input:
    serial_no = int(input.readline())

  best = (0, 0), 0
  best_size = 0
  for size in range(0, 301):
    result = calculate(serial_no, size)
    print("Attempt {}, Result {}".format(size, result))
    if result[1] > best[1]:
      best = result
      best_size = size
  print("Result: {}".format((best,size)))

if __name__ == "__main__":
  main()