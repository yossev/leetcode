class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        if n == 1:
            return float(1)
        else:
            return float(0.5)