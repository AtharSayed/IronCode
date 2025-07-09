# Rotate Array

def func(nums,k):
    n = len(nums)
    k = k%n
    nums[:] = nums[-k:] + nums[:-k]
    return nums


if __name__ =="__main__":
    nums = [1,2,3,4,5,6,7,8]
    k = 3
    res = func(nums,k)
    print(res)
