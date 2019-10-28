from __future__ import annotations
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, s, ans = {0:1}, 0, 0 # 这题的初始化很巧妙，因为空字符的和是0，所以这个必须为一，其实非常合理
        for i, n in enumerate(nums):
            s += n
            ans += count.get(s - k, 0) # 这个要先算，不然会有影响
            count[s] = count.get(s, 0) + 1
        return ans

    # 这题居然很tricky，因为负数的存在, 这个的做法在都是正数的情况下才是正确的
    def subarraySum2(self, nums: List[int], k: int) -> int:
        i, s, ans = 0, 0, 0
        for j, n in enumerate(nums):
            s += n
            while i <= j and s >= k:
                if s == k:
                    ans += 1
                s -= nums[i]
                i += 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3]
    k = 3
    nums = [1]
    k = 0
    nums = [1, -1]
    nums = [1, -1, 0]
    k = 0
    print(sol.subarraySum(nums, k))
