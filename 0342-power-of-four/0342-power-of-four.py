class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1: return True
        for i in range(1,100):
            if pow(4,i) == n:
                return True
        return False