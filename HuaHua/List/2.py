from __future__ import annotations

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def list_print(l):
    if l.next:
        print("{0} => ".format(l.val))
        list_print(l.next)
    else:
        print("{0}".format(l.val))



class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carrier = 0
        dummy_ans = ans = ListNode(0)
        while l1 or l2 or carrier:
            v1 = v2 = 0
            if l1:
                v1, l1 = l1.val, l1.next
            if l2:
                v2, l2 = l2.val, l2.next
            val = v1 + v2 + carrier
            ans.next, carrier = ListNode(val % 10), val // 10
            ans = ans.next
        return dummy_ans.next



if __name__ == '__main__':
    sol = Solution()
    s1 = ListNode(2)
    s1.next = ListNode(4)
    s2 = ListNode(5)
    s2.next = ListNode(6)
    s2 = s2.next
    s2.next = ListNode(7)
    list_print(sol.addTwoNumbers(s1, s2))
