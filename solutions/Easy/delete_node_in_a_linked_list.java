/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

class Solution {
    public void deleteNode(ListNode node) {
        ListNode cursor = node;
        ListNode prev = cursor;
        while(cursor.next != null){
            cursor.val = cursor.next.val;
            prev = cursor;
            cursor = cursor.next;
        }
        prev.next= null;
    }
}
