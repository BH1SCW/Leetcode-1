# 这题要注意tree里面有负数, 然后leaf的时候必须return，这样可以精简一点
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def helper(root, target):
            if not root:
                return False
            if not root.left and not root.right:
                return root.val == target
            return helper(root.left, target - root.val) or helper(root.right, target - root.val)
        return helper(root, sum)



