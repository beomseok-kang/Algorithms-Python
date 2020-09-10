import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

parent = [i for i in range(n + 1)]

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

edges = []
for i in range(n):
  for j in range(i + 1, n):
    if graph[i][j] == 1:
      edges.append((i + 1, j + 1))

for edge in edges:
  a, b = edge
  union_parent(parent, a, b)

routes = list(map(int, input().split()))
root_node = find_parent(parent, routes[0])
all_visitable = True
for route in routes[1:]:
  if find_parent(parent, route) != root_node:
    all_visitable = False
    break

if all_visitable:
  print('YES')
else:
  print('NO')