class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum = 0
        n = len(mat)
        
        for i in range(n):
            sum += mat[i][i]
           
            sum += mat[n - 1 - i][i]
        
        if n%2 == 1:
            mid = n/2
            sum -= mat[mid][mid]
        
        return sum