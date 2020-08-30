# 부품 찾기
import sys

n = int(input())
parts = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
reqs = list(map(int, sys.stdin.readline().rstrip().split()))

for req in reqs:
  if req in parts:
    print("yes", end=" ")
  else:
    print("no", end=" ")
