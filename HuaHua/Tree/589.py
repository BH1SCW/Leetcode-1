from collections import deque
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        q = deque([root])
        ans = []
        while q:
            node = q.popleft()
            if not node:
                continue
            ans += [node.val]
            q.extendleft(reversed(node.children))
        return ans

