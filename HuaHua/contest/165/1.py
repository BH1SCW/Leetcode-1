from __future__ import annotations
class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        board = [[0] * 3 for _ in range(3)]
        turn = 1
        for [i, j] in moves:
            board[i][j] = turn
            turn *= -1
        rows = [sum(row for row in board)]
        cols = [sum(col for col in zip(*board))]
        diag1 = sum([board[i][i] for i in range(3)])
        diag2 = sum([board[i][2 - i] for i in range(3)])
        if 3 in rows or 3 in cols or diag1 == 3 or diag2 == 3: return "A"
        if -3 in rows or -3 in cols or diag1 == -3 or diag2 == -3: return "B"
        if len(moves) == 9: return "Draw"
        return "Pending"




if __name__ == '__main__':
    sol = Solution()
