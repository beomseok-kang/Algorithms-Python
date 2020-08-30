a = 'aaabbbbccccccddeeeeff'

def compress_string(s):
    temp_arr = []
    temp_arr.extend(s)
    length = len(temp_arr)
    result = ''
    count = 1
    for i in range(length):
        if i == (length - 1):
            result += str(count)
            break
        if i == 0 : result += temp_arr[i]
        if temp_arr[i] == temp_arr[i+1]:
            count += 1
        else:
            result += str(count) + temp_arr[i+1]
            count = 1
    return result

print(compress_string(a))