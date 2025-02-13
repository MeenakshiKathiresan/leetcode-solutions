class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        recent_pos = {}

        for i, n in enumerate(nums):
            if n in recent_pos and i - recent_pos[n] <= k:
                return True
            recent_pos[n] = i
        return False

