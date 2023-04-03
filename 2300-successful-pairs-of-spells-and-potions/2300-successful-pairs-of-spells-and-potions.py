class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        
        res = [0] * len(spells)
        length = len(potions)
         
        for i, spell in enumerate(spells):
            
            l, r = 0, len(potions) - 1
            
            while l <= r:
                mid = (l+r)//2
                
                prod = spell * potions[mid]
                
                if prod >= success:
                    r = mid -1
                else:
                    l = mid + 1
                    
            res[i] = max(0, length - (r+1))
            
                    
        return res
                        
                
                    