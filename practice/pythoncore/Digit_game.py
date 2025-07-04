# Find if Digit Game Can Be Won
def fun(nums):
    i = 0
    sing = []
    db = []
    while i<len(nums):
        if nums[i]>=10:
            db.append(nums[i])
            i+=1
        else:
            sing.append(nums[i])
            i+=1
    if sum(sing)>sum(db) or sum(db)>sum(sing):
        return True
    else:
        return False
if __name__ =="__main__":
    nums = [1,2,3,4,5,10]
    res = fun(nums)
    print(res)
