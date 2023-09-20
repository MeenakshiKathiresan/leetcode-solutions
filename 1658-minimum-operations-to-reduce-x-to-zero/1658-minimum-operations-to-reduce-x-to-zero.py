class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)  

        if total < x:
            return -1  
        
        if total == x:
            return len(nums) 

        target = total - x  

        left = 0
        current_sum = 0
        min_operations = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum > target:
                current_sum -= nums[left]
                left += 1

            if current_sum == target:
               
                operations = left + len(nums) - right - 1
                min_operations = min(min_operations, operations)

        return min_operations if min_operations != float('inf') else -1
