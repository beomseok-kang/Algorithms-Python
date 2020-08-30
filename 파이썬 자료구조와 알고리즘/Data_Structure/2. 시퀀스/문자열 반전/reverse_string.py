a = 'Hello World!'

def reverse_string(s):
    temp_arr = [i for i in s]
    temp_arr.reverse()
    return ''.join(temp_arr)

print(reverse_string(a))