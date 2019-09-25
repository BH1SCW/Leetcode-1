from __future__ import annotations

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        ans = []
        r = root
        while True:
            while r:
                stack.append(r)
                r = r.left
            if not stack:
                return ans
            t = stack.pop()
            ans.append(t.val)
            r = t.right




