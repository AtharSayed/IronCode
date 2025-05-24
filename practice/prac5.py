# Python program to check palindrome

def pal(n):
    rev = 0
    temp = n
    while temp > 0:
        digit = temp%10
        rev = rev*10+digit
        temp = temp//10
    return rev

try:
    n = int(input("Enter the number : "))
    res = pal(n)
    if n == res:
        print("The number is palindrome !")
    else :
        print("The number is not a palindrome! ")
except ValueError:
    print("Enter a valid number !")
