# removing duplicate elements in a sorted array

class Solution(object):
    def removeDuplicates(self,n):
        i = 0
        while i < len(n)-1:
            if n[i] == n[i+1]:
                n.pop(i+1)
            else:
                i+=1
        return len(n)


if __name__ =="__main__":
    demo = Solution()
    n = [0,1,1,2,3,3,4]
    count = demo.removeDuplicates(n)
    print("The number of unique elements are : : ",count)
