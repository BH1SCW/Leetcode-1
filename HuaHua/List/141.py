from __future__ import annotations

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and slow:
            try:
                fast = fast.next.next
                slow = slow.next
            except:
                return False
            if fast == slow:
                return True
        return False



if __name__ == '__main__':
    sol = Solution()
    sol.hasCycle(head)
