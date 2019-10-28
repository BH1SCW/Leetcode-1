class Solution:
    # 这个是昨天学习的方法，虽然不是自己想的
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        count = 0
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            count += 1
            if count == k:
                return root.val
            root = root.right

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.ans = None
        def walk(root, count):
            if not root:
                return count
            l = walk(root.left, count)
            if l + 1 == k:
                self.ans = root.val
            r = walk(root.right, l + 1)
            return r
        walk(root, 0)
        return self.ans

