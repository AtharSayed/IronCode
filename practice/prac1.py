# Day-1 -21/5/2025
# Write a function is_even(n) that takes an integer n and returns even and odd based on the number
from multiprocessing.managers import Value


def is_even(n):
    if n%2 ==0:
        return "Even"
    else:
        return "Odd"

try :
    n = int(input("Enter the number : "))
    result = is_even(n)
    print("The result is ",result)
except ValueError:
    print("The entered value is invalid kindly enter proper input !!")