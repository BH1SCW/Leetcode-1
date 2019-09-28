class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def helper(root):
            if root:
                root.left = helper(root.left)
                root.right = helper(root.right)
                if not root.left and not root.right and not root.val:
                    return None
            return root
        return helper(root)

