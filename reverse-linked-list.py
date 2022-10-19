# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        new_head = ListNode(0)
        ptr = new_head
        vals = []
        j = head
        count = 0
        while j!= None:
            vals.append(j.val)
            j = j.next
        for i in range(len(vals)):
            ptr.next = ListNode(vals[len(vals)-1-i])
            ptr = ptr.next
        return new_head.next
        
        
