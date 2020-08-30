import sys

n = int(input())
a = set(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
b = list(map(int, sys.stdin.readline().rstrip().split()))

for i in b:
  if i in a:
    print(1)
  else:
    print(0)