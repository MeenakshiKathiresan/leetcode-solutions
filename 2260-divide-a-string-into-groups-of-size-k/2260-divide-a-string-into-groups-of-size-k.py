class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        curr = ""
        for i, ch in enumerate(s):
            if i % k == 0 and i > 0:
                res.append(curr)
                curr = ""
            curr += ch
        
        if len(curr) > 0:
            res.append(curr)
        
        while len(res[-1]) < k:
            res[-1]+= fill

        return res
            