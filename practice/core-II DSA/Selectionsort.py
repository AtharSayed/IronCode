# Implementing Selection Sort

def selectionsort(mylist):
    n = len(mylist)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if mylist[j]<mylist[min_index]:
                min_index=j
            mylist[i],mylist[min_index]=mylist[min_index],mylist[i]
    return mylist
    
if __name__ =="__main__":
    mylist = [4,3,5,2,1]
    res = selectionsort(mylist)
    print(res)
