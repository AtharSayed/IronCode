# Removing Duplicates Elements in the sorted array

class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums)-1:
            if nums[i] ==nums[i+1]:
                nums.pop(i+1)
            else:
                i+=1
        return len(nums)

if __name__ =="__main__":
    demo = Solution()
    nums = [0,1,1,2,3,3,4]
    res =demo.removeDuplicates(nums)
    print("The total number of unique elements  in the array are : ",res)

