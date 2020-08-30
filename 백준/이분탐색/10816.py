# import sys

# n = int(input())
# a = list(map(int, sys.stdin.readline().rstrip().split()))
# m = int(input())
# b = list(map(int, sys.stdin.readline().rstrip().split()))

# a.sort()

# def bin_search(arr, target, start, end):
#   if start >= end:
#     return None
#   mid = (start + end) // 2
#   if arr[mid] == target:
#     return mid
#   if arr[mid] > target:
#     return bin_search(arr, target, start, mid-1)
#   else:
#     return bin_search(arr, target, mid+1, end)

# for r in b:
#   idx = bin_search(a, r, 0, n)
#   if not idx is None:
#     count = 1
#     step = 1
#     while idx+step >= 0 and idx+step < n and a[idx+step] == r:
#       step += 1
#       count += 1
#     step = 1
#     while idx-step >= 0 and idx-step < n and a[idx-step] == r:
#       step += 1
#       count += 1
#     print(count, end=" ")
#   else:
#     print(0, end=" ")
    
  