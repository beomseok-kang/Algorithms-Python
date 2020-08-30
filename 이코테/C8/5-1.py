n, m = map(int, input().split())
INF = 99999999
dp = [INF] * (10001)
coins = []
for i in range(n):
  coin = int(input())
  coins.append(coin)
  dp[coin] = 1

for i in range(1, m+1):
  for coin in coins:
    if i == coin:
      dp[i] = 1
      continue
    elif i-coin > 0:
      dp[i] = min(dp[i], dp[i-coin] + 1)
    
  
print(dp[m] if dp[m] != INF else -1)