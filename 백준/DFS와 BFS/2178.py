from collections import deque

n, m = map(int, input().split())

mp = []
for i in range(n):
  mp.append(list(map(int, input())))

queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

x, y = 0, 0
queue.append((x, y))

while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 지도에서 벗어난 경우 무시
    if nx < 0 or ny < 0 or nx >= m or ny >= n:
      continue
    # 벽일 경우 무시
    if mp[ny][nx] == 0 :
      continue
    # 처음 방문한 경우 (값이 1) 에만 새로운 값 입력
    if mp[ny][nx] == 1:
      mp[ny][nx] = mp[y][x] + 1
      queue.append((nx, ny))

print(mp[n-1][m-1])