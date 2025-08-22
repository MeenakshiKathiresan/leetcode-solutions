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

                    Queue<(int, int)> queue = new Queue<(int, int)>();
                    queue.Enqueue((i,j));

                    while(queue.Count > 0){
                        var curr = queue.Dequeue();
                        if(seen.Contains(curr)) continue;
                        seen.Add(curr);
                        foreach (var dir in directions){
                            int newX = curr.Item1 + dir[0];
                            int newY = curr.Item2 + dir[1];
                            if (newX >= 0 && newX < grid.Length && 
                            newY >= 0 && newY < grid[newX].Length && 
                            grid[newX][newY] == '1' && !seen.Contains((newX,newY))){
                                queue.Enqueue((newX, newY));
                            }
                        }
                    }
                }
            }
        }
        return res;
    }
}