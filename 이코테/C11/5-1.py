n, m = map(int, input().split())

# 이 문제는 combinations 문제이다. combinations는 n개 중 r개를
# nCr 을 구하면 된다. 현재는 n개 중 2개를 구해야하므로,
# nC2 = n(n+1)/2 이다. 따라서 중복될 경우의 수를 여기서 빼주면
# 답을 구할 수 있다. 중복될 경우의 수들 또한 만약 3이 4개 있다고
# 하면, 4C2가 답이다.

data = list(map(int, input().split()))

data.sort()

rem = data[0]
count = 1
counts = []
for i in data[1:]:
  if rem != i:
    rem = i
    counts.append(count)
    count = 1
  else:
    count += 1
counts.append(count)

result = n * (n-1) / 2

for i in counts:
  result -= i * (i-1) / 2

print(int(result))