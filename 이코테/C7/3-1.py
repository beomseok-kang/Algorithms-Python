import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
rcs = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(rcs)
result = 0

while start <= end:
  mid = (start + end) // 2
  cut = sum(rc-mid for rc in rcs if rc > mid)
  # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
  if cut < m:
    end = mid - 1
  # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
  else:
    # 최대한 덜 잘랐을 때가 정답이므로 여기에서 result를 기록한다.
    result = mid
    start = mid + 1

print(result)