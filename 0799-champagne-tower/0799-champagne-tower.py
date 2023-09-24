class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        rows = [[0] * (i+1) for i in range(101)]
        rows[0][0] = poured
        
        for i in range(query_row +1):
            for j in range(i+1):
                quantity = (rows[i][j] - 1)/2
                
                if quantity > 0 :
                    rows[i+1][j] += quantity
                    rows[i+1][j+1] += quantity
                    
        return min(1, rows[query_row][query_glass])
                    
        