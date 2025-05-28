## Roman to Int using class and functions
class Solution(object):
    def romantoInt(self,s):
        total = 0
        prev_value = 0
        # Creating Dictionary for roman numbers and corresponding integer
        romans_int = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for ch in reversed(s):
            current = romans_int[ch]
            if current < prev_value:
                total -=current
            else:
                total +=current
                prev_value=current
        return total

if __name__=="__main__":
    num1 = Solution()
    x = "XVII"
    res = num1.romantoInt(x)
    print("The number is :",res)
