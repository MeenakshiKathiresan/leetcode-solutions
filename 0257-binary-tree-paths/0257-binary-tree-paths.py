# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res = []
        
        def traverse(curr, str_so_far):
            if curr:
                if curr.right == None and curr.left == None:
                    str_so_far += str(curr.val)
                    res.append(str_so_far)

                str_so_far += str(curr.val) + "->"
                traverse(curr.right, str_so_far)
                traverse(curr.left, str_so_far)

        traverse(root, "")
        return res