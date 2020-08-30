from collections import deque

# x, y
n, m = map(int, input().split())

graph = []
for i in range(m):
  graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()

for i in range(len(graph)):
  for j in range(len(graph[0])):
    if graph[i][j] == 1:
      queue.append((j,i))

while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
      continue
    if graph[ny][nx] == -1:
      continue
    if graph[ny][nx] == 0:
      graph[ny][nx] = graph[y][x] + 1
      queue.append((nx, ny))

answer = 0
for row in graph:
  if max(row) > answer:
    answer = max(row)
  if row.count(0) > 0:
    answer = 0
    break

print(answer-1)
