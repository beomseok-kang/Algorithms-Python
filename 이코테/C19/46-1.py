import heapq
from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)
shark = None
n = int(input())
graph = []
for i in range(n):
  row = list(map(int, input().split()))
  graph.append(row)
  try:
    shark = (i, row.index(9))
  except:
    continue

size = 2
t = 0
ate = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, pq, dist_graph, dist):
  if 0 < graph[x][y] < size:
    heapq.heappush(pq, (dist, x, y))
    return
  elif pq and pq[0][0] < dist:
    return
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= n or ny >= n or nx < 0 or ny < 0:
      continue
    elif dist_graph[nx][ny] <= dist + 1:
      continue
    elif graph[nx][ny] > size:
      continue
    else:
      dist_graph[nx][ny] = dist + 1
      dfs(nx, ny, pq, dist_graph, dist + 1)

# def bfs(x, y, pq, dist_graph):
#   q = deque([(x, y)])
#   while q:
#     x, y = q.popleft()
#     if pq and pq[0][0] < dist_graph[x][y]:
#       continue
#     if 0 < graph[x][y] < size:
#       heapq.heappush(pq, (dist_graph[x][y], x, y))
#       continue
#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]
#       if nx >= n or ny >= n or nx < 0 or ny < 0:
#         continue
#       elif dist_graph[nx][ny] <= dist_graph[x][y] + 1:
#         continue
#       elif graph[nx][ny] > size:
#         continue
#       else:
#         dist_graph[nx][ny] = dist_graph[x][y] + 1
#         q.append((nx, ny))

while True:
  if ate == size:
    size += 1
    ate = 0
  
  pq = []
  x, y = shark
  dist_graph = [[INF] * n for _ in range(n)]
  dist_graph[x][y] = 0

  # bfs(x, y, pq, dist_graph)
  dfs(x, y, pq, dist_graph, 0)

  if pq:
    # original shark position (make it 0)
    graph[x][y] = 0
    # next shark position
    dist, x, y = pq[0]
    t += dist
    ate += 1
    shark = (x, y)
    graph[x][y] = INF
  else:
    break

print(t)