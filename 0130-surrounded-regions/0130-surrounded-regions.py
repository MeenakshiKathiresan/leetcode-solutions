class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        follow all o's connected to the edges and mark as visited
        
        iterate through who whole, not visited os are flipped to X
        """
        visited = set()
        
        def dfs(i, j):
            if (i,j) not in visited:
                visited.add((i,j))
                directions = [[1,0], [-1,0], [0,1],[0,-1]]
                
                for direction in directions:
                    new_i = i + direction[0]
                    new_j = j + direction[1]
                    
                    if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]):
                        if board[new_i][new_j] == "O":
                            dfs(new_i,new_j)
     
        for i in range(len(board)):
            j_0 = 0
            j_n = len(board[0]) -1
            
            if board[i][j_0] == "O":
                dfs(i, j_0)
                
            if board[i][j_n] == "O":
                dfs(i, j_n)
                
        for j in range(len(board[0])):
            i_0 = 0
            i_n = len(board) -1
            
            if board[i_0][j] == "O":
                dfs(i_0, j)
                
            if board[i_n][j] == "O":
                dfs(i_n, j)
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i,j) not in visited:
                    board[i][j] = "X"
            
            