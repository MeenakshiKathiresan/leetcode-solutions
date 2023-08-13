class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        small = min(a,b)
        
        count = 0
        for i in range(1, small//2 + 1):
            if a%i == 0 and b%i == 0:
                count += 1
        if max(a,b) % min(a,b) == 0: return count + 1
        return count
            