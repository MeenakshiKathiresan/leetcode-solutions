public class Solution {
    public void Rotate(int[][] matrix) {
        int n = matrix.Length -1;
        for (int i = 0; i < (n + 2) / 2; i ++) {
            for (int j = 0; j < (n +1)/ 2; j++) {
                
                int temp = matrix[n  - j][i];
                matrix[n - j][i] = matrix[n  - i][n - j];
                matrix[n  - i][n - j ] = matrix[j][n  -i];
                matrix[j][n -  i] = matrix[i][j];
                matrix[i][j] = temp;
            }
        }
    }
}