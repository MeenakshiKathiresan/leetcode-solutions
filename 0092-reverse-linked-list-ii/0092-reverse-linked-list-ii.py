# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head: return
        rhead = head
        n = 0
        prev_in_chain = None
        while head:
            n += 1
            if n == left:
                prev = None
                first_in_rev = head

                # start reversing
                while n <= right:
                    next = head.next
                    head.next = prev
                    prev = head
                    head = next
                    n += 1

                first_in_rev.next = next
                if prev_in_chain:
                    prev_in_chain.next = prev
                else:
                    rhead = prev
                break

            prev_in_chain = head
            head = head.next

        return rhead