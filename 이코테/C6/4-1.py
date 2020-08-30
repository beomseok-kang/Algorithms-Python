n, k = map(int, input().split())
l_a = list(map(int, input().split()))
l_b = list(map(int, input().split()))

for i in range(k):
  if min(l_a) < max(l_b):
    a, b = l_a.index(min(l_a)), l_b.index(max(l_b))
    l_a[a], l_b[b] = l_b[b], l_a[a]

print(sum(l_a))