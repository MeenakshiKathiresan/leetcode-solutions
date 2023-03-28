class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        long_0 = 0
        long_1 = 0
        
        count = 0
        
        prev = '-'
        
        if s == "1": return True
        
        for ch in s:
            if ch == prev:
                count+= 1
                if ch == "1":
                    long_1 = max(long_1, count)
                elif ch == "0":
                    long_0 = max(long_0, count)
            else:
                count = 0
            
            prev = ch
        
        return long_1 > long_0