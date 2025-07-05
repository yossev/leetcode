class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        num_dict = {}

        for num in arr:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1

        max_num = 0

        for num, freq in num_dict.items():
            if num == freq and num > max_num:
                max_num = num
        
        return max_num if max_num > 0 else -1