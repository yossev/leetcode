class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Alot of inplace changes and such, meaning i should use heap ( as it sorts too )
        heapq.heapify(nums)

        num_opeations = 0

        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            ans = (min(x, y) * 2) + max(x, y)
            heapq.heappush(nums, ans)
            num_opeations+=1
        return num_opeations


