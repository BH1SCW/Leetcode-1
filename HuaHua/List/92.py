class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 当数字比较明确的时候还是用for循环，别用while，不然全是if
# 逻辑结构还是要顺应题目
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        pre = dummy = ListNode(0)
        dummy.next = head
        for i in range(m - 1):
            pre = pre.next
        c1 = pre
        pre = pre.next
        t1 = pre
        new_tail = None
        for i in range(n - m + 1):
            tail = pre.next
            detached = pre
            pre = pre.next
            detached.next = new_tail
            new_tail = detached
        c1.next = new_tail
        t1.next = pre
        return head if n > 1 else new_tail


if __name__ == '__main__':
    sol = Solution()
    dummy = head = ListNode(1)
    head.next = ListNode(2)
    head = head.next
    head.next = ListNode(3)
    head = head.next
    head.next = ListNode(4)
    head = head.next
    head.next = ListNode(5)
    head = head.next
    m = 1
    n = 2
    sol = sol.reverseBetween(dummy, m, n)
    print(sol)







