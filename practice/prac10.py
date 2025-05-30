# Sum of digits in a number
def calc(num):
    while num >=10:
        total = 0
        for ch in str(num):
            total += int(ch)
        num = total
    return num

if __name__=="__main__":
    try :
        n = int(input("Enter the number :"))
        res = calc(n)
        print("The digit sum is : ", res)
    except ValueError:
        print("Enter a valid number and try again !")