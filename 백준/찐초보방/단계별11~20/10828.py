import sys
input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
  query = input().rstrip()
  if query == 'pop':
    print(stack.pop() if stack else -1)
  elif query == 'size':
    print(len(stack))
  elif query == 'empty':
    print(int(len(stack) == 0))
  elif query == 'top':
    print(stack[-1] if stack else -1)
  else:
    stack.append(query.split()[1])