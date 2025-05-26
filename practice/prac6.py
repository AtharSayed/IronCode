# To check for armstrong number

def checkarm(n):
    num_str = str(n)     # Converting to string
    num_digits = len(num_str)  # string len function to count the number of elements in the string
    total = sum(int(digit)**num_digits for digit in num_str)
    return total

if __name__=="__main__":
    try:
        n = int(input("Enter the number : "))
        res = checkarm(n)
        if res == n :
            print("The number is armstrong number ")
        else:
            print("The number is not a armstrong number")
    except ValueError:
        print("Enter a valid number and try again !")