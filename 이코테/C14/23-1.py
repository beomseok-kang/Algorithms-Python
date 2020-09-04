import sys
input = sys.stdin.readline

n = int(input().rstrip())

students = []
for _ in range(n):
  name, korean, english, maths = input().split()
  students.append((int(korean), int(english), int(maths), name))

students.sort(key=lambda x: (-x[0], x[1], -x[2], x[3]))

for student in students:
  print(student[3])