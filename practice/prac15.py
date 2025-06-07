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