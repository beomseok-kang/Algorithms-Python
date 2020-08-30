import math

# The funciton below prints all prime numbers until the input
# value, x. Time complexity is O(NloglogN), but requires large
# memory space.

def sieve_of_eratosthenes(x):
  array = [True] * (x+1)
  for i in range(2, int(math.sqrt(x)) + 1):
    if array[i] == True: # if i is prime
      # remove all multiples
      j = 2
      while i * j <= x:
        array[i*j] = False
        j += 1
  
  for i in range(2, x+1):
    if array[i]:
      print(i, end=" ")
