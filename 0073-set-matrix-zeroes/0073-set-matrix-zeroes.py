class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_cols = set()

        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if col == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        

        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0