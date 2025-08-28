class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        # All elements in the same diagonal have the same i - j value
        matrix = mat
        diagonals = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                diagonals[i - j].append(matrix[i][j])
        

        # 2 -  Sort the diagonals
        for key in diagonals:
            diagonals[key].sort(reverse=True) # to pop from end
        

        # 3 put sorted elements back
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = diagonals[i - j].pop()
        

        return (matrix)



        