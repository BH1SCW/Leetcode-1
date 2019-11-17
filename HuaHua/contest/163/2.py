from __future__ import annotations

# 这个土办法超时了
def find(root, target):
    if not root: return False
    if root.val == target: return True
    if target < root.val:
        return find(root.left, target)
    else:
        return find(root.right, target)


class FindElements:
    def __init__(self, root: TreeNode):
        if not root: return
        self.root = root
        if root.val == -1:
            root.val = 0
        if root.left:
            root.left.val = root.val * 2 + 1
            FindElements(root.left)
        if root.right:
            root.right.val = root.val * 2 + 2
            FindElements(root.right)


    # 所以这题跟早上做的题有相似之处，都是利用了二叉树和二进制之间的对应关系
    def find(self, target: int) -> bool:
        root = self.root
        path = bin(target + 1)[3:]
        for d in path:
            if not root: break
            if d == '0': root = root.left
            else: root = root.right
        return root and root.val == target

if __name__ == '__main__':
    sol = Solution()
