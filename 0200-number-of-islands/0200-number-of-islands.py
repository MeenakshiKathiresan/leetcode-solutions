class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # find the number of 1 components
        
        visited = set()
        
        def dfs(i,j):
            
            if (i,j) in visited:
                return 0
            
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
                return 0
            

            if grid[i][j] == "1":
            
                visited.add((i,j))

                directions = [[0,1],[0,-1],[1,0],[-1,0]]

                for direction in directions:
                    dfs(i+direction[0], j+direction[1])

                return 1
            return 0
                
        
        count = 0
        
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if (i,j) not in visited and cell != 0:
                    count += dfs(i,j)
                    
        
        return count