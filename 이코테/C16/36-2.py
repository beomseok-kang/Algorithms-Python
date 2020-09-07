# 이 문제는 최소 편집 거리를 담을 2차원 테이블을 초기화한 후, 최소 편집 거리를
# 계산하여 테이블에 저장하는 과정으로 문제를 해결할 수 있다. 다이나믹 프로그래밍
# 의 점화식은
# 1. 두 문자가 같은 경우: dp[i][j] = dp[i - 1][j - 1]
#       행과 열에 해당하는 문자가 서로 같다면, 왼쪽 위에 해당하는 수를 그대로 삽입한다.
#       (바꿀 필요가 없으므로)
# 2. 두 문자가 다른 경우: dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
#       행과 열에 해당하는 문자가 서로 다르다면, 왼쪽 (삽입), 위쪽 (삭제),
#       왼쪽 위 (교체) 에 해당하는 수 중 가장 작은 수에 1을 더해 삽입

def edit_dist(str1, str2):
  n = len(str1)
  m = len(str2)

  dp = [[0] * (m + 1) for _ in range(n + 1)]

  for i in range(1, n + 1):
    dp[i][0] = i
  for j in range(1, m + 1):
    dp[0][j] = j
  
  for i in range(1, n + 1):
    for j in range(1, m + 1):
      if str1[i - 1] == str2[j - 1]:
        dp[i][j] = dp[i - 1][j - 1]
      else:
        dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
  
  return dp[n][m]

str1 = input()
str2 = input()
print(edit_dist(str1, str2))