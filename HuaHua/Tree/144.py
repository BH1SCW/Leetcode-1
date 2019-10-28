from collections import deque
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        q = deque([root])
        ans = []
        while q:
            node = q.popleft()
            if not node:
                continue
            ans += [node.val]
            q.appendleft(node.right)
            q.appendleft(node.left)
        return ans
    
