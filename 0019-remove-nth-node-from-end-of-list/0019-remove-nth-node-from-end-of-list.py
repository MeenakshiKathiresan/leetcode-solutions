# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length
        # find node num to remove
        # iterate again and remove

        slow = head
        fast = head
        total = 0

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            total += 2

        if fast:
            total += 1

        target = total - n

        # edge case
        if target == 0:
            return head.next

        slow = head
        i = 0
        while slow:
            if i + 1 == target:
                if slow.next:
                    slow.next = slow.next.next
                else:
                    slow.next = None
                break
            
            slow = slow.next
            i += 1
            

        return head     
        