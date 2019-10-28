from __future__ import annotations
import itertools
class Solution:
    # 这题不难，就是这个要优化一下有点无语
    def numSimilarGroups(self, A: List[str]) -> int:
        parent = {a: a for a in A}
        rank = {}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            xr, yr = find(x), find(y)
            if xr == yr:
                return
            if rank.get(xr, 1) < rank.get(yr, 1):
                rank[xr], rank[yr] = rank.get(yr, 1), rank.get(xr, 1)
            parent[yr] = xr
            if rank.get(xr, 1) == rank.get(yr, 1):
                rank[x] = rank.get(yr, 1) + 1
        def is_similiar(x, y):
            diff = [1 for (xi, yi) in zip(x, y) if xi != yi]
            return len(diff) == 2
        n, m = len(A), len(A[0])
        if m > n:
            for i in range(len(A)):
                for j in range(i + 1, len(A)):
                    if is_similiar(A[i], A[j]):
                        union(A[i], A[j])
        else:
            dic = set(A)
            for i in range(len(A)):
                w = A[i]
                for k, l in itertools.combinations(range(m), 2):
                    nb = w[:k] + w[l] + w[k + 1:l] + w[k] + w[l + 1:]
                    if nb in dic:
                        union(w, nb)
        return len([x for x in parent if parent[x] == x])


if __name__ == "__main__":
    sol = Solution()
    A = ["blw", "bwl", "wlb"]
    A = ["tars","rats","arts","star"]
    print(sol.numSimilarGroups(A))

