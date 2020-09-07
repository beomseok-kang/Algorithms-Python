from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
nums = list(map(int, input().split()))

result = bisect_right(nums, x) - bisect_left(nums, x)
if result:
  print(result)
else:
  print(-1)