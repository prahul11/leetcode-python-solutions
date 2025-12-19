coins = [1,2,5]
amount = 11
# https://zhenyu0519.github.io/2020/02/27/lc322/
def coinChange( coins, amount: int) -> int:
    new_coins = sorted(coins)
    dp = [amount for _ in range(amount+1)]
    print(dp)
    dp[0] = 0
    print(dp)
    #dp[11]=5 means 5 coins will get 11 
    for each_amo in range(1,amount+1):
        for coin in new_coins:
            if coin <= each_amo:
                print(f"{each_amo=}, {coin=}")
                dp[each_amo] = min(dp[each_amo], 1+dp[each_amo-coin])
                print(dp)
            else:
                break
    return dp[amount] if dp[amount]<=amount else -1

coinChange(coins, amount)


def coinchange(coins, amount):
    # dp = [amount + 1 for _ in range(amount+1)]
    dp = [amount + 1] * (amount+1)
    dp[0] = 0
    for each_amount in range(1, amount +1):
        for a_coin in coins:
            if a_coin <=each_amount:
                dp[each_amount] = min(dp[each_amount] , dp[each_amount-a_coin] +1)
    return dp[amount] if dp[amount] != (amount +1) else -1


coinchange(coins, amount)