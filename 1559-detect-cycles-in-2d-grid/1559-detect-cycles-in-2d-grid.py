class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if (i, j) in visited:
                    continue

                queue = deque([(i, j, -1, -1)])
                visited.add((i, j))
                ch = grid[i][j]

                while queue:
                    r, c, pr, pc = queue.popleft()

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if not (0 <= nr < rows and 0 <= nc < cols):
                            continue

                        if grid[nr][nc] != ch:
                            continue

                        if nr == pr and nc == pc:
                            continue
                            
                        if (nr, nc) in visited:
                            return True

                        visited.add((nr, nc))
                        queue.append((nr, nc, r, c))

        return False