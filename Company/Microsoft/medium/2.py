# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = dummy
        carrier = 0
        while l1 or l2:
            if not l1:
                if not carrier:
                    cur.next = l2
                    return dummy.next
                else:
                    l1 = ListNode(1)
                    carrier = 0
            if not l2:
                # there is carrier
                if not carrier:
                    cur.next = l1
                    return dummy.next
                else:
                    l2 = ListNode(1)
                    carrier = 0
            result = l1.val + l2.val + carrier # add carrier
            carrier = 0 # clean carrier
            l1, l2 = l1.next, l2.next
            cur.next = ListNode(result % 10)
            cur = cur.next
            if result >= 10:
                carrier = 1
        if carrier:
            cur.next = ListNode(1)
            carrier = 0
        return dummy.next



