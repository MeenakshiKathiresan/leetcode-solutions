class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        i = len(grid) - 1
        j = len(grid[0]) - 1
        right, down = 0, 0
        
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                
                if i == len(grid) - 1:
                    down = right
                    if j < len(grid[0]) -1:
                        down = grid[i][j+1]
                else: 
                    down = grid[i+1][j]

                if j == len(grid[0]) - 1:
                    right = down
                    if i < len(grid) -1:
                        right = grid[i+1][j]
                else:
                    right = grid[i][j+1]
                    
                grid[i][j] += min(right, down)

        return grid[0][0]