class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        
        def dfs(row, col, stone):
            if (stone[0],stone[1]) in visited: return 0
            
            size = 1
            visited.add((stone[0], stone[1]))
            
            # row[stone[0]].remove(stone)
            # col[stone[1]].remove(stone)
            
            print(stone)
            for r in row[stone[0]]:
                # self
                if r[1] != stone[1]:
                    size += dfs(row,col,r)
            
            for c in col[stone[1]]:
                if c[0] != stone[0]:
                    size += dfs(row, col, c)
            
            return size
            
            
        
        # adjacency list
        
        row = {}
        col = {}
        
        # 0 index as row
        # 1 index as col
        
        for stone in stones:
            if stone[0] not in row:
                row[stone[0]] = []
                
            if stone[1] not in col:
                col[stone[1]] = []
                
            row[stone[0]].append(stone)
            col[stone[1]].append(stone)
        
        
        visited = set()
        
        size = 0
        
        for stone in stones:
            if (stone[0],stone[1]) not in visited:
                size += dfs(row, col, stone)-1
 
        return size