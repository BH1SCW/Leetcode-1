import collections
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        counter = collections.Counter()
        def tree_sum(root):
            if not root:
                return 0
            s = tree_sum(root.left) + tree_sum(root.right) + root.val
            counter[s] += 1
            return s
        tree_sum(root)
        max_count = max(counter.values())
        return [s for s in counter if counter[s] == max_count]
