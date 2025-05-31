## Python program to check whether the given number is a result of power of 2


class Solution():
    def checkpwer(self,n):
        if n <= 0:
            return False
        while n % 2 == 0:
            n = n // 2
        return n == 1


if __name__ =="__main__":
    n = int(input("Enter the number : "))
    demo = Solution()
    res = demo.checkpwer(n)
    print(res)