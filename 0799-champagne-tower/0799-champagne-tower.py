class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # numerator - find the pascal value of the element in the triangle
        # denominator - find denominator which is 2 pow row
        # poured - 2 pow row -1 => remaining
        # return => remaining * num/den 
        
        rows = [[0] * (i+1) for i in range(101)]
        rows[0][0] = poured
        
        for i in range(query_row +1):
            for j in range(i+1):
                quantity = (rows[i][j] - 1)/2
                
                if quantity > 0 :
                    rows[i+1][j] += quantity
                    rows[i+1][j+1] += quantity
                    
        return min(1, rows[query_row][query_glass])
                    
        
#         denom = pow(2, query_row)
        
#         rows = []
#         for index in range(query_row):
#             rows.append([])
#             curr_sum = 0
#             for i in range(index+1):
#                 if i == 0 or i == index:
#                     rows[index].append(1)
#                 else:
#                     no = rows[index-1][i-1] + rows[index-1][i]
#                     rows[index].append(no)
#         print(rows)
#         numerator = rows
        
#         return 0
 