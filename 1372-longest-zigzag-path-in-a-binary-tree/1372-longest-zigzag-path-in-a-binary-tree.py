# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.pathlength = 0
        
        def zigzag(root, direction, dist):
            
            
            if root != None :
                self.pathlength = max(self.pathlength, dist)
                if direction == -1:
                    curr = zigzag(root.right, 1, dist + 1)
                    curr = zigzag(root.left, -1, 1)
                elif direction == 1:
                    curr = zigzag(root.left, -1, dist + 1 )
                    curr = zigzag(root.right, 1, 1)

        zigzag(root, 1, 0)
        zigzag(root, -1, 0)
        return self.pathlength