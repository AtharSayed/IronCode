# Maximum between increasing elements

def func(n):
    res = []
    i = 0
    while i < len(n) - 1:
        j = i + 1
        while j < len(n):
            if n[j] > n[i]:
                res.append(n[j] - n[i])
            j += 1
        i += 1

    if not res:
        return -1
    else:
        return max(res)

if __name__ =="__main__":
    n = [8,33,55,68,65,41,63]
    res = func(n)
    print(res)
