def disappear(nums):
    temp = [x for x in range(1,len(nums)+1)]
    diff = set(temp).difference(set(nums))
    return list(diff)

if __name__ =="__main__":
    nums = [1,1]
    res = disappear(nums)
    print(res)
