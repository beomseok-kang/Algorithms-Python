n = int(input())
k = int(input())

# k번째 수는 무조건 k보다 작거나 같다.
start, end = 1, k

while start <= end:
  mid = (start + end) // 2
  
  temp = 0
  for i in range(1, n + 1):
    # 각 행에서 mid보다 작은 수는 min(mid // i, n) 이 된다.
    temp += min(mid // i, n)
  
  # 만약 mid보다 작은 수가 k보다 많다면, mid를 줄여주어야 한다.
  if temp >= k:
    answer = mid
    end = mid - 1
  # 그 반대라면 mid를 늘려주어야 한다.
  else:
    start = mid + 1

print(answer)