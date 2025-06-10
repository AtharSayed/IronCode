# Python program to check for a palindrome
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        rev = 0
        temp = x
        while temp > 0 :
            digit = temp%10
            rev = rev*10+digit
            temp = temp //10
        return rev ==x

if __name__=="__main__":
    num = Solution()
    x = 121
    if num.isPalindrome(x):
        print("The number is Palindrome")
    else:
        print("The number is not palindrome")
