n, m = map(int, input().split())

graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

dp = [[0] * m for _ in range(n)]
dp[0][0] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for y in range(n):
  for x in range(m):
    summary = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= m or ny >= n:
        continue
      if graph[y][x] < graph[ny][nx]:
        summary += dp[ny][nx]
      if graph[y][x] > graph[ny][nx] and dp[y][x] != 0:
        dp[ny][nx] = max(dp[y][x], dp[ny][nx])
    dp[y][x] = max(dp[y][x], summary)

print(dp[n-1][m-1])