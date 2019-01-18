from Algorithm.Heapsort import Rand
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

def reverseFirstK(lists, k):
    head = lists
    if head is None or head.next is None:
        return head, None
    move = head
    oldMove = move
    i = k
    while i >= 2:
        if oldMove is None or oldMove.next is None:
            return reverseFirstK(head, k - i + 1)
        else:
            move = oldMove.next
        tail = move.next # 1(head) -> 2(move) -> (3 -> ...)tail
        move.next = head # 1(head) -> 2(move) -> 1(head)
        oldMove.next = tail # 2(move) -> 1(head) -> (3 -> ...)tail
        head = move# 2(head) -> 1(move) -> (3 -> ...)tail
        i -= 1
    return head, oldMove


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        head, tail = reverseFirstK(head, k)
        printList(head)
        while not tail is None:
            oldTail = tail
            newHead, tail = reverseFirstK(tail.next, k)
            # printList(newHead)
            oldTail.next = newHead
        return head




if __name__ == '__main__':
    a1 = sorted(Rand(1))
    a1 = []
    a1 = [1, 2, 3, 4, 5]
    l1 = makeList(a1)
    # printList(l1)
    sol = Solution()
    printList(sol.reverseKGroup(l1, 4))

