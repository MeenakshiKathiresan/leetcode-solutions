class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        numbers = {}
        
        for i, num in enumerate(nums):
            numbers[num] = i
            
        
        for operation in operations:
            nums[numbers[operation[0]]] = operation[1]
            numbers[operation[1]] = numbers[operation[0]]
            
        
        return nums