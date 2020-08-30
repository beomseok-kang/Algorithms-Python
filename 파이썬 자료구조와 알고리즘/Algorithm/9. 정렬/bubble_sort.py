def bubble_sort(l): # 내 정답
    length = len(l)-1
    for i in range(length-1):
        print(l)
        for j in range(length-i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

def bubble_sort_answer_book(seq): # 책의 정답
    length = len(seq) - 1
    for num in range(length, 0, -1):
        for i in range(num):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
    return seq

list_test_1 = [11, 3, 28, 43, 9, 4]
list_test_2 = [11, 3, 28, 43, 9, 4]

bubble_sort(list_test_1)
bubble_sort_answer_book(list_test_2)

print(list_test_1)
print(list_test_2)