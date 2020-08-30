def find_sqrt_binary_search(n, error=0.001):
    if n == 1:
        return 1
    low = n < 1 and n or 1
    high = n < 1 and 1 or n

    mid = (low + high) / 2
    while abs(mid**2 - n) > error:
        if mid**2 > n:
            high = mid
        elif mid**2 < n:
            low = mid
        mid = (low + high) / 2
    
    return mid

def find_sqrt_book_answer(n, error=0.001):
    lower = n < 1 and n or 1
    upper = n < 1 and 1 or n
    mid = lower + (upper - lower) / 2.0
    square = mid * mid
    while abs(square - n) > error:
        if square < n:
            lower = mid
        else:
            upper = mid
        mid = lower + (upper - lower) / 2.0
        square = mid * mid
    return mid

print(find_sqrt_binary_search(2))
print(find_sqrt_binary_search(9))
