from __future__ import annotations
import math
class Solution:
    # 这个我其实自己也能想明白，已经很接近了
    # 收了这个的启发，其实只需要保持一个候选人就可以了
    # dp的做法是比较容易想到的
    # https://leetcode.com/problems/increasing-triplet-subsequence/discuss/78995/Python-Easy-O(n)-Solution
    def increasingTriplet(self, nums: List[int]) -> bool:
        p1, p2, c1 = math.inf, math.inf, math.inf
        for n in nums:
            if n > p2: return True
            elif n > p1: p2 = n
            elif n > c1:
                p1, p2, c1 = c1, n, math.inf
            else:
                c1 = n
        return False

    def increasingTriplet2(self, nums: List[int]) -> bool:
        N = len(nums)
        maxs = [nums[-1] - 1] * N
        mins = [nums[0] + 1] * N
        for i in range(1, N):
            mins[i] = min(nums[i - 1], mins[i - 1])
        for i in range(N - 1)[::-1]:
            maxs[i] = max(nums[i + 1], maxs[i + 1])
        return bool(sum(mn < n < mx for n, mx, mn in zip(nums, maxs, mins)))

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,1,2,1,2,1,2,1,2]
    print(sol.increasingTriplet(nums))
    nums = [0,4,2,1,0,-1,-3]
    print(sol.increasingTriplet(nums))
    nums = [1, 2, 3, 4, 5]
    print(sol.increasingTriplet(nums))
    nums = [5, 4, 3, 2, 1]
    print(sol.increasingTriplet(nums))
