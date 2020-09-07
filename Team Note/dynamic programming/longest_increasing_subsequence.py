# O(N^2)
def get_lis_length(sequence):
  length = len(sequence)
  # dp table initialize
  dp = [1] * length
  for i in range(length):
    for j in range(i):
      if sequence[i] > sequence[j]:
        dp[i] = max(dp[i], dp[j] + 1)
  return max(dp)

sequence = [1, 2, 3, 5, 8, 2, 9, 10]

print(get_lis_length(sequence)) # [1, 2, 3, 5, 8, 9, 10], answer = 7

# O(N log N)
from bisect import bisect_left

def get_lis_improved(sequence):
  L = [sequence[0]]
  for i in range(1, len(sequence)):
    if L[-1] < sequence[i]:
      L.append(sequence[i])
    else:
      lower_bound = bisect_left(L, sequence[i])
      L[lower_bound] = sequence[i]
  # print(L)
  return len(L)

sequence = [2, 3, 6, 8, 1, 4, 4, 9] # L = [1, 3, 4, 8, 9]
print(get_lis_improved(sequence)) # 5 출력