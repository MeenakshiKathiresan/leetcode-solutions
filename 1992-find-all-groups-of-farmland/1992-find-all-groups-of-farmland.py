class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        # dfs
        # visited
        res = []
        visited = set()
        dir = [[0,1],[1,0]]
        
        def dfs(r, c):
            if 0 <= r <len(land) and 0 <= c < len(land[0]):
                if (r,c) not in visited:
                    if land[r][c] == 1:
                        print(r,c)
                        res[-1][2] = max(r, res[-1][2])
                        res[-1][3] = max(c, res[-1][3])
                        for d in dir:
                            dfs(r + d[0], c + d[1])
                    visited.add((r,c))
        
        for i, row in enumerate(land):
            for j, col in enumerate(row):
                if (i,j) not in visited and land[i][j] == 1: 
                    res.append([i,j,0,0])
                    
                    dfs(i,j)
                    
        return res