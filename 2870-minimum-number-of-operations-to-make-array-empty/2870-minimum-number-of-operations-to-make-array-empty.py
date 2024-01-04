class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        res = 0
        for k, v in count.items():
            res += ceil(v/3)
            if v == 1:
                return -1
        return res
                