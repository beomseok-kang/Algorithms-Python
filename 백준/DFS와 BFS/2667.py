n = int(input())

mp = []
for i in range(n):
  mp.append(list(map(int, input())))

visited = [[False] * n for i in range(n)]

def dfs(x, y):
  result = 0
  if x < 0 or y < 0 or x >= n or y >= n:
    return 0
  if visited[x][y] == False and mp[x][y] != 0:
    result += 1
    visited[x][y] = True
    result += dfs(x-1, y)
    result += dfs(x+1, y)
    result += dfs(x, y-1)
    result += dfs(x, y+1)
  return result

answer = []
count = 0
for x in range(n):
  for y in range(n):
    # 방문한 적이 없고 집이 있음
    if visited[x][y] == False and mp[x][y] != 0:
      count += 1
      answer.append(dfs(x, y))

print(count)
for i in sorted(answer):
  print(i)