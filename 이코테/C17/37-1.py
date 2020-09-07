INF = int(1e9)

n = int(input())
m = int(input())

distances = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
  # a에서 b까지 가는 비용이 c
  a, b, c = map(int, input().split())
  distances[a][b] = min(distances[a][b], c)

for i in range(1, n + 1):
  distances[i][i] = 0

for k in range(1, n + 1):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

for row in distances[1:]:
  print(' '.join(map(lambda x: str(x) if x != INF else '0', row[1:])))