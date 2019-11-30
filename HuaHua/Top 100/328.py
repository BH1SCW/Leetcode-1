from __future__ import annotations
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_odd = ListNode(0)
        even = dummy_even = ListNode(0)
        prev = cur = dummy_odd.next = head
        while cur and cur.next:
            prev, mid, cur = cur, cur.next, cur.next.next
            prev.next = cur
            mid.next, even.next, even = None, mid, mid
        if cur: cur.next = dummy_even.next
        elif prev: prev.next = dummy_even.next
        return dummy_odd.next


