# Remove the given val elements from the array leetcodee

def fun(nums,val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.remove(nums[i])
        else:
            i += 1
    return len(nums)

if __name__ =="__main__":
    nums = [0,1,2,2,3,0,4,2]
    val  = 2
    res = fun(nums,val)
    print(res)
