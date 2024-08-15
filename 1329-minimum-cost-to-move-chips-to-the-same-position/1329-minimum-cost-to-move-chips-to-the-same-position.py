class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        countEven = 0
        countOdd = 0
        for i in range(len(position)):
            if position[i] % 2 == 0:
                countEven += 1
            else:
                countOdd += 1
        return min(countEven, countOdd)
