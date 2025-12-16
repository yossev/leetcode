/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode tort = head;
        ListNode rabbit = head;

        while (tort != null && rabbit.next != null){
            tort = tort.next;
            rabbit = rabbit.next.next;
            if (rabbit == tort) {
                return true;
            }
        }
        return false;

        

    }
}