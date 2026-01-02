class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        counter = Counter(nums)
        for k, v in counter.items():
            if v == n:
                return k