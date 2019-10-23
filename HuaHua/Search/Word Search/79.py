from __future__ import annotations
import itertools
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def neighbor(i, j):
            for dx, dy in (0, 1), (0, -1), (-1, 0), (1, 0):
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y]:
                    yield x, y
        def dfs(word, i, j):
            if not word:
                return True
            for x, y in neighbor(i, j):
                if board[x][y] == word[0]:
                    board[x][y] = ''
                    if dfs(word[1:], x, y):
                        return True
                    board[x][y] = word[0]
            return False
        for i, j in itertools.product(range(m), range(n)):
            if board[i][j] == word[0]:
                board[i][j] = ''
                if dfs(word[1:], i, j):
                    return True
                board[i][j] = word[0]
        return False



