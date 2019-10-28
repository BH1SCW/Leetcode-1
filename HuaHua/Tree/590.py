class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return root
        stack = [(root, 0)]
        ans = []
        while stack:
            node, seen = stack.pop()
            if not seen:
                stack.append((node, 1))
                stack.extend((child, 0) for child in node.children[::-1])
                continue
            ans.append(node.val)
        return ans



