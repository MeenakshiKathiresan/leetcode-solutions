class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        repeat_index = -1
        l = 0 
        r = 0
        max_len = 0
        
        while r < len(s):
            
            if r>0 and s[r-1] == s[r]:
                
                if repeat_index != -1:
                    l = repeat_index
                repeat_index = r
            
            max_len = max(max_len, r-l + 1)
       
            r+= 1
        return max_len
    
    