#Using Lambda functions and returning the results with the default function to the main function

def demo(a,b):
    return lambda :a+b

if __name__ =="__main__":
    try:
        a = int(input("Enter the value of a : "))
        b = int(input("Enter the value of b : "))
        res = demo(a,b)
        print(f"The sum of the numbers is : {res()}")
    except ValueError:
        print("Enter a valid number and try again !")