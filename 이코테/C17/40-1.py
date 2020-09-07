import heapq

n, m = map(int, input().split())

INF = int(1e9)
graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

h = [(0, 1)] # 1로 가는 비용은 0
dist[1] = 0

while h:
  cost, now = heapq.heappop(h)
  if dist[now] < cost:
    continue
  for i in graph[now]:
    nc = cost + 1
    if dist[i] > nc:
      dist[i] = nc
      heapq.heappush(h, (nc, i))

max_dist = max(d for d in dist if d != INF)
max_node = dist.index(max_dist)
num_nodes = dist.count(max_dist)

print(max_node, max_dist, num_nodes)
