class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # Max-Heap Approach to get the heaviest two stones, negate all elements to get max heap

        max_heap = [-stone for stone in stones]

        heapq.heapify(max_heap)


        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            if x!=y:
                heapq.heappush(max_heap, -(x-y))
        

        return -max_heap[0] if max_heap else 0
            

        