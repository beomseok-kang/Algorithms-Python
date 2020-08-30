n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

repeat = k * data[0] + data[1]

result = repeat * (m // (k+1)) + (m % (k+1)) * data[0]

print(result)