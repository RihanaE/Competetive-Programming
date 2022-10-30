class Solution:
    def insertionSortList(self, head):
        new_head = ListNode(-1)
        ptr = head
        while ptr:
            nex = ptr.next
            prev, nxt = new_head, new_head.next
            while nxt:
                if nxt.val > ptr.val: break
                prev = nxt
                nxt = nxt.next
                
            ptr.next = nxt
            prev.next = ptr
            ptr = nex
        
        return new_head.next
