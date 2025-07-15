# Implementing Armstrong number using List Comprehension

def is_armstrong(n):
    temp = str(n)
    num_digit = len(temp)
    res = sum(int(dig)**num_digit for dig in temp)
    return res  if res ==n else None

if __name__ =="__main__":
    num = [x for x in range(0,100) if is_armstrong(x)]
    print(num)
