# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0
        def traverse(node, greatest_so_far):
            nonlocal res
            if not node: return
            if node.val >= greatest_so_far:
                res += 1
            
            greatest_so_far = max(node.val, greatest_so_far)
            traverse(node.left, greatest_so_far)
            traverse(node.right, greatest_so_far)
        
        traverse(root, -10000)
        return res

