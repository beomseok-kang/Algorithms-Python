def find_max_unimodal_array(l):
    len_l = len(l)
    mid = len_l // 2

    if l[mid] > l[mid+1] and l[mid] > l[mid-1]:
        return l[mid]
    elif l[mid] > l[mid+1] and l[mid] < l[mid-1]:
        return find_max_unimodal_array(l[:mid])
    else:
        return find_max_unimodal_array(l[mid+1:])

def find_max_unimodal_book_answer(A):
    if len(A) <= 2:
        return None
    left = 0
    right = len(A) - 1
    while right > left + 1:
        mid = (left + right) // 2
        if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
            return A[mid]
        elif A[mid] > A[mid-1] and A[mid] < A[mid+1]:
            left = mid
        else:
            right = mid
    return None


ll = [1,2,3,4,5,6,8,7,5,4,3,2,1]

print(find_max_unimodal_array(ll))