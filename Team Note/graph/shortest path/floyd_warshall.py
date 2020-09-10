# Floyd-Warshall Algorithm is used to get all the shortest distances
# from one node to another. The time complexity is O(N^3).
#
# Floyd-Warshall Algorithm is based on dynamic programming.

INF = int(1e9)

# n: number of nodes, m: number of edges
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# assumes the cost to move to itself is zero.
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

for _ in range(m):
  a, b, cost = map(int, input().split())
  graph[a][b] = cost

def floyd_warshall(graph):
  for k in range(1, n + 1):
    for a in range(1, n + 1):
      for b in range(1, n + 1):
        graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

floyd_warshall(graph)

for a in range(1, n + 1):
  for b in range(1, n + 1):
    if graph[a][b] == INF:
      print('INFINITY', end=" ")
    else:
      print(graph[a][b], end=" ")
  print()