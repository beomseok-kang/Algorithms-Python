from bisect import bisect_left, bisect_right

def bisect_left_right(arr, x):
  return bisect_left(arr, x), bisect_right(arr, x)

array = [1,2,3,3,3,3,4,5,5]
print(bisect_left_right(array, 3))

# if you get bisect_left and bisect_right, you can simply get the
# count of the number just by getting the difference between
# bisect_right and bisect_left. This gets the count within time
# complexity of O(log N).