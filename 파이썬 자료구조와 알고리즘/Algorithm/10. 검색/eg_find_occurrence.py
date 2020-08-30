from binary_search import binary_search_iter

def find_occurrence(l, n):
    i = binary_search_iter(l, n)
    while l[i] == l[i-1]:
        i -= 1
    count = 1
    while l[i] == l[i+1]:
        i += 1
        count += 1
    return count

def find_occurrence_book_answer(seq, k):
    index_some_k = binary_search_iter(seq, k)
    count = 1
    sizet = len(seq)
    for i in range(index_some_k+1, sizet):
        if seq[i] == k:
            count += 1
        else:
            break
    for i in range(index_some_k-1, -1, -1):
        if seq[i] == k:
            count += 1
        else:
            break
    return count


l1 = [1,2,3,3,3,3,3,3,5,6,7,8]
print(find_occurrence(l1, 3))