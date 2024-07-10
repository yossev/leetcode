class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            num_str = str(x)[::-1]
        else:
            num_str = '-' + str(x)[1:][::-1]  # Handle negative sign separately

        reversed_num = int(num_str)
        
        if reversed_num > 2**31 - 1 or reversed_num < -2**31:
            return 0
        
        return reversed_num
