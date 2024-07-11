class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count_odd = 0
        for num in arr:
            if num % 2 == 1:
                count_odd+=1
            else:
                count_odd = 0

            if count_odd == 3:
                return True
        return False 
