class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        l = [root]
        ans = []
        while l:
            values = []
            nl = []
            for tree in l:
                values.append(tree.val)
                if tree.left:
                    nl.append(tree.left)
                if tree.right:
                    nl.append(tree.right)
            ans.append(values)
            l = nl
        return ans




