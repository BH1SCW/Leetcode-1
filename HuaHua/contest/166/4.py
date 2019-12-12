from __future__ import annotations


# 这个我
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        N = m * n
        init = sum(mat[ind // n][ind % n] << ind for ind in range(N))
        q = set([init])
        steps = 0
        seen = set()
        def move(mat, ind):
            i, j = ind // n, ind % n
            new = mat ^ (1 << ind)
            for ni, nj in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= ni < m and 0 <= nj < n:
                    new = new ^ (1 << (ni * n + nj))
            return new
        while q:
            if 0 in q: return steps
            steps += 1
            seen |= q
            q = set(move(mat, ind) for mat in q for ind in range(N)) - seen
        return -1

    def minFlips3(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        N = m * n
        init = 0
        for ind in range(N):
            i, j = ind // n, ind % n
            init += mat[i][j] << ind
        q = [init]
        steps = 0
        seen = set()
        while q:
            nq = []
            for mat in q:
                if not mat: return steps
                if mat in seen: continue
                seen.add(mat)
                for ind in range(N):
                    # if not mat & (1 << ind): continue
                    i, j = ind // n, ind % n
                    new = mat ^ (1 << ind)
                    for ni, nj in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                        if 0 <= ni < m and 0 <= nj < n:
                            x = ni * n + nj
                            new = new ^ (1 << x)
                    nq.append(new)
            q = nq
            steps += 1
        return -1


    def minFlips2(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        N = m * n
        init = 0
        for ind in range(N):
            i, j = ind // n, ind % n
            init += mat[i][j] << ind
        memo = {}
        search = set()
        def dfs(mat, d):
            if not mat: return 0
            if mat in memo: return memo[mat]
            search.add(mat)
            ans = math.inf
            for ind in range(N):
                if not mat & (1 << ind): continue
                i, j = ind // n, ind % n
                new = mat ^ (1 << ind)
                for ni, nj in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                    if 0 <= ni < m and 0 <= nj < n:
                        x = ni * n + nj
                        new = new ^ (1 << x)
                if new in search: continue
                # temp = dfs(new, d + 1)
                # if temp + 1 <= ans:
                #     print(new, temp + 1)
                #     ans = temp + 1
                ans = min(ans, dfs(new, d + 1) + 1)
            memo[mat] = ans
            search.remove(mat)
            return ans
        return dfs(init, 0)



if __name__ == '__main__':
    sol = Solution()
    mat = [[1, 1, 1], [1, 0, 1], [0, 0, 0]]
    print(sol.minFlips(mat))
    mat = [[0, 0], [0, 1]]
    print(sol.minFlips(mat))
    mat = [[0]]
    print(sol.minFlips(mat))
    mat = [[1, 0, 0], [1, 0, 0]]
    print(sol.minFlips(mat))
