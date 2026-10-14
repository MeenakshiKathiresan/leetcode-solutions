
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        res = 0
        seen = {0: 1}

        for num in nums:
            prefix_sum += num

            # We need an earlier prefix sum equal to prefix_sum - k
            res += seen.get(prefix_sum - k, 0)

            # Record the current prefix sum
            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

        return res
