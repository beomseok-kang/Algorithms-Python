import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

dp = [[0] * m for _ in range(n)]
dp[0][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def visit(x, y):
  if y == n - 1 and x == m - 1:
    return 1
  if dp[y][x]:
    return dp[y][x]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or ny < 0 or nx >= m or ny >= n:
      continue
    if graph[ny][nx] < graph[y][x]:
      dp[y][x] += visit(nx, ny)
  return dp[y][x]

visit(0, 0)
print(dp[n-1][m-1])