from collections import defaultdict

def count_sort_dict(a):
    b, c = [], defaultdict(list)
    for x in a:
        c[x].append(x)
    for k in range(min(c), max(c) + 1):
        b.extend(c[k])
    return b

seq = [3,5,2,6,8,1,0,3,5,6,2,5,4,1,5,3]

result = count_sort_dict(seq)
print(result)