# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def traverse(root, l_node, r_node):
            if root is None: 
                return True
            
            if l_node is not None:
                if l_node.val >= root.val:
                    return False
            if r_node is not None:
                if r_node.val <= root.val:
                    return False
                    
            return traverse(root.left, l_node, root) and traverse(root.right, root, r_node)
                

        return traverse(root, None, None)

