class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        N, cur = 0, head
        while cur:
            N += 1
            cur = cur.next
        def merge(l, r):
            prev = dummy = ListNode(0)
            while l and r:
                if l.val <= r.val:
                    prev.next, prev, l = l, l, l.next # 所以这个地方要注意，先后是有顺序的，千万不要搞错，这还是第一次注意到
                else:
                    prev.next, prev, r = r, r, r.next
            prev.next = l or r
            return dummy.next

        def merge_sort(head, n):
            if n <= 1:
                return head
            prev = r = head
            c = n // 2
            while c > 0:
                c -= 1
                prev, r = r, r.next
            prev.next = None
            l = merge_sort(head, n // 2)
            r = merge_sort(r, (n + 1) // 2)
            return merge(l, r)
        return merge_sort(head, N)

