n = int(input())
seq = list(map(int, input().split()))

dp = [[1, [seq[i]]] for i in range(n)]

for i in range(len(seq)):
  for j in range(i):
    if seq[i] > seq[j]:
      if dp[j][0] + 1 > dp[i][0]:
        dp[i] = [dp[j][0] + 1, dp[j][1] + [seq[i]]]

length, subseq = max(dp)

print(length)
for i in subseq:
  print(i, end=" ")