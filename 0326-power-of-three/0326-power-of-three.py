class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 3^19 = 1162261467, this is the largest power 3 number for 32bit
        # any odd number needs to divide this number perfectly, or otherwise its not a power of 3

        return n > 0 and 1162261467 % n == 0
