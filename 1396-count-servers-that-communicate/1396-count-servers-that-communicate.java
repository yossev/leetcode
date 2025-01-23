class Solution {
    public int countServers(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        
        // Initialize row_sum and col_sum arrays to store server counts
        int[] rowSum = new int[m];
        int[] colSum = new int[n];

        for (int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == 1){
                    rowSum[i]++;
                    colSum[j]++;
                }
            }
        }

        int result = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {  
                    if (rowSum[i] > 1 || colSum[j] > 1) {
                        result++;
                    }
                }
            }
        }

        return result;


    }
}