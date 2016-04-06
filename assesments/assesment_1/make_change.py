def make_change(coins=[1], amount=0):
    if amount == 0:
        return []
    if len(coins) == 0:
        raise ("Can't make change")
    max_coin = coins[0]
    for coin in coins[1:]:
        if coin < amount and coin > max_coin:
            max_coin = coin
    return [max_coin] + make_change(coins, amount - max_coin)

if __name__ == '__main__':
    print('Your change is', make_change([1, 5, 10, 25], 42))
    print('Your change is', make_change([1, 5, 10, 25], 123))
    print('Your change is', make_change([1, 5, 10, 25, 100], 123))
