from collections import deque

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        
        # Find the starting position '*'
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "*":
                    start = (i, j)
        
        queue = deque([(start[0], start[1], 0)])
        visited = set([(start[0], start[1])])
        
        while queue:
            curr_i, curr_j, dist = queue.popleft()
            
            if grid[curr_i][curr_j] == "#":
                return dist
            
            for direction in directions:
                new_i = curr_i + direction[0]
                new_j = curr_j + direction[1]
                
                if 0 <= new_i < rows and 0 <= new_j < cols and grid[new_i][new_j] != "X" and (new_i, new_j) not in visited:
                    queue.append((new_i, new_j, dist + 1))
                    visited.add((new_i, new_j))
                        
        return -1
