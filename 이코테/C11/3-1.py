data = input()

z_count = 0
o_count = 0

now = data[0]
if now == '1':
  o_count += 1
else:
  z_count += 1

for i in data[1:]:
  if i == now:
    continue
  else:
    if i == '1':
      o_count += 1
      now = '1'
    else:
      z_count += 1
      now = '0'

print(min(z_count, o_count))