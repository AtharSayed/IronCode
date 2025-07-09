# Count Pairs
def countPairs(nums,target):
    n =len(nums)
    count = 0
    i = 0
    j = i+1
    while i < n:
        while j <n:
            if nums[i]+nums[j] < target:
                count +=1
                j+=1
            else:
                j+=1
        i+=1
        j=i+1
    return count

if __name__ =="__main__":
    nums = [-6,2,5,-2,-7,-1,3]
    target = -2
    res = countPairs(nums,target)
    print(res)
