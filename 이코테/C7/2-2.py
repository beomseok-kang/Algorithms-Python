# 부품 찾기
import sys

n = int(input())
parts = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
reqs = list(map(int, sys.stdin.readline().rstrip().split()))

parts.sort()
def bin_search(arr, target, start, end): # l = list, r = request
  if start > end:
    return None
  mid = (start + end) // 2
  if arr[mid] == target:
    return mid
  elif arr[mid] > target:
    return bin_search(arr, target, start, mid-1)
  else:
    return bin_search(arr, target, mid+1, end)

for req in reqs:
  if bin_search(parts, req, 0, len(parts)):
    print("yes", end=" ")
  else:
    print("no", end=" ")