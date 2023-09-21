class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        i = 0
        j = 0
        
        nums = []
        
        while  i < len(nums1) or j < len(nums2):
            
            if i == len(nums1):
                nums.append(nums2[j])
                j+=1
                continue
                
            elif j == len(nums2):
                nums.append(nums1[i])
                i+=1
                continue
            
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
            
        
        if len(nums)%2 == 0:
            return (nums[int(len(nums)/2)] + nums[int(len(nums)/2)-1])/2
        else:
            return nums[int(len(nums)/2)]
        
        
        