n, m = map(int, input().split())

# 방문한 위치 저장하기 위한 맵
d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

count = 1
turn_time = 0
while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x, y = nx, ny
    count += 1
    turn_time = 0
    continue
  # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
  else:
    turn_time += 1
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 뒤로 이동할 수 있다면 이동하기
    if array[nx][ny] == 0:
      x, y = nx, ny
    else:
      break
    turn_time = 0

print(count)