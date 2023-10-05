public class Solution {
    public void SetZeroes(int[][] matrix) {
        int row0 = 0;
        
        for(int i = 0; i < matrix.Length; i++){
            for (int j = 0; j < matrix[0].Length; j++){
                if (matrix[i][j] == 0)
                {
                    matrix[0][j] = 0;
                    if(i == 0){
                        row0 = 1;
                    }else{
                      matrix[i][0] = 0;
                    }
                }
            }
        }
        
        for(int i = 1; i < matrix.Length; i++){
            for (int j = 1; j < matrix[0].Length; j++){
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                {
                    matrix[i][j] = 0;
                }
            }
        }
        
        if (matrix[0][0] == 0){
            for (int i = 0; i <matrix.Length; i++){
                matrix[i][0] = 0;
            }
        }
        
        if(row0 == 1){
            for (int j = 0; j < matrix[0].Length; j++){
                matrix[0][j] = 0;
            }
        }
        
        
        
        
    }
}
