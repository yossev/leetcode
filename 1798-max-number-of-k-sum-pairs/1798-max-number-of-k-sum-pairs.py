class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res, l, r = 0, 0, len(nums) - 1
        nums.sort()
        while l < r:
            S = nums[l]+nums[r]

            if S > k:
                r-=1
            elif S < k:
                l+=1
            else:
                res+=1
                l+=1
                r-=1
        return res