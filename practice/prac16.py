# 263. Ugly Number
# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
class Solution():
    def isUgly(self,n):
        if n<=0:
            return False
        while n%2 == 0:
            n = n//2
        while n%3 == 0:
            n = n//3
        while n %5 == 0:
            n = n//5

        return n==1

if __name__=="__main__":
    try:
        n = int(input("Enter the number : "))
        demo = Solution()
        res = demo.isUgly(n)
        print(res)
    except ValueError:
        print("Enter a valid number and try again !")

