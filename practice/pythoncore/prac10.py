# Find sqrt of a given number

def sqrt(n):
    i = 0
    while i*i<=n:
        i+=1
    return i-1


if __name__=="__main__":
    try:
        n=int(input("Enter the number : "))
        res = sqrt(n)
        print("The square root of the number is : ",res)
    except ValueError:
        print("Enter a valid number and try again !")