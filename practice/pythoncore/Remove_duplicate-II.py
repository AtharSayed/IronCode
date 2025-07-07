# Remove the given val elements from the array
def dup(n):
    i = 0
    while i < len(n):
        occur = n.count(n[i])
        if occur >2:
            n.remove(n[i])
            occur -=1
        else:
            i+=1
    return len(n)

if __name__ =="__main__":
    nums = [0,0,1,1,1,1,2,3,3]
    res = dup(nums)
    print(res)
