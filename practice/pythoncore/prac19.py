# Printing numbers in even position of the string

def evenpos(n):
    i=0
    new =[]
    while i < len(n):
        if i %2 ==0:
            new.append(n[i])
            i+=1
        else:
            new.append('')
            i+=1
    return ''.join(new)

if __name__=="__main__":
    n =input("Enter the string:")
    res = evenpos(n)
    print("The even string is :",res)
