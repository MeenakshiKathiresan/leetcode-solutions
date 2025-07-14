public class Solution {
    public int[][] FloodFill(int[][] image, int sr, int sc, int color) {

        int orig = image[sr][sc];
        if (orig == color) return image;
        Queue<(int x, int y)> q = new Queue<(int, int)>();
        q.Enqueue((sr, sc));
        int m = image.Length;
        int n = image[0].Length;
        image[sr][sc] = color;

        int[,] directions = new int[4,2] {{0,1},{0,-1},{1,0},{-1,0}};

        while(q.Count > 0){
            (int x, int y) curr =  q.Dequeue();

            for (int i = 0; i < 4; i++){
                int newR = curr.x + directions[i, 0];
                int newC = curr.y + directions[i, 1];

                if (0 <= newR && newR < m && 0 <= newC && newC < n && image[newR][newC] == orig){
                    image[newR][newC] = color; 
                     q.Enqueue((newR, newC));
                }
            }
        }

        return image;
    }
}