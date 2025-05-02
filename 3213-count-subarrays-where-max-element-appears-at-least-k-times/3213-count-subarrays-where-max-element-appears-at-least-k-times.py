class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # find max element
        # when max element is contained - len - end of window
        # move right

        max_el = max(nums)

        count = 0
        res = 0
        left = 0
        for i, right in enumerate(nums):
            if right == max_el:
                count += 1
            
            while count >= k:
                res += len(nums) - i
                if nums[left] == max_el:
                    count -= 1
                left += 1
        return res

            