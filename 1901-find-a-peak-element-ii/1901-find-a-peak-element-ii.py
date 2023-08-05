class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        for i, row in enumerate(mat):
            for j, item in enumerate(row):
                
                count = 0
                for direction in directions:
                    new_i = i + direction[0]
                    new_j = j + direction[1]
                    
                    
                    if new_i >= len(mat) or new_i < 0:
                        count += 1
                        
                    elif new_j >= len(mat[0]) or new_j < 0:
                        count += 1
                        continue
                    
                    elif mat[new_i][new_j] < mat[i][j]:
                        count += 1
                    else:
                        break
                if count == 4:
                    return [i,j]

