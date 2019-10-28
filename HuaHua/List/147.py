class Solution:
    # 做linked list的时候一定要画图。。不然很容易出错，看了一下别人的答案，我这个已经相当简洁了
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head: return head
        old, new, head.next = head.next, head, None
        dummy = ListNode(0)
        dummy.next = new
        while old:
            prev, cur = dummy, dummy.next
            while cur and cur.val < old.val:
                prev, cur = cur, cur.next
            node, old = old, old.next
            prev.next, node.next = node, cur
        return dummy.next


