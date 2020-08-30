# 첫 번째 방식

def merge_sort(seq):
    if len(seq) < 2:
        return seq
    mid = len(seq) // 2 # 중간점 찾기
    left, right = seq[:mid], seq[mid:]
    if len(left) > 1: # 재귀
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)
    
    result = []
    while left and right: # 좌측 배열과 우측 배열 병합
        if left[-1] >= right [-1]:
            result.append(left.pop())
        else:
            result.append(right.pop())
    result.reverse()
    return (left or right) + result # 합쳐진 배열 반환

# 두 번째 방식

def merge_sort_sep(seq):
    if len(seq) < 2:
        return seq
    mid = len(seq) // 2
    left = merge_sort_sep(seq[:mid])
    right = merge_sort_sep(seq[mid:])
    return merge(left, right)

def merge(left, right):
    if not left or not right:
        return left or right
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: # left와 right가 정렬되어 있다는 가정 하에 둘을 순차적으로 병합
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if left[i:]:
        result.extend(left[i:])
    if right[j:]:
        result.extend(right[j:])
    return result

# 두 정렬된 배열을 정렬

def merge_2n(left, right):
    if not left or not right:
        return left or right
    result = []
    while left and right:
        if left[-1] >= right[-1]:
            result.append(left.pop())
        else:
            result.append(right.pop())
    result.reverse()
    return (left or right) + result


# 제자리 정렬로 구현

def merge_two_arrays_inplace(l1, l2):
    if not l1 or not l2:
        return l1 or l2
    p2 = len(l2) - 1
    p1 = len(l1) - len(l2) -1
    p12 = len(l1) -1
    while p2 >= 0 and p1 >= 0:
        item_to_be_merged = l2[p2]
        item_bigger_array = l1[p1]
        if item_to_be_merged < item_bigger_array:
            l1[p12] = item_bigger_array
            p1 -= 1
        else:
            l1[p12] = item_to_be_merged
            p2 -= 1
        p12 -= 1
    return l1

# 파일 병합

def merge_files(list_files):
    result = []
    final = []
    for filename in list_files:
        aux = []
        with open(filename, 'r') as file:
            for line in file:
                aux.append(int(line))
        result.append(aux)
    final.extend(result.pop())
    for l in result:
        final = merge(l, final)
    return final

print(merge_sort([6,3,5,7,9,5,3,2,1]))
print(merge_sort_sep([6,3,5,7,9,5,3,2,1]))
seq1 = [1,2,4,5,8,9]
seq2 = [2,4,6,6,8]
print(merge_2n(seq1, seq2))

seq1 = [1,2,4,5,8,9,0,0,0,0,0]
seq2 = [2,4,6,6,8]
merge_two_arrays_inplace(seq1, seq2)
print(seq1)

list_files = ['./a.dat', './b.dat', './c.dat']
print(merge_files(list_files))