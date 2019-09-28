
class Solution:
    def reverseList_iter(self, head: ListNode) -> ListNode:
        if not head:
            return None
        new_list = head
        tail = head.next
        head.next = None
        while tail:
            h = tail
            tail = tail.next
            h.next = new_list
            new_list = h
        return new_list

    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        def reverse(head):
            if head.next:
                tail = head.next
                tail = reverse(tail)
                tail.next = head
                head.next = None
            else:
                dummy.next = head
            return head
        if head:
            reverse(head)
            return dummy.next
        else:
            return None

