# Checking for monotonic Array

def func(nums):
    n = len(nums)
    i = 0
    count = 0
    while i < n - 1 and nums[i] <= nums[i + 1]:
        i += 1
        count += 1
    if count == n - 1:
        return True
    i = 0
    count = 0
    while i < n - 1 and nums[i] >= nums[i + 1]:
        i += 1
        count += 1
    if count == n - 1:
        return True

    return False

if __name__ == "__main__":
    nums = [6, 5, 4, 4]
    res = func(nums)
    print(res)
