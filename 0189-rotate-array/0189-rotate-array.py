class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [1,2,3,4,5,6,7]
        
        """
        
        n = len(nums)
        k = k % n
        
        modified_count = 0
        
        start = 0
        
        while modified_count < n:
            
            curr_index = start
            curr_num = nums[start]
            while True:
                next_index = (curr_index + k) % n


                next_num = nums[next_index]
                nums[next_index] = curr_num

                curr_num = next_num
                curr_index = next_index

                modified_count += 1
            
                if start == curr_index:
                    break
            start += 1
        
      
        
        