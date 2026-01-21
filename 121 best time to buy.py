prices = [7,1,5,3,6,4]

def buysell(prices):
    curr_min = prices[0]
    curr_max = curr_min
    profit = 0
    for i in range(1,len(prices)):
        if prices[i] > curr_max:
            curr_max = prices[i]
            p  = curr_max - curr_min
            if p > profit:
                profit = p
        if prices[i] < curr_min:
            curr_min, curr_max = prices[i], prices[i] 
    return profit

print(buysell(prices))
print(buysell([7,6,4,3,1]))        

