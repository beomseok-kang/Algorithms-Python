from deque import Deque
import string
import collections

def check_palindrome(string):
    temp = string.lower()
    d = Deque()
    for i in temp:
        if not i in " '\"":
            d.enqueue_back(i)
        else:
            continue
    
    h_leng = d.size() // 2
    for i in range(h_leng):
        if d.dequeue() == d.dequeue_front():
            continue
        else:
            return False
    return True

STRIP = string.whitespace + string.punctuation + "\"'"
def check_palindrome_answer_book(str1):
    d = Deque()

    for s in str1.lower():
        if s not in STRIP:
            d.enqueue(s)
    
    eq = True
    while d.size() > 1 and eq:
        if d.dequeue_front() != d.dequeue():
            eq = False

    return eq


palindrome = 'Madam Im Adam'
not_palindrome = 'Hello World!'
print(check_palindrome(palindrome))
print(check_palindrome(not_palindrome))

print(check_palindrome_answer_book(palindrome))
print(check_palindrome_answer_book(not_palindrome))