class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        frequency_map = {}
        for num in nums:
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1

        sorted_items = sorted(frequency_map.items(), key=lambda x: (x[1], -x[0]))

        result = []
        for num, freq in sorted_items:
            result.extend([num] * freq)

        return result
