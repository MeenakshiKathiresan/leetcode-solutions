# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        if root == None or (root.right == None and root.left == None):
            return root.val
        
        def getNumber(root, num):
            
            if root == None:
                return '0'
            
            if root.right == None and root.left == None: 
                return num * 10 + root.val
            
            n1 = getNumber(root.right, num * 10 + root.val)
            
            n2 = getNumber(root.left, num * 10 + root.val)
            
            
            return int(n1) + int(n2)

            
        return getNumber(root, 0)
        
    