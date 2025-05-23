### Finding maximum of two numbers

def find_max(a, b):
    if a > b:
        return a
    elif a == b:
        return "Both numbers are the same"
    else:
        return b
try:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    result = find_max(a, b)
    print("The max of two numbers is:", result)
except ValueError:
    print("Enter a valid number!!")
