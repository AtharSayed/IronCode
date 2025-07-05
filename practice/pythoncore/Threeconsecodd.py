# Three consecutive odds in the array
def fun(arr):
    count  = 0
    for nums in arr:
        if nums%2 != 0:
            count +=1
        if count == 3:
            return True
    else:
        count = 0
    return False

if __name__ =="__main__":
    nums = [1,2,34,3,4,5,7,23,12]
    res = fun(nums)
    print(res)
