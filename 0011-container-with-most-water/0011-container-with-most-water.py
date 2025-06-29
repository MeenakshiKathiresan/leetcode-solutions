class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Steps:
        1. 2 pointers - left and right
        2. Calculate the area - min of (ht[left], [right]) * (right - left) => ht x width
        3. Move the lower value pointer 
        4. Iterate until left and right meet
        """
        res = 0
        left = 0
        right = len(height) - 1

        while left < right:
            curr = min(height[left], height[right]) * (right - left)
            res = max(res, curr)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res