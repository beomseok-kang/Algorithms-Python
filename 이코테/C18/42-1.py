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

g = int(input())
p = int(input())

parent = [i for i in range(g + 1)]

result = 0
for _ in range(p):
  data = find_parent(parent, int(input()))
  if data == 0: # 현재 루트 노드가 0이라면 종료
    break
  union_parent(parent, data, data - 1)
  result += 1

print(result)