# Changing keys count

def fun(s):
    count = 0
    i = 0
    for i in range(len(s)):
        if s[i].lower()!=s[i-1].lower():
            count+=1
    return count

if __name__ =="__main__":
    s ="aAbBcC"
    res = fun(s)
    print(res)
