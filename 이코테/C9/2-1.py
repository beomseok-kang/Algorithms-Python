import sys

input = sys.stdin.readline

# n = 노드 개수, m = 간선 개수
n, m = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n + 1):
  graph[a][a] = 0

for _ in range(m):
  a, b = map(int, input().split())
  # a에서 b로 가는 비용과 b에서 a로 가는 비용 모두 1
  graph[a][b] = 1
  graph[b][a] = 1

for k in range(1, n + 1):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

x, k = map(int, input().split())

cost = graph[1][k] + graph[k][x]
print(cost if cost < INF else -1)