class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 2 pointers - 2 walls
        # choose the lower of the two - definitely guarded
        # add prev wall - curr height to trapped water and move

        """

        """

        left = 0
        right = len(height) - 1

        l_wall_ht = 0
        r_wall_ht = 0

        res = 0

        while left <= right:
            if l_wall_ht <= r_wall_ht:
                if height[left] < l_wall_ht:
                    res += l_wall_ht - height[left]

                l_wall_ht = max(l_wall_ht, height[left])
                left += 1
                
            else:
                if height[right] < r_wall_ht:
                    res += r_wall_ht - height[right]

                r_wall_ht = max(r_wall_ht, height[right])
                right -= 1

        return res