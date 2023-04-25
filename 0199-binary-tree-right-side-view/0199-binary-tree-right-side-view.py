# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root == None: return []
        res = []
        queue = deque([root])
        
        while queue:
            n = len(queue)
            val = None
            for i in range(n):
            
                curr = queue.popleft()
                if val == None:
                    val = curr.val
                    res.append(val)
                if curr.right != None:
                    queue.append(curr.right)
                if curr.left != None:
                    queue.append(curr.left)
            #res.append(curr.val)
            
        return res