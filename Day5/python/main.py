def item_and_next(iterable):
  # Get an iterator and pull the first value.
  it = iter(iterable)
  last = next(it)
  # Run the iterator to exhaustion (starting from the second value).
  for val in it:
    # Report the *previous* value (more to come).
    yield last, val
    last = val
  # Report the last value.
  yield last, None


def reduce_polymer(input):
  output = ""
  skip_next = False
  for item, next_item in item_and_next(input):
    if next_item is None:
      if skip_next:
        break
      output = output + item
      break
    if skip_next:
      skip_next = False
      continue
    if abs(ord(item) - ord(next_item)) == 32:
      skip_next = True
      continue
    output = output + item
  return output, len(output)

def fully_reduce_polymer(polymer):
  last_len = len(polymer)
  iterations = 0
  while True:
    polymer, new_len = reduce_polymer(polymer)
    if last_len == new_len:
      break
    last_len = new_len
    iterations = iterations + 1
  return len(polymer)

def main():
  with open("../input.txt") as input:
    polymer = input.readline()
    shortest = len(polymer)
    for unit in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
      print("Checking {}".format(unit))
      check_polymer = polymer.replace(unit, "").replace(chr(ord(unit) + 32), "")
      check_len = fully_reduce_polymer(check_polymer)
      if check_len < shortest:
        shortest = check_len
    print("The shortest was {}".format(shortest))


if __name__ == '__main__':
  main()