from __future__ import annotations
import itertools
class Solution:
    # bottom-up version
    # 这个的要点是先把matrix给sort一下
    # Time： O(mn * log(mn))
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def neighbor(x, y):
            for i, j in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                if 0 <= i < M and 0 <= j < N:
                    yield i, j
        M, N = len(matrix), len(matrix[0])
        nums = sorted([(matrix[i][j], i, j) for i, j in itertools.product(range(M), range(N))], key=lambda x: x[0])
        dp = [[1] * N for _ in range(M)]
        ans = 0
        for value, i, j in nums:
            dp[i][j] = max([dp[ni][nj] + 1 for ni, nj in neighbor(i, j) if matrix[ni][nj] < value] + [1])
            ans = max(dp[i][j], ans)
        return ans


    # 这题还是挺简单的，不知道为啥是hard
    # Time: O(mn)
    # Storage: O(mn)
    def longestIncreasingPath2(self, matrix: List[List[int]]) -> int:
        def neighbor(x, y):
            for i, j in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                if 0 <= i < M and 0 <= j < N:
                    yield i, j
        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])
        memo, ans = {}, 0
        def dfs(i, j):
            if (i, j) in memo: return memo[i, j]
            memo[i, j] = 1
            for ni,nj in neighbor(i, j):
                if matrix[i][j] < matrix[ni][nj]:
                    memo[i, j] = max(memo[i, j], dfs(ni, nj) + 1)
            return memo[i, j]
        return max(dfs(i, j) for i in range(M) for j in range(N))

if __name__ == '__main__':
    sol = Solution()
    nums = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    print(sol.longestIncreasingPath(nums))
    nums = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
    print(sol.longestIncreasingPath(nums))
