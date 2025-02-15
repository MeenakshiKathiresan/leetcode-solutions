# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        def traverse(node, curr_sum):
            if not node: return False
            if node and not node.right and not node.left:
                if curr_sum + node.val == targetSum:
                    return True
                return False
            if curr_sum > targetSum: return False
            
            left = traverse(node.left, node.val + curr_sum)
            right = traverse(node.right, node.val + curr_sum)

            return left or right
        
        return traverse(root, 0)