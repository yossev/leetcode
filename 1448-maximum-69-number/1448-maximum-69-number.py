class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = list(str(num))

        for i in range(0, len(num_str)):
            if num_str[i] == '6':
                num_str[i] = '9'
                break
        return int("".join(num_str))