# Check whether the string is palindrome or not

def checkpal(n):
    total = []
    for ch in reversed(n):
        total.append(ch)
    string = ''.join(total)
    return string

if __name__ =="__main__":
    n = input("Enter the string : ")
    res = checkpal(n)
    if n == res:
        print("The string is palindrome !")
    else:
        print("The string is not a palindrome !")
