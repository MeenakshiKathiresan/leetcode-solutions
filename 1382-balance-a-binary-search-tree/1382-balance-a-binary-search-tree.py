# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # convert whole into list
        # convert it back?
        
        elems = []
        def traverse(root):
            if root == None: return
            traverse(root.left)
            elems.append(root.val)
            traverse(root.right)
        
        def build_bst(start, end):
            
            if start > end: return
            
            mid = (start + end) // 2
            
            left = build_bst(start, mid - 1)
            right = build_bst(mid + 1, end)
            
            node = TreeNode(elems[mid], left, right)
            return node
        
        traverse(root)
        return build_bst(0, len(elems) - 1)