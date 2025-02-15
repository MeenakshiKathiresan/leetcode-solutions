# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
    
        r = 0
        head = ListNode(0, None)
        rhead = head
        last = None
        while l1 and l2:
            
            res = l1.val + l2.val + r
            head.val = res % 10
            r = res // 10
            head.next = ListNode(0, None)

            last = head
            head = head.next
            l1 = l1.next
            l2 = l2.next

        
        while l1:
            res = l1.val + r
            head.val = res % 10
            r = res // 10

            head.next = ListNode(0, None)

            last = head
            l1 = l1.next
            head = head.next

        while l2:
            res = l2.val + r
            head.val = res % 10
            r = res // 10

            last = head
            head.next = ListNode(0, None)
            head = head.next
            l2 = l2.next

        if r != 0:
            head.val = r
        else:
            last.next = None
        return rhead