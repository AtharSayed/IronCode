# Implementing Insertion  Sort

def func(nums):
    n = len(nums)
    for i in range(1,n):
        insert_index = i
        current_val = nums[i]
        for j in range(i-1,-1,-1):
            if nums[j] > current_val:
                nums[j+1]=nums[j]
                insert_index = j
            else:
                break
        nums[insert_index] = current_val
    return nums

if __name__ =="__main__":
    nums = [9,8,7,6,5,4,3,2,1]
    res = func(nums)
    print(res)
