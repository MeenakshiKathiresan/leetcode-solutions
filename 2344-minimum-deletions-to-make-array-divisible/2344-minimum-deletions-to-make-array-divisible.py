class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:

        gcd = numsDivide[0]
        for num in numsDivide[1:]:
            gcd = math.gcd(gcd, num)
        
        nums.sort()
    
        for i, num in enumerate(nums):
            if gcd % num == 0: return i
            if num > gcd:
                break
        
        return -1