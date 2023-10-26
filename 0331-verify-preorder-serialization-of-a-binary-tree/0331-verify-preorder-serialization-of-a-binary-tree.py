class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        items = 1

        for node in preorder.split(','):
            items -= 1
            
            if items < 0:
                return False
            
            if node != '#':
                items += 2
        
        return items == 0