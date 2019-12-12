class Solution:
    def countNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(root, n):
            self.ans = max(self.ans, n)
            if root.left: dfs(root.left, n << 1)
            if root.right: dfs(root.right, n << 1 | 1)
        if not root: return 0
        dfs(root, 1)
        return self.ans

    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        q = [root]
        ans = 0
        while q:
            new = []
            ans += len(q)
            for node in q:
                if node.left: new.append(node.left)
                if node.right: new.append(node.right)
            q = new
        return ans
