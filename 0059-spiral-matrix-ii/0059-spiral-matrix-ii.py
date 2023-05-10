class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for i in range(n)] for i in range(n)]
        count = 0
        edgeI = 0
        edgeJ = 0
        
        while count < (n*n):
            i = edgeI
            for j in range(edgeJ, n - edgeJ):
                count += 1 
                res[i][j] = count
            j = n - edgeJ - 1
            for i in range(edgeI + 1, n - edgeI):
                count += 1
                res[i][j] = count
            i = n - edgeI - 1
            for j in range(n - edgeJ - 2, edgeJ - 1, -1):
                count += 1
                res[i][j] = count
            j = edgeJ
            for i in range(n - edgeI - 2, edgeI, -1):
                count += 1
                res[i][j] = count
                
            edgeI += 1
            edgeJ += 1
            
        return res

