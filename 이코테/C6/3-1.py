n = int(input())

l = []
for i in range(n):
  std, score = map(str, input().split())
  l.append((score,std))

for i in sorted(l, key=lambda x: int(x[0])):
  print(i[1], end=" ")
