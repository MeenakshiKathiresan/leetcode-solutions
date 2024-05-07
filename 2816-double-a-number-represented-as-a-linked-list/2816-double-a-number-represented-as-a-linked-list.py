# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        rhead = head
        def double_helper(node):
            
            if node == None:
                return 0
            
            node.val = double_helper(node.next) + node.val * 2
            remainder = node.val // 10
            node.val = node.val % 10
            
            return remainder
        
        remainder = double_helper(head)
        if remainder != 0:
            new_head = ListNode(remainder, rhead)
            return new_head
        return rhead