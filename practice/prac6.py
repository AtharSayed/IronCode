# To check for armstrong number

def armstrong(n):
        arm = 0
        n = str(n)
        digit = len(n)
        for ch in n:
            arm += int(ch) ** digit
        return arm

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