from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if graph[i][j] != 0:
      data.append((graph[i][j], 0, i, j))

# sort를 하고 나면 어차피 작은 값들이 앞으로 오게 되므로, 자연적으로 이 작은 값들이
# 먼저 처리가 되어 후에 탐색을 할 때 값을 비교할 필요가 없어진다. 그래프의 해당 좌표에
# 바이러스가 있는지 없는지만 처리를 하면 된다.

data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while q:
  virus, s, x, y = q.popleft()
  if s == target_s:
    break
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx and nx < n and 0 <= ny and ny < n:
      if graph[nx][ny] == 0:
        graph[nx][ny] = virus
        q.append((virus, s + 1, nx, ny))

print(graph[target_x-1][target_y-1])