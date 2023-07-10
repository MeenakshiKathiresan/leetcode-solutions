# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        def getDepth(root, height):
            
            if root == None:
                return sys.maxint
            if root.right == None and root.left == None:
                return height
            
            left = getDepth(root.left, height + 1)
            right = getDepth(root.right, height + 1)
            
            return min(left, right)
        
        return getDepth(root, 1)