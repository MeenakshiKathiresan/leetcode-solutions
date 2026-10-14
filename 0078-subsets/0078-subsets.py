class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def branch(i, curr):
            if i >= len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            branch(i + 1, curr)
            curr.pop()
            branch(i + 1, curr)

        branch(0, [])
        return res