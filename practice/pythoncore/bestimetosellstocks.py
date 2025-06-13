# Best time to buy and sell stocks

def stocks(n):
    i = 0
    j = 1
    profit = 0
    if not n or len(n)<2:
        return 0

    while j<len(n):
        if n[j]>n[i]:
            profit = max(profit,n[j]-n[i])
        else:
            i =j
        j+=1
    return profit

if __name__ =="__main__":
    try:
        user_input = input("Enter integers separated by spaces: ")
        n = list(map(int, user_input.split()))
        res = stocks(n)
        print(res)
    except ValueError:
        print("Enter a valid number and try again !")