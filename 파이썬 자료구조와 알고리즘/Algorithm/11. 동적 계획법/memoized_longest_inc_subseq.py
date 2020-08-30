from bisect import bisect
from itertools import combinations
from functools import wraps
from benchmark import benchmark

def naive_longest_inc_subseq(seq):
    for length in range(len(seq), 0, -1):
        for sub in combinations(seq, length):
            if list(sub) == sorted(sub):
                return len(sub)

def dp_longest_inc_subseq(seq):
    L = [1] * len(seq)
    res = []
    for cur, val in enumerate(seq):
        for pre in range(cur):
            if seq[pre] <= val:
                L[cur] = max(L[cur], 1 + L[pre])
    return max(L)

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

def memoized_longest_inc_subseq(seq):
    @memo
    def L(cur):
        res = 1
        for pre in range(cur):
            if seq[pre] <= seq[cur]:
                res = max(res, 1 + L(pre))
        return res
    return max(L(i) for i in range(len(seq)))

def longest_inc_bisec(seq):
    end = []
    for val in seq:
        idx = bisect(end, val)
        if idx == len(end):
            end.append(val)
        else:
            end[idx] = val
    return len(end)

s1 = [94, 8, 78, 22, 38, 79, 93, 8, 84, 39]

@benchmark
def test_naive():
    print(naive_longest_inc_subseq(s1))

@benchmark
def test_dynamic_programming():
    print(dp_longest_inc_subseq(s1))

@benchmark
def test_memoization():
    print(memoized_longest_inc_subseq(s1))

@benchmark
def test_bisec():
    print(longest_inc_bisec(s1))

test_naive()
test_dynamic_programming()
test_memoization()
test_bisec()