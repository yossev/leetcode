class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] += 1
        

        return [item[0] for item in heapq.nlargest(k, hashmap.items(), key=lambda x: x[1])]
