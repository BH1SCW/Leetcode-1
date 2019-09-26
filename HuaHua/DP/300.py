from __future__ import annotations
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        T = [1] * l
        for i in range(l):
            for j in range(i):
                if nums[j] < nums[i]:
                    T[i] = max(T[i], T[j] + 1)
        return max(T) if T else 0

if __name__ == '__main__':
    sol = Solution()
    nums = [10,9,2,5,3,7,101,18]
    print(sol.lengthOfLIS(nums))
