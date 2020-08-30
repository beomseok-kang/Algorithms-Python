# 재귀 함수

def binary_search_rec(seq, target, low, high):
    if low > high:
        return None
    mid = (low + high) // 2
    if target == seq[mid]:
        return mid
    elif target < seq[mid]:
        return binary_search_rec(seq, target, low, mid-1)
    else:
        return binary_search_rec(seq, target, mid+1, high)

# 반복문

def binary_search_iter(seq, target):
    high, low = len(seq), 0
    while low < high:
        mid = (high + low) // 2
        if target == seq[mid]:
            return mid
        elif target < seq[mid]:
            high = mid
        else:
            low = mid + 1
    return None

l = [1,2,3,4,5,6,7,8,9,10]
target = 8
# print(binary_search_rec(l, target, 0, 10))
# print(binary_search_iter(l, target))