# MOST BASIC, O(X^2)
def is_prime_number_basic(x):
  for i in range(2, x):
    if x % i == 0:
      return False
  return True

# SLIGHTLY IMPROVED, O(X^(1/2))
import math
def is_prime_number_sqrt(x):
  # From 2 to sqrt of x, check every number
  for i in range(2, int(math.sqrt(x)) + 1):
    if x % i == 0:
      return False
  return True