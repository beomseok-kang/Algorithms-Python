from itertools import combinations

n = int(input())
board = []
teachers = []
spaces = []

for i in range(n):
  board.append(list(input().split()))
  for j in range(n):
    if board[i][j] == 'T':
      teachers. append((i, j))
    if board[i][j] == 'X':
      spaces.append((i, j))

def watch(x, y, direction):
  if direction == 0: # 왼쪽 감시
    while y >= 0:
      if board[x][y] == 'S':
        return True
      if board[x][y] == 'O':
        return False
      y -= 1
  if direction == 1: # 오른쪽 감시
    while y < n:
      if board[x][y] == 'S':
        return True
      if board[x][y] == 'O':
        return False
      y += 1
  if direction == 2: # 위쪽 감시
    while x >= 0:
      if board[x][y] == 'S':
        return True
      if board[x][y] == 'O':
        return False
      x -= 1
  if direction == 3:
    while x < n:
      if board[x][y] == 'S':
        return True
      if board[x][y] == 'O':
        return False
      x += 1
  return False

def process():
  for x, y in teachers:
    for i in range(4):
      if watch(x, y, i):
        return True
  return False

find = False

for data in combinations(spaces, 3):
  # 장애물 설치
  for x, y in data:
    board[x][y] = 'O'
  # 학생이 한 명도 감지되지 않는 경우
  if not process():
    find = True
    break
  # 원래대로 돌려놓기
  for x, y in data:
    board[x][y] = 'X'

if find:
  print('YES')
else:
  print('NO')
