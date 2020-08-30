import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# number of city(node) n, number of edge m, starting city c (start)
n, m, c = map(int, input().split())

graph = [[] for i in range(n + 1)]

# initialization
time = [INF] * (n + 1)

for _ in range(m):
  # from city x to city y, cost(time) is z
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

def dijkstra_improved(start):
  q = []
  # time, start
  heapq.heappush(q, (0, start))
  time[start] = 0
  while q:
    # shortest time taking node
    t, now = heapq.heappop(q)
    # if calculations already done, continue
    if time[now] < t:
      continue
    # check other adjacent nodes
    for edge in graph[now]:
      # Check line 19: edge[1] = time taken
      cost = t + edge[1]
      # If the new cost lower than the recorded one, update and push new info
      if cost < time[edge[0]]:
        time[edge[0]] = cost
        heapq.heappush(q, (cost, edge[0]))

dijkstra_improved(c)
count = -1 # disinclude the city itself (where time is 0)
for i in range(1, n + 1):
  if time[i] != INF:
    count += 1

print('{0} {1}'.format(count, max(t for t in time if t != INF)))