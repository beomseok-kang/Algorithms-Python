n = 20

def n_fibonacci(num):
    result = 1
    fibonacci_arr = []
    for i in range(num):
        fibonacci_arr.append(result)
        if i < 2: continue
        temp = fibonacci_arr[i-1]
        result += temp
    return result

print(n_fibonacci(n))
