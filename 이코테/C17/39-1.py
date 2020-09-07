import heapq

INF = int(1e9)
tc = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(tc):
  n = int(input())
  mp = [[INF] * (n + 1)]
  for _ in range(n):
    mp.append([INF] + list(map(int, input().split())))
  
  h = [(mp[1][1], 1, 1)] # (cost, x, y)
  costs = [[INF] * (n + 1) for _ in range(n + 1)] # 가상의 0, 0
  costs[1][1] = mp[1][1]
  while h:
    cost, x, y = heapq.heappop(h)
    if costs[y][x] < cost:
      continue
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
      nc = cost + mp[ny][nx] # new cost
      if nc < costs[ny][nx]:
        costs[ny][nx] = nc
        heapq.heappush(h, (nc, nx, ny))
  
  print(costs[n][n])
  
