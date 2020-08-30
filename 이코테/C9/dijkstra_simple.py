# 간단한 다익스트라 알고리즘의 구현
# 그러나 시간 복잡도가 O(V^2) 이다 (V 는 노드, vertex 의 개수)
# 전체 노드의 개수가 5000개 이하라면 이 코드로 문제를 풀 수 있지만,
# 그 이상이라면 개선된 다익스트라를 써야한다.

import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n + 1)]

visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
  # a = node a, b = node b, cost = cost of edge
  a, b, cost = map(int, input().split())
  graph[a].append((b, cost))

# 방문하지 않은 노드 중 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1, n + 1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  # 시작 노드에 대해서 초기화
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1]
  # 시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
  for i in range(n - 1):
    # 현재 최단 거리가 가장 짧은 노드를 꺼내 방문 처리
    now = get_smallest_node()
    visited[now] = True
    # 현재 노드와 연결된 다른 노드를 확인
    for j in graph[now]:
      cost = distance[now] + j[1]
      # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[j[0]]:
        distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])