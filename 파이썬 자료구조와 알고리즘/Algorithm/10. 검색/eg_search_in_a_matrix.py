def search_in_a_matrix(m1, value):
    rows = len(m1)
    cols = len(m1[0])
    lo = 0
    hi = rows * cols

    while lo < hi:
        mid = (lo + hi) // 2
        row = mid // cols
        col = mid % cols
        v = m1[row][col]
        if v == value:
            return True
        elif v > value:
            hi = mid
        else:
            lo = mid + 1
    return False

matrix = [[1,3,5], [7,9,11], [13,15,17]]

print(search_in_a_matrix(matrix, 2))
print(search_in_a_matrix(matrix, 3))

