class Solution(object):
    def pairSum(self, head):
        n, max_sum, i = 1, 0, 1
        l_head, r_head = head, ListNode(head.val)
        while head.next:
            n+=1
            node = ListNode(head.next.val, r_head)
            r_head = node
            head = head.next
        while i <= n/2:
            max_sum = max(l_head.val + r_head.val, max_sum)
            i+=1
            l_head = l_head.next
            r_head = r_head.next
        return max_sum
