from collections import deque

# 노드와 간선 개수 입력받기
v, e = map(int, input().split())
# 각 노드의 진입 차수를 기록할 리스트를 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 (그래프) 초기화
graph = [[] for _ in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
  a, b = map(int, input().split())
  # a에서 b로 가는 간선
  graph[a].append(b)
  # 진입 차수를 1 증가
  indegree[b] += 1

def topology_sort():
  result = []
  q = deque()
  for i in range(1, v + 1):
    if indegree[i] == 0:
      q.append(i)
  
  while q:
    a = q.popleft()
    result.append(a)
    for b in graph[a]:
      indegree[b] -= 1
      if indegree[b] == 0:
        q.append(b)

  for i in result:
    print(i, end=" ")

topology_sort()
