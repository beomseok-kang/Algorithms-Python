def binary_search(arr, x, start, end):
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == x:
      return mid
    elif arr[mid] > x:
      end = mid - 1
    else:
      start = mid + 1
  return None

n, x = map(int, input().split())
nums = list(map(int, input().split()))

idx = binary_search(nums, x, 0, len(nums))

left, right = -1, -1
while True:
  if idx < 1:
    break
  if nums[idx-1] != x:
    left = idx
    break
  idx -= 1

while True:
  if idx >= n - 1:
    break
  if nums[idx+1] != x:
    right = idx
    break
  idx += 1

result = (right + 1) - left
print(left, right)
print(result if result else -1)