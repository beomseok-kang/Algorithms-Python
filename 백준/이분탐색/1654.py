import sys

n, k = map(int, input().split())
arr = []
for i in range(n):
  arr.append(int(sys.stdin.readline().rstrip()))

start = 0
end = max(arr)
result = end
while start <= end:
  mid = (start + end) // 2
  if mid == 0:
    break
  temp = 0
  for i in arr:
    temp += i // mid
  if temp < k:
    end = mid - 1
    result = end
  else:
    result = start
    start = mid + 1

print(result)