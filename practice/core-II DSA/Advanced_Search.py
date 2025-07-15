# Implementing Binary Search by sorting unsorted array with bubble sort first and then finding the target element 

def sorting(nums):
    swap = True
    while swap:
        swap = False
        i = 0
        while i <len(nums)-1:
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
                swap =True
                i+=1
            else:
                i+=1
    return nums
def search(nums,target):
    n = len(nums)
    left = 0
    right = len(nums)-1
    while left<=right:
        mid = (left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1

if __name__ =="__main__":
    nums = [4,3,1,7,9,2,8]
    sorting(nums)
    target =int(input("Enter the number : "))
    res = search(nums,target)
    print(res)
