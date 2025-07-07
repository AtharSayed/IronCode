# Baseball Game  Problem
def fun(nums):
    i = 0
    new = []
    while i < len(nums):
        if nums[i].isdigit() or (nums[i][0] == '-' and nums[i][1:].isdigit()):
            new.append(int(nums[i]))
            i+=1
        elif nums[i].isalpha():
            if nums[i] == "C":
                new.pop()
                i+=1
            elif nums[i]=="D":
                new.append(new[-1]+new[-1])
                i+=1
        elif nums[i]=="+":
            tot = new[-1] + new[-2]
            new.append(tot)
            i+=1
    return sum(new)

if __name__ =="__main__":
    nums = ["5","2","C","D","+"]
    res = fun(nums)
    print(res)
