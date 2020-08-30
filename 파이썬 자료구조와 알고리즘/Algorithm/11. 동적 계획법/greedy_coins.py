coins = [500, 100, 50, 10]

def greedy_coins(money):
    result = []
    count = 0
    for coin in coins:
        num_coin = money // coin
        count += num_coin
        result.append(num_coin)
        money = money % coin
    return result, count

m = 5380
r, c = greedy_coins(m)
print(r, c)

