## Python program to calculate the sum of the digits using while loop


# def digits(n):
#     total = 0
#     for ch in str(n):
#         total += int(ch)
#     return total

def digits(n):
    total = 0
    while n > 0:
        total += n%10
        n = n//10
    return total

if __name__ =="__main__":
    try:
        n =int(input("Enter the number : "))
        res = digits(n)
        print("The sum of the digits is ",res)
    except ValueError:
        print("Enter a valid number and try again !")