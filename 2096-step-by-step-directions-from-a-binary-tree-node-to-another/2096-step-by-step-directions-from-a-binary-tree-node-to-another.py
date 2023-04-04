# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    visited = set()
    
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        # find path to start
        # find path to dest
        
        # remove common prefix
        
        # place dest as it is from mismatch
        # for start -> convert all to U
        
        def getCode(root, dest, path):
            stack = [(root, path)]
            while stack:
                node, curr_path = stack.pop()
                if node.val == dest:
                    return curr_path
                if node.left:
                    stack.append((node.left, curr_path + "L"))
                if node.right:
                    stack.append((node.right, curr_path + "R"))
            return None
            
        start_code = getCode(root, startValue, "")
        
        ans = ""
        dest_code = getCode(root, destValue, "")
        start_index = 0
        
        for i in range(min(len(start_code), len(dest_code))):
            if start_code[i] != dest_code[i]:
                break
            start_index += 1
        
        start_code = start_code[start_index:]
        dest_code = dest_code[start_index:]
        
        ans = "U" * len(start_code) + dest_code
        
        return ans