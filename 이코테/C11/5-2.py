n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11
for x in data:
  # 각 무게의 볼링공 카운트
  array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
  # 무게가 i인 볼링공의 개수 제외
  n -= array[i]
  # B가 선택하는 경우의 수와 곱하기
  result += array[i] * n

print(result)