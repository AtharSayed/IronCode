# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.

class Solution():
    def checkpal(self,n):
        i = 0
        rev = n
        new = []
        ch = 0
        for i in reversed(rev):
            if i.isalnum():
                new.append(i.lower())

        new = ''.join(new)
        original = ''.join([c.lower() for c in n if c.isalnum()])

        print("Reversed cleaned:", new)
        print("Forward cleaned :", original)

        if new == original:
            return True
        else:
            return False
if __name__ =="__main__":
    n = input("Enter the string :")
    demo = Solution()
    res = demo.checkpal(n)
    print(res)
