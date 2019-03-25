from functools import reduce
class Solution:
    def solveNQueens(self, n: int) -> 'List[List[str]]':
        rows = [0] * n
        cols = [0] * n
        diags1 = [0] * (2 * n - 1)
        diags2 = [0] * (2 * n - 1)
        board = [['.'] * n for _ in range(n)]
        ans = []
        def fill(i, j, num):
            if j == n:
                return
            if i == n:
                ans.append([reduce(lambda x, y: x+y, ls) for ls in board])
                return
            di1 = i + j
            di2 = n - 1 - i + j
            if (not cols[i] and not rows[j] and not diags1[di1] and not diags2[di2]):
                cols[i] = 1
                rows[j] = 1
                diags1[di1] = 1
                diags2[di2] = 1
                board[i][j] = 'Q'
                fill(i + 1, 0, num - 1)
                cols[i] = 0
                rows[j] = 0
                diags1[di1] = 0
                diags2[di2] = 0
                board[i][j] = '.'
            fill(i, j + 1, num)
        fill(0, 0, n)
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



