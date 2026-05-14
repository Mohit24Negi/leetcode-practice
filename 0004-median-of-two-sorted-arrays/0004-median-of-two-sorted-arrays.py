class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = sorted(nums1 + nums2)
        if len(a)%2 ==0:
            return sum(a[len(a)//2-1:len(a)//2+1])/2
        else:
            return a[len(a)//2]