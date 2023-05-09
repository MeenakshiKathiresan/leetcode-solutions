public class Solution {
    public IList<int> SpiralOrder(int[][] matrix) {
        List<int> spiral = new List<int>();
        int count = 0;
        
        int width = matrix[0].Length;
        int height = matrix.Length;
        int len = width * height;
        int i = 0, j = 0;
        bool right = true;
        bool down = true;
        int edge = 0;
        while(count<len){
            spiral.Add(matrix[i][j]);
            if(j<width-1-edge && right){
                j++;
            }else if(i<height-1-edge && down){
                i++;
                right = false;
            }else if(j-1>=edge && !right){
                j--;
                down =false;
            }else{
                i--;
                if(i==edge+1){
                    edge += 1;
                    
                right = true;
                down = true;
                }
            }
            count+=1;
        }
        return spiral;
    }
}