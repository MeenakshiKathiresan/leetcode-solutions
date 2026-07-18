class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        # y is the smaller number
        def gcd(x, y):
            if x % y == 0:
                return y
            else:
                return gcd(y, x % y)

        sm, lg = 10000, 0

        for num in nums:
            if num < sm:
                sm = num
            
            if num > lg:
                lg = num
        
        return gcd(lg, sm)