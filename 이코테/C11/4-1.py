n = int(input())
data = list(map(int, input().split()))

data.sort()
sums = []
for i in range(n):
  for j in range(i + 1, n + 1):
    sums.append(sum(data[i:j]))

result = 1
while True:
  if not result in sums:
    print(result)
    break
  result += 1