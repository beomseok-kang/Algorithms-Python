import heapq

n = int(input())

uglies = {1}
h = [1]

while len(uglies) < n:
  a = heapq.heappop(h)
  uglies.add(a)
  for i in [2, 3, 5]:
    heapq.heappush(h, a * i)

res = sorted(uglies)
print(res)
print(res[n-1])