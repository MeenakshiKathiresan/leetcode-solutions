# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
  
        # find max of the array and create a node
        # store max index
        # recursively call for left and right half
        
        def createMaxNode(numsList):
            
            max_num = -1
            max_index = -1
            for i, num in enumerate(numsList):
                if num > max_num:
                    max_num = num
                    max_index = i
            if max_index == -1:
                return None
            
            node = TreeNode(max_num)
            node.left = createMaxNode(numsList[:max_index])
            node.right = createMaxNode(numsList[max_index+1:])
            return node
        
        return createMaxNode(nums)
        