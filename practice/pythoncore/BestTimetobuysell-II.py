# Best Time to Buy and Sell Stocks -II (Maximum Profit)

def maxProfit(prices):
    i = 0
    n = len(prices)
    profit = []
    while i < n-1:
        if prices[i+1]>prices[i]:
            buy = prices[i]
            sell = prices[i+1]
            profit.append(sell-buy)
            i+=1
        else:
            i+=1
    return sum(profit)

if __name__ =="__main__":
    prices =[7,1,5,3,6,4]
    res = maxProfit(prices)
    print(res)
