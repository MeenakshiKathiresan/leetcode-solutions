# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        res = []
        
        def set_parent(root, parent):
            if root:
                root.parent = parent
                set_parent(root.right, root)
                set_parent(root.left, root)
            
        set_parent(root, None)
        
        visited = set()
        
        def dfs(root, distance):
            
            if not root or root in visited:
                return None
            visited.add(root)
            
            if distance == 0:
                res.append(root.val)
                return
                
            else:
                dfs(root.parent, distance - 1)
                dfs(root.right, distance - 1)
                dfs(root.left, distance - 1)
                
        dfs(target, k)
        
        return res
            
            
                
        