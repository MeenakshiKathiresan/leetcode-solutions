class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        visited = set()
        
        def dfs(grid, i, j):
            
            
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            
            if 0 <= i < len(grid) and 0<= j < len(grid[0]):
        
                if (i,j) in visited or grid[i][j] == 1: return True
                else:
                        visited.add((i,j))
                        isClosed = True
                        
                            
                        for direction in directions:
                            currI = i + direction[0]
                            currJ = j + direction[1]
                            
                            
                            if  not dfs(grid, currI, currJ):
                                isClosed = False
                        return isClosed
            else:
                return False
        
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and (i,j) not in visited and dfs(grid, i, j):
                    count+=1
                    
        return count
                            
                            
                            
                            
                            
                            
                    