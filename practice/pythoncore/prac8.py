## Roman to Integer

class Solution():
    def romantoInt(self,s):
        total = 0
        prev_state = 0
        romans_map = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for ch in reversed(s):
            current = romans_map[ch]
            if current < prev_state:
                total -= current
            else:
                total +=current
                prev_state=current
        return total

if __name__=="__main__":
    demo = Solution()
    try:
        x = str(input("Enter the roman numeral : "))
        res = demo.romantoInt(x)
        print("The integer representation of the number is : ", res)
    except ValueError as e :
        print("Error",e)