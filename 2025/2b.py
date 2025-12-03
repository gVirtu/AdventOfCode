from collections import deque
import bisect

count = 0

LIMIT = 10 ** 12
SQRT_LIMIT = 10 ** 6
invalid_id_set = set()

def generate_ids_from(num: int):
  i = 2

  while True:
    candidate = int(str(num)*i)
    if candidate > LIMIT:
      break
    # print(f'{candidate} was added')
    invalid_id_set.add(candidate)
    i += 1

def generate_id_set():
  queue = deque()

  for i in range(1, 10):
    queue.append(i)
    
  while len(queue):
    current = queue.popleft()
    # print(f'processing {current}...')
    generate_ids_from(current)
    
    for i in range(10):
      nxt = int(str(current) + str(i))
      if (nxt < SQRT_LIMIT):
        queue.append(nxt)

line = input()
range_strings = line.split(',')

generate_id_set()

invalid_ids = sorted(invalid_id_set)

for range_string in range_strings:
  [st, en] = range_string.split('-')
  
  start_index = bisect.bisect_left(invalid_ids, int(st))
  start = invalid_ids[start_index]
  
  end_index = bisect.bisect_right(invalid_ids, int(en))
  end = invalid_ids[end_index]
  
  incr = sum(invalid_ids[start_index:end_index])
  
  # print({'start_index': start_index, 'end_index': end_index, 'start': start, 'end': end, 'incr': incr})
  
  count += incr

print(count)
