from math import sqrt

n = int(input())
nums = list(map(int, input().split()))

def is_prime(num):
  if num < 2:
    return False
  if num == 2:
    return True
  for i in range(2, int(sqrt(num)) + 1):
    if num % i == 0:
      return False
  return True

count = 0
for num in nums:
  if is_prime(num):
    count += 1

print(count)