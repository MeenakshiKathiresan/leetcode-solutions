class Solution:
    def numberOfMatches(self, n: int) -> int:
         
        def count(n, total):
            if n < 2: return total
            if n % 2 == 0:
                total += n//2 + count(n//2, total)
            else:
                total += (n-1)/2 + count(((n-1)/2) +1, total)
            return total
        
        total = 0
        return int(count(n, total))