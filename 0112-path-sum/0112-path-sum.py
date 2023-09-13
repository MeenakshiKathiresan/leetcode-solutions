# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, curr_sum):
            
            if root:
                # leaf node
                if root.right == None and root.left == None:
                    if curr_sum + root.val == targetSum:
                        return True

                else:
                    return dfs(root.right, curr_sum + root.val) or dfs(root.left, curr_sum + root.val)
                    
                     

                
                
        return dfs(root, 0)
            