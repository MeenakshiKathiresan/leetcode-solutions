class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        paths = set()
        
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == 1: 
                    
                    queue = deque([(i,j)])
                    
                    path = ""
                    
                    while queue:
                        (r,c) = queue.pop()
                        
                        grid[r][c] = 0

                        directions = [(0,1),(0,-1),(1,0),(-1,0)]
                        directions = {
                            'r':(0,1),
                            'l':(0,-1),
                            'd':(1,0),
                            'u':(-1,0)
                        }

                        for key, direction in directions.items():
                            curr_i = r + direction[0]
                            curr_j = c + direction[1]
                            
                            if 0 <= curr_i < len(grid) and 0 <= curr_j <len(grid[0]) and grid[curr_i][curr_j] == 1:
                                queue.append((curr_i,curr_j))
                                path+=key
                            else:
                                path += '-'
                    
                    path+="c"
                    paths.add(path)
        return len(paths)