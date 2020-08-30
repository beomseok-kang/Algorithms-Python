from stack import Stack

def balance_parenthesis(string):
    s = Stack()

    for i in string:
        if i == '(':
            s.push(i)
        else:
            if s.isEmpty():
                return False
            s.pop()
    
    return s.isEmpty()

def balance_parenthesis_book_answer(string):
    s = Stack()
    balanced = True
    index = 0

    while index < len(string) and balanced:
        symbol = string[index]

        if symbol == '(': # '(' 가 들어오면 스택에 넣는다.
            s.push(symbol)
        else: # ')' 가 들어오면 둘 중 하나
            if s.isEmpty(): # 비어 있다면 (즉 '(' 의 수보다 ')' 의 수가 더 많다면)
                balanced = False
            else: # 아니라면 그냥 '(' 를 스택에서 하나 없애준다.
                s.pop()
        
        index += 1
    
    if balanced and s.isEmpty():
        return True
    else:
        return False

print(balance_parenthesis('(()))'))
print(balance_parenthesis('((()))'))
print(balance_parenthesis('(((())'))
print(balance_parenthesis('((()()))'))
print(balance_parenthesis_book_answer('(()))'))
print(balance_parenthesis_book_answer('((()))'))
print(balance_parenthesis_book_answer('(((())'))
print(balance_parenthesis_book_answer('((()()))'))