class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        friends = []
        for i in range(n):
            friends.append(i+1)
        
        eliminate = 0
        
        while len(friends)>1:
            
            count = len(friends)
            
            eliminate = ((eliminate + k) % count)-1
            
            # cyclic
            if eliminate == -1: eliminate = len(friends)-1
                
            remove = friends.pop(eliminate)
            
            
        return friends[0]
        
        
        