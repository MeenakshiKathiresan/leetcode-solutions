class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # count cells surrounded by water
        
        # dfs
        
        visited = set()
        
        def dfs(i, j):
            
            count = 0
            
            # out of bounds
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])): 
                return count
            
            if (i,j) in visited or grid[i][j] == 0:
                return count
            
            
            
            count += 1
            
            visited.add((i,j))
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            
            for direction in directions:
                count += dfs(i + direction[0], j+ direction[1])
            
            return count
            
            
            
        count = 0
        
        
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if grid[i][j] == 1:
                    if i == 0 or i == (len(grid) - 1) or j == 0 or j == (len(grid[0])-1):
                        dfs(i,j)

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if grid[i][j] == 1:
                    count += dfs(i,j)
                    
        return count