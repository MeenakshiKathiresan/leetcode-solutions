from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        """
        bfs levels taken to cover all
        if all navigation done and rotten not touched - then we return -1
        """
        orange_count = 0
        total = 0
        queue = deque([])
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 1:
                    orange_count += 1

                if col == 2:
                    queue.append((i,j))
        
        if orange_count == 0: return 0
        # all rotten are the starting point
        time = -1
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        while queue:
            time += 1
            
            for _ in range(len(queue)):
                i, j = queue.popleft()

                for d in directions:
                    currX = d[0] + i
                    currY = d[1] + j
                    # in bounds
                    if 0 <= currX < len(grid) and 0 <= currY < len(grid[0]) and grid[currX][currY] == 1:
                        orange_count -= 1
                        queue.append((currX, currY))
                        grid[currX][currY] = 2
        
        if orange_count > 0: return -1
        return time