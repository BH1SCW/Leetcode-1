class Solution:
    def solveNQueens(self, n: int) -> 'List[List[str]]':
        rows = [0] * n
        cols = [0] * n
        diags1 = [0] * (2 * n - 1)
        diags2 = [0] * (2 * n - 1)
        board = [['.'] * n for _ in range(n)]
        ans = []
        def dfs(i):
            if i == n:
                ans.append([''.join(ls) for ls in board])
                return
            for j in range(n):
                di1 = i + j
                di2 = n - 1 - i + j
                if (not cols[i] and not rows[j] and not diags1[di1] and not diags2[di2]):
                    cols[i], rows[j], diags1[di1], diags2[di2], board[i][j] = 1, 1, 1, 1, 'Q'
                    dfs(i + 1)
                    cols[i], rows[j], diags1[di1], diags2[di2], board[i][j] = 0, 0, 0, 0, '.'
        dfs(0)
        return ans


    # 0   1   2
# 0   0   1   2
# 1   1   2   3
# 2   2   3   4
#     0   1   2
# 2   2   3   4
# 1   1   2   3
# 0   0   1   2
if __name__ == '__main__':
    sol = Solution()
    n = 4
    print(sol.solveNQueens(4))



