from bisect import bisect_left

n = int(input())
seq = list(map(int, input().split()))

l = [seq[0]]
p = [0] * n

for i in range(1, len(seq)):
  if l[-1] < seq[i]:
    l.append(seq[i])
    p[i] = len(l) - 1
  else:
    new = bisect_left(l, seq[i])
    l[new] = seq[i]
    p[i] = new

res = []
count = len(l) - 1
for i in range(n-1, -1, -1):
  if p[i] == count:
    res.append(seq[i])
    count -= 1

print(len(l))
for i in range(len(l) - 1, -1, -1):
  print(res[i], end=" ")