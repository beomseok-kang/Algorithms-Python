t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  raw = list(map(int, input().split()))
  dp = []
  golds = []
  for i in range(n):
    dp.append([0] * m)
    golds.append(raw[m * i : m * (i + 1)])
  for i in range(n):
    dp[i][0] = golds[i][0]
  for j in range(1, m):
    for i in range(n):
      if i == 0: # 위쪽 끝
        dp[i][j] = max(dp[i+k][j-1] + golds[i][j] for k in range(0, 2))
      elif i == n - 1: # 아래쪽 끝
        dp[i][j] = max(dp[i+k][j-1] + golds[i][j] for k in range(-1, 1))
      else:
        dp[i][j] = max(dp[i+k][j-1] + golds[i][j] for k in range(-1, 2))
  print(max(dp[i][m-1] for i in range(n)))