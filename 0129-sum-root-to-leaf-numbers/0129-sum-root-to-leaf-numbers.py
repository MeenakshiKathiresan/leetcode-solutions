# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def traverse(node, sum):
            if not node: return 0
            
            sum = (sum * 10) + node.val

            if not node.right and not node.left:
                return sum
            
            return traverse(node.left, sum) + traverse(node.right, sum)
        return traverse(root, 0)
