# Implementing Quick Sort

def quicksort(nums):
    if len(nums)<=1:
        return nums
    pivot = nums[len(nums)//2]
    middle = [x for x in nums if x==pivot]
    left = [x for x in nums if x<pivot]
    right = [x for x in nums if x>pivot]
    return quicksort(left) + middle + quicksort(right)




if __name__ =="__main__":
    nums = [9,8,7,6,5,4,3,2,1]
    res = quicksort(nums)
    print(res)
