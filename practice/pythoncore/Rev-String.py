# Reverse String with O(1) extra memory 

def func(s):
    left = 0
    right  = len(s)-1
    while left<=right:
        s[left],s[right]=s[right],s[left]
        left +=1
        right -=1
    return s

if __name__ =="__main__":
    s = ["h", "e", "l", "l", "o"]
    res = func(s)
    print(res)
