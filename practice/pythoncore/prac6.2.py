from prac6 import armstrong  # Importing function from the previous code file

if __name__=="__main__":
    try:
        n = int(input("Enter the number : "))
        res = armstrong(n)
        if res == n :
            print("The number is armstrong number ")
        else:
            print("The number is not a armstrong number")
    except ValueError:
        print("Enter a valid number and try again !")