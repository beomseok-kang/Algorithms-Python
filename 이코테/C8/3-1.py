n = int(input())
store = list(map(int, input().split()))

dp = [0] * 100
dp[0] = store[0]
dp[1] = max(store[1], store[0])
for i in range(2, n):
  # 2 인덱스 전과 1 인덱스 전의 숫자가 같다면, 그 전 숫자가 더해지지
  # 않았다는 의미이므로 바로 더해주는 것이 최댓값이 된다. 그 전 숫자가
  # 0이었다면 더해졌더라도 숫자가 바뀌지 않았을 것이므로 더하든 아니든
  # 똑같다. 따라서 이 경우 더해주어도 상관이 없다.
  if dp[i-2] == dp[i-1]:
    dp[i] = dp[i-1] + store[i]
  else:
    dp[i] = max(dp[i-1], dp[i-2] + store[i])

print(dp[n-1])


  