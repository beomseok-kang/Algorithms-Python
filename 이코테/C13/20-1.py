n = int(input())
graph = []
for _ in range(n):
  graph.append(input().split())

teachers = []
empties = []

for y in range(n):
  for x in range(n):
    if graph[y][x] == 'T':
      teachers.append((x, y))
    elif graph[y][x] == 'X':
      empties.append((x, y))

direction = [(0, -1), (1, 0), (0, 1), (-1, 0)] # 위 오른쪽 아래 왼쪽 순, (x, y)

def couldnt_catch(teacher, graph_copy):
  x, y = teacher
  for i in range(4):
    nx = x + direction[i][0]
    ny = y + direction[i][1]
    if teacher_catch_student(nx, ny, i, graph_copy):
      return False
  return True

def teacher_catch_student(x, y, dir_i, graph_copy):
  if x >= n or y >= n or x < 0 or y < 0:
    return False
  if graph_copy[y][x] == 'S':
    return True
  elif graph_copy[y][x] == 'O':
    return False
  nx = x + direction[dir_i][0]
  ny = y + direction[dir_i][1]
  return teacher_catch_student(nx, ny, dir_i, graph_copy)

from itertools import combinations
from copy import deepcopy

graph_copy = []
hidable = False

for iteration in combinations(empties, 3):
  graph_copy = deepcopy(graph)
  for x, y in iteration:
    graph_copy[y][x] = 'O'
  count = 0
  for teacher in teachers:
    if couldnt_catch(teacher, graph_copy):
      count += 1
  if count == len(teachers):
    hidable = True
    break

if hidable:
  print('YES')
else:
  print('NO')