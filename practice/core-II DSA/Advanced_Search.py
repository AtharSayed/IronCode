# Sorting unsorted array and then searching using binary Search
def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def bubble(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

if __name__ == "__main__":
    nums = list(map(int, input("Enter the list of numbers: ").split()))
    target = int(input("Enter the target number: "))
    bubble(nums)
    res = search(nums, target)
    print("Index of target (in sorted array):", res)
