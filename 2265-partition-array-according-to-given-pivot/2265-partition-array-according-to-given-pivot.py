class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        # O(1) Space Solution

        # First Pass for: Smaller than pivot nums
        res = []
        for i in nums:
            if i < pivot:
                res.append(i)
        

        # Second Pass for: pivots
        for i in nums:
            if i == pivot:
                res.append(i)
        
        # Third Pass for: larger than pivots

        for i in nums:
            if i > pivot:
                res.append(i)

        return res