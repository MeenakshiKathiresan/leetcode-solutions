class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # have 2 sets, all num existing, all num visited

        num_map = set(nums)
        visited = set()
        res = 0

        for num in nums:
            if num not in visited:
                visited.add(num)
                curr = num + 1
                count = 1
                while curr in num_map and curr not in visited:
                    count += 1
                    visited.add(curr)
                    curr += 1
                
                curr = num - 1
                while curr in num_map and curr not in visited:
                    visited.add(curr)
                    count += 1
                    curr -= 1
                res = max(res, count)


        return res