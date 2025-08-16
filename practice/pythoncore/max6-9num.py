# Maximum number 6-9 number 

def max69_number(num):
    n = len(str(num))
    num = [int(digit) for digit in str(num)]
    i = 0
    while i < n:
        if num[i] == 6:
            num[i] = 9
            break
        i += 1
    num = "".join(str(d) for d in num)
    return int(num)
if __name__ == "__main__":
    num = 9969
    res = max69_number(num)
    print(res)
