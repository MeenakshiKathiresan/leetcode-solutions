class Solution:
    def fib(self, n: int) -> int:
        
        def fibHelper(n, memo = {}):
            if n in memo: return memo[n]
            
            if n == 0: return 0
            if n <= 2: return 1
            
            memo[n] = fibHelper(n-1, memo) + fibHelper(n-2, memo)
            return memo[n]
        
        return fibHelper(n)