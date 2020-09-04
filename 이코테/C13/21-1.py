n, l, r = map(int, input().split())

countries = []
for i in range(n):
  countries.append(list(map(int, input().split())))

t = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def visit_node(graph, connection, visited, nodes):
  if not connection in nodes:
    nodes.append(connection)
  x, y = connection
  if visited[y][x]:
    return
  else:
    visited[y][x] = True
  if graph[y][x]:
    for connection in graph[y][x]:
      visit_node(graph, connection, visited, nodes)

def get_nodes(graph, visited):
  nodes_arr = []
  for y in range(n):
    for x in range(n):
      nodes = []
      if visited[y][x] == False:
        nodes.append((x, y))
        if graph[y][x]:
          for connection in graph[y][x]:
            visit_node(graph, connection, visited, nodes)
      if nodes:
        nodes_arr.append(nodes)
  return nodes_arr

def merge_population(countries, visited, nodes):
  total = 0
  for node in nodes:
    x, y = node
    total += countries[y][x]
  average = total // len(nodes)
  for node in nodes:
    x, y = node
    countries[y][x] = average

while True:
  moved = False
  graph = [[[] for _0_ in range(n)] for _1_ in range(n)]
  visited = [[False] * n for _ in range(n)]
  for y in range(n):
    for x in range(n):
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
          continue
        if l <= abs(countries[ny][nx] - countries[y][x]) <= r:
          graph[y][x].append((nx, ny))
          moved = True
  nodes_arr = get_nodes(graph, visited)
  for nodes in nodes_arr:
    merge_population(countries, visited, nodes)
  if moved == False:
    break
  t += 1

print(t)