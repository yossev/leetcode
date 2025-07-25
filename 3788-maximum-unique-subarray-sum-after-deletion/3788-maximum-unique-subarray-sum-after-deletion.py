class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Negative Numbers checker
        if all(n < 0 for n in nums):
            return max(nums)
        

        unique = set(nums)

        return sum(n for n in unique if n > 0)