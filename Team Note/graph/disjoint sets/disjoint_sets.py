# Disjoint sets are the sets of nodes that does not share a common
# root node (parent). Root node itself represents the set.

# Disjoint sets can be modified with two operations:
#   1. find
#     The operation "find A" finds a parent node (root parent node)
#     of the node A.
#   2. union
#     The operation "union A, B" firstly finds the parent nodes of
#     each node. Then, say the root node of A is A' and that of B
#     is B', then commonly, if A' is smaller than B', set the parent
#     node of A' as B'. So the root node of all the nodes will be
#     A'.

# 1. find: find parent of node x from the table, parent.
# 1-1. find parent of node x, but does not change the parent node
#      of the node x to its root node. It can be inefficient.
def find_parent(parent, x):
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return x

# 1-2. find root node of node x, and changes the parent node of
#      node x to its root node. Becomes more efficient.
def find_parent_improved(parent, x):
  if parent[x] != x:
    # changes the parent to the root node.
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 2. union: union two nodes, a and b
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

# set default: parent node of each node is itself.
for i in range(1, v + 1):
  parent[i] = i

# edge means union of two nodes
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

# print root nodes of each node (and hence which disjoint set it
# belongs to).
for i in range(1, v + 1):
  print(find_parent(parent, i), end=" ")

print()

# print 
