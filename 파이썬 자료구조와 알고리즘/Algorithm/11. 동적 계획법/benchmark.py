from functools import wraps
import time

def benchmark(method):
    @wraps(method)
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print('{0} s'.format(te-ts))
        return result
    return timed