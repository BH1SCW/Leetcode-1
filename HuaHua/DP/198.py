from __future__ import annotations

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = len(nums)
        if l == 1:
            return nums[0]
        T = [[0, 0] for i in range(l)]
        T[0] = [0, nums[0]]
        T[1] = [nums[0], nums[1]]
        for i in range(2, l):
            T[i][1] = max(T[i - 1][0], T[i - 2][1], T[i - 2][0]) + nums[i]
            T[i][0] = max(T[i - 1][1], T[i - 1][0])
        return max(T[-1])


if __name__ == '__main__':
    sol = Solution()
    s = [1,2,3,1]
    s = [2,7,9,3,1]
    print(sol.rob(s))

