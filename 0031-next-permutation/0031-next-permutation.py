class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # => traverse reverse
        # => if in ascending, simple, just switch the first pair of ascending
        # => if descending, get the whole descending section, get the next biggest compared to left of the descending section. Next biggest is kept in place of left, left + all elements of descending are sorted 
        # => if fully in reverse sorted, return reverse
        
        nd = len(nums) - 1 
        cmp_nd = nd - 1 
        if nums[nd] > nums[cmp_nd]:
            temp = nums[nd]
            nums[nd] = nums[cmp_nd]
            nums[cmp_nd] = temp
            return
        else:
            # get the descending section
            start = nd
            while cmp_nd >= 0 and nums[nd] <= nums[cmp_nd]:
                cmp_nd -= 1
                nd -= 1

            if cmp_nd == -1:
                print("rev")
                nums[:] = nums[::-1]
            else:
                target = nums[cmp_nd]
                print(cmp_nd)
                next_element = 101
                next_element_nd = -1
                for i in range(cmp_nd+1, start+1):
                    if nums[i] > target:
                        if nums[i] < next_element:
                            next_element = nums[i]
                            next_element_nd = i
                
                # switch next element and cmp_nd
                temp = nums[cmp_nd]
                nums[cmp_nd] = nums[next_element_nd]
                nums[next_element_nd] = temp
                
                # sort cmp_nd + 1 to end
                #nums = nums[:cmp_nd+1] + sorted(nums[cmp_nd+1:])
                nums[cmp_nd+1:] = sorted(nums[cmp_nd+1:])
                    
     