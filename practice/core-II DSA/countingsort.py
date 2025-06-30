# Counting sort
def countingsort(arr):
    max_val = max(arr)
    count = [0]*(max_val+1)

    while len(arr)>0:
        num = arr.pop(0)
        count[num]+=1

    for i in range(len(count)):
        while count[i]>0:
            arr.append(i)
            count[i]-=1
    return arr

if __name__ =="__main__":
    myarr = [2,3,4,5,1,6]
    res = countingsort(myarr)
    print(res)
