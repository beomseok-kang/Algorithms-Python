def insertion_sort(l): # 내 정답
    length = len(l)
    for i in range(1, length, 1):
        print(l)
        for j in range(i, 0, -1):
            if l[j] < l[j-1]:
                l[j-1], l[j] = l[j], l[j-1]

print('test 1 (my answer)')
list_test_1 = [11, 3, 28, 43, 9, 4]
insertion_sort(list_test_1)
print(list_test_1)

def insertion_sort_answer_book(seq): # 책의 정답
    for i in range(1, len(seq)):
        print(seq)
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
    return seq

def insertion_sort_rec(seq, i=None): # 책 정답, 재귀 방식, 시작 지점을 설정할 수 있음.
    if i is None:
        i = len(seq) - 1
    if i == 0:
        return i
    insertion_sort_rec(seq, i-1)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1
    return seq

print('test 2 (book answer)')
list_test_2 = [11, 3, 28, 43, 9, 4]
list_test_3 = [11, 3, 28, 43, 9, 4]
insertion_sort_answer_book(list_test_2)
print(list_test_2)
insertion_sort_rec(list_test_3)
print(list_test_3)