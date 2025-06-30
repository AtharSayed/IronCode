# Improved Bubble sort approach
def bubblesort(mylist):
    n = len(mylist)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if mylist[j] > mylist[j+1]:
                mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
                swapped = True
        if not swapped:
            break
    return mylist

if __name__ =="__main__":
    mylist = [7,3,4,2,1,12,11]
    res = bubblesort(mylist)
    print(res)
