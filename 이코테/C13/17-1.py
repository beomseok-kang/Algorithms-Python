import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(lambda x: [int(x), 0], input().split())))

s, tx, ty = map(int, input().split()) # target x, target y

times = [[] for _ in range(s + 1)]

for i in range(n): # x axis
  for j in range(n): # y axis
    if graph[i][j][0] > 0:
      times[0].append((graph[i][j][0], i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
t = 0

while t < s:
  times[t].sort(reverse=True)
  while times[t]:
    val, x, y = times[t].pop()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue
      if graph[nx][ny][0] == 0:
        graph[nx][ny] = [val, t+1]
        times[t+1].append((val, nx, ny))
      elif graph[nx][ny][0] > val and graph[nx][ny][1] == t + 1:
        graph[nx][ny] = [val, t+1]
        times[t+1].append((val, nx, ny))
  t += 1

print(graph[tx-1][ty-1][0])
