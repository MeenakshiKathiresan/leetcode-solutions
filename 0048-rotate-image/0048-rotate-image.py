class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rn = len(matrix)
        n = rn - 1

        for i in range((rn + 1)//2):
            for j in range(rn//2):
                t = matrix[i][j]
                matrix[i][j] = matrix[n-j][i]
                matrix[n-j][i] = matrix[n-i][n-j]
                matrix[n-i][n-j] = matrix[j][n-i]
                matrix[j][n-i] = t