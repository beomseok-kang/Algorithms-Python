import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))

cards.sort()

for q in queries:
  print(bisect_right(cards, q) - bisect_left(cards, q), end=" ")