import random

def quick_select_cache(seq, k):
    len_seq = len(seq)
    if len_seq < 2:
        return seq[0]
    
    ipivot = len_seq // 2
    pivot = seq[ipivot]
    smallerList = [x for i, x in enumerate(seq) if x <= pivot and i != ipivot]
    largerList = [x for i, x in enumerate(seq) if x > pivot and i != ipivot]

    m = len(smallerList)
    if k == m:
        return pivot
    elif k < m:
        return quick_select_cache(smallerList, k)
    else:
        return quick_select_cache(largerList, k-m-1)

def swap(seq, x, y):
    seq[x], seq[y] = seq[y], seq[x]

# def quick_select(seq, k, left=None, right=None):
#     left = left or 0
#     right = right or len(seq) - 1
#     ipivot = random.randint(left, right)
#     pivot = seq[ipivot]

#     swap(seq, ipivot, right)
#     swapIndex, i = left, left
#     while i < right:
#         if pivot < seq[i]:
#             swap(seq, i, swapIndex)
#             swapIndex += 1
#         i += 1
    
#     swap(seq, right, swapIndex)
    
#     rank = len(seq) - swapIndex
#     if k == rank:
#         return seq[swapIndex]
#     elif k < rank:
#         return quick_select(seq, k, swapIndex + 1, right)
#     else:
#         return quick_select(seq, k, left, swapIndex - 1)

seq = [3, 7, 2, 1, 4, 6, 5, 10, 9, 11]
k = len(seq) // 2
print(quick_select_cache(seq,0))
