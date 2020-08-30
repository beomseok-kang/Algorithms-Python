n, m = map(int, input().split())
l = []
for i in range(n):
  l.append(list(map(int, input().split())))

rem = min(l[0])
for i in range(1,n):
  comp = min(l[i])
  if rem < comp:
    rem = comp

print(rem)