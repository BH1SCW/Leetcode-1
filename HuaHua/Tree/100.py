from __future__ import annotations

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def helper(t1, t2):
            if t1 and t2 and t1.val == t2.val:
                return helper(t1.left, t2.left) and helper(t1.right, t2.right)
            if not t1 and not t2:
                return True
            return False
        return helper(p, q)

