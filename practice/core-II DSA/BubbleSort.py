# Implementing a Bubble Sort

def Bubblesort(n):
    swapped = True
    while swapped:
        swapped = False
        i=0
        while i < len(n)-1:
            if n[i] > n[i + 1]:
                n[i], n[i + 1] = n[i + 1], n[i]
                swapped = True
            i+=1
    return n

n = [7,12,9,11,3]
res = Bubblesort(n)
print(res)
