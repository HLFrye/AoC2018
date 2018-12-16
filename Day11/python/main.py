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

def get_subgrid_total(grid, x, y):
  return grid[y][x] + grid[y][x+1] + grid[y][x+2] + grid[y+1][x] + grid[y+1][x+1] + grid[y+1][x+2] + grid[y+2][x] + grid[y+2][x+1] + grid[y+2][x+2]

def calculate(input):
  grid = populate_grid(input)

  max_fuel_level = 0
  max_point = None
  for x in range(0, 297):
    for y in range(0, 297):
      level = get_subgrid_total(grid, x, y)
      if level > max_fuel_level:
        max_fuel_level = level
        max_point = x,y

  return max_point

def print_power_level(input, x, y):
  grid = populate_grid(input)
  return grid[y][x]

def main():
  with open("../input.txt") as input:
    serial_no = int(input.readline())
    
  print("Result: {}".format(calculate(serial_no)))

if __name__ == "__main__":
  main()