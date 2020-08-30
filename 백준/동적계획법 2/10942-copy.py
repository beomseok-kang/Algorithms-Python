import sys

n = int(input())

d = [int(i) for i in sys.stdin.readline().split()]
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
  dp[i][i] = 1
  if i < n-1 and d[i] == d[i+1]:
    dp[i][i+1] = 1
for i in range(1, n):
  for j in range(1, i+1):
    if d[i] == d[i-j]  and dp[i-j+1][i-1] == 1:
      dp[i-j][i] = 1

qn = int(input())

for _ in range(qn):
  i,j = map(int, sys.stdin.readline().split())
  print(dp[i-1][j-1])