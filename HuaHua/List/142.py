from __future__ import annotations

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and slow:
            try:
                fast = fast.next.next
                slow = slow.next
            except:
                return None
            if fast == slow:
                while slow != head:
                    slow, head = slow.next, head.next
                return slow
        return None




if __name__ == '__main__':
    sol = Solution()
    sol.hasCycle(head)