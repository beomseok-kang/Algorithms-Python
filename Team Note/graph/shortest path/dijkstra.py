# Dijkstra algorithm gets the shortest path to all the nodes
# from one node. The time complexity is O(E log V).
#
# Dijkstra algorithm is based on greedy algorithm, and uses
# priority queue (in this case embodied with min heap).

import heapq

INF = int(1e9)

# n: number of nodes, m: number of edges
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
  # the cost from node a to node b is cost
  a, b, cost = map(int, input().split())
  graph[a].append((b, cost))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      # if the new cost is shorter, update the distance with
      # the shorter cost one.
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)
for i in range(1, n + 1):
  if distance == INF:
    print('INFINITY')
  else:
    print(distance[i])