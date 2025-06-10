# capitalize the title at every starting word 
class Solution():
    def capitalizeTitle(self,n):
        n = n.split()
        result = []

        for word in n:
            if len(word) <=2:
                result.append(word.lower())
            else:
                result.append(word[0].upper() + word[1:].lower())

        result  = " ".join(result)
        return  result

if __name__ =="__main__":
    n =input("Enter the title: ")
    demo = Solution()
    res = demo.capitalizeTitle(n)
    print(res)