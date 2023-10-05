class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        def convertRowCol(i,j):
            for row in range(len(matrix[0])):
                if matrix[i][row] != 0:
                    matrix[i][row] = "x"
 
            for col in range(len(matrix)):
                if matrix[col][j]!= 0:
                    matrix[col][j] = "x"
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    convertRowCol(i,j)
        
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "x":
                    matrix[i][j] = 0
        