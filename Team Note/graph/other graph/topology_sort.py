# Topology sort is used to sort the nodes in a sequence that is
# required.
#
# Topology sort is done with the sequence below:
# 1. Put the node that has indegree of 0 into a queue.
# 2. Until the queue gets empty, repeat the following:
#   2-1. Popleft a node from queue and remove all the edges starting
#        from the popped node.
#   2-2. Put new nodes that have indegree of 0 into the queue.

from collections import deque

# v: number of nodes (vertex), e: number of edges
v, e = map(int, input().split())
indegree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]

# edges input
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  indegree[b] += 1

def topology_sort():
  result = []
  q = deque()
  for i in range(1, v + 1):
    if indegree[i] == 0:
      q.append(i)
  
  while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)
  
  for i in result:
    print(i, end=" ")

topology_sort()