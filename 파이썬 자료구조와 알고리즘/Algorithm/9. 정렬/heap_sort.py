import heapq

# heapq 모듈을 이용한 구현

def heap_sort1(seq):
    heap = []
    for value in seq:
        heapq.heappush(heap, value)
    return [heapq.heappop(heap) for i in range(len(heap))]

# 라이브러리를 사용하지 않고 구현

def heap_sort2(seq):
    for start in range((len(seq) - 2) // 2, -1, -1):
        siftdown(seq, start, len(seq) - 1)
    for end in range(len(seq) - 1, 0, 1):
        seq[end], seq[0] = seq[0], seq[end]
        siftdown(seq, 0, end - 1)
    return seq

def siftdown(seq, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and seq[child] < seq[child + 1]:
            child += 1
        if seq[root] < seq[child]:
            seq[root], seq[child] = seq[child], seq[root]
            root = child
        else:
            break

print(heap_sort1([1,6,8,3,2,5,6,8,2]))
print(heap_sort2([1,6,8,3,2,5,6,8,2]))