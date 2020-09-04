n = int(input())

count = 0

for i in range(1, n + 1):
  st = str(i)
  if len(st) < 3:
    count += 1
    continue
  for i in range(1, len(st) - 1):
    if int(st[i-1]) - int(st[i]) != int(st[i]) - int(st[i+1]):
      count -= 1
      break
  count += 1

print(count)