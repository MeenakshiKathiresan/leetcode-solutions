class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        
        res = 0
        for i, ch in enumerate(s):
            if ch == "0":
                if count == 1:
                    res += count
                else:
                    res += (count * (count + 1))//2
                count = 0
            else:
                count += 1
       
            
        if count == 1:
            res += count
        else:
            res += (count * (count + 1))//2
        return res % (10 ** 9 + 7)