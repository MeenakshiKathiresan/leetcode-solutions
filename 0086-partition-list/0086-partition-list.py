# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return head
        lhead = lower = ListNode(0)
        ghead = greater = ListNode(0)

        while head:
            if head.val < x:
                lower.next = head
                lower = lower.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next

            greater.next = None
            lower.next = ghead.next
        return lhead.next