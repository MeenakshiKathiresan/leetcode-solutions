class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index_map = {}
        for i, num in enumerate(nums):
            index_map[num] = i
        
        for i, num in enumerate(nums):
            x = target - num 
            if x in index_map and index_map[x] != i:
                return [i, index_map[x]]