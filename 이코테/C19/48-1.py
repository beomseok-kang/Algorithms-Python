n, m, k = map(int, input().split())

graph = []
shark_p = [None] * (m + 1)
shark_priority = [[] for _ in range(m + 1)]
# (shark, scent strength)
scents = [[[0, 0] for __ in range(n)] for _ in range(n)]

for i in range(n):
  data = list(map(int, input().split()))
  for j in range(n):
    if data[j] != 0:
      shark_p[data[j]] = (i, j)
      scents[i][j] = [data[j], k]
  graph.append(data)

directions = [0] + list(map(lambda x: int(x) - 1, input().split()))

for i in range(1, m + 1):
  for j in range(4):
    shark_priority[i].append(list(map(lambda x: int(x) - 1, input().split())))

t = 0
# 1, 2, 3, 4 each means up, down, left, right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_graph(nx, ny):
  if nx < 0 or ny < 0 or nx >= n or ny >= n:
    return False
  else:
    return True

def update_scent():
  for i in range(n):
    for j in range(n):
      if scents[i][j][1] != 0:
        strength = scents[i][j][1]
        if strength - 1 == 0:
          scents[i][j] = [0, 0]
        else:
          scents[i][j][1] -= 1
      if graph[i][j] != 0:
        scents[i][j] = [graph[i][j], k]

def move(shark, x, y, nx, ny, d):
  graph[x][y] = 0
  if graph[nx][ny] != 0 and graph[nx][ny] < shark:
    shark_p[shark] = None
  else:
    graph[nx][ny] = shark
    shark_p[shark] = (nx, ny)
    directions[shark] = d

def break_loop():
  count = 0
  for i in shark_p:
    if i != None:
      count += 1
  if count == 1:
    return True
  else:
    return False

def possible_moves(shark, x, y):
  no_scent = []
  my_scent = []
  # seeking for block with no scent.
  for j in range(4):
    nx = x + dx[j]
    ny = y + dy[j]
    if not in_graph(nx, ny):
      continue
    elif scents[nx][ny][1] == 0:
      no_scent.append((nx, ny))
    elif scents[nx][ny][0] == shark:
      my_scent.append((nx, ny))
  # if there is no block with no scent
  if no_scent:
    return no_scent
  else:
    return my_scent

while True:
  if t > 1000:
    t = -1
    break
  if break_loop():
    break
  t += 1
  for i in range(1, 1 + m):
    if shark_p[i] != None:
      x, y = shark_p[i]
      d = directions[i]
      possible = possible_moves(i, x, y)
      priority = shark_priority[i][d]
      for j in priority:
        nx = x + dx[j]
        ny = y + dy[j]
        if (nx, ny) in possible:
          move(i, x, y, nx, ny, j)
          break
  update_scent()
        
print(t)