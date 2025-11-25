class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n = 1
        if k % 2 == 0 or k % 5 == 0: return -1
        ct = 1
        while ct < 100000:
            if n % k == 0:
                return ct
            else:
                n = n * 10 + 1
                ct += 1
        return -1