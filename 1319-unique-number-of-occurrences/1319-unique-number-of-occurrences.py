class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        nums = {}

        # Count occurrences of each number in the array
        for i in arr:
            if i in nums:
                nums[i] += 1
            else:
                nums[i] = 1

        # Check if all occurrence counts are unique
        occurrences = list(nums.values())
        return len(occurrences) == len(set(occurrences))
