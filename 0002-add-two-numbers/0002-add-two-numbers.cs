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
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode l3 = new ListNode();
        ListNode head = l3;
        
        int carry = 0;
       
        while (l1 != null || l2 != null){
            int firstNo = 0, secondNo = 0;
            
            
            if (l1 != null){
                firstNo = l1.val;
            }
            if (l2!=null){
                secondNo = l2.val;
            }
            
            l3.val = (firstNo + secondNo + carry)%10;
            carry = (firstNo + secondNo + carry)/10;
            
            
            if (l1 != null && l1.next != null){
                l1 = l1.next;
             
            }else{
                l1 = null;
            }
            
            if (l2!= null && l2.next != null){
                l2 = l2.next;
            }else{
                l2 = null;
            }
            
            
            if (l1 != null || l2 != null){
                
            
            l3.next = new ListNode();
            l3 = l3.next;
            }else{
                if (carry >0) {
                l3.next = new ListNode();
            l3 = l3.next;
                l3.val += carry;
            }}
          
            
        }
        
        return head;
    }
}
