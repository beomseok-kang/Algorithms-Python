n = input()
length = len(n)
summary = 0

# 왼쪽 부분 자릿수 합
for i in range(length // 2):
  summary += int(n[i])
# 오른쪽 부분 자릿수 합 빼주기
for i in range(length // 2, length):
  summary -= int(n[i])

# 왼쪽과 오른쪽 자릿수 합이 동일한지 검사
if summary == 0:
  print('LUCKY')
else:
  print('READY')