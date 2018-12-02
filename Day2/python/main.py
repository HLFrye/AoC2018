def differences(id1, id2):
  diff_count = 0
  for idx, val in enumerate(id1.strip()):
    if id1[idx] != id2[idx]:
      diff_count = diff_count + 1
  return diff_count

def find_correct_box(lines):
  for id1 in lines:
    for id2 in lines:
      if differences(id1, id2) == 1:
        return id1, id2  

def find_same_letters(id1, id2):
  output = ""
  for idx, val in enumerate(id1.strip()):
    if id1[idx] == id2[idx]:
      output = output + id1[idx]
  return output

def main():
  with open("./input.txt") as input:
    lines = input.readlines()
    id1, id2 = find_correct_box(lines)
    print(find_same_letters(id1, id2))


if __name__ == '__main__':
  main()