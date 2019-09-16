from __future__ import annotations

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = len(nums)
        if l == 1:
            return nums[0]
        T = [[0, 0] for i in range(l)]
        # don't rob the first house
        T[0] = [0, 0]
        T[1] = [0, nums[1]]
        for i in range(2, l):
            T[i][1] = max(T[i - 1][0], T[i - 2][1], T[i - 2][0]) + nums[i]
            T[i][0] = max(T[i - 1][1], T[i - 1][0])
        temp = max(T[-1])
        # rob the first one
        T = [[0, 0] for i in range(l)] # remember to reinit
        T[0] = [nums[0], nums[0]]
        T[1] = [nums[0], 0]
        for i in range(2, l):
            T[i][1] = max(T[i - 1][0], T[i - 2][1], T[i - 2][0]) + nums[i]
            T[i][0] = max(T[i - 1][1], T[i - 1][0])
        # only if the last one
        if T[-1][0] > temp:
            return T[-1][0]
        return temp


if __name__ == '__main__':
    sol = Solution()
    s = [2,3,2]
    s = [1,2,3,1]
    print(sol.rob(s))

