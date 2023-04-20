# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # bfs 
        # track of positions? max and min of that layer 
        if not root:
            return 0
        
        queue = [(root, 1)]
        max_width = 0
        
        while queue:
            level_size = len(queue)
            _, level_start = queue[0]
            _, level_end = queue[-1]
            max_width = max(max_width, level_end - level_start + 1)
            
            for i in range(level_size):
                node, index = queue.pop(0)
                if node.left:
                    queue.append((node.left, index*2))
                if node.right:
                    queue.append((node.right, index*2+1))
                    
        return max_width