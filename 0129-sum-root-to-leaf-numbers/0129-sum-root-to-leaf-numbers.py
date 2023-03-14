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
                print(str(num) + str(root.val), "returns")
                return str(num) + str(root.val)
            
            n1 = getNumber(root.right, num + str(root.val))
            
            n2 = getNumber(root.left, num + str(root.val))
            
            
            return int(n1) + int(n2)

            
        num = getNumber(root, '')
        
        return num