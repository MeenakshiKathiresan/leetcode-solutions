public class Solution {
    public int MinimumArea(int[][] grid) {
        int left, right, up, down;
        right = down = 0;
        left = up = 10000;

        for (int i = 0; i < grid.Length; i++){
            for (int j = 0; j < grid[0].Length; j++){
                if (grid[i][j] == 1){
                    left = Math.Min(left, j);
                    right = Math.Max(right, j);
                    up = Math.Min(up, i);
                    down = Math.Max(down, i);
                }
            }
        }
        int width = right - left + 1;
        int height = down - up + 1;
        return width * height;
        
    }
}