# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def helper(node):
            if node:
                helper(node.left)
                ans.append(node.val)
                helper(node.right)
            else:
                return
        helper(root)

