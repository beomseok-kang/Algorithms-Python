n, m = map(int, input().split())
edges = []
total_cost = 0
for _ in range(m):
  x, y, z = map(int, input().split())
  total_cost += z
  edges.append((z, x, y))

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

parent = [i for i in range(n)]
edges.sort()
result = 0

for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(total_cost - result)