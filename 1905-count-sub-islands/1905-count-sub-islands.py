class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        
        count = 0
        
        def dfs(grid1, grid2, i , j):
            
            
            if not (0 <= i < len(grid2) and 0 <= j <len(grid2[0])):
                return True
            
            
            if grid2[i][j] == 0:
                return True
            
            if grid2[i][j] != grid1[i][j]:
                return False
            
            grid2[i][j] = 0
            
            matched = True
            
            
            
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            
            for direction in directions:
                currI = i + direction[0]
                currJ = j + direction[1]
                
                if not dfs(grid1, grid2, currI, currJ):
                    matched = False
                
            return matched
            
            
            
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                
                if grid2[i][j] == 1:
                    
                    if dfs(grid1, grid2, i, j):
                        count += 1
                        
        return count
        
        