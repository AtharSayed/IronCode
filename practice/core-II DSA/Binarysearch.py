# Implementing Binary Search 

def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ =="__main__":
  n = [1,2,3,4,5,6,13,44,65,78,99]
  target = int(input("Enter the number : "))
  res = search(n,target)
  print(res)

