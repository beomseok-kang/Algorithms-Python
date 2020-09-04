n, m = map(int, input().split())

graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

houses = []
chickens = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 0:
      continue
    elif graph[i][j] == 1:
      houses.append((i, j))
    else:
      chickens.append((i, j))

def chicken_dist(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

import itertools

sum_val = int(1e9)
for combination in itertools.combinations(chickens, m):
  temp_sum_val = 0
  for house in houses:
    min_val = int(1e9)
    for chicken in combination:
      min_val = min(min_val, chicken_dist(house, chicken))
    temp_sum_val += min_val
  sum_val = min(sum_val, temp_sum_val)

print(sum_val)