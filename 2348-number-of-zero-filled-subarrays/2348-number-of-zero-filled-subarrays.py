class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        zero_counter = 0
        sub_count = 0 
        
        def calculate(count):
            total = 0
            for i in range(count):
                total += (i+1)
            return total
        
        for num in nums:
            if num == 0:
                zero_counter += 1
            else:
                if zero_counter > 0:
                    sub_count += calculate(zero_counter)
                    zero_counter = 0
            
        if zero_counter > 0:
            sub_count += calculate(zero_counter)
            zero_counter = 0
            
        return sub_count