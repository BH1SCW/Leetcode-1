from __future__ import annotations
# 我的写法属于比较efficient的，但在写法上不一定是最简洁的，因为我是考虑盒子的运动而不是人的运动，
# https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/discuss/431528/Python-Dijkstra-Short
# 这个写法参照人的运动，会有更多的冗余，但是写法上比较简洁
# next的写法会让代码的长度比较短
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        def can_reach(i1, j1, i2, j2, visited, bi, bj):
            if (i1, j1) == (i2, j2): return True
            visited[i1][j1] = 1
            for ni, nj in (i1, j1 - 1), (i1, j1 + 1), (i1 - 1, j1), (i1 + 1, j1):
                if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] != '#' and (ni, nj) != (bi, bj) and not visited[ni][nj]:
                    if can_reach(ni, nj, i2, j2, visited, bi, bj): return True
            return False
        def bfs(q):
            step = 0
            while q:
                new = []
                for bi, bj, pi, pj, d in q:
                    if grid[bi][bj] == 'T': return step
                    if visited[bi][bj][d]: continue
                    visited[bi][bj][d] = 1
                    for dx, dy in moves.keys():
                        ni, nj, npi, npj = bi + dx, bj + dy, bi - dx, bj - dy
                        if 0 <= ni < N and 0 <= nj < M and 0 <= npi < N and 0 <= npj < M and grid[ni][nj] != '#' and (ni, nj) != (bi, bj) and not visited[ni][nj][moves[dx, dy]]:
                            if can_reach(pi, pj, npi, npj, [[0] * M for _ in range(N)], bi, bj):
                                new.append((ni, nj, bi, bj, moves[dx, dy]))
                q = new
                step += 1
            return -1
        N, M = len(grid), len(grid[0])
        visited = [[[0] * 4 for _ in range(M)] for _ in range(N)]
        moves = {(0, 1):0, (0, -1):1, (1, 0):2, (-1, 0):3}
        bi = bj = pi = pj = 0
        q = []
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 'B': bi, bj = i, j
                if grid[i][j] == 'S': pi, pj = i, j
        for dx, dy in moves.keys():
            npi, npj = bi - dx, bj - dy
            if 0 <= npi < N and 0 <= npj < M and grid[npi][npj] != '#' and (npi, npj) != (bi, bj):
                if can_reach(pi, pj, npi, npj, [[0] * M for _ in range(N)], bi, bj): q.append((bi, bj, npi, npj, moves[dx, dy]))
        return bfs(q)



if __name__ == '__main__':
    sol = Solution()
    grid = [["#",".",".","#","T","#","#","#","#"],["#",".",".","#",".","#",".",".","#"],["#",".",".","#",".","#","B",".","#"],["#",".",".",".",".",".",".",".","#"],["#",".",".",".",".","#",".","S","#"],["#",".",".","#",".","#","#","#","#"]]
    print(sol.minPushBox(grid))
    grid = [["#", "#", "#", "#", "#", "#"], ["#", "T", "#", "#", "#", "#"], ["#", ".", ".", "B", ".", "#"], ["#", ".", "#", "#", ".", "#"], ["#", ".", ".", ".", "S", "#"], ["#", "#", "#", "#", "#", "#"]]
    print(sol.minPushBox(grid))
    grid = [["#", "#", "#", "#", "#", "#"], ["#", "T", "#", "#", "#", "#"], ["#", ".", ".", "B", ".", "#"], ["#", "#", "#", "#", ".", "#"], ["#", ".", ".", ".", "S", "#"], ["#", "#", "#", "#", "#", "#"]]
    print(sol.minPushBox(grid))
    grid = [["#", "#", "#", "#", "#", "#"], ["#", "T", ".", ".", "#", "#"], ["#", ".", "#", "B", ".", "#"], ["#", ".", ".", ".", ".", "#"], ["#", ".", ".", ".", "S", "#"], ["#", "#", "#", "#", "#", "#"]]
    print(sol.minPushBox(grid))
    grid = [["#", "#", "#", "#", "#", "#", "#"], ["#", "S", "#", ".", "B", "T", "#"], ["#", "#", "#", "#", "#", "#", "#"]]
    print(sol.minPushBox(grid))
