# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.
class Solution():
    def sqroot(self,n):
        i = 0
        while i*i<=n:
            i +=1
        return i-1

if __name__=="__main__":
    sq = Solution()
    n = 60
    res = sq.sqroot(n)
    print("The square root of the number is : ",res)
