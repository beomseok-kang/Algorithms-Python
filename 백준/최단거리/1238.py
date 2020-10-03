# Dijkstra Algorithm

import heapq
INF = int(1e9)
n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
opp_graph = [[] for _ in range(n + 1)]
d_from_x = [INF] * (n + 1)
d_to_x = [INF] * (n + 1)

for _ in range(m):
  # a 에서 b 로 가는 비용이 t
  a, b, t = map(int, input().split())
  graph[a].append((b, t))
  opp_graph[b].append((a, t))

# starting from x
q1 = []
heapq.heappush(q1, (0, x))
d_from_x[x] = 0
while q1:
  t, b = heapq.heappop(q1)
  if d_from_x[b] < t:
    continue
  else:
    for b_new, t_new in graph[b]:
      cost = t + t_new
      if cost < d_from_x[b_new]:
        d_from_x[b_new] = cost
        heapq.heappush(q1, (cost, b_new))

# coming to x
q2 = []
heapq.heappush(q2, (0, x))
d_to_x[x] = 0
while q2:
  t, b = heapq.heappop(q2)
  if d_to_x[b] < t:
    continue
  else:
    for b_new, t_new in opp_graph[b]:
      cost = t + t_new
      if cost < d_to_x[b_new]:
        d_to_x[b_new] = cost
        heapq.heappush(q2, (cost, b_new))

result = 0
for i in range(1, n + 1):
  result = max(result, d_from_x[i] + d_to_x[i])

print(result)