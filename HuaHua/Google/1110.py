class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        def helper(root, is_root, ans):
            if not root: return None
            is_del = root.val in to_delete
            if is_root and not is_del:
                ans.append(root)
            root.left = helper(root.left, is_del, ans)
            root.right = helper(root.right, is_del, ans)
            return None if is_del else root
        ans = []
        helper(root, True, ans)
        return ans

    def delNodes2(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root: return [root]

        def helper(root, to_delete, ans, parent, side):
            if not root: return
            left, right = root.left, root.right
            if root.val in to_delete:
                if root.left and not root.left.val in to_delete:
                    ans.append(root.left)
                if root.right and not root.right.val in to_delete:
                    ans.append(root.right)
                to_delete.remove(root.val)
                if side == 0:
                    parent.left = None
                else:
                    parent.right = None
                root.left = root.right = None
            helper(left, to_delete, ans, root, 0)
            helper(right, to_delete, ans, root, 1)

        s = set(to_delete)
        ans = [root] if not root.val in s else []
        helper(root, s, ans, TreeNode(0), 0)
        return ans
