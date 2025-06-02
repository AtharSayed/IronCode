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
