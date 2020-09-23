# from copy import deepcopy
# # shark number is 9999

# dx = [False, -1, -1, 0, 1, 1, 1, 0, -1]
# dy = [False, 0, -1, -1, -1, 0, 1, 1, 1]

# def newP(x, y, d):
#   if d >= 9:
#     d -= 8
#   nx = x + dx[d]
#   ny = y + dy[d]
#   return nx, ny, d

# graph = []
# fish = [None] * 17
# for i in range(4):
#   row = list(map(int, input().split()))
#   temp = []
#   for j in range(4):
#     temp.append((row[2 * j], row[2 * j + 1]))
#     fish[row[2 * j]] = (i, j)
#   graph.append(temp)

# def print_g():
#   for i in range(4):
#     print(graph[i])

# def rearrange(graph, fish):
#   for i in range(1, 17):
#     if fish[i] == None:
#       continue
#     x, y = fish[i]
#     f, d = graph[x][y]
#     for _ in range(8):
#       nx, ny, d = newP(x, y, d)
#       if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
#         d += 1
#         continue
#       elif graph[nx][ny] and graph[nx][ny][0] == 9999:
#         d += 1
#         continue
#       else:
#         if graph[nx][ny] == None:
#           graph[x][y] = None
#           graph[nx][ny] = (f, d)
#           fish[f] = (nx, ny)
#         else:
#           # 바꿔주고 넣기
#           graph[x][y] = (f, d)
#           nf = graph[nx][ny][0]
#           graph[nx][ny], graph[x][y] = graph[x][y], graph[nx][ny]
#           fish[f], fish[nf] = fish[nf], fish[f]
#         break

# def get_positions(graph, shark):
#   x, y = shark
#   d = graph[x][y][1]
#   nx, ny = x, y
#   positions = []
#   while True:
#     nx += dx[d]
#     ny += dy[d]
#     if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
#       break
#     if not graph[nx][ny] == None:
#       positions.append((nx, ny))
#   return positions

# result = 0

# def dfs(graph, fish, x, y, total):
#   global result
#   array = deepcopy(graph)
#   fish = deepcopy(fish)

#   #현재 위치의 물고기 먹기
#   f, d = array[x][y]
#   total += f
#   array[x][y] = (9999, d)
#   fish[f] = None

#   rearrange(array, fish)

#   positions = get_positions(array, (x, y))
#   if len(positions) == 0:
#     result = max(result, total)
#     return
#   for nx, ny in positions:
#     dfs(array, fish, nx, ny, total)

# dfs(graph, fish, 0, 0, 0)
# print(result)