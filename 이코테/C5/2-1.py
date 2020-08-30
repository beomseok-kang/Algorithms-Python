# DFS (깊이 우선 탐색) 예시

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=" ")
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

graph = [
  [], # 0 이란 노드가 존재하지 않으므로
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)