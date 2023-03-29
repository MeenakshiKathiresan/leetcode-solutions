class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        
        for i, num in enumerate(nums):
            if target - num in numbers and i != numbers[target-num]:
                return [i, numbers[target - num]]
            
            numbers[num] = i
            
            
            
  