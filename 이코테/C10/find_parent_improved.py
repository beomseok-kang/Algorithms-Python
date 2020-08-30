# x가 속한 집합의 루트 노드 찾기
def find_parent(parent, x):
  if parent[x] != x:
    # 루트 노드가 아니라면, 루트 노드를 찾을 때 까지 재귀적으로 호출한다.
    parent[x] = find_parent(parent, parent[x])
  return parent[x]