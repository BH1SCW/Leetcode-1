# This problem is just a tree traversal problem
# Recursive is easy:
# the inorder is easy,
# f(root):
#     f(root.left)
#     f'(root.val)
#     f(root.right)
#             1
#     2               3
# 4       5
# the stack would be something like this(from bottom to up)
# f is omitted, 1 2 4 -> 1 2 5 -> 1 2 -> 1; 1 3 -> 1
# so the print result would be
# 4 5 2 1 3
# In this probel,
# 4 5 2 1 3 None None

# in order
# None 4 None 2 None 2 None 1 None 3 None
# post order
# None None 4 None None 5 2 None None 3 1

# however the preorder shold be much easier for this problem
# 1 2 4 None None 5 None None 3 None None


from Algorithm.Heapsort import Rand

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def traverse(self, s):
        s.append(self.val)
        # print(self.val)
        if self.left:
            self.left.traverse(s)
        else:
            s.append(None)
            # print('None')
        if self.right:
            self.right.traverse(s)
        else:
            s.append(None)
            # print('None')

def ConstructTree(l, i):
    if l[i]:
        t = TreeNode(l[i])
        left = 2 * (i + 1) - 1
        right = 2 * (i + 1)
        if left >= len(l):
            t.left = None
        else:
            t.left = ConstructTree(l, left)
        if right >= len(l):
            t.right = None
        else:
            t.right = ConstructTree(l, right)
        return t
    else:
        return None

def serial(root, result):
    if root != None:
        result.append(root.val)
        serial(root.left, result)
        serial(root.right, result)
    else:
        result.append(None)

def deserial(s):
    mid = len(s) // 2
    if s[mid] == "None":
        return None
    else:
        t = TreeNode(int(s[mid]))
        t.left = deserial(s[0: mid])
        t.right = deserial(s[mid + 1: ])
        return t

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def doit(node):
            if node != None:
                result.append(node.val)
                doit(node.left)
                doit(node.right)
            else:
                result.append(None)
        result = []
        doit(root)
        return " ".join(str(e) for e in result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def doit():
            val = next(l)
            if val != 'None':
                t = TreeNode(val)
                t.left = doit()
                t.right = doit()
                return t
            else:
                return None
        l = data.split(" ")
        l = iter(l)
        t = doit()
        return t


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
if __name__ == '__main__':
    sol = Codec()
    l = Rand(5)
    l = [1, 2, 3, 4, 5]
    l = [1, 2, 3, None, None, 4, 5, None, None, None, None]
    print(l)
    tree = ConstructTree(l, 0)
    flat = []
    tree.traverse(flat)
    print(flat)

    data = sol.serialize(tree)
    print(data)
    result = sol.deserialize(data)
    print(sol.serialize(result))

