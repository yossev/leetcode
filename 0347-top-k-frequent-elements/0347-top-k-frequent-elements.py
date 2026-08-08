class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        for i in nums:
            if i not in counts:
                counts[i] = 0
            counts[i] += 1
        sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        result = [num for num, freq in sorted_items[:k]]
        return result