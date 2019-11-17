from __future__ import annotations
from math import gcd as bltin_gcd
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        if nums[0] == 1: return True
        for i in range(1, len(nums)):
            nums[i] = bltin_gcd(nums[i], nums[i - 1])
            if nums[i] == 1:
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    nums = [6, 10, 15]
    print(sol.isGoodArray(nums))
    nums = [12, 5, 7, 23]
    print(sol.isGoodArray(nums))
    nums = [29, 6, 10]
    print(sol.isGoodArray(nums))
    nums = [3, 6]
    print(sol.isGoodArray(nums))
