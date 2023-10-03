class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        res = 0
        
        for k, v in counter.items():
            for i in range(1, v):
                res += i
                
        return res