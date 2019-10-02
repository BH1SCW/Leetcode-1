class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root):
            if not root:
                return None, None, True
            lmin, lmax, lb = helper(root.left)
            rmin, rmax, rb = helper(root.right)
            if not lb or root.left and lmax >= root.val:
                return None, None, False
            if not rb or root.right and rmin <= root.val:
                return None, None, False
            return lmin if lmin else root.val, rmax if rmax else root.val, True
        return helper(root)

