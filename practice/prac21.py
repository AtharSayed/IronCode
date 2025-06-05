# Python program to find extra character between two strings

def diff(s,t):
    s_list = list(s)
    for char in t:
        if char in s_list:
            s_list.remove(char) # For better tracking of the variable it is removed
        else:
            return char
if __name__ =="__main__":
    try:
        s = input("Enter the string : ")
        t = input("Enter the second string : ")
        res = diff(s,t)
        print("The difference between the string is : ",res)
    except ValueError:
        print("Enter a valid number and try again !")
