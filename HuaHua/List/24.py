class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = dummy = ListNode(0)
        n1 = dummy.next = head
        n2 = head.next if head else head
        while n1 and n2:
            prev.next, n1.next, n2.next = n2, n2.next, n1
            prev = n1
            n1, n2 = n1.next, n1.next.next if n1.next else None
        return dummy.next

