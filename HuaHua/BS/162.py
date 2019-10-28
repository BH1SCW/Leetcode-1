import math
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-math.inf] + nums + [-math.inf]
        l, h = 1, len(nums) - 2
        while l <= h:
            m = (l + h) // 2
            if nums[m - 1] < nums[m] and nums[m] > nums[m + 1]:
                return m
            elif nums[m - 1] > nums[m]:
                h = m - 1
            else:
                l = m + 1



