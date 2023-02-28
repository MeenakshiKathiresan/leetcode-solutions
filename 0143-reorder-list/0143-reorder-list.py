# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # find center
        # from centre reverse
        # then merge
        
        # find center
        slow = fast = head
        
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # if fast is null -> even
            # if fast.next is null -> odd
        
        
        prev = None
        curr = slow
        
        
        while curr:
            upnext = curr.next
            curr.next = prev
            prev = curr
            curr = upnext
        
        head_first = True
        rhead = head
        
        while prev.next:
            temp = head.next
            head.next = prev
            head = temp
            
            temp = prev.next
            prev.next = head
            prev = temp

        return rhead