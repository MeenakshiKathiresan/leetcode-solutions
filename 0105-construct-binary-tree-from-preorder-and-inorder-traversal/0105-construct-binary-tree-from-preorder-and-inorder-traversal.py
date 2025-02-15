# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        r = preorder.pop(0)
        r_index = inorder.index(r)

        root = TreeNode(r)
        root.left = self.buildTree(preorder, inorder[:r_index])
        root.right = self.buildTree(preorder, inorder[r_index + 1:])

        return root

