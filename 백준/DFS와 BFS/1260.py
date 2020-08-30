from collections import deque

n, m, v = map(int, input().split())

edges = []
for i in range(m):
  edges.append(list(map(int, input().split())))
edges.sort()
print(edges)

stack = []
dfs_visited = [False] * n

def dfs(stack, v, visited):
  if visited[v-1]:
    return
  stack.append(v)
  visited[v-1] = True
  print(v, end=" ")
  for i in edges:
    if i[0] == v:
      dfs(stack, i[1], visited)
    if i[1] == v:
      dfs(stack, i[0], visited)

dfs(stack, v, dfs_visited)
print()

queue = deque()
bfs_visited = [False] * n

def bfs(queue, v, visited):
  queue.append(v)
  visited[v-1] = True
  while queue:
    out = queue.popleft()
    print(out, end=" ")
    for i in edges:
      if i[0] == out and visited[i[1]-1] == False:
        queue.append(i[1])
        visited[i[1]-1] = True
      if i[1] == out and visited[i[0]-1] == False:
        queue.append(i[0])
        visited[i[0]-1] = True

bfs(queue, v, bfs_visited)

############################ UNSOLVED YET
