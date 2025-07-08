# Array sorting with O(nlogn) Time complexity(Using Merge Sort)

class Solution(object):
    def sortArray(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]
        sortedLeft = self.sortArray(leftHalf)
        sortedRight = self.sortArray(rightHalf)
        return self.merge(sortedLeft, sortedRight)

    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

if __name__ =="__main__":
    mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
    res = Solution()
    tot = res.sortArray(mylist)
    print(tot)
