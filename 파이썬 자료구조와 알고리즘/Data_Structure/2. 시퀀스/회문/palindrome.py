a = 'hello world!'
b = '여보 안경 안보여'

def is_palindrome(s):
    original_str = s.replace(' ', '')
    temp_str = original_str
    temp_arr = []
    temp_arr.extend(temp_str)
    temp_arr.reverse()
    temp_str = ''.join(temp_arr)
    return temp_str == original_str

print(is_palindrome(a))
print(is_palindrome(b))