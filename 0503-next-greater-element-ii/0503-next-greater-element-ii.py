class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n
        stack = []  # stores indices

        for i in range(2 * n):
            curr = nums[i % n]

            while (stack and curr > nums[stack[-1]]):
                prev_index = stack.pop()
                res[prev_index] = curr
            
            if i < n:
                stack.append(i)

        return res




