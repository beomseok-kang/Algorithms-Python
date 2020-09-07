n = int(input())

ugly = [0] * n
ugly[0] = 1 # 첫 번째 못생긴 수

# 2배, 3배, 5배를 위한 인덱스
i2 = i3 = i5 = 0
# 첫 곱셈 값
next2, next3, next5 = 2, 3, 5

for l in range(1, n):
  # 가능한 곱셈 결과 중 가장 작은 수를 선택
  ugly[l] = min(next2, next3, next5)
  # 인덱스에 따라 곱셈 결과를 증가
  if ugly[l] == next2:
    i2 += 1
    next2 = ugly[i2] * 2
  if ugly[l] == next3:
    i3 += 1
    next3 = ugly[i3] * 3
  if ugly[l] == next5:
    i5 += 1
    next5 = ugly[i5] * 5

print(ugly)
print(ugly[n - 1])