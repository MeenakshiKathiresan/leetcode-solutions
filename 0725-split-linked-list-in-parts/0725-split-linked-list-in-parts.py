# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        new_head = head
        count = 0
        while head:
            head = head.next
            count += 1
        
        split_size = count // k
        add_one_count = count % k
        
        head = new_head
       
        res = []
        count = 0
        
        new_head = head
        
        while head:
            
            plus_one = 0
            count += 1 
            if len(res) < add_one_count:
                plus_one = 1
                
            if count < (split_size + plus_one):
                head = head.next
            else:
                res.append(new_head)
                new_head = head.next
                head.next = None
                head = new_head
                count = 0
            
        
        while len(res) < k:
            res.append(None)
        
        return res
        
        
        
        
        