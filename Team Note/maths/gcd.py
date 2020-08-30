import math

def gcd_math(a, b):
  return math.gcd(a, b)

def gcd_euclidean(a, b):
  a, b = max(a, b), min(a, b)
  while b != 0:
    a, b = b, a % b
  return a

def lcm(a, b):
  return int(a * b / gcd_euclidean(a, b))

a = 12
b = 20
print(gcd_euclidean(a, b))
print(lcm(a, b))