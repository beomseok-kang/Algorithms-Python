n = int(input()) # 노드의 개수
m = int(input()) # 간선의 개수
edges = []
for i in range(m):
  edges.append(list(map(int, input().split())))

# 0도 있다고 가정하여 더 간편하고 알아보기 쉽게 만듦
adj_list = []
for i in range(n+1):
  adj_list.append([])

for edge in edges:
  a, b = edge
  adj_list[a].append(b)
  adj_list[b].append(a)

visited = [False] * (n + 1)

def dfs(graph, v, visited):
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

dfs(adj_list, 1, visited)
print(visited.count(True)-1) # 1번 컴퓨터는 제외