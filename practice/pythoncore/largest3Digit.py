# Largest 3 Digit same number in a String 

def largest(num):
    n = len(num)
    i = 0
    res = []

    while i <= n-3:
        if num[i]==num[i+1]==num[i+2]:
            res.append(num[i:i+3])
            i+=3
        else:
            i+=1
    if res:
        return max(res)
    else:
        return ""

if __name__ == "__main__":
    num = input("Enter the string: ")
    res = largest(num)
    print(res)
