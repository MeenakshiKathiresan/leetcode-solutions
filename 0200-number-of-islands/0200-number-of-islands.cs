public class Solution {
    public int NumIslands(char[][] grid) {

                
        int res = 0;
        HashSet<(int, int)> seen = new HashSet<(int, int)>();
        int[][] directions = new int[4][] {
            new int[] {0, 1},
            new int[] {0, -1},
            new int[] {1, 0},
            new int[] {-1, 0}
        };

        for (int i = 0; i < grid.Length; i++){
            for (int j = 0; j < grid[i].Length; j++){
                if(grid[i][j] == '1' && !seen.Contains((i,j))){
                    res++;
                    Console.WriteLine($"{i}, {j}");
                    DFS(i,j);
                }
            }
        }

        void DFS(int i, int j){
            foreach (var dir in directions){
                int newX = i + dir[0];
                int newY = j + dir[1];
                if (newX >= 0 && newX < grid.Length && 
                newY >= 0 && newY < grid[newX].Length && 
                grid[newX][newY] == '1' && !seen.Contains((newX,newY))){
                    seen.Add((newX,newY));
                    DFS(newX, newY);
                }
            }
        }

        
        return res;
    }
}