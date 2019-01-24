from Algorithm.Heapsort import Rand
# important: this is not hard, but this method is too fussy.
# The reason is that i did everything inplace. However, with a dummy node, things would be much much easier
# important: everything would be more fussier when INPLACE, please avoid this and use dummy variables as often as possible.
import math
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def makeList(s):
    if len(s) == 0:
        return None
    s1 = ListNode(s[0])
    head = s1
    for i in range(1, len(s)):
        s1.next = ListNode(s[i])
        s1 = s1.next
    return head

def printList(s):
    s1 = ""
    while not (s is None):
        s1 += str(s.val)
        s1+= " "
        s = s.next
    print(s1)




class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
        while True:
            count = 0
            while r and count < k:  # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                return dummy.next





if __name__ == '__main__':
    a1 = sorted(Rand(1))
    a1 = []
    a1 = [1, 2, 3, 4, 5]
    l1 = makeList(a1)
    # printList(l1)
    sol = Solution()
    printList(sol.reverseKGroup(l1, 4))

