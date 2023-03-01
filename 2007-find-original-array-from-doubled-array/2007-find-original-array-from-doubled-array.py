class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # need to see if numbers have pairs
        # max/2 is the end of first array
        def search(num, start):
            
            start = start + 1
            end = len(self.nums)-1

            while start <= end:
                mid = int((start + end) / 2)

                if self.nums[mid] < num:
                    start = mid + 1
                elif self.nums[mid] > num:
                    end = mid -1
                else:
                    # pop that element
                    self.nums.pop(mid)
                    return True

            return False
        
        # binary search for element.. and pop it
        self.nums = sorted(changed)
        i = 0
        
        while i < len(self.nums):
            
            # search for ith pair
            # if exists, pop it
            if not search(self.nums[i]*2, i):
                return []
            i+=1
            
        return self.nums
            
        
     
            
            