# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        first_time = True
        prev = None
        
        while current and current.next:
            second = current 
            first = current.next
            next_node = first.next

            if prev:
                prev.next = first

            first.next = second
            second.next = next_node
            prev = second

            current = next_node 

            if first_time:
                head = first
                first_time = False

        return head