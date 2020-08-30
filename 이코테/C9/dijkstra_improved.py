# 개선된 다익스트라 알고리즘
# 최악의 경우에도 시간 복잡도가 O(E log V) 이다 (E는 간선, V는 노드)

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n + 1)]

distance = [INF] * (n + 1)

for _ in range(m):
  # a = node a, b = node b, cost = cost of edge
  a, b, cost = map(int, input().split())
  graph[a].append((b, cost))

for g in graph:
  print(g)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    # 최단 거리가 가장 짧은 노드의 정보 꺼내기
    dist, now = heapq.heappop(q)
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
    if distance[now] < dist:
      continue
    # 현재 노드와 연결된 다른 인접한 노드들을 확인
    for i in graph[now]:
      cost = dist + i[1]
      # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])


