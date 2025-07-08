# Number of elements greater then the given element in the array
def small(nums):
    i = 0
    result = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[j]<nums[i]:
                count +=1
        result.append(count)
    return result
if __name__ =="__main__":
    nums = [8,1,2,2,3]
    res = small(nums)
    print(res)
