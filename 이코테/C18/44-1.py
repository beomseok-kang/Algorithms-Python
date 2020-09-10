# import sys
# input = sys.stdin.readline

# n = int(input())

# planets = []
# for _ in range(n):
#   planets.append(tuple(map(int, input().split())))

# edges = []

# for i in range(n - 1, -1, -1):
#   x1, y1, z1 = planets.pop()
#   for j in range(i - 1, -1, -1):
#     x2, y2, z2 = planets[j]
#     cost = min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))
#     edges.append((cost, i, j))

# def find_parent(parent, x):
#   if parent[x] != x:
#     parent[x] = find_parent(parent, parent[x])
#   return parent[x]

# def union_parent(parent, a, b):
#   a = find_parent(parent, a)
#   b = find_parent(parent, b)
#   if a < b:
#     parent[b] = a
#   else:
#     parent[a] = b

# parent = [i for i in range(n)]
# edges.sort()

# result = 0

# for edge in edges:
#   cost, a, b = edge
#   if find_parent(parent, a) != find_parent(parent, b):
#     union_parent(parent, a, b)
#     result += cost

# print(result)