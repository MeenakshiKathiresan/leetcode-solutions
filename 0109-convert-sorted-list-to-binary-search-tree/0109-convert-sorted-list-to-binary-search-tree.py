# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        
        def sortedArrayToBST(nums):
        
            if len(nums) <1: return None

            left = 0
            right = len(nums)-1

            mid = int((left+right)/2)

            root = TreeNode(nums[mid])

            root.left = sortedArrayToBST(nums[:mid])
            root.right = sortedArrayToBST(nums[mid+1:])

            return root
        
        while head:
            nums.append(head.val)
            head = head.next
        
        print(nums)
        
        return sortedArrayToBST(nums)
        
        
        