class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        min_nums = []
        result = []

        for arr in matrix:
            min_nums.append(min(arr))
        

        transposed_matrix = list(zip(*matrix))
        max_in_columns = [max(column) for column in transposed_matrix]

        for i in max_in_columns:
            if i in min_nums:
                result.append(i)

        return result