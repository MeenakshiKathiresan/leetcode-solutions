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
    public ListNode DeleteDuplicates(ListNode head) {
        
        ListNode ptr = head;
        while(ptr != null && ptr.next!=null){
            if (ptr.val == ptr.next.val){
                ptr.next = ptr.next.next;
            }else{
                 ptr = ptr.next;
            }
           
        }
        return head;
        
    }
}