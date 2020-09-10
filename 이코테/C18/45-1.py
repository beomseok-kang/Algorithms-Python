import sys
input = sys.stdin.readline

tc = int(input())

def search_parent(parent, a, b):
  # is a one of b's parents?
  if parent[a] == a:
    return False
  if parent[b] == a:
    return True
  return search_parent(parent, a, parent[a])


for _ in range(tc):
  n = int(input())
  rank = [0] + list(map(int, input().split()))
  m = int(input())
  changes = [tuple(map(int, input().split())) for _ in range(m)]
  
  parent = [0] * (n + 1)
  parent[rank[1]] = rank[1]
  IMPOSSIBLE = False

  for i in range(1, n):
    # higher rank = parent of the next rank
    parent[rank[i + 1]] = rank[i]
  
  for change in changes:
    # a got higher rank than b
    a, b = change
    if parent[b] == a:
      IMPOSSIBLE = True
      break
    if search_parent(parent, a, b):
      continue
    else:
      parent[b] = a
  
  # for i in range(1, n + 1):
  #   for j in range(i + 1, n + 1):
  #     if parent
  # leaf_node = rank[n - 1]
  # for i in range(1, n + 1):
  #   if parent[i] == rank[i]:
  #     if not root_node:
  #       root_node = rank[i]
  #     else:
  #       IMPOSSIBLE = True
  #       break
  
  if IMPOSSIBLE:
    print('IMPOSSIBLE')
  else:
    result = []
    for 
  
    

