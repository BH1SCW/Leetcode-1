class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        ans = [0]
        def helper(node, num):
            if not node:
                return
            v = num * 10 + node.val
            if not node.left and not node.right:
                ans[0] += v
                return
            helper(node.left, v)
            helper(node.right, v)
        helper(root, 0)
        return ans[0]

