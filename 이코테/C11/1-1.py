import heapq

n = int(input())
advs = list(map(int, input().split()))
advs.sort()

count = 0
while advs:
  m = []
  m.append(advs.pop(0))
  while max(m) != len(m) and advs:
    m.append(advs.pop(0))
  if max(m) == len(m):
    count += 1
  
print(count)