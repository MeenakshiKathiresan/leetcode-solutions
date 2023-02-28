class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head or not head.next:
            return None


        first = slow = fast = head

        while fast.next and fast.next.next:
     
            slow = slow.next
            fast = fast.next.next

        if not fast.next:
            tmp = first 
            while tmp:
                if tmp.next != slow:
                    tmp = tmp.next
                else:
                    tmp.next = tmp.next.next
                    break
        
        else:
            slow.next = slow.next.next


        return first
