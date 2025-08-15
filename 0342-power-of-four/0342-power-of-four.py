class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Checks if its power of 2, then checks if its power of 4 
        # Any power of 4 modulo 3 yields 1
        if n <= 0:
            return False
        return (n & (n - 1)) == 0 and (n % 3 == 1)