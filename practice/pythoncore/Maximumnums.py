# Maximum Number of integer to choose

def fun(banned, n, maxSum):
    banned_set = set(banned)
    tot = 0
    count = 0
    for i in range(1,n+1):
        if i in banned_set:
            continue
        if tot + i > maxSum:
            break
        tot +=i
        count +=1
    return count


if __name__ =="__main__":
    banned = [1,2,3,4,5,6,7]
    n = 8
    maxSum = 1
    res = fun(banned,n,maxSum)
    print(res)
