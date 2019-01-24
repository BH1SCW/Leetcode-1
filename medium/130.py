class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0]) if board else 0
        ind = [[False] * n] * m
        searched = set()
        def getNeighbors(i, j):
            neighbors = []
            if j + 1 <= n - 1:
                neighbors.append((i, j + 1))
            if j - 1 >= 0:
                neighbors.append((i, j - 1))
            if i + 1 <= m - 1:
                neighbors.append((i + 1, j))
            if i - 1 >= 0:
                neighbors.append((i - 1, j))
            return neighbors
        def dfs(i, j):
            searched.add((i, j))
            for s0, s1 in getNeighbors(i, j):
                item = board[s0][s1]
                if item == 'O' and not (s0, s1) in searched:
                        dfs(s0, s1)
        # search range, main function
        l1 = [(0, j) for j in range(n)]
        l1 += [(m - 1, j) for j in range(n)]
        l1 += [(i, 0) for i in range(m)]
        l1 += [(i, n - 1) for i in range(m)]
        for i, j in l1:
            # search only
            if board[i][j] == 'O' and not (i, j) in searched:
                dfs(i, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not (i, j) in searched:
                    board[i][j] = 'X'

if __name__ == '__main__':
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    sol = Solution()
    sol.solve(board)




