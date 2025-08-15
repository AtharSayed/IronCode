# Finding the median of two sorted arrays
import statistics

def find_median(nums1,nums2):
    merged = sorted(nums1+nums2)
    n = len(merged)
    if n % 2 == 1:
        return merged[n//2]
    else:
        return (merged[n//2]-1 + merged[n//2])/2.0
    

if __name__ =="__main__":
    nums1 = [1,3]
    nums2 = [2]
    res  = find_median(nums1,nums2)
    print(res)
