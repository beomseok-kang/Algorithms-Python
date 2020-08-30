# 한 함수로 구현

def quick_sort_cache(seq):
    if len(seq) < 2:
        return seq
    ipivot = len(seq) // 2 # 피벗 인덱스 (그냥 중간에 있는 값)
    pivot = seq[ipivot] # 피벗
    before = [x for i, x in enumerate(seq) if x <= pivot and i != ipivot]
    after = [x for i, x in enumerate(seq) if x > pivot and i != ipivot]
    return quick_sort_cache(before) + [pivot] + quick_sort_cache(after)

# 두 함수로 구현

def partition_devided(seq):
    pivot, seq = seq[0], seq[1:] # (맨 처음에 있는 값)
    before = []
    after = []
    before = [x for x in seq if x <= pivot]
    after = [x for x in seq if x > pivot]
    return before, pivot, after
def quick_sort_cache_devided(seq):
    if len(seq) < 2:
        return seq
    before, pivot, after = partition_devided(seq)
    return quick_sort_cache_devided(before) + [pivot] + quick_sort_cache_devided(after)

# 캐시 사용 안하고 두 함수로 나누어 구현

def partition(seq, start, end):
    pivot = seq[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and seq[left] <= pivot:
            left += 1
        while left <= right and pivot < seq[right]:
            right -= 1
        if right < left:
            done = True
        else:
            seq[left], seq[right] = seq[right], seq[left]
    seq[start], seq[right] = seq[right], seq[start]
    return right
def quick_sort(seq, start, end):
    if start < end:
        pivot = partition(seq, start, end)
        quick_sort(seq, start, pivot - 1)
        quick_sort(seq, pivot + 1, end)
    return seq

print(quick_sort_cache([2,6,8,3,2,3,5,6,1,2,9]))
print(quick_sort_cache_devided([2,6,8,3,2,3,5,6,1,2,9]))

seq = [2,6,8,3,2,3,5,6,1,2,9]
print(quick_sort(seq, 5, 10))