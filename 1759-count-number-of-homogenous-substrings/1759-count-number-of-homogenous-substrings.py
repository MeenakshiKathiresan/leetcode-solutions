class Solution:
    def countHomogenous(self, s: str) -> int:
        # continuous count -> (n * n+1) /2
        
        count = 0
        prev_ch = s[0]
        
        res = 0
        for i, ch in enumerate(s):
            
            
            if prev_ch != ch:
                if count == 1:
                    res += count
                else:
                    res += (count * (count + 1))//2
                count = 0
                
            count += 1
            prev_ch = ch
            
        if count == 1:
            res += count
        else:
            res += (count * (count + 1))//2
        return res % (10 ** 9 + 7)
                