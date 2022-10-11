class Solution(object):
    def deleteDuplicates(self, head):
        new_hd =  ListNode(0, head)
        ptr1 = new_hd
        while head != None:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                ptr1.next = head.next 
            else:
                ptr1 = ptr1.next
            head =  head.next
            
        return new_hd.next
