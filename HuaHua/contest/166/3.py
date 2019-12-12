from __future__ import annotations


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def divide(target):
            return sum((n + target - 1) // target for n in nums)
        low, high = 1, max(nums) + 1
        while low < high:
            mid = (low + high) // 2
            if divide(mid) <= threshold:
                high = mid
            else:
                low = mid + 1
        return low


if __name__ == '__main__':
    sol = Solution()
    nums = [1]
    threshold = 1
    print(sol.smallestDivisor(nums, threshold))
    nums = [1, 2, 5, 9]
    threshold = 6
    print(sol.smallestDivisor(nums, threshold))
    nums = [2, 3, 5, 7, 11]
    threshold = 11
    print(sol.smallestDivisor(nums, threshold))
    nums = [19]
    threshold = 5
    print(sol.smallestDivisor(nums, threshold))

