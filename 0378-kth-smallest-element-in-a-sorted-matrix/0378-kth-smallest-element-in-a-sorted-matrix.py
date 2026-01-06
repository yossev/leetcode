class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Flatten The Matrix from 2D to 1D
        m = sum(matrix, [])
        # Turn this into a priority Queue / Heap
        heapq.heapify(m)

        # Keep Popping till we reach kth element
        for i in range(k-1):
            heapq.heappop(m)
        

        # Finally pop the kth element and return it

        return heapq.heappop(m)
