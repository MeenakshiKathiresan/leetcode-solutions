# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([root])
        if not root: return 0

        max_sum = -float('inf')
        max_level_index = 0
        level_index = 0
        while queue:

            n = len(queue)
            level_sum = 0
            for i in range(n):
                curr = queue.popleft()
                level_sum += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if level_sum > max_sum:
                max_level_index = level_index
                max_sum = level_sum

            level_index += 1
        
        return max_level_index + 1
                
