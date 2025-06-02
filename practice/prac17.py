# Converting roman number to integer 

class Solution():
    def romantoint(self,no):
        total = 0
        prev_state = 0
        current_state = 0
        roman_map = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for ch in reversed(no):
            current_state = roman_map[ch]

            if current_state < prev_state:
                total -=current_state
            else:
                total +=current_state
            prev_state = current_state
        return total



if __name__ =="__main__":
    no  = input("Enter the roman number :")
    demo = Solution()
    res = demo.romantoint(no)
    print(res)

