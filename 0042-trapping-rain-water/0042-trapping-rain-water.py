class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if len(height)==0: return 0
        
        left = 0
        right = len(height) - 1
        
        lmax = height[left]
        rmax = height[right]
        
        ans = 0
        
        while left < right:
            if lmax < rmax:
                left += 1
                lmax = max(lmax, height[left])
                ans += (lmax - height[left])
            
            else:
                right -= 1
                rmax = max(rmax, height[right])
                ans += rmax - height[right]
                
        return ans
