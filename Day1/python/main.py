def freq_seq(filename):
  with open(filename) as input:
    inputs = input.readlines()
    line = 0
    while True:
      yield inputs[line]
      line = (line + 1) % len(inputs)

def main():
  freq = 0
  seen_freqs = set([0])
  for line in freq_seq("./input.txt"):
    freq = freq + int(line)

    if freq in seen_freqs:
      print("The target frequency is: {}".format(freq))
      return
    seen_freqs.add(freq)

if __name__ == "__main__":
  main()