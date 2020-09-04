from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

visited = [-1] * (n + 1)

queue = deque()
queue.append(x)
visited[x] = 0

while queue:
  a = queue.popleft()
  for i in graph[a]:
    if visited[i] == -1:
      visited[i] = visited[a] + 1
      queue.append(i)

printCheck = False
for i in range(1, n + 1):
  if visited[i] == k:
    print(i)
    printCheck = True

if not printCheck:
  print(-1)