class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = set()
        
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if grid[i][j] == "1" and (i,j) not in visited:
                    res += 1
                    stack = deque([(i,j)])
                    visited.add((i,j))
                    
                    while stack:
                        curr_i, curr_j = stack.popleft()
                        
                        for d in directions:
                            new_i = curr_i + d[0]
                            new_j = curr_j + d[1]
                            
                            if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]):
                                if grid[new_i][new_j] == "1" and (new_i, new_j) not in visited:
                                    
                                    stack.append((new_i, new_j))
                                    visited.add((new_i, new_j))
        return res
                            
                        
                    