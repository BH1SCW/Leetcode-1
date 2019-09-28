from __future__ import annotations
from collections import deque
# 这个部分还是很tricky的
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        ans = Node(node.val, [])
        dic = {node: ans}
        queue = deque([node])
        while queue:
            nd = queue.popleft()
            copy_nd = dic[nd]
            for n in nd.neighbors:
                if not n in dic:
                    # 在这里帅了跟头，一定要注意复制的时候
                    copy = Node(n.val, [])
                    dic[n] = copy
                    copy_nd.neighbors.append(copy)
                    queue.append(n)
                else:
                    copy_nd.neighbors.append(dic[n])
        return ans





