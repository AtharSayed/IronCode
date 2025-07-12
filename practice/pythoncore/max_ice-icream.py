# Maximum Ice Cream Bars
def fun(costs,coins):
    i = 0
    tot = 0
    n = len(costs)
    costs.sort()
    while i <n:
        tot += costs[i]
        if tot>coins:
            return i
        else:
            i+=1
    return i

if __name__ =="__main__":
    costs = [10,6,8,7,7,8]
    coins = 10
    res = fun(costs,coins)
    print(res)
