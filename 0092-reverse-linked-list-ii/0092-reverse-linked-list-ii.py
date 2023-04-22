# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if head == None or head.next == None or left == right:
            return head
        
        count = 1
        rhead = head
        prev = head
        
        while head and count < left:
            count += 1
            prev = head
            head = head.next
            
        last = head
        prev_node = None
        while head and count <= right:
            count += 1
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node
            
        prev.next = prev_node
        last.next = head
        if left == 1:
            rhead = prev_node
        
        return rhead