# Return common factor between numbers
# Code needs to be memory optimized kept it for later now : O(A+B) --> Time Complexity 
if __name__ =="__main__":
        a = int(input("Enter the number : "))
        b = int(input("Enter the number : "))
        i = 1
        factor_a = []
        while i<=a:
            if a%i==0:
                factor_a.append(i)
                i+=1
            else:
                i+=1
        print(factor_a)
        j=1
        factor_b = []
        while j <= b:
            if b % j == 0:
                factor_b.append(j)
                j += 1
            else:
                j += 1
        print(factor_b)
        factor_a = set(factor_a)
        factor_b = set(factor_b)
        common = factor_a.intersection(factor_b)
        print(len(common))
