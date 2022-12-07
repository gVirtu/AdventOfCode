from collections import defaultdict

signal = input()
unique = defaultdict(int)
capacity = 14

for i in range(len(signal)):
  unique[signal[i]] += 1

  if i >= capacity:
    to_remove = signal[i - capacity]
    unique[to_remove] -= 1

    if unique[to_remove] == 0:
      del unique[to_remove]

  if len(unique.keys()) == capacity:
    print(i + 1)
    break
