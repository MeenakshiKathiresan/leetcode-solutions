class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        
        res = [0] * len(spells)
         
        for i, spell in enumerate(spells):
            
            l, r = 0, len(potions) - 1
            
            while l <= r:
                mid = (l+r)//2
                
                prod = spell * potions[mid]
                prev_prod = spell * potions[max(0, mid-1)]
                if prod >= success:
                    if prev_prod >= success and mid == 0: 
                            res[i] = len(potions)
                            break
                    elif prev_prod < success:
                        res[i] = len(potions) - mid
                        break
                    else:
                        r = mid -1
                else:
                    l = mid + 1
            
                    
        return res
                        
                
                    