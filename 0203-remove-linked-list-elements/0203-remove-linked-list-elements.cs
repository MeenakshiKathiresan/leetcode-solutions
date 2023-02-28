/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode RemoveElements(ListNode head, int val) {
        ListNode prev = head;
        if (head == null){
            return head;
        }
        ListNode curr = head.next;
        
        

        
        while (curr != null){
            if (curr.val == val){
                prev.next = curr.next;
            }else{
                  prev = curr;
            }
          
            
            curr = curr.next;
        }
        
        if (head!=null && head.val == val){
            return head.next;
        }

        
        return head;
    }
}