# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        
        def helper(root):
            if root == None:
                return False
            
            if root.right == None and root.left == None:
                # leaf node
                
                if root.val == 0:
                    return False
                else:
                    return True
            if root.val == 2:
                return helper(root.right) or helper(root.left)
            elif root.val == 3:
                return helper(root.right) and helper(root.left)
        
        return helper(root)
            