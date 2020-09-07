a = input()
b = input()

rem = 0
st = ''
for i in a:
  for idx, j in enumerate(b[rem:]):
    if j == i:
      rem = idx
      st += i

print(len(b) - len(st))
    