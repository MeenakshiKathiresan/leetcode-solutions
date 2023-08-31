class Solution:
    def rob(self, numbers: List[int]) -> int:
        if len(numbers) == 1: return numbers[0]
        
        
        def rob_helper(nums):
            

            prev = nums[0]
            prev2 = 0


            for i in range(1, len(nums)):

                take = nums[i]
                if i > 1:
                    take = nums[i] + prev2

                not_take = prev

                curr = max(take, not_take)
                
                prev2 = prev
                prev = curr
                

            return prev
        
        return max(rob_helper(numbers[:len(numbers)-1]), rob_helper(numbers[1:]))