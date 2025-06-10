<<<<<<< HEAD
# To check if the given number is a power of 4

class Solution():
    def power(self,n):
        if n<=0:
            return False
        while n % 4 == 0:
            n = n //4 
        return n ==1

if __name__ =="__main__":
    demo = Solution()
    n = int(input("Enter the number : "))
    res = demo.power(n)
    print(res)
=======
# 492. Construct the Rectangle

import math
class Solution():
    def Rectarea(self,n):
        w = math.sqrt(n)
        while w >0:
            if n%w ==0:
                return [n//w,w]
            w-=1
        return [n,1]


if __name__ == "__main__":
    n = int(input("Enter the number : "))
    demo = Solution()
    res = demo.Rectarea(n)
    print(res)
>>>>>>> d55ae3a70d549e655d8b541ac803f15d2afa05dd
