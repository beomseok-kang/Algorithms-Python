from stack import Stack

def decimal_to_nth(number, n):
    s = Stack()
    num = number
    result = ''

    while num >= n:
        s.push(num % n)
        num = num // n
    s.push(num)

    while not s.isEmpty():
        result += str(s.pop())

    return result

print(decimal_to_nth(30, 2))
print(decimal_to_nth(37, 3))