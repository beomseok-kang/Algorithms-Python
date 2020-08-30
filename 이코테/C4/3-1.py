n, m = map(int, input().split())
x, y, d = map(int, input().split())
mp = []
for i in range(n):
  mp.append(list(map(int, input().split())))

visited = []
for i in range(n):
  visited.append([0]*m)
visited[y][x] = 1

print(visited)

move = [(0,-1), (1,0), (0,1), (-1,0)]

count = 0
while True:
  d += 1
  d = (d + 4) % 4
  x_new = x + move[d][0]
  y_new = y + move[d][1]
  count += 1
  if count == 4:
    d += 2
    d = (d + 4) % 4
    x = x + move[d][0]
    y = y + move[d][1]
    if mp[y][x] == 1:
      break
  if x_new < 0 or x_new >= m or y_new < 0 or y_new >= n: # 맵 밖으로 벗어날 시
    continue
  elif mp[y_new][x_new] == 1 or visited[y_new][x_new] >= 1:
    continue
  else:
    x, y = x_new, y_new
    visited[y][x] += 1

print(visited)

result = 0
for i in range(len(visited)):
  for j in visited[i]:
    if j != 0:
      result += 1

print(result)