class Solution:
    def minimumLength(self, s: str) -> int:
        
        mod_s = s
        while len(mod_s) > 0 and mod_s[0] == mod_s[-1]:
            
            if len(mod_s) == 1:
                return 1
            # remove all s[0] in front and back
            char = mod_s[0]
            i = 0
            
            while i < len(mod_s) and mod_s[i] == char:
                i += 1
                
            j = len(mod_s) - 1
            
            while  j >= 0 and mod_s[j] == char:
                j -= 1
            mod_s = mod_s[i: j+1]
            
        
        
        return len(mod_s)