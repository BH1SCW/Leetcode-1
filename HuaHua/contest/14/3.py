from __future__ import annotations


from collections import defaultdict
class Solution(object):
    # 我知道问题是啥了。。我这个算法只加了immediate children
    def deleteTreeNodes(self, nodes, parent, value):
        children = defaultdict(list)
        for i in range(nodes):
            children[parent[i]].append(i)
        def dfs(i):
            count = 1
            acc = value[i]
            for child in children[i]:
                v, c = dfs(child)
                acc += v
                count += c
            if acc: return acc, count
            return acc, 0
        return dfs(0)[1]



    def deleteTreeNodes2(self, nodes, parent, value):
        """
        :type nodes: int
        :type parent: List[int]
        :type value: List[int]
        :rtype: int
        """
        dic = defaultdict(int)
        for i, v in enumerate(value):
            dic[parent[i]] += v
            dic[i] += v
        count = 0
        for node in dic:
            if node == -1: continue
            p = node
            while dic[p] != 0 and p != 0:
                p = parent[p]
            count += int(dic[p] != 0)
        return count




if __name__ == '__main__':
    sol = Solution()
    nodes = 5
    parent = [-1, 0, 0, 1, 1]
    value = [-686, -842, 616, -739, -746]
    print(sol.deleteTreeNodes(nodes, parent, value))
    nodes = 7
    parent = [-1, 0, 0, 1, 2, 2, 2]
    value = [1, -2, 4, 0, -2, -1, -2]
    print(sol.deleteTreeNodes(nodes, parent, value))
    nodes = 7
    parent = [-1, 0, 0, 1, 2, 2, 2]
    value = [1, -2, 4, 0, -2, -1, -1]
    print(sol.deleteTreeNodes(nodes, parent, value))

