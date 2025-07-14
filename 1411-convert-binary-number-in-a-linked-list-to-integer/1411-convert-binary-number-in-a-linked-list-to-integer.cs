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
    public int GetDecimalValue(ListNode head) {
        ListNode slow = head;
        int len = 0;
        while(slow != null){
            len += 1;
            slow = slow.next;
        }
        len--;
        int res = 0;
        while (head != null){
            if(head.val == 1){
                Console.WriteLine(len);
                res += (int) Math.Pow(2, len);
            }
            len--;
            head = head.next;
        }
        return res;
    }
}