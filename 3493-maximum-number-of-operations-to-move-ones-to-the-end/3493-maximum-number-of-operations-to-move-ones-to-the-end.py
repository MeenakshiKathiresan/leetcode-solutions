class Solution:
    def maxOperations(self, s: str) -> int:
        # 1 seen so far
        # when 0, enable can load
        # when 1 and can load, add 0 seen so far

        count_1 = 0
        can_load = False
        res = 0
        for ch in s:
            if ch == "1":
                if can_load:
                    res += count_1
                count_1 += 1
                can_load = False
            else:
                can_load = True
        
        if s[-1] == "0":
            res += count_1
        return res