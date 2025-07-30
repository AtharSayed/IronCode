# Find all duplicates in an array
def fun(nums):
    count = {}
    dups = []
    for num in nums:
        if num in count:
            count[num]+=1
        else:
            count[num]=1
    for num,freq in count.items():
        if freq > 1:
            dups.append(num)
    return dups

if __name__ =="__main__":
    nums = [4,3,2,7,8,2,3,1]
    res = fun(nums)
    print(res)
