data = input()
mid = int(len(data) / 2)

if sum(int(i) for i in data[:mid]) == sum(int(i) for i in data[mid:]):
  print('LUCKY')
else:
  print('READY')