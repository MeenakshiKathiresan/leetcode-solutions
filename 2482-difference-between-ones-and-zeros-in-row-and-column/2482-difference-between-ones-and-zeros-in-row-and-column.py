class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)
        m = len(grid[0])
        row_ones = [0] * n
        col_ones = [0] * m
        
        diff = [[0] * m for _ in range(n)]

        
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 1:
                    row_ones[i] += 1
                    col_ones[j] += 1
        for i in range(n):
            for j in range(m):
                row_one = row_ones[i]
                col_one = col_ones[j]
                
                row_zero = m - row_one
                col_zero = n - col_one
                diff[i][j] = row_one + col_one - row_zero - col_zero
        return diff