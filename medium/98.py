# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import math
# TODO: this can be refined, many redundant if
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def validBST(node):
            if not node:
                return True, None, None
            else:
                left, left_min, left_max = True, None, None
                right, right_min, right_max = True, None, None
                if node.left:
                    left, left_min, left_max = validBST(node.left)
                if node.right:
                    right, right_min, right_max = validBST(node.right)
                if left and right:
                    lb = node.val
                    ub = node.val
                    if left_max:
                        if left_max >= node.val:
                            return False, None, None
                        else:
                            lb = left_min
                    if right_min:
                        if right_min <= node.val:
                            return False, None, None
                        else:
                            ub = right_max
                    return True, lb, ub
                else:
                    return False, None, None
        b, _, _ = validBST(root)
        return b

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(1)
    root2 = TreeNode(4)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root.right = root2
    sol = Solution()
    sol.isValidBST(root)

