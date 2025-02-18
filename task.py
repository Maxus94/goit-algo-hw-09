import timeit

def find_coins_greedy(sum):
    result = {}
    coins = [50, 25, 10, 5, 2, 1]
    for coin in coins:
        while coin <= sum:
            if result.get(coin):
                result[coin] +=1
            else:
                result.update({coin: 1})
            sum -=coin
    return result
    
def find_min_coins(sum):
    coins = [50, 25, 10, 5, 2, 1]    
    min_coins_required = [0] + [float('inf')] * sum
    coins_used = [0] * (sum + 1)
    for i in range (1, sum + 1):
        for coin in coins:            
            if i >= coin and min_coins_required[i - coin] + 1 < min_coins_required[i]:
                min_coins_required[i] = min_coins_required[i - coin] + 1
                coins_used[i] = coin         
    
    coins_count = {}
    
    while sum > 0:
        coin = coins_used[sum]
        if coins_count.get(coin):
            coins_count[coin] +=1
        else:
            coins_count.update({coin: 1})                    
        sum -= coin    

    return coins_count

print(timeit.timeit('find_coins_greedy(113)', number=1000, globals=globals()), find_coins_greedy(113), " - greedy for 13")
print(timeit.timeit('find_min_coins(113)', number=1000, globals=globals()), find_min_coins(113), " - dynamic for 13\n")

print(timeit.timeit('find_coins_greedy(113)', number=1000, globals=globals()), find_coins_greedy(113), " - greedy for 113")
print(timeit.timeit('find_min_coins(113)', number=1000, globals=globals()), find_min_coins(113), " - dynamic for 113\n")

print(timeit.timeit('find_coins_greedy(1113)', number=1000, globals=globals()), find_coins_greedy(113), " - greedy for 1113")
print(timeit.timeit('find_min_coins(1113)', number=1000, globals=globals()), find_min_coins(113), " - dynamic for 1113\n")