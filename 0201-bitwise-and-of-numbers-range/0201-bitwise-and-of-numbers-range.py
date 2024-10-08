class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        shift_count = 0

        while left < right:
            left>>=1
            right>>=1
            shift_count+=1

        return left << shift_count