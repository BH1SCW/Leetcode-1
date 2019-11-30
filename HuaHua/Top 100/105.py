from __future__ import annotations
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder: return None
        val = preorder[0]
        root = TreeNode(val)
        if len(preorder) == 1: return root
        pos = inorder.index(val)
        inorder_left, inorder_right = inorder[:pos], inorder[pos + 1:]
        preorder_left, preorder_right = preorder[1:pos + 1], preorder[pos + 1:]
        root.left, root.right  = self.buildTree(preorder_left, inorder_left), self.buildTree(preorder_right, inorder_right)
        return root

