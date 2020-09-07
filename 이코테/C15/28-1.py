n = int(input())
nums = list(map(int, input().split()))

start = 0
end = len(nums)
result = -1
while start <= end:
  mid = (start + end) // 2
  if nums[mid] == mid:
    result = mid
    break
  elif nums[mid] > mid:
    end = mid - 1
  else:
    start = mid + 1

print(result)