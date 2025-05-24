# Python program to check for a palindrome


def palindrome(n):
    rev = 0
    temp =n
    while temp > 0:
        digit = temp%10
        rev = rev*10 +digit
        temp = temp//10
    return rev

try:
    n= int(input("Enter the number : "))
    if n<0:
        print("Enter a positive number !")
    res = palindrome(n)
    if n ==res:
        print("The number is a palindrome !")
    else:
        print("The number is not a palindrome !")
except ValueError:
        print("Enter a valid number and try again !")
