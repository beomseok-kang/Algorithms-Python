import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
  a, b = map(int, input().split())
  indegree[b] += 1
  graph[a].append(b)

q = []
for i in range(1, n + 1):
  if indegree[i] == 0:
    heapq.heappush(q, i)

result = []
while q:
  i = heapq.heappop(q)
  result.append(i)
  for j in graph[i]:
    indegree[j] -= 1
    if indegree[j] == 0:
      heapq.heappush(q, j)

for i in result:
  print(i, end=" ")