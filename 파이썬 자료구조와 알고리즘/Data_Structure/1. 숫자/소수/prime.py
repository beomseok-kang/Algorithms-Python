# 제곱근을 이용하는 소수 찾기.
# n이라는 숫자가 들어왔을 때, m이라는 n의 제곱근을 찾는다.
# 그리고 만약 n이 소수가 아니라면, n = a*b이다.
# 따라서 a*b = m*m이 되며, 이 경우,
# min(a,b) <= m 이 항상 성립한다.
# 따라서 m까지의 수를 검색한다면,
# 적어도 하나의 n과 나누어 떨어지는 수를 발견할 것이고,
# 이것은 n이 소수가 아님을 증명해주는 것이다.

import math

def is_prime(n):
    m = math.sqrt(n)
    i = 1
    while i < m :
        i += 1
        if n % i == 0:
            return False
            break
    return True

print(is_prime(20))