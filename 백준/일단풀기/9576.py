# import heapq

# t = int(input())

# for _ in range(t):
#   n, m = map(int, input().split())
#   queries = []
#   for __ in range(m):
#     a, b = map(int, input().split())
#     heapq.heappush(queries, (b - a, a, b))
  
#   while queries:
#     diff, a, b = heapq.heappop(queries)
