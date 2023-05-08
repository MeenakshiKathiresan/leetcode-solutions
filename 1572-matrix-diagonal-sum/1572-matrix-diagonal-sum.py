class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum = 0
        n = len(mat)
        
        for i in range(n):
            for j in range(n):
                if i == j or i+j == n-1:
                    sum += mat[i][j]
        
        
        return sum