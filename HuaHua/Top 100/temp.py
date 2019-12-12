import itertools
def output(grid):
     m, n = len(grid), len(grid[0])
     board = [[0] * n for _ in range(m)]
     def bfs(q):
         while q:
             new = []
             for i, j, day in q:
                 if board[i][j] and board[i][j] < day + 1: continue
                 board[i][j] = day + 1
                 for ni, nj in (i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1):
                     if 0 <= ni < m and 0 <= nj < n and grid[i][j] != '#':
                         new.append((ni, nj, day + 1))
             q = new
     bfs([(0, 0, -1)])
     for i, j in itertools.product(range(m), range(n)):
         if board[i][j] == '$' and board:
             bfs([(i, j, board[i][j] - 1)])
     return sum(sum(b) for b in board)




