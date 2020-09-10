from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

stack = [v]
dfs_visited = [False] * (n + 1)

def dfs():
  while stack:
    node = stack.pop()
    if dfs_visited[node] == True:
      continue
    print(node, end=" ")
    dfs_visited[node] = True
    for edge in sorted(graph[node], reverse=True):
      stack.append(edge)

dfs()
print()

queue = deque()
queue.append(v)
bfs_visited = [False] * (n + 1)

def bfs():
  while queue:
    node = queue.popleft()
    if bfs_visited[node] == True:
      continue
    print(node, end=" ")
    bfs_visited[node] = True
    for edge in sorted(graph[node]):
      queue.append(edge)
bfs()