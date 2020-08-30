# from collections import deque

# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#   graph.append(list(map(int, input())))

# check_dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# def check(x, y):
#   if x <= -1 or x >= n or y <= -1 or y >= m:
#     return False
#   if graph[x][y] == 1:
#     return True
#   return False

# def bfs(x, y, visited):
#   queue = deque([(x,y)])
#   while queue:
#     v = queue.popleft()
#     for i, j in check_dir:
#       if check(x+i, y+j):
#         queue.append([x+i, y+j])
    
