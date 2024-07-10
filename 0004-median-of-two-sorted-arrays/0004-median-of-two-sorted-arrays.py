class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = nums1+nums2
        merged.sort()
        median = 1
        n = len(merged)

        if n % 2 != 0:  
            median = merged[n // 2]  
        else:  
            median = (merged[n // 2 - 1] + merged[n // 2]) / 2.0
        
        return median