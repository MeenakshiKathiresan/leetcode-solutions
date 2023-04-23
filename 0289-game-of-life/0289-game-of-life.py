class Solution(object):
    def gameOfLife(self, new_board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        
        board = copy.deepcopy(new_board)
        
        def getNeighborCount(i,j):
            count = 0
            directions = [[0,1],[0,-1],[1,0],[-1,0],[-1,1],[1,1],[1,-1],[-1,-1]]
            
            for direction in directions:
                curr_i = i + direction[0]
                curr_j = j + direction[1]
                if 0 <= curr_i < len(board) and 0 <= curr_j < len(board[0]):
                    count += board[curr_i][curr_j]
            
            return count
        
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                neigh = getNeighborCount(i,j)
                curr = board[i][j]
                if board[i][j] == 1:
                    if neigh < 2 or neigh > 3:
                        curr = 0
                else:
                    if neigh == 3:
                        curr = 1
                new_board[i][j] = curr
               
       
        return new_board