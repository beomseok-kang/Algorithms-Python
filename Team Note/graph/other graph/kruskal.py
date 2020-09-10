# Spanning tree is a subgraph of a graph that includes all the
# nodes but does not have any cycle.

# Kruskal's algorithm finds the spanning tree that has the lowest
# sum of costs of edges by using greedy algorithm. The time complexity
# of Kruskal's algorithm is O(E log E), where E is the number of
# edges.

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

# v: number of nodes (vertex), e: number of edges
v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0 # total cost after kruskal algorithm

for i in range(1, v + 1):
  parent[i] = i

for _ in range(e):
  a, b, cost = map(int, input().split())
  # for sorting, set the cost as the first element of tuple.
  edges.append((cost, a, b))

edges.sort()
for edge in edges:
  cost, a, b = edge
  # union only if no cycle happens.
  if find_parent(parent, a) == find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(result)