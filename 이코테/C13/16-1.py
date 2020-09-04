from itertools import combinations
from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

vacants = []
viruses = []

for y in range(n):
  for x in range(m):
    if graph[y][x] == 0:
      vacants.append((x, y))
    elif graph[y][x] == 2:
      viruses.append((x, y))

g_copy = []
max_val = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for walls in combinations(vacants, 3):
  queue = deque(viruses)
  g_copy = deepcopy(graph)
  for wall in walls:
    x, y = wall
    g_copy[y][x] = 1
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= m or ny >= n:
        continue
      elif g_copy[ny][nx] == 0:
        g_copy[ny][nx] = 2
        queue.append((nx, ny))
  z_count = 0
  for row in g_copy:
    z_count += row.count(0)
  max_val = max(max_val, z_count)

print(max_val)