n_string = input()

result = 0
for i in range(len(n_string)):
  n = int(n_string[i])
  if n == 0:
    continue
  if n == 1:
    result += 1
  elif result == 0:
    result += n
  else:
    result *= n

print(result)