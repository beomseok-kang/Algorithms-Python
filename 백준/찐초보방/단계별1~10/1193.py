def find_frac(step, n):
  div = step + 1
  if step % 2 == 0:
    print('{0}/{1}'.format(n, div - n))
  else:
    print('{0}/{1}'.format(div - n, n))

n = int(input())

step = 1
while True:
  if step >= n:
    break
  else:
    n -= step
  step += 1

find_frac(step, n)