class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        grid_check = {}
        count = 0
        
        for row in grid:
                curr = tuple(row)
                if curr not in grid_check:
                    grid_check[curr] = 0
                    
                grid_check[curr] += 1
                
                
        for c in range(len(grid)):
            col = [grid[i][c] for i in range(len(grid))]
            curr = tuple(col)
            if curr in grid_check:
                count+=grid_check[curr]
                
   
                
        return count
            