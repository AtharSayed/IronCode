# Implementing Selection Sort 
def fun(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if nums[i]>nums[j]:
                min_index = j
        nums[i],nums[min_index]=nums[min_index],nums[i]
    return nums


if __name__ =="__main__":
    nums = list(map(int,input("Enter the elements :").split()))
    res = fun(nums)
    print(res)
