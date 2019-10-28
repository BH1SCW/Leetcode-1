from __future__ import annotations
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            n = nums[i]
            if n - 1 > len(nums) - 1 or n - 1 < 0 or n == i + 1 or nums[n - 1] == n:
                i += 1
            else:
                nums[i], nums[n - 1] = nums[n - 1], nums[i]
        for i, n in enumerate(nums):
            if n != i + 1:
                return i + 1
        return len(nums) + 1

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,0]
    print(sol.firstMissingPositive(nums))
    nums = [3, 4, -1, 1]
    print(sol.firstMissingPositive(nums))
    nums = [7,8,9,11,12]
    print(sol.firstMissingPositive(nums))
    nums = []
    print(sol.firstMissingPositive(nums))
    nums = [1]
    print(sol.firstMissingPositive(nums))
    nums = [1, 1]
    print(sol.firstMissingPositive(nums))
