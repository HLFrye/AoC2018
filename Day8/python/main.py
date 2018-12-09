def get_meta_sum(input_items):
  num_children = input_items[0]
  num_meta = input_items[1]
  total_read = 2

  child_amounts = []

  for child in range(0, num_children):
    child_sum, child_num_read = get_meta_sum(input_items[total_read::])
    child_amounts.append(child_sum)
    total_read = total_read + child_num_read
  meta_start = input_items[total_read::]

  total = 0
  for meta in range(0, num_meta):
    meta_value = meta_start[meta]
    if num_children == 0:
      total = total + meta_value
    else:
      if (meta_value - 1) < len(child_amounts):
        total = total + child_amounts[meta_value - 1]
    total_read = total_read + 1

  return total, total_read

def main():
  with open("../input.txt") as input:
    buf = list(map(lambda x: int(x), input.read().split()))
  
  total, num_read = get_meta_sum(buf)

  print(total)


if __name__ == "__main__":
  main()