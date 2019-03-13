def connectTree(root):
    if root is None:
        return root
    left = connectTree(root.left)
    right = connectTree(root.right)
    if root.left is None:
        # do nothing
        return root
    if root.right is None:
        # do nothing
        return root
    l = root.left
    r = root.right
    while not l is None and not r is None:
        l.next = r
        l = l.right if l.right else l.left
        r = r.left if r.left else r.right
    return root

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        connectTree(root)