from itertools import combinations
import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
  n = int(input())
  clothes = dict()
  count = 1

  for __ in range(n):
    c, t = input().split() # cloth, type
    if clothes.get(t) is None:
      clothes[t] = 1
    else:
      clothes[t] += 1
  
  # 한 옷의 종류가 n가지라고 했을 때, 입지 않는 것까지 포함하여
  # 해당 옷의 종류를 n+1가지라고 가정할 수 있다. 따라서 이 경우
  # 옷들을 하나라도 입을 경우는 (n+1)*(m+1) ... - 1 이 된다.
  # (마지막 -1은 아무것도 입지 않았을 때가 된다.)
  
  vals = list(clothes.values())
  for val in vals:
    count *= val + 1

  print(count - 1)