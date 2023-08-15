class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        
        repeat_index = -1
        repeat_count = 0
        l = 0 
        r = 0
        prev = ""
        max_len = 0
        
        while r < len(s):
            
            if prev == s[r]:
                
                max_len = max(max_len, r-l)
                if repeat_index != -1:
                    l = repeat_index
                repeat_index = r
                repeat_count += 1
            
            
            prev = s[r]
            r+= 1
            
        s = s[::-1]
        repeat_index = -1
        repeat_count = 0
        l = 0 
        r = 0
        prev = ""
        while r < len(s):
            
            if prev == s[r]:
                max_len = max(max_len, r-l)
                if repeat_index != -1:
                    l = repeat_index
                repeat_index = r
                repeat_count += 1
            
            
            prev = s[r]
            r+= 1
        
        #max_len = max(max_len, r-l)
        if repeat_count <= 1: max_len = len(s)
        return max_len
    
    