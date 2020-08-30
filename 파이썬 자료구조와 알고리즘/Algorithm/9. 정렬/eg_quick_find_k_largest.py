#####################

def partition(seq):
    pivot, seq = seq[0], seq[1:]
    before = []
    after = []
    before = [x for x in seq if x <= pivot]
    after = [x for x in seq if x > pivot]
    return before, pivot, after

def find_k_largest(seq, k):
    # 먼저 피벗을 기준으로 오른쪽 왼쪽 분리
    before, pivot, after = partition(seq)
    after.append(pivot)
    length_after = len(after)
    result = []
    if k == length_after: # k와 길이가 같다면 바로 반환하면 된다.
        result.extend(after)
    elif k < length_after: # k보다 길이가 길다면 잘라주어야 한다.
        result.extend(find_k_largest(after, k))
    else: # k보다 길이가 작다면 앞에서 잘라서 붙여준다.
        result.extend(after)
        result.extend(find_k_largest(before, k - length_after))
    return result
    
#######################

import random

def swap(seq, x, y):
    seq[x], seq[y] = seq[y], seq[x]

def quick_select(seq, k, left=None, right=None):
    left = left or 0
    right = right or len(seq) - 1
    ipivot = random.randint(left, right)
    pivot = seq[ipivot]

    # 피벗을 정렬 범위 밖으로 이동
    swap(seq, ipivot, right)
    swapIndex, i = left, left
    while i < right:
        if seq[i] < pivot:
            swap(seq, i, swapIndex)
            swapIndex += 1
        i += 1
    
    # 피벗 위치 확정
    swap(seq, right, swapIndex)
    
    #피벗 위치 확인
    rank = len(seq) - swapIndex
    if k == rank:
        return seq[swapIndex]
    elif k < rank:
        return quick_select(seq, k, left=swapIndex+1, right=right)
    else:
        return quick_select(seq, k, left=left, right=swapIndex-1)

def find_k_largest_answer_book(seq, k):
    kth_largest = quick_select(seq, k)
    result = []
    for item in seq:
        if item >= kth_largest:
            result.append(item)
    return result

print(find_k_largest([7,7,7,7,8,9,2,2,4,5,6,2,0,3,3,7], 4))
print(find_k_largest_answer_book([7,7,7,7,8,9,2,2,4,5,6,2,0,3,3,7], 4))