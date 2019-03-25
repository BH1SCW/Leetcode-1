class Solution:
    def solveSudoku(self, board: 'List[List[str]]') -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[0] * 10 for _ in range(9)]
        cols = [[0] * 10 for _ in range(9)]
        boxs = [[0] * 10 for _ in range(9)]
        # init
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    n = int(board[i][j])
                    bi = i // 3 + j // 3 * 3
                    rows[i][n] = 1
                    cols[j][n] = 1
                    boxs[bi][n] = 1

        def fill(i, j):
            if i == 9:
                return True
            next_j = (j + 1) % 9
            next_i = i + 1 if next_j == 0 else i
            if board[i][j] != '.':
                return fill(next_i, next_j)
            else:
                bi = i // 3 + j // 3 * 3
                for n in range(1, 10):
                    if (not rows[i][n] and not cols[j][n] and not boxs[bi][n]):
                        board[i][j] = str(n)
                        rows[i][n] = 1
                        cols[j][n] = 1
                        boxs[bi][n] = 1
                        if fill(next_i, next_j):
                            return True
                        else:
                            board[i][j] = '.'
                            rows[i][n] = 0
                            cols[j][n] = 0
                            boxs[bi][n] = 0
                return False

        fill(0, 0)


if __name__ == '__main__':
    sol = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(sol.solveSudoku(board))
    print(board)
