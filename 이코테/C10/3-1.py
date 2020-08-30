import sys
input = sys.stdin.readline

n, m = map(int, input().split())

roads = []
parent = [i for i in range(n+1)]
for i in range(m):
  a, b, cost = map(int, input().split())
  roads.append((cost, a, b))

roads.sort()

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

total_cost = 0
# max_record = 0
last = 0 # 어차피 마지막으로 포함되는 간선이 가장 비용이 큰 간선일 것이다.
for road in roads:
  cost, a, b = road
  # 사이클이 발생하지 않는 경우에만 집합에 포함시킨다.
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    total_cost += cost
    # max_record = max(max_record, cost)
    last = cost

print(total_cost - last)
