from functools import wraps
from benchmark import benchmark

def memo(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@memo
def fib_memo(n):
    if n < 2:
        return 1
    else:
        return fib_memo(n-1) + fib_memo(n-2)

def fib_without_memo(n):
    if n < 2:
        return 1
    else:
        return fib_without_memo(n-1) + fib_without_memo(n-2)

@benchmark
def test_memo(n):
    print(fib_memo(n))

@benchmark
def test_without_memo(n):
    print(fib_without_memo(n))

test_memo(35)
test_without_memo(35)