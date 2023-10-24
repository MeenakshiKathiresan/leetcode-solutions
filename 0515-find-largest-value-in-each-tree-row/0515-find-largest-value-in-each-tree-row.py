# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        #{0:[1], 1:[3,2]...}
        
        tree_dict = {}
        
        
        def dfs(node, level):
            if node:
                if level not in tree_dict:
                    tree_dict[level] = []
                tree_dict[level].append(node.val)
                
                dfs(node.right, level + 1)
                dfs(node.left, level + 1)
        max_level = 0
        dfs(root, 0)
        
        res = []
        for k,v in tree_dict.items():
            res.append(max(v))
        return res
        
                