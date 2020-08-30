# Binary search can only be used when the list is already sorted.
# The time complexity of binary search is O(log N)

def binary_search_recursive(arr, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if arr[mid] == target:
    return mid
  elif arr[mid] > target:
    return binary_search_recursive(arr, target, start, mid-1)
  else:
    return binary_search_recursive(arr, target, mid+1, end)

def binary_search_loop(arr, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None