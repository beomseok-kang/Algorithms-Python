data = sorted(input())

total = 0
idx = 0
for i, d in enumerate(data):
  if d.isdigit():
    total += int(d)
  else:
    idx = i
    break

print(''.join(data[idx:]) + (str(total) if int(total) else ''))