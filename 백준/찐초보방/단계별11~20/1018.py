from copy import deepcopy

n, m = map(int, input().split())

board = []
for _ in range(n):
  board.append(input())

wd = m - 8
hd = n - 8
min_val = int(1e9)
colors = ['B', 'W']

for i in range(hd + 1):
  new_board = deepcopy(board[i:i+8])
  for j in range(wd + 1):
    for k in range(2):
      standard_color = colors[k]
      count = 0
      for y in range(8):
        for x in range(8):
          if (y % 2 == 0 and x % 2 == 0) or (y % 2 == 1 and x % 2 == 1):
            if new_board[y][j+x] != standard_color:
              count += 1
          else:
            if new_board[y][j+x] == standard_color:
              count += 1
      min_val = min(min_val, count)

print(min_val)