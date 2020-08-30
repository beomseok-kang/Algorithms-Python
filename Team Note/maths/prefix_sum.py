# n 번째부터 m 번째까지의 숫자들의 합을 구하려면 P[m] - P[n-1]
# 와 같은 계산으로 구할 수 있다. 이를 prefix sum (접두사 합) 이라고
# 한다.

# number of data, n
n = 5
# all the data
data = [10, 20, 30, 40, 50]

# prefix sum calculations
sum_val = 0
prefix_sum = [0]
for d in data:
  sum_val += d
  prefix_sum.append(sum_val)

left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])