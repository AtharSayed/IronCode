# Rotate Array

def rotate(nums,k):
    n = len(nums)
    k = k%n
    nums[:] = nums[-k:] + nums[:-k]
    return nums

if __name__ =="__main__":
    nums = [1,2,3,4,5,6,7]
    k = int(input("Enter the nums to rotate : "))
    res = rotate(nums,k)
    print(res)
