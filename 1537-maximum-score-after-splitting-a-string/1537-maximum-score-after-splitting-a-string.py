class Solution:
    def maxScore(self, s: str) -> int:
        count_1 = s.count("1")
        count_0 = 0 
        res = 0

        for i in range(len(s) - 1):
            ch = s[i]
            if ch == "0":
                count_0 += 1
            else:
                count_1 -= 1
            
            res = max(res, count_0 + count_1)
        
        return res