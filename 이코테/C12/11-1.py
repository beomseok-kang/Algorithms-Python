import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
k = int(input())
apples = []
for _ in range(k):
  apples.append(tuple(map(lambda x: int(x) - 1, input().split())))
l = int(input())
change = deque()
for _ in range(l):
  change.append(tuple(map(str, input().split())))

snake = deque()
snake.append((0, 0))
# 위 오른쪽 아래 왼쪽 각각 0 1 2 3
cur_dir = 1
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)
next_dir = change.popleft()

t = 0

while True:
  t += 1
  ny = snake[-1][0] + dy[cur_dir]
  nx = snake[-1][1] + dx[cur_dir]
  if ny < 0 or nx < 0 or ny >= n or nx >= n:
    break
  if (ny, nx) in snake:
    break
  if (ny, nx) in apples:
    snake.append((ny, nx))
    apples.remove((ny, nx))
  else:
    snake.append((ny, nx))
    snake.popleft()
  if next_dir[0] == str(t):
    if next_dir[1] == 'D':
      cur_dir += 1
    else:
      cur_dir -= 1
    if cur_dir < 0:
      cur_dir = 4 + cur_dir
    elif cur_dir >= 4:
      cur_dir = cur_dir - 4
    if change:
      next_dir = change.popleft()

print(t)