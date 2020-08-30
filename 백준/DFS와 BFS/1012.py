import sys
sys.setrecursionlimit(50000)

num_test = int(input())
cases = []
for i in range(num_test):
  cases.append([])
  m, n, k = map(int, input().split())
  for j in range(n):
    cases[i].append([0] * m)
  for j in range(k):
    x, y = map(int, input().split())
    cases[i][y][x] = 1

def dfs(x, y, n, m, i):
  if y < 0 or x < 0 or y >= n or x >= m:
    return False
  if cases[i][y][x] == 2:
    return False
  if cases[i][y][x] == 1:
    cases[i][y][x] = 2
    dfs(x-1, y, n, m, i)
    dfs(x+1, y, n, m, i)
    dfs(x, y-1, n, m, i)
    dfs(x, y+1, n, m, i)
    return True
  return False

# visited = 2, unvisited = 1, no cabbage = 0
count = [0] * num_test
for i in range(len(cases)):
  n = len(cases[i])
  for y in range(len(cases[i])):
    m = len(cases[i][0])
    for x in range(len(cases[i][0])):
      if dfs(x, y, n, m, i):
        count[i] = count[i] + 1

for i in count:
  print(i)