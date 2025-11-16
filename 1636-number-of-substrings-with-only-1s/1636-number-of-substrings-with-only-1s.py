class Solution:
    def numSub(self, s: str) -> int:
        # how nany 1s are together - count
        # n x (n + 1) / 2
        count = 0
        res = 0
        curr = 0
        mod = (10 ** 9) + 7
        for ch in s:
            if ch == "1":
                count += 1
            else:
                curr = count * (count + 1)//2
                res += curr % mod
                count = 0

        curr = count * (count + 1)//2
        res += curr % mod
        return res