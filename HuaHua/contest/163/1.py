from __future__ import annotations
class Solution:
    # 这题虽然没什么好说的，不过这个做法可谓是很巧妙了，sum还能展平，学到了
    # https://leetcode.com/problems/shift-2d-grid/discuss/431225/Python-4-lines
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        col, nums = len(grid[0]), sum(grid, [])
        k = k % len(nums)
        nums = nums[-k:] + nums[:-k]
        return [nums[i:i+col] for i in range(0, len(nums), col)]

    def shiftGrid2(self, grid: List[List[int]], k: int) -> List[List[int]]:
        N, M = len(grid), len(grid[0])
        def shift(new, old):
            for i in range(N):
                for j in range(M):
                    if i == N - 1 and j == M - 1:
                        new[0][0] = old[i][j]
                    elif j == M - 1:
                        new[i + 1][0] = old[i][j]
                    else:
                        new[i][j + 1] = old[i][j]
        old = grid
        for _ in range(k):
            new = [row[:] for row in old]
            shift(new, old)
            old = new
        return old




if __name__ == '__main__':
    sol = Solution()
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 1
    print(sol.shiftGrid(grid, k))
    grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
    k = 4
    print(sol.shiftGrid(grid, k))
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 9
    print(sol.shiftGrid(grid, k))
