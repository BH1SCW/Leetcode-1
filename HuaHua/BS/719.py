from __future__ import annotations
# 这道题还是蛮有意思的，只要是二分法的话，基本上都是要用一个可以比较的东西出来，这题就是用一个O(n)的方法计算比某个distance小的pair数。
# 我不是自己想的，相比HuaHua的做法，我做了一个优化，一开始我用的是数组纪录dp，后来就只用一个数就行了。另外就是C++可以用暴力找j，但是python会超时，
# 所以我纪录了一下之前的位置，从之前开始找会快一点。
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def smaller(d, k):
            prev = 0
            ans = 0
            for i in range(len(nums) - 1):
                j = prev if prev else i + 1
                while j < len(nums) and nums[j] - nums[i] <= d:
                    j += 1
                ans += j - i - 1
                if ans >= k:
                    return ans
                prev = j
            return ans
        nums.sort()
        l, h = 0, nums[-1]
        while l < h:
            mid = (l + h) // 2
            if smaller(mid) >= k:
                h = mid
            else:
                l = mid + 1
        return l

if __name__ == '__main__':
    sol = Solution()
    nums, k = [1, 3, 1], 1
    nums, k = [1, 1, 1], 2
    print(sol.smallestDistancePair(nums, k))
