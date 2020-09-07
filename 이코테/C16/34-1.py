# 가장 긴 증가하는 부분 수열 (Longest Increasing Subsequence) 로 알려진
# 전형적 다이나믹 프로그래밍 문제의 아이디어와 같다.

n = int(input())

dp = [1] * n

soldiers = list(map(int, input().split()))

for i in range(n):
  for j in range(i):
    if soldiers[i] < soldiers[j]:
      dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))