p = list(input())

scenarios = [
  (2,1),
  (-2,1),
  (1,2),
  (-1,2),
  (2,-1),
  (-2,-1),
  (1,-2),
  (-1,-2)
]

col = 'abcdefgh'
row = '12345678'

idx = (col.index(p[0]), row.index(p[1]))
count = 0

for sc in scenarios:
  c_i = idx[0] + sc[0]
  r_i = idx[1] + sc[1]
  if c_i >= 0 and c_i < 8 and r_i >= 0 and r_i < 8:
    count += 1

print(count)
