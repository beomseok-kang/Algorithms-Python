def is_group_word(s):
  group = [s[0]]
  for i in s[1:]:
    if i == group[-1]:
      continue
    elif i in group:
      return False
    else:
      group.append(i)
  return True

n = int(input())

count = 0
for i in range(n):
  if is_group_word(input()):
    count += 1

print(count)
