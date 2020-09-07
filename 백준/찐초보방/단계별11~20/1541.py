query = input()
evaluator = ''

minused = False
num = ''

for q in query:
  if q.isdigit():
    num += q
  else:
    evaluator += num.lstrip('0')
    num = ''
    if q == '+' and minused:
      evaluator += '-'
    else:
      evaluator += q
      if q == '-' and not minused:
        minused = True

evaluator += num.lstrip('0')

print(eval(evaluator))