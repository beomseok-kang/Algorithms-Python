n = int(input())

l = []
for i in range(n):
  l.append(int(input()))

print(' '.join(str(i) for i in sorted(l, reverse=True)))