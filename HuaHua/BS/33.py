from __future__ import annotations


# 逻辑上面没什么问题，但是要考虑很多特殊情况，比如没有pivot，比如high和low要不要加一，比如空的list
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot(nums):
            low, high = 0, len(nums) - 1
            while low < high:
                mid = (low + high) // 2
                if nums[mid] >= nums[0]:
                    if nums[mid] >= nums[mid + 1]:
                        return mid
                    else:
                        low = mid + 1
                else:
                    high = mid
            return low
        if not nums:
            return -1
        p = find_pivot(nums)
        if nums[0] <= target <= nums[p]:
            low, high = 0, p
        else:
            low, high = p + 1, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1


if __name__ == '__main__':
    sol = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    target = 3
    nums = [1, 3]
    target = 2
    print(sol.search(nums, target))
