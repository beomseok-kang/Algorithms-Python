import sys
input = sys.stdin.readline

n = int(input())
nums = []

for _ in range(n):
  nums.append(int(input()))

for i in sorted(nums):
  print(i)