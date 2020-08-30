def selection_sort(l): # 내 정답
    length = len(l)
    for i in range(length-1):
        print(l)
        j_min = i
        for j in range(i, length):
            if l[j] < l[j_min]:
                j_min = j
        l[i], l[j_min] = l[j_min], l[i]

def selection_sort_answer_book(seq):
    length = len(seq)
    for i in range(length-1):
        print(seq)
        min_j = i
        for j in range(i+1, length):
            if seq[min_j] > seq[j]:
                min_j = j
        seq[i], seq[min_j] = seq[min_j], seq[i]
    return seq

list_test_1 = [11, 3, 28, 43, 9, 4]
list_test_2 = [11, 3, 28, 43, 9, 4]

print('test 1 (book answer)')

selection_sort(list_test_1)
print(list_test_1)

print('test 2 (book answer)')

selection_sort_answer_book(list_test_2)
print(list_test_2)