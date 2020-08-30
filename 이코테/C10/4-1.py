from collections import deque

n = int(input())

graph = [[] for _ in range(n + 1)]
time = [0] * (n + 1)
indegree = [0] * (n + 1)

for i in range(1, n + 1):
  cs = list(map(int, input().split()))
  for j in range(len(cs)):
    if j == 0:
      time[i] = cs[0]
      continue
    if cs[j] == -1:
      break
    else:
      graph[cs[j]].append(i)
      indegree[i] += 1

queue = deque()
for i in range(1, n + 1):
  if indegree[i] == 0:
    queue.append(i)

while queue:
  a = queue.popleft()
  for b in graph[a]:
    indegree[b] -= 1
    if indegree[b] == 0:
      time[b] += time[a]
      queue.append(b)

for i in range(1, n + 1):
  print(time[i])

## 오답일 가능성 높음. 책의 정답은 4-2.py 참고