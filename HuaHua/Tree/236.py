# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 我的做法还行，但是不够精简，这个是参考了别人的做法，非常的精简
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root
        left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = [root]
        def dfs(root):
            if not root:
                return False, False
            fpl, fql = dfs(root.left)
            fpr, fqr = dfs(root.right)
            find_p = root == p or fpl or fpr
            find_q = root == q or fql or fqr
            if find_p and find_q:
                ans[0] = root
                return False, False
            return find_p, find_q
        dfs(root)
        return ans[0]

