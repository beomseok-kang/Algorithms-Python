def sequential_search(seq, n):
    for item in seq:
        if item == n:
            return True
    return False

l = [5,8,3,3,4,6,2,2,9,1]
print(sequential_search(l, 1))
print(sequential_search(l, 10))