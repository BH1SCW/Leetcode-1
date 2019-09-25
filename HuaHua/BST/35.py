from __future__ import annotations


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        if target <= nums[0]:
            return 0
        low, high = 0, len(nums) - 1
        while low < high - 1:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid
            else:
                high = mid
        return high

