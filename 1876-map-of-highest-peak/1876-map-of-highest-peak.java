import java.util.*;

class Solution {
    public int[][] highestPeak(int[][] isWater) {
        int rows = isWater.length;
        int cols = isWater[0].length;
        int[][] result = new int[rows][cols];
        Queue<int[]> queue = new LinkedList<>();

        // Initialize the queue and set initial heights
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (isWater[i][j] == 1) {
                    result[i][j] = 0; // Water cells start at height 0
                    queue.offer(new int[]{i, j});
                } else {
                    result[i][j] = -1; // Land cells are unvisited
                }
            }
        }

        // Directions for neighboring cells: up, down, left, right
        int[][] directions = {
            {-1, 0}, {1, 0}, {0, -1}, {0, 1}
        };

        // BFS traversal
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int row = cell[0], col = cell[1];

            for (int[] dir : directions) {
                int newRow = row + dir[0];
                int newCol = col + dir[1];

                // If the cell is within bounds and unvisited
                if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols && result[newRow][newCol] == -1) {
                    result[newRow][newCol] = result[row][col] + 1; // Set height
                    queue.offer(new int[]{newRow, newCol}); // Add to queue
                }
            }
        }

        return result;
    }
}