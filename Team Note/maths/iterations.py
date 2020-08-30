import itertools

data = [1,2,3]

def permutations(data):
  for i in itertools.permutations(data, 2):
    print(tuple(i), end=" ")

def combinations(data):
  for i in itertools.combinations(data, 2):
    print(tuple(i), end=" ")

def product(data):
  # 중복 허용 permutations
  for i in itertools.product(data, repeat=2):
    print(tuple(i), end=" ")

def combinations_with_replacement(data):
  # 중복 허용 combinations
  for i in itertools.combinations_with_replacement(data, 2):
    print(tuple(i), end=" ")


print('permutations:', end=" ")
permutations(data)
print()
print('combinations:', end=" ")
combinations(data)
print()
print('product:', end=" ")
combinations_with_replacement(data)
print()
print('combinations with replacement:', end=" ")
combinations_with_replacement(data)
