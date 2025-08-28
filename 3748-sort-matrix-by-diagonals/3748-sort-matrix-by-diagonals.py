from collections import defaultdict, deque

class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(grid)
        cols = len(grid[0])
        
        # Dictionaries to store the diagonal elements
        upper_diagonals = defaultdict(list)
        lower_diagonals = defaultdict(list)

        # Collect elements for each diagonal
        for i in range(rows):
            for j in range(cols):
                diff = i - j
                if diff < 0:
                    # Upper triangle diagonals
                    upper_diagonals[diff].append(grid[i][j])
                else:
                    # Lower triangle and main diagonals
                    lower_diagonals[diff].append(grid[i][j])

        # Sort the diagonals
        for diff in upper_diagonals:
            upper_diagonals[diff].sort() # Sort ascending
            upper_diagonals[diff] = deque(upper_diagonals[diff])
        
        for diff in lower_diagonals:
            lower_diagonals[diff].sort(reverse=True) # Sort descending
            lower_diagonals[diff] = deque(lower_diagonals[diff])

        # Place the sorted elements back into the grid
        for i in range(rows):
            for j in range(cols):
                diff = i - j
                if diff < 0:
                    # Place from upper diagonals
                    grid[i][j] = upper_diagonals[diff].popleft()
                else:
                    # Place from lower diagonals
                    grid[i][j] = lower_diagonals[diff].popleft()
        
        return grid