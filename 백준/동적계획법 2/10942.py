# import sys

# n = int(input())
# d = list(map(int, sys.stdin.readline().rstrip().split()))

# dp = [[0] * n for i in range(n)]

# for i in range(n): # 길이가 1
#   dp[i][i] = 1
# for i in range(n-1): # 길이가 2
#   if d[i] == d[i+1]:
#     dp[i][i+1] = 1
# for i in range(2,n): # 길이가 3 이상
#   for j in range(n-i):
#     if d[j] == d[j+1] and dp[j+1][i+j-1] == 1:
#       dp[j][i+j] = 1

# m = int(input())

# for _ in range(m):
#   i,j = [int(a) for a in sys.stdin.readline().split()]
#   print(dp[i-1][j-1])

# # qs = []
# # for i in range(m):
# #   qs.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

# # # for q in qs:
# #   i,j = q
# #   print(dp[i-1][j-1])




# # for q in qs:
# #   count = (q[1] - q[0]) // 2
# #   for i in range((q[1] - q[0]) // 2):
# #     if dp[q[1]-1-i][q[0]-1-i] == True:
# #       count -= 1
# #       continue
# #     else:
# #       if dp[q[1]-1-i][q[0]-1-i] == False:
# #         print(0)
# #         break
# #       else:
# #         if array[q[1]-1-i] == array[q[0]-1-i]:
# #           count -= 1
# #           dp[q[1]-1-i][q[0]-1-i] = True
# #         else:
# #           dp[q[1]-1-i][q[0]-1-i] = False
# #           print(0)
# #           break
# #   if count == 0:
# #     print(1)

# # for q in qs:
# #   count = (q[1] - q[0]) // 2
# #   for i in range(count):
# #     if array[q[1]-1-i] == array[q[0]-1-i]:
# #       count -= 1
# #     else:
# #       print(0)
# #       break
# #   if count == 0:
# #     print(1)
