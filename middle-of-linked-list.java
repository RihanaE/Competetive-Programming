/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
          ListNode cur = head, ptr =head;
            
          while(ptr.next != null){
              ptr =ptr.next;
              cur = cur.next;
              if(ptr.next!= null)
                  ptr = ptr.next;
              else
                  break;
          }
        return cur;
    }
}
