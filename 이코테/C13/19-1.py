from itertools import permutations

n = int(input())

nums = list(map(int, input().split()))

plus, minus, mult, div = map(int, input().split())

calcs = []
for _ in range(plus):
  calcs.append('+')
for _ in range(minus):
  calcs.append('-')
for _ in range(mult):
  calcs.append('*')
for _ in range(div):
  calcs.append('/')

def pluss(a, b):
  return a + b
def minuss(a, b):
  return a - b
def multiply(a, b):
  return a * b
def divide(a, b):
  if a >= 0:
    return a // b
  if a < 0:
    return -(-a // b)

min_val = int(1e9)
max_val = int(-1e9)
for iteration in permutations(calcs, n - 1):
  result = nums[0]
  for idx, calc in enumerate(iteration):
    if calc == '+':
      result = pluss(result, nums[idx+1])
    elif calc == '-':
      result = minuss(result, nums[idx+1])
    elif calc == '*':
      result = multiply(result, nums[idx+1])
    else:
      result = divide(result, nums[idx+1])
  min_val, max_val = min(min_val, result), max(max_val, result)

print(max_val)
print(min_val)