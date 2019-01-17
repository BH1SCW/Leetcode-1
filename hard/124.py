# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

global max_value
max_value = 0

def  left(i):
    return (i + 1) * 2 - 1

def  right(i):
    return (i + 1) * 2


def maxPathsum(l, i):
    global max_value
    if i >= len(l) or l[i] == None:
        return 0
    # the value if the node is in the path, which is to return
    val1 = max(maxPathsum(l, left(i)), maxPathsum(l, right(i)), 0) + l[i]
    # the value if the node is the root
    val2 = max(maxPathsum(l, left(i)), 0) + max(maxPathsum(l, right(i)), 0) + l[i]
    max_value = max(val2, max_value)
    return val1



global max_value
max_value = 0
def maxPath(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    global max_value
    if root == None:
        return 0
    left = maxPath(root.left)
    right = maxPath(root.right)
    # the value if the node is in the path, which is to return
    val1 = max(left, right, 0) + root.val
    # the value if the node is the root
    val2 = max(left, 0) + max(right, 0) + root.val
    max_value = max(val2, max_value)
    return val1

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global max_value
        max_value = root.val
        maxPath(root)
        val = max_value
        return val


if __name__ == "__main__":
    l = [1,2,3]
    l = [-10,9,20,None,None,15,7]
    # l = [-10,9,20]
    print(maxPathsum(l, 0))
    print(max_value)

