import time

times = 100000000

start = time.time()

# for 과 in, range
i = [0 for _ in range(times)]
mid1 = time.time()
print(mid1-start)

# 곱셈 연산자
i = [0] * times
mid2 = time.time()
print(mid2-mid1)
