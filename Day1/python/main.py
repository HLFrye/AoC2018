def freq_seq(filename):
  with open(filename) as input:
    inputs = input.readlines()
    line = 0
    while True:
      yield inputs[line]
      line = (line + 1) % len(inputs)

def main():
  freq = 0
  seen_freqs = {
    "0": 1
  }
  for line in freq_seq("./input.txt"):
    if line[0] == '+':
      freq = freq + int(line[1::])
    else:
      freq = freq - int(line[1::])
    freq_str = str(freq)
    if freq_str in seen_freqs:
      print("The target frequency is: {}".format(freq))
      return
    seen_freqs[freq_str] = 1

if __name__ == "__main__":
  main()