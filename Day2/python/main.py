def has_repeat(repeat_count, line):
  components = {}
  for char in line:
    if char in components:
      components[char] = components[char] + 1
    else:
      components[char] = 1
  for key,value in components.items():
    if value == repeat_count:
      return True
  return False

def has_two_repeat(line):
  return has_repeat(2, line)

def has_three_repeat(line):
  return has_repeat(3, line)

def main():
  two_count = 0
  three_count = 0
  with open("./input.txt") as input:
    for line in input.readlines():
      if has_two_repeat(line):
        two_count = two_count + 1
      if has_three_repeat(line):
        three_count = three_count + 1
  print("Checksum calculated: {}".format(two_count * three_count))


if __name__ == '__main__':
  main()