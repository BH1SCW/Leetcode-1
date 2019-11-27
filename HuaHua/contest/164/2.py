from __future__ import annotations


class Solution:
    # 这题我的思路跟大牛一致
    # https://leetcode.com/problems/count-servers-that-communicate/discuss/436665/Python-Simple-and-Concise
    # 不知道有没有constant space的做法
    def countServers(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        rows = [sum(row) for i, row in enumerate(grid)]
        cols = [sum(col) for i, col in enumerate(zip(*grid))]
        count = 0
        for i in range(M):
            for j in range(N):
                if not grid[i][j]: continue
                count += int(rows[i] > 1 or cols[j] > 1)
        return count







    # def countServers(self, grid: List[List[int]]) -> int:
    #     moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #     M, N = len(grid), len(grid[0])
    #     for i in range(M):
    #         for j in range(N):
    #             if not grid[i][j]: continue
    #             for dx, dy in moves:
    #                 ni, nj = i + dx, j + dy
    #                 if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] > 0:
    #                     grid[i][j] += 1
    #     count = 0
    #     for i in range(M):
    #         for j in range(N):
    #             count += int(grid[i][j] > 1)
    #     return count




if __name__ == '__main__':
    sol = Solution()
    grid = [[1, 0], [0, 1]]
    print(sol.countServers(grid))
    grid = [[1, 0], [1, 1]]
    print(sol.countServers(grid))
    grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    print(sol.countServers(grid))
    grid = [[1,0,0,1,0],[0,0,0,0,0],[0,0,0,1,0]]
    print(sol.countServers(grid))
