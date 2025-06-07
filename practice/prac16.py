# multiplicatin table

def multip(n):
    i = 0
    while i<=10:
        print(n,"x",i,"=",n*i)
        i+=1

if __name__=="__main__":
    try:
        n  = int(input("Enter the table number : "))
        res = multip(n)
    except ValueError:
        print("Enter a valid number and try again !")
    