class Solution {
    public List<List<Integer>> generate(int numRows) {

    // DP Solution
        List<List<Integer>> triangle = new ArrayList<List<Integer>>();
        triangle.add(new ArrayList<>());
        triangle.get(0).add(1); // Init Row

        for(int rowNum = 1; rowNum < numRows; rowNum++){
            List<Integer> row = new ArrayList<>();
            List<Integer> prevRow = triangle.get(rowNum - 1);

            // First Row Element is always 1
            row.add(1);


            for (int j = 1; j < rowNum; j++){
                row.add(prevRow.get(j - 1) + prevRow.get(j));
            };
            
            // The last row element is always 1
            row.add(1);

            triangle.add(row);
        }
        return triangle;
    }
}