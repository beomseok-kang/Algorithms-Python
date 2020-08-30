# import sys

# m, n = map(int, input().split())
# graph = []
# dp = []

# for _ in range(m):
#   graph.append(tuple(map(int, sys.stdin.readline().split())))
#   dp.append([0]*n)

# dp[0][0] = 1
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# count = 0

# def find_route(x, y):
#   global count
#   if x < 0 or y < 0 or x >= n or y >= m:
#     return
#   if x == n-1 and y == m-1:
#     count += 1
#   for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if not (nx < 0 or ny < 0 or nx >= n or ny >= m):
#       if graph[ny][nx] < graph[y][x]:
#         find_route(nx, ny)

# find_route(0,0)
# print(count)