class Solution:
    def convert(self, st: str, numRows: int) -> str:
        
        if numRows == 1:
            return st
    
        rows = [""] * numRows
        
        current = 0
        down = True
        for i, s in enumerate(st):
            rows[current] += s
            
            if down:
                current += 1 
            else:
                current -= 1
            
            if current == len(rows):
                down = False
                current -= 2
            elif current == -1:
                down = True
                current += 2
        return ''.join(rows)
            