class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = sum(matrix, []) # Better than a nested loop
        heapq.heapify(m) 

        for i in range( k-1 ):
            heapq.heappop(m)
        

        return heapq.heappop(m) # Since the rest isnt important


