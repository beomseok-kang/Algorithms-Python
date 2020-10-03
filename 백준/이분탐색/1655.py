from bisect import bisect_right
import sys
input = sys.stdin.readline

n = int(input())

count = 0
array = []

res = []
for i in range(n):
  count += 1
  num = int(input())
  j = bisect_right(array, num)
  array.insert(j, num)
  if count % 2 == 0:
    print(array[count // 2 - 1])
  else:
    print(array[count // 2])