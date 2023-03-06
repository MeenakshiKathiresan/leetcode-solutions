# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        n1, n2 = 0, 0
        
        
        while l1:
            n1 = n1 * 10 + l1.val 
            l1 = l1.next
            
        while l2:
            n2 = n2 * 10 + l2.val
            l2 = l2.next
            
        # reverse ans:
        # 7807
        res = n1+n2
        
        ans =str(res)
        
        head = rhead = ListNode()
        
        while len(ans) > 0:
            
            head.val = int(ans[0])
            print(ans[0])
            ans = ans[1:]
            if len(ans) > 0:
                head.next = ListNode()
            head = head.next
            
            
        return rhead
        
        
        