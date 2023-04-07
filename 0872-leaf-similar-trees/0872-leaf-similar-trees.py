# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        l1 = []
        l2 = []
        
        def dfs(root, lis):
            if root == None:
                return
            if root.left == None and root.right == None:
                lis.append(root.val)
                
            dfs(root.left, lis)
            dfs(root.right, lis)
        
        dfs(root1, l1)
        dfs(root2, l2)
        
        return l1 == l2