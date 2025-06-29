# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        3 pointer approach
        1 for prev
        1 for curr
        1 for next
        """

        prev = None
        next = None

        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next

        return prev

