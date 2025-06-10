
# Converting Decimal to Hexadecimal number 

class Solution(object):
    def toHex(self, num):
        if num == 0:
            return "0"
        
        if num < 0:
            num = num + (1 << 32)
        
        hex_map = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
        result = []
        
        while num > 0:
            remainder = num % 16
            num = num // 16
            
            if remainder >= 10:
                digit = hex_map[remainder]
            else:
                digit = str(remainder)
            
            result.append(digit)
        
        result.reverse()
        
        return ''.join(result)
    


if __name__=="__main__":
    demo = Solution()
    num = int(input("Enter the decimal number : "))
    res = demo.toHex(num)
    print("The hex number is :",res)


