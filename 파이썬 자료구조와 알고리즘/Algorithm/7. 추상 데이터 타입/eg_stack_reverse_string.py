from stack import Stack

def reverse_string_with_stack(string):
    s = Stack()
    result = ''
    
    for i in string:
        s.push(i)

    while not s.isEmpty():
        result += s.pop()

    return result

print(reverse_string_with_stack('Hello World!'))